from decimal import Decimal

import numpy as np

def calculate_kinematics_t_min(
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    epsilon: float, 
    verbose: bool = False) -> float:
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
        one_minus_xb = Decimal("1.") - x_Bjorken

        # (2): Calculate the numerator:
        numerator = (Decimal("2.") * one_minus_xb * (Decimal("1.") - (Decimal("1.") + epsilon**2).sqrt())) + epsilon**2

        # (3): Calculate the denominator:
        denominator = (Decimal("4.") * x_Bjorken * one_minus_xb) + epsilon**2

        # (4): Obtain the t minimum
        t_minimum = Decimal("-1.0") * squared_Q_momentum_transfer * numerator / denominator

        # (4.1): If verbose, print the result:
        if verbose:
            print(f"> Calculated t_minimum to be:\n{t_minimum}")

        # (5): Print the result:
        return t_minimum

    except Exception as ERROR:
        print(f"> Error calculating t_minimum: \n> {ERROR}")
        return Decimal("0.0")