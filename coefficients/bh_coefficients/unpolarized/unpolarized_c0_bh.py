import numpy as np

from statics.masses.particle_masses import _MASS_OF_PROTON_IN_GEV

def calculate_c_0_unpolarized_bh(
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
    ## Description
    Equation (35) of the BKM02 Formalism.

    ## Arguments:
        
    ## Returns:

    ## Notes:
    (1): This coefficient is in Equation (35) from
        this paper:
        https://arxiv.org/pdf/hep-ph/0112108.pdf
    """

    try:

        # (1): Calculate the common appearance of F1 + F2:
        addition_of_form_factors_squared = (Dirac_form_factor_F1 + Pauli_form_factor_F2)**2

        # (2): Calculate the common appearance of a weighted sum of F1 and F2:
        weighted_combination_of_form_factors = Dirac_form_factor_F1**2 - (squared_hadronic_momentum_transfer_t * Pauli_form_factor_F2**2 / (4. * _MASS_OF_PROTON_IN_GEV**2))

        # (3): Calculate the common appearance of delta^{2} / Q^{2} = t / Q^{2}
        t_over_Q_squared = squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer
        
        # (4):  The first line that contributes to c^{(0)}_{BH}:
        first_line = 8. * shorthand_k**2 * (((2. + 3. * epsilon**2) * weighted_combination_of_form_factors / t_over_Q_squared) + (2. * x_Bjorken**2 * addition_of_form_factors_squared))

        # (5): The first part of the second line:
        second_line_first_part = (2. + epsilon**2) * ((4. * x_Bjorken**2 * _MASS_OF_PROTON_IN_GEV**2 / squared_hadronic_momentum_transfer_t) * (1. + t_over_Q_squared)**2 + 4. * (1 - x_Bjorken) * (1. + (x_Bjorken * t_over_Q_squared))) * weighted_combination_of_form_factors
        
        # (6): The second part of the second line:
        second_line_second_part = 4. * x_Bjorken**2 * (x_Bjorken + (1. - x_Bjorken + (epsilon**2 / 2.)) * (1 - t_over_Q_squared)**2 - x_Bjorken * (1. - 2. * x_Bjorken) * t_over_Q_squared**2) * addition_of_form_factors_squared

        # (7): The second line in its entirety, which is just a prefactor times the addition of the two parts calculated earlier:
        second_line = (2. - lepton_energy_fraction_y)**2 * (second_line_first_part + second_line_second_part)

        # (8): The third line:
        third_line = 8. * (1. + epsilon**2) * (1. - lepton_energy_fraction_y - (epsilon**2 * lepton_energy_fraction_y**2 / 4.)) * (2. * epsilon**2 * (1 - (squared_hadronic_momentum_transfer_t / (4. * _MASS_OF_PROTON_IN_GEV**2))) * weighted_combination_of_form_factors - x_Bjorken**2 * (1 - t_over_Q_squared)**2 * addition_of_form_factors_squared)

        # (9): Add everything up to obtain the first coefficient:
        c0_unpolarized_BH = first_line + second_line + third_line

        # (9.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c0_unpolarized_BH to be:\n{c0_unpolarized_BH}")

        # (10): Return the coefficient:
        return c0_unpolarized_BH
    
    except Exception as ERROR:
        print(f"> Error in computing c0_unpolarized_BH:\n> {ERROR}")
        return 0.