try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_s_2_minus_plus_longitudinally_polarized_V(
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float, 
    k_tilde: float,
    verbose: bool = True) -> float:
    """
    """

    try:

        # (1): Calculate the recurrent quantity sqrt(1 + epsilon^2):
        root_one_plus_epsilon_squared = np.sqrt(1. + epsilon**2)

        # (2): Calculate t/Q^{2}:
        t_over_Q_squared = squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer

        # (3): Calculate the first two terms in the brackets:
        first_bracket_term = (2. - x_Bjorken) * (1. + root_one_plus_epsilon_squared) + epsilon**2

        # (4): Calculate the third term in the brackets (it's harder than the second):
        third_bracket_term = t_over_Q_squared * (epsilon**2 + x_Bjorken * (3. - 2. * x_Bjorken + root_one_plus_epsilon_squared))

        # (5): Calculate the second term in brackets:
        second_bracket_term = 4. * k_tilde**2 * (1. - 2. * x_Bjorken) / (squared_Q_momentum_transfer * root_one_plus_epsilon_squared)

        # (6): Calculate the prefactor:
        prefactor = -4. * target_polarization * (2. - lepton_energy_fraction_y) * np.sqrt(1. - lepton_energy_fraction_y * lepton_energy_fraction_y**2 * epsilon**2 / 4.) / root_one_plus_epsilon_squared**5

        # (7): Calculate the coefficient:
        s_2_minus_plus_LP_V = prefactor * t_over_Q_squared * (first_bracket_term + second_bracket_term + third_bracket_term)
        
        # (7.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated s_2_minus_plus_LP_V to be:\n{s_2_minus_plus_LP_V}")

        # (8): Return the coefficient:
        return s_2_minus_plus_LP_V

    except Exception as ERROR:
        print(f"> Error in calculating s_2_minus_plus_LP_V for Interference Term:\n> {ERROR}")
        return 0.