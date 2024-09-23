try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_c_0_minus_plus_longitudinally_polarized_V(
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

        # (3): Calculate first part of the first term:
        first_term_first_part = (4. - 2. * x_Bjorken + 3. * epsilon**2) * (1. - lepton_energy_fraction_y - lepton_energy_fraction_y**2 * epsilon**2 / 4.)

        # (4): Calculate second  part of the first term:
        first_term_second_part =  1. + t_over_Q_squared * (4. * x_Bjorken * (1. - x_Bjorken) + epsilon**2) / (4. - 2. * x_Bjorken + 3. * epsilon**2)

        # (5): Calculate the third part of the first term:
        first_term_third_part = root_one_plus_epsilon_squared - 1. + t_over_Q_squared * (1. - 2. * x_Bjorken + root_one_plus_epsilon_squared)

        # (6): Calculate the first term:
        first_term = first_term_first_part * first_term_second_part * first_term_third_part

        # (7): Calculate the second term:
        second_term = 2. * (2. - lepton_energy_fraction_y)**2 * (root_one_plus_epsilon_squared - 1. + 2. * x_Bjorken) * k_tilde**2 / squared_Q_momentum_transfer

        # (8): Calculate the prefactor:
        prefactor = 2. * lepton_helicity * target_polarization * lepton_helicity * t_over_Q_squared / root_one_plus_epsilon_squared**5

        # (9): Calculate the coefficient:
        c_0_minus_plus_LP_V = prefactor * (first_term + second_term)

        # (9.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c_0_minus_plus_LP_V to be:\n{c_0_minus_plus_LP_V}")

        # (10): Return the coefficient:
        return c_0_minus_plus_LP_V

    except Exception as ERROR:
        print(f"> Error in calculating c_0_minus_plus_LP_V for Interference Term:\n> {ERROR}")
        return 0.