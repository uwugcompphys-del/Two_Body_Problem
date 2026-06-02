import math
import numpy as np
import csv
import os
import body_mass as bm
import constants as const


def delete_csv():
    # Get directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Combine directory with filename
    csv_path = os.path.join(script_dir, "binary_star.csv")

    if(os.path.exists(csv_path) and os.path.isfile(csv_path)):
        os.remove(csv_path)
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
    vy1 = v1
    vx2 = 0
    vy2 = -v2

    return np.array([x1, y1, x2, y2, vx1, vy1, vx2, vy2])

def calculate_derivatives(current_values):
    """Calculates the derivatives of position and velocity"""
# calculate derrivatives (position, velocity)
# gravity calculation?
    x1, y1, x2, y2, vx1, vy1, vx2, vy2 = current_values

    dx = x2 - x1
    dy = y2 - y1
    r = math.sqrt(dx**2 + dy**2)

    m1 = bm.body_mass(const.h, const.rf_1, const.p0_1)[1]
    m2 = bm.body_mass(const.h, const.rf_2, const.p0_2)[1]

    F = (const.G * m1 * m2) / r**2
    Fx = F * (dx / r)
    Fy = F * (dy / r)

    ax1 = Fx / m1
    ay1 = Fy / m1
    ax2 = -Fx / m2
    ay2 = -Fy / m2


    return np.array([vx1, vy1, vx2, vy2, ax1, ay1, ax2, ay2]), r #list of velocity and accelerations

#verlet method:

def verlet_method(current_values, dt):
    """estimates next position of both bodies using Stormer-Verlet"""
    x1, y1, x2, y2, vx1, vy1, vx2, vy2 = current_values
    print("******", x1)
    der = calculate_derivatives(current_values)
    ax1, ay1, ax2, ay2 = der[4], der[5], der[6], der[7]

    new_x1 = x1 + vx1 * dt + 0.5 * ax1*dt ** 2
    new_y1 = y1 + vy1 * dt + 0.5 * ay1*dt ** 2 
    new_x2 = x2 + vx2 * dt + 0.5 * ax2*dt ** 2
    new_y2 = y2 + vy2 * dt + 0.5 * ay2*dt ** 2

    new_state = np.array([new_x1, new_y1, new_x2, new_y2, vx1, vy1, vx2, vy2])
    new_der = calculate_derivatives(new_state)
    new_ax1, new_ay1, new_ax2, new_ay2 = new_der[4], new_der[5], new_der[6], new_der[7]

    new_vx1 = vx1 + 0.5*(ax1 + new_ax1)*dt
    new_vy1 = vy1 + 0.5*(ay1 + new_ay1)*dt
    new_vx2 = vx2 + 0.5*(ax2 + new_ax2)*dt
    new_vy2 = vy2 + 0.5*(ay2 + new_ay2)*dt

    return np.array([new_x1, new_y1, new_x2, new_y2, new_vx1, new_vy1, new_vx2, new_vy2])

def Create_csv():
    # Get directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Combine directory with filename
    csv_file_path = os.path.join(script_dir, 'binary_star.csv')
    print(f"Saving to: {csv_file_path}")

    Frames = 600
    dt = 1000 / 60

    m1 = bm.body_mass(const.h, const.rf_1, const.p0_1)[1]
    m2 = bm.body_mass(const.h, const.rf_2, const.p0_2)[1]

    with open(csv_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time','x1', 'x2', 'y1', 'y2'])
        
        current_values = setup_initial_conditions(const.rf_1, const.rf_2, m1, m2, const.G)
        Time = 1
        for frame in range(Frames):
            current_values = verlet_method(current_values, dt)
            writer.writerow([Time, current_values[0], current_values[2], current_values[1], current_values[3]])
            Time += 1