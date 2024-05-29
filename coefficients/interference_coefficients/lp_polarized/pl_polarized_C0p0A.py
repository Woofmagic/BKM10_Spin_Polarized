try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

from coefficients.interference_coefficients.lp_polarized.pl_polarized_C0p0 import calculate_c_0_zero_plus_longitudinally_polarized

def calculate_c_0_zero_plus_longitudinally_polarized_A(
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

        # (1): Calculate the modulation to C_{0+}^{LP, A}:
        modulating_factor = -1. * (x_Bjorken * (1. + (squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer))) / (1. - x_Bjorken)

        # (2): Calculate the C_{0+}^{LP} coefficient:
        c_0_zero_plus_LP = calculate_c_0_zero_plus_longitudinally_polarized(
            lepton_polarization,
            target_polarization,
            squared_Q_momentum_transfer, 
            x_Bjorken, 
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y, 
            shorthand_k,
            verbose
        )

        # (3): Calculate everything:
        c_0_zero_plus_A_LP = c_0_zero_plus_LP * modulating_factor

        # (3.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c_0_zero_plus_A_LP to be: {c_0_zero_plus_A_LP}")

        # (4): Return the coefficient:
        return c_0_zero_plus_A_LP

    except Exception as ERROR:
        print(f"> Error in calculating c_0_zero_plus_A_LP for Interference Term:\n> {ERROR}")
        return 0.