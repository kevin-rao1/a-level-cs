"""
In this repo so I can use the venv.
FC6, or Flight Computational Cd-based Control Configuration-space Calculator, is a simulation framework created by C6 Aerospace specifically for the S-IX vehicle. 
It uses an iterative binary search of apogees predicted with an RK4-based integrator at varying drag coefficients to find the most optimal one. Very optimised for low/slow conditions. 
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
    
    def predict_ap(self, deployment):
        # euler instead of RK4 for now
        #copy data to avoid state pollution
        internal_vel = list(self.rocket.velocity) # lists are mutable.
        internal_pos = list(self.rocket.position)
        internal_mass = self.rocket.mass
        internal_cd = self.rocket.base_cd + deployment*self.rocket.servo_cd_max
        internal_area = self.rocket.area
        max_time = 15
        
        # simulates up to 15 seconds of flight, but breaks early on apogee. 
        # Assumes rocket always points prograde, so weathercocking is completely unaccounted for. 
        for t in range(int(max_time//self.deltaT)): 
            density = self.find_density(internal_pos[1])
            speed = math.sqrt(internal_vel[0]**2 + internal_vel[1]**2)
            internal_accel = [0,0]

            # find force
            k = 0.5*density*internal_area*internal_cd # k=1/2*Rho*A*Cd, so kv^2 = Fd
            force = [-k*speed*internal_vel[0], -k*speed*internal_vel[1] - self.g*internal_mass] # use some vector maths to find the force vector [x,y]

            # update acceleration, velocity and position vectors
            internal_accel[0] = force[0]/internal_mass # F=ma
            internal_accel[1] = force[1]/internal_mass
            internal_pos[0] += internal_vel[0]*self.deltaT # s=u+vt
            internal_pos[1] += internal_vel[1]*self.deltaT
            internal_vel[0] += internal_accel[0]*self.deltaT # v=u+at
            internal_vel[1] += internal_accel[1]*self.deltaT

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