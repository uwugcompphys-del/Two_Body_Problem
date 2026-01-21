import numpy as np
import math
import constants as cont

## import the python file that has rho
# solve first order differential equation dM/dr = 4(pi)r^2 * rho(r)

## try to find where the pressure equals zero this will predict the radius 

def rho(p_0, rf, r):
    """
    calculate the current density
    input: 
    initial density (p_0), final radius (rf) and current radius
    outputs:
    the current density (p)
    """
    p = p_0 * (1 - (r / rf)**2)
    return p



def deriv(r, m, p_0, rf):
    """
    calulate the righthand side of dm/dr = 4πr²p(r)
    inputs: 
    current radius (r), current mass (m)
    outputs
    4πr²p(r)
    """

    return 4 * math.pi * r**2 * rho(p_0, rf, r )  #4πr²p(r) where rho takes input of p_0, rf, r




def body_mass(h, rf, p_0):
    """ 
    Solves the first order differential equation dM/dr = 4πr²p(r)
    to compute the total mass of a celestial body.
    Uses the 4th order Runge Kutta (RK4) numerical method to
    evaluate M(r) given an input density function p(r) and initial conditions
    inputs:
    step size (h), final radius (rf) and inital density(p_0)
    Note:
    Returns
    radius ,mass 
    """
    
    numb_steps = int((rf)/h)
    r = 0
    m = 0

    for i in range(numb_steps):

        k1 = deriv(r,m, p_0, rf)
        k2 = deriv(r + h/2, m + h * k1/2, p_0, rf)
        k3 = deriv(r + h/2, m + h * k2/2, p_0, rf)
        k4 = deriv(r + h, m + h * k3, p_0, rf)

        m = m + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        r = r + h  ## make h be a constant in the py file for conts, try to have numb_steps be about 900


    return r, m










