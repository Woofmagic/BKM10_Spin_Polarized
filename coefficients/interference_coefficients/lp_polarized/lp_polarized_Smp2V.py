from decimal import Decimal

import numpy as np

def calculate_s_2_minus_plus_longitudinally_polarized_V(
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float, 
    k_tilde: float,
    verbose: bool = False) -> float:
    """
    """

    try:

        # (1): Calculate the recurrent quantity sqrt(1 + epsilon^2):
        root_one_plus_epsilon_squared = sqrt(Decimal("1.") + epsilon**2)

        # (2): Calculate t/Q^{2}:
        t_over_Q_squared = squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer

        # (3): Calculate the first two terms in the brackets:
        first_bracket_term = (Decimal("2.") - x_Bjorken) * (Decimal("1.") + root_one_plus_epsilon_squared) + epsilon**2

        # (4): Calculate the third term in the brackets (it's harder than the second):
        third_bracket_term = t_over_Q_squared * (epsilon**2 + x_Bjorken * (Decimal("3.")  - Decimal("2.") * x_Bjorken + root_one_plus_epsilon_squared))

        # (5): Calculate the second term in brackets:
        second_bracket_term = Decimal("4.") * k_tilde**2 * (Decimal("1.") - Decimal("2.") * x_Bjorken) / (squared_Q_momentum_transfer * root_one_plus_epsilon_squared)

        # (6): Calculate the prefactor:
        prefactor = Decimal("4.") * target_polarization * (Decimal("2.") - lepton_energy_fraction_y) * sqrt(Decimal("1.") - lepton_energy_fraction_y - lepton_energy_fraction_y**2 * epsilon**2 / Decimal("4.0")) / root_one_plus_epsilon_squared**5

        # (7): Calculate the coefficient:
        s_2_minus_plus_LP_V = prefactor * t_over_Q_squared * (first_bracket_term + second_bracket_term + third_bracket_term)
        
        # (7.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated s_2_minus_plus_LP_V to be:\n{s_2_minus_plus_LP_V}")

        # (8): Return the coefficient:
        return s_2_minus_plus_LP_V

    except Exception as ERROR:
        print(f"> Error in calculating s_2_minus_plus_LP_V for Interference Term:\n> {ERROR}")
        return Decimal("0.0")