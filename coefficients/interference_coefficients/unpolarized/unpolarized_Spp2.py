try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_s_2_plus_plus_unpolarized(
    lepton_helicity: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    epsilon: float,
    lepton_energy_fraction_y: float,
    t_prime: float,
    verbose: bool = False) -> float:
    """
    """

    try:

        # (1): Calculate the recurrent quantity sqrt(1 + epsilon^2):
        root_one_plus_epsilon_squared = sqrt(Decimal("1.") + epsilon**2)

        # (2): Calculate the quantity t'/Q^{2}:
        tPrime_over_Q_squared = t_prime / squared_Q_momentum_transfer

        # (3): Calculate a fancy, annoying quantity:
        fancy_y_stuff = Decimal("1.") - lepton_energy_fraction_y - epsilon**2 * lepton_energy_fraction_y**2 / Decimal("4.0")

        # (4): Calculate the first bracket term:
        first_bracket_term = (epsilon**2 - x_Bjorken * (root_one_plus_epsilon_squared - 1.)) / (Decimal("1.") + root_one_plus_epsilon_squared - Decimal("2.") * x_Bjorken)

        # (5): Calculate the second bracket term:
        second_bracket_term = (Decimal("2.") * x_Bjorken + epsilon**2) * tPrime_over_Q_squared / (Decimal("2.") * root_one_plus_epsilon_squared)

        # (6): Calculate the prefactor:
        prefactor = -Decimal("4.") * lepton_helicity * fancy_y_stuff * lepton_energy_fraction_y * (Decimal("1.") + root_one_plus_epsilon_squared - Decimal("2.") * x_Bjorken) * tPrime_over_Q_squared/ root_one_plus_epsilon_squared**3

        # (7): Calculate the coefficient
        s_2_plus_plus_unp = prefactor * (first_bracket_term + second_bracket_term)
        
        # (7.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated s_2_plus_plus_unp to be: {s_2_plus_plus_unp}")

        # (6): Return the coefficient:
        return s_2_plus_plus_unp

    except Exception as ERROR:
        print(f"> Error in calculating s_2_plus_plus_unp for Interference Term:\n> {ERROR}")
        return Decimal("0.0")