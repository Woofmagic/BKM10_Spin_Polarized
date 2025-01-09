from statics.masses.particle_masses import _MASS_OF_PROTON_IN_GEV

from decimal import Decimal

import numpy as np
    
def calculate_kinematics_epsilon(
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    verbose: bool = False) -> float:
    """
    Description
    --------------
    Calculate epsilon, which is just a ratio of kinematic quantities:
    \epsilon := 2 * m_{p} * x_{B} / Q

    Parameters
    --------------
    squared_Q_momentum_transfer: (float)
        kinematic momentum transfer to the hadron. 

    x_Bjorken: (float)
        kinematic Bjorken X

    verbose: (bool)
        Debugging console output.
    

    Notes
    --------------
    """
            
    try:

        # (1): Calculate Epsilon right away:
        epsilon = (Decimal("2.") * x_Bjorken * _MASS_OF_PROTON_IN_GEV) / squared_Q_momentum_transfer.sqrt()

        # (1.1): If verbose, print the result:
        if verbose:
            print(f"> Calculated epsilon to be:\n{epsilon}")

        # (2): Return Epsilon:
        return epsilon
    
    except Exception as ERROR:
        print(f"> Error in computing kinematic epsilon:\n> {ERROR}")
        return Decimal("0.0")