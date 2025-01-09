from decimal import Decimal

import numpy as np

def calculate_c_1_minus_plus_longitudinally_polarized_A(
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

        # (1): Calculate t/Q^{2}:
        t_over_Q_squared = squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer

        # (2): Calculate the multiplicative part of it:
        main_part = t_over_Q_squared * (Decimal("1.") - (Decimal("1.") - Decimal("2.") * x_Bjorken) * t_over_Q_squared)

        # (3): Calculate the prefactor:
        prefactor = Decimal("16. ") * lepton_helicity * target_polarization * x_Bjorken * lepton_energy_fraction_y * (Decimal("2.") - lepton_energy_fraction_y) / (Decimal("1.") + epsilon**2)**2.5

        # (4): Calculate the coefficient:
        c_1_minus_plus_LP_A = prefactor * main_part

        # (4.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c_1_minus_plus_LP_A to be:\n{c_1_minus_plus_LP_A}")

        # (5): Return the coefficient:
        return c_1_minus_plus_LP_A

    except Exception as ERROR:
        print(f"> Error in calculating c_1_minus_plus_LP_A for Interference Term:\n> {ERROR}")
        return Decimal("0.0")