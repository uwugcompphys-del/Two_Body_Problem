import math
import numpy as np
import csv
import os
import body_mass as bm
import constants as const

#Time, x1, x2, y1, y2
#1 and 2 are the two different celestial bodies
#i need to return their positions a csv file, 900 Frames

#position x1, y1, x2, y2
#velocities vx1, vy1, vx2, vy2 
# i need to calculate their orbital speed
#acceleration (given to me)



def delete_csv():
    file = 'binary_star.csv'
    if(os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)
        print("file deleted")
    else:
        print("file not found")

def setup_initial_conditions(r1, r2, m1, m2, G):
    """This will calculate positions and velocities at t=0, using the velocities needed for a stable orbit"""
    r = r1 + r2
    v1 = math.sqrt(G * m2 * r1 / r**2) 
    v2 = math.sqrt(G * m1 * r2 / r**2)

    x1 = -r1
    y1 = 0
    x2 = r2
    y2 = 0

# velocities are perpendicular to position vectors for circular orbits
    vx1 = 0
    vy1 = -v1
    vx2 = 0
    vy2 = v2

    return np.array([x1, y1, x2, y2, vx1, vy1, vx2, vy2])

def calculate_derivatives(current_values):
    """Calculates the derivatives of position and velocity"""
# calculate derrivatives (position, velocity)
# gravity calculation?
    x1, y1, x2, y2, vx1, vy1, vx2, vy2 = current_values

    dx = x2 - x1
    dy = y2 - y1
    r = math.sqrt(dx**2 + dy**2)

    F = (const.G * bm.body_mass(const.h, const.rf_1, const.p0_1)[1] * bm.body_mass(const.h, const.rf_2, const.p0_2)[1]) / r**2
    Fx = F * (dx / r)
    Fy = F * (dy / r)

    ax1 = Fx / bm.body_mass(const.h, const.rf_1, const.p0_1)[1]
    ay1 = Fy / bm.body_mass(const.h, const.rf_1, const.p0_1)[1]
    ax2 = -Fx / bm.body_mass(const.h, const.rf_2, const.p0_2)[1]
    ay2 = -Fy / bm.body_mass(const.h, const.rf_2, const.p0_2)[1]


    return np.array([vx1, vy1, vx2, vy2, ax1, ay1, ax2, ay2]) #list of velocity and accelerations

#RK4 method:

def Rk4_method(current_values, dt):
    """Estimates the next position of both celestial bodies and updates current_values"""
    k1 = calculate_derivatives(current_values)
    k2 = calculate_derivatives(current_values + dt * k1/2)
    k3 = calculate_derivatives(current_values + dt * k2/2)
    k4 = calculate_derivatives(current_values + dt * k3)
    return current_values + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)

def Create_csv():
    
    Frames = 600

    with open('binary_star.csv', 'a', newline='') as file:
        dt = 1000/60
        writer = csv.writer(file)
        writer.writerow(['Time','x1', 'x2', 'y1', 'y2'])
        
        current_values = setup_initial_conditions(const.rf_1, const.rf_2, bm.body_mass(const.h, const.rf_1, const.p0_1)[1], bm.body_mass(const.h, const.rf_2, const.p0_2)[1], const.G)
        Time = 1
        for positions in range(Frames):
            writer.writerow([Time, current_values[0], current_values[1], current_values[2], current_values[3]])
            Time += 1
            current_values = Rk4_method(current_values, dt)