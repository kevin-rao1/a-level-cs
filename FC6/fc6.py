"""
In this repo so I can use the venv.
FC6, or Flight Computational Cd-based Control Configuration-space Calculator, is a simulation framework created by C6 Aerospace specifically for the S-IX vehicle. 
It uses an iterative binary search of apogees predicted with an RK4-based integrator at varying drag coefficients to find the most optimal one. 
"""
import math
import statistics

class Sim:
    def __init__(self, temp:float, pressure:float, humidity:float, deltaT:float, target_ap:float, rocket:"Rocket"):
        self.groundtemp = temp # degrees Kelvin
        self.groundpressure = pressure # Pascals, at ground.
        self.humidity = humidity # relative humidity
        self.deltaT = deltaT # timestep, s
        self.target_ap = target_ap # target apogee, m
        self.g = 9.80665
        self.rocket = rocket
        self.update_density()
    
    def update_density(self):
        r_dry = 287.058 # J/kgK, Specific gas constant for dry air
        r_vapour = 461.495 # J/kgK, Specific gas constant for water vapour
        altitude = self.rocket.position[1]
        pressure = self.find_local_pressure(altitude) # find pressure
        temp = self.find_local_temp(altitude)
        es = 610.78*(10**( (7.5 * (temp-273.15)) / (temp - 35.85) )) # Saturation pressure from Tetens equation in Pa
        p_vapour = es*(self.humidity/100) # Actual water vapour pressure
        p_dry = pressure - p_vapour
        self.density = (p_dry/(r_dry*temp)) + (p_vapour / (r_vapour*temp))

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
            self.rocket.servo_deployment = mid_val
            error = self.predict_ap() - self.target_ap
            if abs(error) <= 0.01: # within 1cm
                return mid_val
            if error <-0.01: # undershoot
                search_range[1] = mid_val
            if error >0.01: #overshoot
                search_range[0] = mid_val
        return mid_val
    
    def predict_ap(self):
        pass


class Rocket:
    def __init__(self, mass:float, thrust_curve:list, base_cd:float, base_area:float, servo_cd_max:float):
        self.acceleration = [0,0] # x,y in m/s^2
        self.velocity = [0,0] # x,y in m/s
        self.position = [0,0] # x,y in m
        self.apogee = 0 # m
        self.mass = mass # kg
        self.base_cd = base_cd # Cd with servo closed
        self.base_area = base_area # area with servo closed in m^2
        self.servo_cd_max = servo_cd_max # maximum Cd the servo can add
        self.thrust_curve = thrust_curve # value of thrust every timestep
        self.servo_deployment = 0 # from 0 to 1, where 1 is fully extended
    
    def get_cd(self):
        return self.base_cd + self.servo_deployment*self.servo_cd_max