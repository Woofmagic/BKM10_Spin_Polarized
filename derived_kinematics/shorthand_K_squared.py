try:
    import numpy as np
except ImportError:
    print("> NumPy is not installed. Please install NumPy to use this script.") 

def calculate_kinematics_k_squared( 
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    lepton_energy_fraction_y: float,
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    squared_hadronic_momentum_transfer_t_minimum: float,
    verbose: bool = False) -> float:
    """
    Description
    --------------
    Equation (30) in the BKM Formalism, available
    at this link: https://arxiv.org/pdf/hep-ph/0112108.pdf

    Parameters
    --------------
    epsilon: (float)

    squared_Q_momentum_transfer: (float)

    x_Bjorken: (float)

    lepton_energy_fraction_y: (float)

    squared_hadronic_momentum_transfer_t: (float)

    squared_hadronic_momentum_transfer_t_minimum: (float)

    verbose: (bool)
        Debugging console output.

    Returns
    --------------
    k_squared : (float)
        result of the operation
    
    Notes
    --------------
    """
    
    try:

        # (1): Calculate recurring quantity 1 - xB -- this IS multiplicative quantity one!
        one_minus_x_bjorken = 1. - x_Bjorken

        # (2): Multiplicative Quantity Two:
        second_multiplicative_quantity = 1. - lepton_energy_fraction_y - (lepton_energy_fraction_y**2 * epsilon**2 / 4.)

        # (3): Multiplicative Quantity Three:
        third_multiplicative_quantity = 1. - (squared_hadronic_momentum_transfer_t_minimum / squared_hadronic_momentum_transfer_t)

        # (3): Multiplicative Quantity Four - First Term:
        fourth_multiplicative_quantity_first_term = np.sqrt(1. + epsilon**2)

        # (4): Multiplicative Quantity Four - Second Term - Numerator:
        fourth_multiplicative_quantity_second_term_numerator = 4. * x_Bjorken * one_minus_x_bjorken + epsilon**2

        # (5): Multiplicative Quantity Four - Second Term - Denominator:
        fourth_multiplicative_quantity_second_term_denominator = 4. * one_minus_x_bjorken

        # (6): Multiplicative Quantity Four - Prefactor:
        fourth_multiplicative_quantity_second_term_prefactor = ((squared_hadronic_momentum_transfer_t - squared_hadronic_momentum_transfer_t_minimum ) / squared_Q_momentum_transfer)

        # (7): Multiplicative Quantity Four:
        fourth_multiplicative_quantity_second_term = fourth_multiplicative_quantity_second_term_prefactor* fourth_multiplicative_quantity_second_term_numerator / fourth_multiplicative_quantity_second_term_denominator

        # (8): Multiplicative Quantity Four in Whole:
        fourth_multiplicative_quantity = fourth_multiplicative_quantity_first_term + fourth_multiplicative_quantity_second_term

        # (9): Calculate the prefactor of the entire thing:
        k_squared_prefactor = squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer
    
        # (9): Calculate the final quantity: K^{2}
        k_squared = -1. * k_squared_prefactor * one_minus_x_bjorken * second_multiplicative_quantity * third_multiplicative_quantity * fourth_multiplicative_quantity

        if verbose:
            print(f"> Calculated k_squared to be:\n{k_squared}")

        # (10) Return K^{2}:
        return k_squared

    except Exception as ERROR:
        print(f"> Error in calculating K^2\n> {ERROR}")
        return 0.