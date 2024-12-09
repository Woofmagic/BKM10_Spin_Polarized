from decimal import Decimal

try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_s_2_plus_plus_longitudinally_polarized_V(
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float, 
    t_prime: float,
    k_tilde: float,
    verbose: bool = False) -> float:
    """
    """

    try:

        # (1): Calculate the recurrent quantity sqrt(1 + epsilon^2):
        root_one_plus_epsilon_squared = sqrt(Decimal("1.") + epsilon**2)

        # (2): Calculate the first contribution to the bracket term:
        bracket_term_second_term = (Decimal("3.")  - root_one_plus_epsilon_squared - (Decimal("2.") * x_Bjorken) + (epsilon**2 / x_Bjorken)) * x_Bjorken * t_prime / squared_Q_momentum_transfer

        # (3): Calculate second contribution to the bracket term:
        bracket_term_first_term = Decimal("4.") * k_tilde**2 * (Decimal("1.") - Decimal("2.") * x_Bjorken) / (root_one_plus_epsilon_squared * squared_Q_momentum_transfer)

        # (4): Calculate the bracket term:
        bracket_term = squared_hadronic_momentum_transfer_t * (bracket_term_first_term - bracket_term_second_term) / squared_Q_momentum_transfer

        # (5): Calculate the prefactor:
        prefactor = Decimal("4.") * target_polarization * (Decimal("2.") - lepton_energy_fraction_y) * (Decimal("1.") - lepton_energy_fraction_y - epsilon**2 * lepton_energy_fraction_y**2 / Decimal("4.0")) / root_one_plus_epsilon_squared**5

        # (6): Calculate the coefficient
        s_2_plus_plus_V_LP = prefactor * bracket_term

        # (6.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated s_2_plus_plus_V_LP to be:\n{s_2_plus_plus_V_LP}")

        # (7): Return the coefficient:
        return s_2_plus_plus_V_LP

    except Exception as ERROR:
        print(f"> Error in calculating s_2_plus_plus_V_LP for Interference Term:\n> {ERROR}")
        return Decimal("0.0")