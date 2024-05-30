try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_c_2_zero_plus_longitudinally_polarized(
    lepton_polarization: float,
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float, 
    shorthand_k: float,
    verbose: bool = True) -> float:
    """
    """

    try:

        # (1): Calculate the annoying quantity sqrt(1 - y - y^{2} epsilon^{2} / 2)
        root_combination_of_y_and_epsilon = np.sqrt(1. - lepton_energy_fraction_y - (lepton_energy_fraction_y**2 * epsilon**2 / 4.))

        # (2): Calculate the "prefactor":
        prefactor = -8. * np.sqrt(2.) * lepton_polarization * target_polarization * shorthand_k * lepton_energy_fraction_y / (1. + epsilon**2)**2

        # (3): Calculate everything:
        c_2_zero_plus_LP = prefactor * root_combination_of_y_and_epsilon * (1. + x_Bjorken * squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer)

        # (3.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c_2_zero_plus_LP to be:\n{c_2_zero_plus_LP}")

        # (4): Return the coefficient:
        return c_2_zero_plus_LP

    except Exception as ERROR:
        print(f"> Error in calculating c_2_zero_plus_LP for Interference Term:\n> {ERROR}")
        return 0.