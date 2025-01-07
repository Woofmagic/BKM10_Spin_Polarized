try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_c_0_plus_plus_longitudinally_polarized(
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
        root_one_plus_epsilon_squared = sqrt(Decimal("1.") + epsilon**2)

        # (2): Calculate the recurrent quantity t/Q^{2}:
        t_over_Q_squared = squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer

        # (3): Calculate the first term in the brackets: 
        first_bracket_term = (Decimal("2.") - lepton_energy_fraction_y)**2 * k_tilde**2 / squared_Q_momentum_transfer

        # (4): Calculate the first part of the second term in brackets:
        second_bracket_term_first_part = Decimal("1.") - lepton_energy_fraction_y + (epsilon**2 * lepton_energy_fraction_y**2 / Decimal("4.0"))

        # (5): Calculate the second part of the second term in brackets:
        second_bracket_term_second_part = x_Bjorken * t_over_Q_squared - (epsilon**2 * (Decimal("1.") - t_over_Q_squared) / Decimal("2.0"))

        # (6): Calculate the third part of the second term in brackets:
        second_bracket_term_third_part = Decimal("1.") + t_over_Q_squared * (root_one_plus_epsilon_squared - Decimal("1.") + Decimal("2.") * x_Bjorken / (Decimal("1.") + root_one_plus_epsilon_squared))

        # (7): Stitch together the second bracket term:
        second_bracket_term = second_bracket_term_first_part * second_bracket_term_second_part * second_bracket_term_third_part

        # (8): Calculate the prefactor:
        prefactor = Decimal("4.") * lepton_helicity * target_polarization * lepton_energy_fraction_y * (Decimal("1.") + root_one_plus_epsilon_squared) / root_one_plus_epsilon_squared**5

        # (9): Calculate the entire thing:
        c_0_plus_plus_LP = prefactor * (first_bracket_term + second_bracket_term)

        # (9.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c_0_plus_plus_LP to be:\n{c_0_plus_plus_LP}")

        # (10): Return the coefficient:
        return c_0_plus_plus_LP

    except Exception as ERROR:
        print(f"> Error in calculating c_0_plus_plus_LP for Interference Term:\n> {ERROR}")
        return Decimal("0.0")