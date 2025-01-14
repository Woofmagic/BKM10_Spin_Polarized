from decimal import Decimal

import numpy as np

def calculate_s_2_minus_plus_longitudinally_polarized(
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float, 
    verbose: bool = False) -> float:
    """
    """

    try:

        # (1): Calculate the recurrent quantity sqrt(1 + epsilon^2):
        root_one_plus_epsilon_squared = np.sqrt(1. + epsilon**2)

        # (2): Calculate t/Q^{2}:
        t_over_Q_squared = squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer

        # (3): Calculate one plus sqrt(1 + epsilon^2):
        fancy_epsilon_term = 1. + root_one_plus_epsilon_squared

        # (4): Calculate the first bracket term:
        first_bracket_term = t_over_Q_squared * (2. * fancy_epsilon_term + epsilon**2 * root_one_plus_epsilon_squared - x_Bjorken * (3. * (1. + root_one_plus_epsilon_squared) - epsilon**2))
        
        # (5): Calculate the second term:
        second_bracket_term = t_over_Q_squared**2 * (epsilon**2 - 2. * x_Bjorken**2 * (2. + root_one_plus_epsilon_squared) + x_Bjorken * (3.  - epsilon**2 + root_one_plus_epsilon_squared))
        
        # (6): Combine all the terms:
        entire_bracket_term = first_bracket_term + second_bracket_term + epsilon**2 * fancy_epsilon_term

        # (7): Calculate the prefactor:
        prefactor = 4. * target_polarization * (2. - lepton_energy_fraction_y) * (1. - lepton_energy_fraction_y - (lepton_energy_fraction_y**2 * epsilon**2 / 4.)) / root_one_plus_epsilon_squared**6

        # (8): Calculate the coefficient:
        s_2_minus_plus_LP = prefactor * entire_bracket_term

        # (8.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated s_2_minus_plus_LP to be:\n{s_2_minus_plus_LP}")

        # (9): Return the coefficient:
        return s_2_minus_plus_LP

    except Exception as ERROR:
        print(f"> Error in calculating s_2_minus_plus_LP for Interference Term:\n> {ERROR}")
        return 0.