"""
In this repo so I can use the venv.
FC6, or Flight Computational Cd-based Control Configuration-space Calculator, is a simulation framework created by C6 Aerospace specifically for the S-IX vehicle. 
It uses an iterative binary search of apogees predicted with an RK4-based integrator at varying drag coefficients to find the most optimal one. Very optimised for low/slow conditions. 
Then, the resultant Cd is passed to a slew rate limiter and a centering proportional controller with the gain tied to dynamic pressure.
Designed for very subsonic (<150m/s) speeds, tropospheric altitudes, linear airbrakes and assumes rocket always points prograde. 
"""
import math
import statistics

class ApogeeNotFoundException(Exception):
    pass

class Sim:
    def __init__(self, temp:float, pressure:float, humidity:float, deltaT:float, target_ap:float, rocket:"Rocket"):
        self.groundtemp = temp # degrees Kelvin
        self.groundpressure = pressure # Pascals, at ground.
        self.humidity = humidity # relative humidity
        self.deltaT = deltaT # timestep, s
        self.target_ap = target_ap # target apogee, m
        self.g = 9.80665
        self.rocket = rocket
        self.density = self.find_density(self.rocket.position[1])
    
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
        max_iterations = 20
        search_range = [0,1]
        for i in range(max_iterations):
            mid_val = statistics.mean(search_range)
            error = self.predict_ap(mid_val) - self.target_ap
            if abs(error) <= 0.01: # within 1cm
                return mid_val
            if error <-0.01: # undershoot
                search_range[1] = mid_val
            if error >0.01: #overshoot
                search_range[0] = mid_val
        return mid_val
    
    def find_derivatives(self, vel, pos, mass, cd, area):
        """returns [vel, accel], a list of lists."""
        density = self.find_density(max(0,pos[1]))
        speed = math.sqrt(vel[0]**2 + vel[1]**2)
        k = 0.5*density*area*cd # k=1/2*Rho*A*Cd, so kv^2 = F
        drag_x = -k * speed * vel[0]
        drag_y = -k * speed * vel[1]
        accel = [drag_x/mass, (drag_y/mass) - self.g]
        return list(vel), accel
    
    def predict_ap(self, deployment):
        #copy data to avoid state pollution
        internal_vel = list(self.rocket.velocity) # lists are mutable.
        internal_pos = list(self.rocket.position)
        internal_mass = self.rocket.mass
        internal_cd = self.rocket.base_cd + deployment*self.rocket.servo_cd_max
        internal_area = self.rocket.area
        max_time = 15
        dt = self.deltaT
        
        # simulates up to 15 seconds of flight, but breaks early on apogee. 
        # Assumes rocket always points prograde, so weathercocking is completely unaccounted for. 
        for t in range(int(max_time//self.deltaT)): 
            #rk4 things
            k1_v, k1_a = self.find_derivatives(internal_vel, internal_pos, internal_mass, internal_cd, internal_area)

            pos_k2 = [internal_pos[i] + k1_v[i] * 0.5 * dt for i in range(2)]
            vel_k2 = [internal_vel[i] + k1_a[i] * 0.5 * dt for i in range(2)]
            k2_v, k2_a = self.find_derivatives(vel_k2, pos_k2, internal_mass, internal_cd, internal_area)

            pos_k3 = [internal_pos[i] + k2_v[i] * 0.5 * dt for i in range(2)]
            vel_k3 = [internal_vel[i] + k2_a[i] * 0.5 * dt for i in range(2)]
            k3_v, k3_a = self.find_derivatives(vel_k3, pos_k3, internal_mass, internal_cd, internal_area)

            pos_k4 = [internal_pos[i] + k3_v[i] * dt for i in range(2)]
            vel_k4 = [internal_vel[i] + k3_a[i] * dt for i in range(2)]
            k4_v, k4_a = self.find_derivatives(vel_k4, pos_k4, internal_mass, internal_cd, internal_area)

            for i in range(2):
                internal_pos[i] += (dt / 6.0) * (k1_v[i] + 2*k2_v[i] + 2*k3_v[i] + k4_v[i])
                internal_vel[i] += (dt / 6.0) * (k1_a[i] + 2*k2_a[i] + 2*k3_a[i] + k4_a[i])

            # apogee detection
            if internal_vel[1] <= 0:
                return internal_pos[1]
        raise ApogeeNotFoundException


class Rocket:
    def __init__(self, mass:float, thrust_curve:list, base_cd:float, area:float, servo_cd_max:float):
        self.velocity = [0,0] # x,y in m/s
        self.position = [0,0] # x,y in m
        self.apogee = 0 # m
        self.mass = mass # kg
        self.base_cd = base_cd # Cd with servo closed
        self.area = area # area in m^2
        self.servo_cd_max = servo_cd_max # maximum Cd the servo can add
        self.thrust_curve = thrust_curve # value of thrust every timestep
        self.servo_deployment = 0 # from 0 to 1, where 1 is fully extended
    
    def get_cd(self):
        return self.base_cd + self.servo_deployment*self.servo_cd_max
        #airbrakes are designed to be fully linear, so this is valid so long any boundary flow is negligible. 