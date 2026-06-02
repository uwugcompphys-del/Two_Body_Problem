import numpy as np
import matplotlib.pyplot as plt
import csv, os
import Position_Velocity_Acceleration as pva
import constants as const
import body_mass as bm

def energy():
    """
    
    """
    
    script_dir = os.path.dirname(os.path.abspath(__file__))

    csv_path = os.path.join(script_dir, "Energy_values.csv")

    if os.path.exists(csv_path):
        os.remove(csv_path)
        print(f"File '{csv_path}' deleted successfully.")
    else:
        print(f"File '{csv_path}' does not exist.")


    Frames = 600

    with open(csv_path, 'a', newline='') as file:
        dt = 1000/60
        
        writer = csv.writer(file)
        writer.writerow(['Time','ke1', 'ke2', 'Ue1', 'Et'])

        current_values = pva.setup_initial_conditions(const.rf_1, const.rf_2, 
                                                      bm.body_mass(const.h, const.rf_1, const.p0_1)[1], 
                                                      bm.body_mass(const.h, const.rf_2, const.p0_2)[1], 
                                                      const.G)
        
        Time = 1
        for positions in range(Frames):
            ke1 = 1/2 * (bm.body_mass(const.h, const.rf_1, const.p0_1)[1]) * (pva.verlet_method(current_values, dt)[4] + pva.verlet_method(current_values, dt)[5])**2
            ke2 = 1/2 * (bm.body_mass(const.h, const.rf_2, const.p0_2)[1]) * (pva.verlet_method(current_values, dt)[6] + pva.verlet_method(current_values, dt)[7])**2
            Ue = (-const.G * (bm.body_mass(const.h, const.rf_1, const.p0_1)[1]) * (bm.body_mass(const.h, const.rf_2, const.p0_2)[1]))/(pva.calculate_derivatives(current_values)[1])
            Et = ke1 + ke2 + Ue
            writer.writerow([Time, ke1, ke2, Ue, Et])
            Time+=1
            current_values = pva.verlet_method(current_values, dt)