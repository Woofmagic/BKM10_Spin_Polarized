from decimal import Decimal

def calculate_kinematics_skewness_parameter(
    squared_Q_momentum_transfer: float,
    x_Bjorken: float,
    squared_hadronic_momentum_transfer_t: float,
    verbose: bool = False) -> float:
    """
    ## Description
    Calculate the Skewness Parameter.

    :param squared_Q_momentum_transfer float:
        kinematic momentum transfer to the hadron

    :param x_Bjorken float:
        kinematic Bjorken X

    :param verbose bool:
        Debugging console output.
    
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
    
    except Exception as error:
        print(f"> Error in computing skewness xi:\n> {error}")
        return 0.