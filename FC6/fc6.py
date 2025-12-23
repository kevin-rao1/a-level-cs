"""
In this repo so I can use the venv.
FC6, or Flight Computational Cd-based Control Configuration-space Calculator, is a simulation framework created by C6 Aerospace specifically for the S-IX vehicle. 
It uses an iterative binary search of apogees predicted with an RK4-based integrator at varying drag coefficients to find the most optimal one. Very optimised for low/slow conditions. 
Then, the resultant Cd is passed to a slew rate limiter and a centering proportional controller with the gain tied to dynamic pressure.
Everything only works until apogee! All the force calculations break down after apogee. The simulation should always be stopped at apogee. 
Designed for very subsonic (<150m/s) speeds, tropospheric altitudes, linear airbrakes and assumes rocket always points prograde. 
This is designed for accuracy over speed to tune gain. The Arduino C++ version will run on the Pico and be designed for speed. 

Rail length is suboptimally hardcoded for 3m. This should probably change at some point. 
Only CD changes are modelled right now. Wind tunnel tests may yet reveal that area changes also need to be modelled, though this is unlikely.

To implement:
- slew rate limiter
- proportional centre squeezing controller tied to dynamic pressure
- some kind of Sim.step() that actually updates Rocket, including randomness e.g. in thrust, wind, etc to test robustness
- sweep through different sims to find optimal gain (high accuracy, low jitter) in proportional controller

To figure out:
- how to tune oscillation penalty from flight data

Values for S-IX: target_ap = 228.6m, oscillation_penalty = TBD, mass = 0.65, base_cd = TBD, area = TBD, servo_cd_max = TBD. 
"""
import math
import statistics
import csv
import bisect

class ApogeeNotFoundException(Exception):
    pass

class Sim:
    def __init__(self, temp:float, pressure:float, humidity:float, wind:tuple, deltaT:float, target_ap:float, oscillation_penalty:float, rocket:"Rocket"):
        self.groundtemp = temp # degrees Kelvin
        self.groundpressure = pressure # Pascals, at ground.
        self.humidity = humidity # relative humidity
        self.deltaT = deltaT # timestep, s
        self.target_ap = target_ap # target apogee, m
        self.g = 9.80665
        self.wind = wind
        self.oscillation_penalty = oscillation_penalty # to account for AoA, need to tune, suggested 1.05
        self.current_time = 0
        self.rocket = rocket
        self.density = self.find_density(self.rocket.position[1]) # will be updated during main sim, not predict_ap
    
    def find_density(self, altitude: float):
        r_dry = 287.058 # J/kgK, Specific gas constant for dry air
        r_vapour = 461.495 # J/kgK, Specific gas constant for water vapour
        pressure = self.find_local_pressure(altitude) # find pressure
        temp = self.find_local_temp(altitude)
        es = 610.78*(10**( (7.5 * (temp-273.15)) / (temp - 35.85) )) # Saturation pressure from Tetens equation in Pa
        p_vapour = es*(self.humidity/100) # Actual water vapour pressure
        p_dry = pressure - p_vapour
        return (p_dry/(r_dry*temp)) + (p_vapour / (r_vapour*temp))

    def find_local_temp(self, altitude: float):
        return self.groundtemp - (0.0065*altitude)
        
    def find_local_pressure(self, altitude: float):
        temp = self.find_local_temp(altitude)
        return self.groundpressure * (temp / self.groundtemp) ** 5.2558
    
    def find_optimal_deployment(self):
        if self.rocket.position[1] < 4: # clears rail at 3m
            return 0 # do not deploy brakes while on rail
        max_iterations = 20
        search_range = [0,1]
        for i in range(max_iterations):
            mid_val = statistics.mean(search_range)
            error = self.predict_ap(mid_val) - self.target_ap
            if abs(error) <= 0.1: # within 10cm
                return mid_val
            if error <-0.1: # undershoot
                search_range[1] = mid_val
            if error >0.1: #overshoot
                search_range[0] = mid_val
        return mid_val
    
    def find_derivatives(self, vel, pos, mass, cd, thrust, area):
        """returns [vel, accel], a list of lists."""
        density = self.find_density(max(0,pos[1]))

        if pos[1] < 3: # clears rail at 3m, 0 x velocity on rail
            rvel_x = -self.wind[0]
            rvel_y = vel[1] - self.wind[1]
            airspeed = math.sqrt(rvel_x**2 + rvel_y**2)
            
            thrust_x = 0
            thrust_y = thrust
            
            k = 0.5*density*area*cd # k=1/2*Rho*A*Cd, so kv^2 = F
            drag_x = 0
        else: # off rail
            rvel_x = vel[0] - self.wind[0]
            rvel_y = vel[1] - self.wind[1]
            airspeed = math.sqrt(rvel_x**2 + rvel_y**2)
            
            if airspeed <= 0.1:
                thrust_x = 0
                thrust_y = thrust
            else:
                thrust_x = thrust * (rvel_x / airspeed)
                thrust_y = thrust * (rvel_y / airspeed)
                
            k = 0.5*density*area*cd*self.oscillation_penalty # not on rail, so weathercocking applied. 
            drag_x = -k * airspeed * rvel_x
        
        drag_y = -k * airspeed * rvel_y
        accel_x = (drag_x + thrust_x) / mass
        accel_y = (drag_y + thrust_y) / mass - self.g
        
        # prevent falling through ground
        if pos[1] <= 0 and accel_y < 0:
            accel_y = 0
            
        accel = [accel_x, accel_y]
        return list(vel), accel

    def find_mass_delta(self, thrust, dt):
        return (thrust/(self.rocket.isp*self.g))*dt
    
    def predict_ap(self, deployment):
        #copy data to avoid state pollution
        internal_vel = list(self.rocket.velocity) # lists are mutable.
        internal_pos = list(self.rocket.position)
        internal_mass = self.rocket.mass
        internal_cd = self.rocket.get_cd(deployment)
        internal_area = self.rocket.area
        starting_timestep = int(self.current_time//self.deltaT)
        max_timestep = int(15//self.deltaT)
        dt = self.deltaT

        # simulates up to 15 seconds of flight, but breaks early on apogee. 
        # Assumes rocket always points prograde, so weathercocking is probably overaccounted for. 
        for step in range(starting_timestep, max_timestep+starting_timestep): 
            #rk4 things
            current_time = step * dt

            thrust_k1 = self.rocket.get_thrust(current_time, dt)
            mass_k1 = internal_mass # Mass at start of step
            k1_v, k1_a = self.find_derivatives(internal_vel, internal_pos, internal_mass, internal_cd, thrust_k1, internal_area)

            thrust_k2 = self.rocket.get_thrust(current_time + 0.5 * dt, dt)
            mass_k2 = internal_mass - self.find_mass_delta(thrust_k1, 0.5*dt)
            pos_k2 = [internal_pos[i] + k1_v[i] * 0.5 * dt for i in range(2)]
            vel_k2 = [internal_vel[i] + k1_a[i] * 0.5 * dt for i in range(2)]
            k2_v, k2_a = self.find_derivatives(vel_k2, pos_k2, mass_k2, internal_cd, thrust_k2, internal_area)

            thrust_k3 = self.rocket.get_thrust(current_time + 0.5 * dt, dt)
            mass_k3 = internal_mass - self.find_mass_delta(thrust_k2, 0.5*dt)
            pos_k3 = [internal_pos[i] + k2_v[i] * 0.5 * dt for i in range(2)]
            vel_k3 = [internal_vel[i] + k2_a[i] * 0.5 * dt for i in range(2)]
            k3_v, k3_a = self.find_derivatives(vel_k3, pos_k3, mass_k3, internal_cd, thrust_k3, internal_area)

            thrust_k4 = self.rocket.get_thrust(current_time + dt, dt)
            mass_k4 = internal_mass - self.find_mass_delta(thrust_k3, dt)
            pos_k4 = [internal_pos[i] + k3_v[i] * dt for i in range(2)]
            vel_k4 = [internal_vel[i] + k3_a[i] * dt for i in range(2)]
            k4_v, k4_a = self.find_derivatives(vel_k4, pos_k4, mass_k4, internal_cd, thrust_k4, internal_area)

            # Update mass for next step using RK4 weighted average of mass flow
            dmdt_k1 = -thrust_k1 / (self.rocket.isp * self.g)
            dmdt_k2 = -thrust_k2 / (self.rocket.isp * self.g)
            dmdt_k3 = -thrust_k3 / (self.rocket.isp * self.g)
            dmdt_k4 = -thrust_k4 / (self.rocket.isp * self.g)
            internal_mass += (dt / 6.0) * (dmdt_k1 + 2*dmdt_k2 + 2*dmdt_k3 + dmdt_k4)

            for i in range(2):
                internal_pos[i] += (dt / 6.0) * (k1_v[i] + 2*k2_v[i] + 2*k3_v[i] + k4_v[i])
                internal_vel[i] += (dt / 6.0) * (k1_a[i] + 2*k2_a[i] + 2*k3_a[i] + k4_a[i])

            # apogee detection
            if internal_vel[1] < 0 and internal_pos[1] > 1: # prevent trigger at t=0
                return internal_pos[1]
        raise ApogeeNotFoundException


class Rocket:
    def __init__(self, mass:float, thrust_csv_path:str, isp:float, base_cd:float, area:float, servo_cd_max:float):
        self.velocity = [0,0] # x,y in m/s
        self.position = [0,0] # x,y in m
        self.apogee = 0 # m
        self.mass = mass # kg
        self.base_cd = base_cd # Cd with servo closed
        self.area = area # area in m^2
        self.servo_cd_max = servo_cd_max # maximum Cd the servo can add
        self.thrust_curve = self.load_thrust_curve(thrust_csv_path) # value of thrust every timestep
        self.isp = isp # f25w is 220.6s
        self.servo_deployment = 0 # from 0 to 1, where 1 is fully extended
    
    def load_thrust_curve(self, path:str):
        data = []
        with open(path, 'r') as file:
            reader = csv.reader(file)
            next(reader) # Skip header
            for row in reader:
                try:
                    if row:
                        data.append((float(row[0]), float(row[1]))) # (time, thrust)
                except ValueError:
                    continue
        return data # [(t0, F0), (t1, F1), ...]

    def get_cd(self, deploy=None):
        if deploy is None: # defaults to this when called, not when defined.
            deploy = self.servo_deployment
        return self.base_cd + deploy*self.servo_cd_max
        #airbrakes are designed to be fully linear, so this is valid so long any boundary flow is negligible. Verify in wind tunnel. 
    
    def get_thrust(self, time:float, dt):
        # Linear interpolation function by Gemini 3
        curve = self.thrust_curve
        if not curve:
            return 0
        
        # If before start, return 0 (or first value?)
        if time < curve[0][0]:
            return 0
        
        # If after end, return 0
        if time > curve[-1][0]:
            return 0
            
        # Find interval
        # Optimization: could use bisect, but linear scan is okay for small curves
        # For larger curves, bisect is better.
        # bisect_right returns insertion point after time
        idx = bisect.bisect_right(curve, (time, float('inf')))
        
        if idx == 0:
            return curve[0][1]
        if idx >= len(curve):
            return 0
            
        # Interpolate between idx-1 and idx
        t0, f0 = curve[idx-1]
        t1, f1 = curve[idx]
        
        if t1 == t0:
            return f0
            
        slope = (f1 - f0) / (t1 - t0)
        return f0 + slope * (time - t0)