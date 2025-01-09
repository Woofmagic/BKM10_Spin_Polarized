import numpy as np

from statics.masses.particle_masses import _MASS_OF_PROTON_IN_GEV

def calculate_c_1_unpolarized_bh(
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float,
    shorthand_k: float,
    Dirac_form_factor_F1: float, 
    Pauli_form_factor_F2: float, 
    verbose: bool = False) -> float:
    """
    # Title: `calculate_c_1_unpolarized_bh`

    ## Description:
    Numerically evaluate Equation (36) of the BH02 Formalism.

    ## Arguments:
    squared_Q_momentum_transfer: (float)

    x_Bjorken: (float)

    squared_hadronic_momentum_transfer_t: (float)

    epsilon: (float)

    lepton_energy_fraction_y: (float)

    shorthand_k: (float)

    Dirac_form_factor_F1: (float)

    Pauli_form_factor_F2: (float)

    verbose: (bool)
        Debugging console output.

    Notes
    --------------
    (1): This coefficient is in Equation (36) from
        this paper:
        https://arxiv.org/pdf/hep-ph/0112108.pdf
    """

    try:

        # (1): Calculate the common appearance of F1 + F2:
        addition_of_form_factors_squared = (Dirac_form_factor_F1 + Pauli_form_factor_F2)**2

        # (2): Calculate the common appearance of a weighted sum of F1 and F2:
        weighted_combination_of_form_factors = Dirac_form_factor_F1**2 - ((squared_hadronic_momentum_transfer_t / (Decimal("4.") * _MASS_OF_PROTON_IN_GEV**2)) * Pauli_form_factor_F2**2)
        
        # (3):  The first part of the first line:
        first_line_first_part = ((Decimal("4.") * x_Bjorken**2 * _MASS_OF_PROTON_IN_GEV**2 / squared_hadronic_momentum_transfer_t) - Decimal("2.") * x_Bjorken - epsilon**2) * weighted_combination_of_form_factors
        
        # (4): The first part of the second line:
        first_line_second_part = Decimal("2.") * x_Bjorken**2 * (Decimal("1.") - (Decimal("1.") - Decimal("2.") * x_Bjorken) * (squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer)) * addition_of_form_factors_squared

        # (5): Multiply by the prefactor to obtain c^{(1)}_{BH}
        c1_unpolarized_BH = Decimal("8. ") * shorthand_k * (Decimal("2.") - lepton_energy_fraction_y) * (first_line_first_part + first_line_second_part)
        
        # (5.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c1_unpolarized_BH to be:\n{c1_unpolarized_BH}")

        # (6): Return the coefficient:
        return c1_unpolarized_BH
    
    except Exception as ERROR:
        print(f"> Error in computing c1_unpolarized_BH:\n> {ERROR}")
        return Decimal("0.0")