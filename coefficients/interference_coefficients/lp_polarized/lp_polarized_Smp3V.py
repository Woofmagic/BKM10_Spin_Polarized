try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_s_3_plus_plus_longitudinally_polarized_V(
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float,
    t_prime: float,
    shorthand_k: float,
    verbose: bool = False) -> float:
    """
    """

    try:

        # (1): Calculate the recurrent quantity sqrt(1 + epsilon^2):
        root_one_plus_epsilon_squared = np.sqrt(1. + epsilon**2)

        # (2): Calculate the recurrent quantity 1 - x_{B}
        one_minus_xb = 1. - x_Bjorken

        # (3): Calculate the bracket term:
        bracket_term = 4. * one_minus_xb + t_prime * (4. * one_minus_xb * x_Bjorken + epsilon**2) / (squared_Q_momentum_transfer * root_one_plus_epsilon_squared)

        # (4): Calcualte the prefactor:
        prefactor = -4. * target_polarization * shorthand_k * (1. - lepton_energy_fraction_y - lepton_energy_fraction_y**2 * epsilon**2 / 4.) / root_one_plus_epsilon_squared**5

        # (5): Calculate the entire thing:
        s_3_plus_plus_LP_V = prefactor * squared_hadronic_momentum_transfer_t * bracket_term / squared_Q_momentum_transfer

        # (5.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated s_3_plus_plus_LP_V to be:\n{s_3_plus_plus_LP_V}")

        # (6): Return the coefficient:
        return s_3_plus_plus_LP_V

    except Exception as ERROR:
        print(f"> Error in calculating s_3_plus_plus_LP_V for Interference Term:\n> {ERROR}")
        return 0.