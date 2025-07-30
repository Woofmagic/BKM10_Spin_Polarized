from decimal import Decimal

from statics.masses.particle_masses import _MASS_OF_PROTON_IN_GEV

try:
    import numpy as np
    
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")
    
def calculate_kinematics_epsilon_squared(
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    verbose: bool = False) -> float:
    """
    Description
    --------------
    Calculate epsilon, which is just a ratio of kinematic quantities:
    \epsilon^{2} := 4 * m_{p}^{2} * x_{B}^{2} / Q^{2}

    Parameters
    --------------
    squared_Q_momentum_transfer: (float)
        kinematic momentum transfer to the hadron

    x_Bjorken: (float)
        kinematic Bjorken X

    verbose: (bool)
        Debugging console output.
    

    Notes
    --------------
    """

    try:

        # (1): Calculate it right away:
        epsilon_squared = (4. * _MASS_OF_PROTON_IN_GEV**2 * x_Bjorken**2) / squared_Q_momentum_transfer

        # (1.1): If verbose, print the result:
        if verbose:
            print(f"> Calculated epsilon squared to be:\n{epsilon_squared}")

        # (2): Return Epsilon:
        return epsilon_squared
    
    except Exception as ERROR:
        print(f"> Error in computing kinematic epsilon squared:\n> {ERROR}")
        return 0.