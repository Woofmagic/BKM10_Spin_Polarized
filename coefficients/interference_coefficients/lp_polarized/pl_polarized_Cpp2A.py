from decimal import Decimal

import numpy as np

def calculate_c_2_plus_plus_longitudinally_polarized_A(
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
        root_one_plus_epsilon_squared = sqrt(Decimal("1.") + epsilon**2)

        # (2): Calculate the recurrent quantity t/Q^{2}
        t_over_Q_squared = squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer

        # (3): Calculate the recurrent quantity 1 + sqrt(1 + epsilon^2):
        one_plus_root_epsilon_stuff = Decimal("1.") + root_one_plus_epsilon_squared

        # (4): Calculate one of the multiplicative factors:
        first_multiplicative_factor = (Decimal("1.") - root_one_plus_epsilon_squared) - t_over_Q_squared * (one_plus_root_epsilon_stuff - Decimal("2.") * x_Bjorken)

        # (5): Calculate the second multiplicative factor:
        second_multiplicative_factor = x_Bjorken * t_over_Q_squared * (Decimal("1.") - t_over_Q_squared * (Decimal("1.") - Decimal("2.") * x_Bjorken))

        # (6): Calculate the prefactor:
        prefactor = Decimal("4.") * lepton_helicity * target_polarization * lepton_energy_fraction_y * (Decimal("1.") - lepton_energy_fraction_y - (lepton_energy_fraction_y**2 * epsilon**2 / Decimal("4.0"))) / root_one_plus_epsilon_squared**5

        # (7): Calculate the entire thing:
        c_2_plus_plus_A_LP = prefactor * first_multiplicative_factor * second_multiplicative_factor

        # (7.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c_2_plus_plus_A_LP to be:\n{c_2_plus_plus_A_LP}")

        # (8): Return the coefficient:
        return c_2_plus_plus_A_LP

    except Exception as ERROR:
        print(f"> Error in calculating c_2_plus_plus_A_LP for Interference Term:\n> {ERROR}")
        return Decimal("0.0")