try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_c_2_minus_plus_longitudinally_polarized_V(
    lepton_helicity: float,
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

        # (3): Calculate the first factor:
        first_factor = 4. - 2. * x_Bjorken + 3. * epsilon**2 + t_over_Q_squared * (4. * x_Bjorken * (1. - x_Bjorken) + epsilon**2)

        # (4): Calculate the second factor:
        second_factor = 1. + root_one_plus_epsilon_squared - t_over_Q_squared * (1. - root_one_plus_epsilon_squared - 2. * x_Bjorken)

        # (5): Calculate the prefactor
        prefactor = -2. * lepton_helicity * target_polarization * lepton_energy_fraction_y * (1. - lepton_energy_fraction_y - (lepton_energy_fraction_y**2 * epsilon**2 / 4.)) * t_over_Q_squared / root_one_plus_epsilon_squared**5

        # (6): Calculate the coefficient:
        c_2_minus_plus_LP_V = prefactor * first_factor * second_factor

        # (6.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c_2_minus_plus_LP_V to be:\n{c_2_minus_plus_LP_V}")

        # (7): Return the coefficient:
        return c_2_minus_plus_LP_V

    except Exception as ERROR:
        print(f"> Error in calculating c_2_minus_plus_LP_V for Interference Term:\n> {ERROR}")
        return 0.