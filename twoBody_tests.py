import numpy as np 
import matplotlib.pyplot as plt

def generate_circular_orbits(r0:float, m:float=1, M:float=1):
    """
    Generate the initial conditions requried for circular orbit for 2 masses m and M spaced some distance r0 apart => radius = r0/2
    Return 2 dicts each speecifying the position and velocity of the masses
    """
    omega = np.sqrt((m+M)/(r0**3))
    v0 = omega * (r0  /2)
    
    mass1_initConds = {"position":(-r0/2,0), "velocity":(0, -v0)} 
    mass2_initConds = {"position":(r0/2, 0), "velocity":(0,v0)}

    return mass1_initConds, mass2_initConds


def verify_circular_orbits(mass1_positions:np.ndarray, mass2_positions:np.ndarray):
    separation = np.linalg.norm(mass1_positions[0]-mass2_positions[0])
    for i in range(len(mass1_positions)):
        if np.abs(np.linalg.norm(mass1_positions[i]-mass2_positions[i])-separation)>1e-3:
            print("The orbit is not circular!")
            return None 
    print("The orbit is sufficiently circular")