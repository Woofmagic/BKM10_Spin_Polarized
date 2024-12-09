try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_c_0_plus_plus_unpolarized_V(
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

        # (3): Calculate the recurrent quantity 1 + sqrt(1 + epsilon^2):
        one_plus_root_epsilon_stuff = Decimal("1.") + root_one_plus_epsilon_squared

        # (4): Compute the first term in the brackets:
        first_term_in_brackets = (Decimal("2.") - lepton_energy_fraction_y)**2 * k_tilde**2 / (root_one_plus_epsilon_squared * squared_Q_momentum_transfer)

        # (5): First multiplicative term in the second term in the brackets:
        second_term_first_multiplicative_term = Decimal("1.") - lepton_energy_fraction_y - (epsilon**2 * lepton_energy_fraction_y**2 / Decimal("4.0"))

        # (6): Second multiplicative term in the second term in the brackets:
        second_term_second_multiplicative_term = one_plus_root_epsilon_stuff / Decimal("2.0")

        # (7): Third multiplicative term in the second term in the brackets:
        second_term_third_multiplicative_term = Decimal("1.") + t_over_Q_squared

        # (8): Fourth multiplicative term numerator in the second term in the brackets:
        second_term_fourth_multiplicative_term = Decimal("1.") + (root_one_plus_epsilon_squared - Decimal("1.") + (Decimal("2.") * x_Bjorken)) * t_over_Q_squared / one_plus_root_epsilon_stuff

        # (9): Fourth multiplicative term in its entirety:
        second_term_in_brackets = second_term_first_multiplicative_term * second_term_second_multiplicative_term * second_term_third_multiplicative_term * second_term_fourth_multiplicative_term

        # (10): The prefactor in front of the brackets:
        coefficient_prefactor = Decimal("8. ") * (Decimal("2.") - lepton_energy_fraction_y) * x_Bjorken * t_over_Q_squared / root_one_plus_epsilon_squared**4

        # (11): The entire thing:
        c_0_plus_plus_V_unp = coefficient_prefactor * (first_term_in_brackets + second_term_in_brackets)

        # (11.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c_0_plus_plus_V_unp to be:\n{c_0_plus_plus_V_unp}")

        # (12): Return the coefficient:
        return c_0_plus_plus_V_unp

    except Exception as ERROR:
        print(f"> Error in calculating c_0_plus_plus_V_unp for Interference Term:\n> {ERROR}")
        return Decimal("0.0")