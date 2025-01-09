import numpy as np

def calculate_c_2_minus_plus_longitudinally_polarized(
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

        # (2): Calculate t/Q^{2}:
        t_over_Q_squared = squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer

        # (3): Calculate the first term:
        first_term = epsilon**2 * (Decimal("1.") + root_one_plus_epsilon_squared)

        # (4): Calculate the second term:
        second_term = Decimal("2.") * t_over_Q_squared * ((Decimal("1.") - x_Bjorken) * epsilon**2 + x_Bjorken * (Decimal("1.") + root_one_plus_epsilon_squared))

        # (5): Calculate the third term:
        third_term = t_over_Q_squared**2 * (Decimal("2.") * x_Bjorken + epsilon**2) * (Decimal("1.") - Decimal("2.") * x_Bjorken - root_one_plus_epsilon_squared)

        # (6): Calculate the prefactor:
        prefactor = Decimal("2.") * lepton_helicity * target_polarization * lepton_energy_fraction_y * (Decimal("1.") - lepton_energy_fraction_y - (lepton_energy_fraction_y**2 * epsilon**2 / Decimal("4.0"))) / root_one_plus_epsilon_squared**5

        # (7): Calculate the coefficient:
        c_3_minus_plus_LP = prefactor * (first_term + second_term + third_term)

        # (7.1): If verbose, log the output:
        if verbose:
            print(f"> c_3_minus_plus_LP c_3_minus_plus_LP to be:\n{c_3_minus_plus_LP}")

        # (8): Return the coefficient:
        return c_3_minus_plus_LP

    except Exception as ERROR:
        print(f"> Error in calculating c_3_minus_plus_LP for Interference Term:\n> {ERROR}")
        return Decimal("0.0")