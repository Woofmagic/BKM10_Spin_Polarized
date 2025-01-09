from decimal import Decimal

import numpy as np

def calculate_s_1_minus_plus_longitudinally_polarized_A(
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float, 
    shorthand_K: float,
    verbose: bool = False) -> float:
    """
    """

    try:

        # (1): Calculate the recurrent quantity sqrt(1 + epsilon^2):
        root_one_plus_epsilon_squared = sqrt(Decimal("1.") + epsilon**2)

        # (2): Calculate t/Q^{2}:
        t_over_Q_squared = squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer

        # (3): Calculate 1 + sqrt(1 + epsilon^2):
        fancy_epsilon_term = Decimal("1.") + root_one_plus_epsilon_squared

        # (4): Calculate the prefactor of the first term:
        prefactor_first_term = Decimal("2.") - Decimal("2.") * lepton_energy_fraction_y + lepton_energy_fraction_y**2 + epsilon**2 * lepton_energy_fraction_y**2 / Decimal("2.0")

        # (5): Calculate the prefactor of the second term:
        prefactor_second_term = Decimal("1.") - lepton_energy_fraction_y + lepton_energy_fraction_y**2 * epsilon**2 / Decimal("4.0")

        # (6): Calculate the meat of the first term:
        main_first_term = Decimal("1.") - t_over_Q_squared * (Decimal("1.") - root_one_plus_epsilon_squared - Decimal("2.") * x_Bjorken) / fancy_epsilon_term

        # (7): Calculate the meat of the second term:
        main_second_term = Decimal("3.")  - root_one_plus_epsilon_squared - t_over_Q_squared * (Decimal("3.0") + root_one_plus_epsilon_squared - 6. * x_Bjorken)

        # (8): Calculate the bracket term in its entirety:
        bracket_term = prefactor_first_term * fancy_epsilon_term * main_first_term + prefactor_second_term * main_second_term

        # (9): Calculate the prefactor:
        prefactor = Decimal("8. ") * target_polarization * shorthand_K * x_Bjorken * t_over_Q_squared / root_one_plus_epsilon_squared**6

        # (10): Calculate entire coefficient in one:
        s_1_minus_plus_LP_A = prefactor * bracket_term
        
        # (10.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated s_1_minus_plus_LP_A to be:\n{s_1_minus_plus_LP_A}")

        # (11): Return the coefficient:
        return s_1_minus_plus_LP_A

    except Exception as ERROR:
        print(f"> Error in calculating s_1_minus_plus_LP_A for Interference Term:\n> {ERROR}")
        return Decimal("0.0")