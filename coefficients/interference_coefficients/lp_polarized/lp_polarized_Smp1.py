try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_s_1_minus_plus_longitudinally_polarized(
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float, 
    shorthand_K: float,
    verbose: bool = True) -> float:
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
        first_bracket_term = (2. - lepton_energy_fraction_y)**2 * (one_minus_epsilon_stuff + 2. * epsilon**2 + t_over_Q_squared * (one_minus_epsilon_stuff - 2. * x_Bjorken))

        # (5): Calculate the inner part of the second bracket term:
        second_bracket_term_inner_part = epsilon**2 - 4. * root_one_plus_epsilon_squared + 2. * x_Bjorken * (1. + root_one_plus_epsilon_squared)

        # (6): Calculate the outer part of the second bracket term:
        second_bracket_term_outer_part = 2. + epsilon**2 - 2. * root_one_plus_epsilon_squared + t_over_Q_squared * second_bracket_term_inner_part

        # (7): Calculate the prefactor of the second bracket term:
        second_bracket_term_prefactor = -1. * (1. - lepton_energy_fraction_y - lepton_energy_fraction_y**2 * epsilon**2 / 4.)

        # (8): Calculate entire coefficient in one:
        s_1_minus_plus_LP = -4. * target_polarization * shorthand_K * (first_bracket_term + second_bracket_term_prefactor * second_bracket_term_outer_part) / root_one_plus_epsilon_squared**6
        
        # (8.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated s_1_minus_plus_LP to be:\n{s_1_minus_plus_LP}")

        # (9): Return the coefficient:
        return s_1_minus_plus_LP

    except Exception as ERROR:
        print(f"> Error in calculating s_1_minus_plus_LP for Interference Term:\n> {ERROR}")
        return 0.