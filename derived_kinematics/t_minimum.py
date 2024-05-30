try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_kinematics_t_min(
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    epsilon: float, 
    verbose: bool = True) -> float:
    """
    Description
    --------------
    Calculate t_{min}.

    Parameters
    --------------
    epsilon: (float)

    Returns
    --------------
    t_minimum: (float)
        t_minimum

    Notes
    --------------
    """
    try:

        # (1): Calculate 1 - x_{B}:
        one_minus_xb = 1. - x_Bjorken

        # (2): Calculate the numerator:
        numerator = (2. * one_minus_xb * (1. - np.sqrt(1. + epsilon**2))) + epsilon**2

        # (3): Calculate the denominator:
        denominator = (4. * x_Bjorken * one_minus_xb) + epsilon**2

        # (4): Obtain the t minimum
        t_minimum = -1. * squared_Q_momentum_transfer * numerator / denominator

        # (4.1): If verbose, print the result:
        if verbose:
            print(f"> Calculated t_minimum to be:\n{t_minimum}")

        # (5): Print the result:
        return t_minimum

    except Exception as ERROR:
        print(f"> Error calculating t_minimum: \n> {ERROR}")
        return 0.