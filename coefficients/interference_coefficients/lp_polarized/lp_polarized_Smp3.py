import numpy as np

def calculate_s_3_minus_plus_longitudinally_polarized(
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float, 
    shorthand_K: float,
    verbose: bool = False) -> float:
    """
    """

    try:

        # (1): Calculate the recurrent quantity sqrt(1 + epsilon^2):
        root_one_plus_epsilon_squared = sqrt(Decimal("1.") + epsilon**2)

        # (2): Calculate t/Q^{2}:
        t_over_Q_squared = squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer

        # (3): Calculate 1 + sqrt(1 + epsilon^2):
        one_plus_epsilon_stuff = Decimal("1.") + root_one_plus_epsilon_squared

        # (4): Calculate the major contribution:
        major_part = Decimal("2.") * one_plus_epsilon_stuff + epsilon**2 + t_over_Q_squared * (epsilon**2 + Decimal("2.") * x_Bjorken * one_plus_epsilon_stuff)

        # (5): Calculate the prefactor:
        prefactor = Decimal("4.") * target_polarization * shorthand_K * (Decimal("1.") - lepton_energy_fraction_y - lepton_energy_fraction_y**2 * epsilon**2 / Decimal("4.0")) / root_one_plus_epsilon_squared**6

        # (6): Calculate entire coefficient in one:
        s_3_minus_plus_LP = prefactor * major_part
        
        # (6.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated s_3_minus_plus_LP to be:\n{s_3_minus_plus_LP}")

        # (7): Return the coefficient:
        return s_3_minus_plus_LP

    except Exception as ERROR:
        print(f"> Error in calculating s_3_minus_plus_LP for Interference Term:\n> {ERROR}")
        return Decimal("0.0")