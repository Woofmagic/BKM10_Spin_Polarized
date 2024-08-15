try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_s_3_minus_plus_longitudinally_polarized(
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
        fancy_epsilon_term = 1. + root_one_plus_epsilon_squared

        # (4): Calculate the first term in brackets:
        bracket_term = 2. * fancy_epsilon_term + epsilon**2 + t_over_Q_squared * (epsilon**2 + 2. * x_Bjorken * fancy_epsilon_term)

        # (5): Calculate the prefactor:
        prefactor = 4. * target_polarization * shorthand_K * (1. - lepton_energy_fraction_y * lepton_energy_fraction_y**2 * epsilon**2 / 4.) / root_one_plus_epsilon_squared**6

        # (6): Calculate entire coefficient in one:
        s_3_minus_plus_LP = prefactor * bracket_term
        
        # (6.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated s_3_minus_plus_LP to be:\n{s_3_minus_plus_LP}")

        # (7): Return the coefficient:
        return s_3_minus_plus_LP

    except Exception as ERROR:
        print(f"> Error in calculating s_3_minus_plus_LP for Interference Term:\n> {ERROR}")
        return 0.