from decimal import Decimal

def calculate_kinematics_skewness_parameter(
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float, 
    verbose: bool = False) -> float:
    """
    Description
    --------------
    Calculate the Skewness Parameter
    x_{i} = x_{B} * (1 + \frac{ t Q^{2} }{ 2 } ) ... FUCK OFF

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

        # (1): The Numerator:
        numerator = (1. + (squared_hadronic_momentum_transfer_t / (2. * squared_Q_momentum_transfer)))

        # (2): The Denominator:
        denominator = (2. - x_Bjorken + (x_Bjorken * squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer))

        # (3): Calculate the Skewness Parameter:
        skewness_parameter = x_Bjorken * numerator / denominator

        # (3.1): If verbose, print the output:
        if verbose:
            print(f"> Calculated skewness xi to be:\n{skewness_parameter}")

        # (4): Return Xi:
        return skewness_parameter
    
    except Exception as ERROR:
        print(f"> Error in computing skewness xi:\n> {ERROR}")
        return 0.