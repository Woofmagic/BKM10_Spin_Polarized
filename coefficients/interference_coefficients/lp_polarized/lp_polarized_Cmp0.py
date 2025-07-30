from decimal import Decimal

import numpy as np

def calculate_c_0_minus_plus_longitudinally_polarized(
    lepton_helicity: float,
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
        root_one_plus_epsilon_squared = np.sqrt(1. + epsilon**2)

        # (2): Calculate t/Q^{2}:
        t_over_Q_squared = squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer

        # (3): Calculate 1 - sqrt(1 + epsilon^2):
        one_minus_epsilon_stuff = 1. - root_one_plus_epsilon_squared

        # (4): Calculate the first term in brackets:
        first_bracket_term = k_tilde**2 * (2. - lepton_energy_fraction_y)**2 * one_minus_epsilon_stuff / squared_Q_momentum_transfer

        # (5): Calculate large parentheses term in second bracket term:
        second_bracket_term_last_part = one_minus_epsilon_stuff - t_over_Q_squared * (1. - 2. * x_Bjorken + root_one_plus_epsilon_squared)

        # (6): Calculate the middle part of the second bracket term:
        second_bracket_term_middle_part = 2. * x_Bjorken * t_over_Q_squared - (1. - t_over_Q_squared) * epsilon**2

        # (7): Calculate the second bracket term:
        second_bracket_term = 0.5 * (1. - lepton_energy_fraction_y - lepton_energy_fraction_y**2 * epsilon**2 / 4.) * second_bracket_term_middle_part * second_bracket_term_last_part

        # (8): Calculate the prefactor:
        prefactor = 4. * lepton_helicity * target_polarization * lepton_energy_fraction_y / root_one_plus_epsilon_squared**5
        
        # (9): Calculate the coefficient:
        c_0_minus_plus_LP = prefactor * (first_bracket_term + second_bracket_term)

        # (9.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c_0_minus_plus_LP to be:\n{c_0_minus_plus_LP}")

        # (10): Return the coefficient:
        return c_0_minus_plus_LP

    except Exception as ERROR:
        print(f"> Error in calculating c_0_minus_plus_LP for Interference Term:\n> {ERROR}")
        return 0.