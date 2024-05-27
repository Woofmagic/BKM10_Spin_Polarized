try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

from statics.masses.particle_masses import _MASS_OF_PROTON_IN_GEV

def calculate_c_2_unpolarized_bh( 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    k_shorthand: float,
    Dirac_form_factor_F1: float, 
    Pauli_form_factor_F2: float, 
    verbose: bool = True) -> float:
    """
    Description
    --------------
    Equation (36) of the BH02 Formalism.

    Parameters
    --------------
    x_Bjorken: (float)

    squared_hadronic_momentum_transfer_t: (float)

    k_shorthand: (float)

    Dirac_form_factor_F1: (float)

    Pauli_form_factor_F2: (float)

    verbose: (bool)
        Debugging console output.

    Notes
    --------------
    (1): This coefficient is in Equation (37) from
        this paper:
        https://arxiv.org/pdf/hep-ph/0112108.pdf
    """

    try:

        # (1): Calculate the common appearance of F1 + F2:
        addition_of_form_factors_squared = (Dirac_form_factor_F1 + Pauli_form_factor_F2)**2

        # (2): Calculate the common appearance of a weighted sum of F1 and F2:
        weighted_combination_of_form_factors = Dirac_form_factor_F1**2 - ((squared_hadronic_momentum_transfer_t/ (4. * _MASS_OF_PROTON_IN_GEV**2)) * Pauli_form_factor_F2**2)
        
        # (3): A quick scaling of the weighted sum of F1 and F2:
        first_part_of_contribution = (4. * _MASS_OF_PROTON_IN_GEV**2 / squared_hadronic_momentum_transfer_t) * weighted_combination_of_form_factors
        
        # (4):  Multiply by the prefactor to obtain the coefficient.
        c2_unpolarized_BH = 8. * x_Bjorken**2 * k_shorthand**2 * (first_part_of_contribution + 2. * addition_of_form_factors_squared)
        
        # (4.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c2_unpolarized_BH to be: {c2_unpolarized_BH}")

        # (5): Return the coefficient:
        return c2_unpolarized_BH
    
    except Exception as E:
        print(f"> Error in computing c2_unpolarized_BH:\n> {E}")
        return 0.