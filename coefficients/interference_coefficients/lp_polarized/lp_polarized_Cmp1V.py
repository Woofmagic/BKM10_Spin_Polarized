try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_c_1_minus_plus_longitudinally_polarized_V(
    lepton_polarization: float,
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

        # (3): Calculate the first term:
        first_term = 5. - 4. * x_Bjorken + 3. * epsilon**2 - root_one_plus_epsilon_squared

        # (4): Calculate the second term:
        second_term = -1. * t_over_Q_squared * (1. - epsilon**2 - root_one_plus_epsilon_squared - 2. * x_Bjorken * (4. - 4. *  x_Bjorken - root_one_plus_epsilon_squared))

        # (5): Calculate the prefactor
        prefactor = -4. * lepton_polarization * target_polarization * lepton_energy_fraction_y * (2. - lepton_energy_fraction_y) * t_over_Q_squared / root_one_plus_epsilon_squared**5

        # (6): Calculate the coefficient:
        c_1_minus_plus_LP_V = prefactor * (first_term + second_term)

        # (6.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c_1_minus_plus_LP_V to be:\n{c_1_minus_plus_LP_V}")

        # (7): Return the coefficient:
        return c_1_minus_plus_LP_V

    except Exception as ERROR:
        print(f"> Error in calculating c_1_minus_plus_LP_V for Interference Term:\n> {ERROR}")
        return 0.