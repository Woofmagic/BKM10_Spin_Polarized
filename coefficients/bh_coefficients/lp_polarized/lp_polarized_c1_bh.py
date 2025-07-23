from decimal import Decimal

from statics.masses.particle_masses import _MASS_OF_PROTON_IN_GEV

from utilities.mathematics.polarization import check_polarization_datatype

import numpy as np
    
def calculate_c_1_longitudinally_polarized_bh(
    lepton_helicity: float,
    target_polarization: float,
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
    Equation (39) of the BKM02 Formalism.

    ## Arguments:
        - lepton_helicity: (float)
        - target_polarization: (float)
        - squared_Q_momentum_transfer: (float)
        - x_Bjorken: (float)
        - squared_hadronic_momentum_transfer_t: (float)
        - epsilon: (float)
        - lepton_energy_fraction_y: (float)
        - shorthand_K: (float)
        - Dirac_form_factor_F1: (float)
        - Pauli_form_factor_F2: (float)
        - verbose: (bool)
            Debugging console output.

    ## Notes
    (1): This coefficient is in Equation (39) from
        the BKM02 Formalism, available here:
        https://arxiv.org/pdf/hep-ph/0112108.pdf
    """

    if (check_polarization_datatype(lepton_helicity) or check_polarization_datatype(target_polarization)) is False:
        raise ValueError("> Received unacceptable polarization type.")
    
    try:
        
        # (1): Calculate the common appearance of F1 + F2:
        sum_of_form_factors = (Dirac_form_factor_F1 + Pauli_form_factor_F2)

        # (2): Calculate the frequent appearance of t/4mp
        t_over_four_mp_squared = squared_hadronic_momentum_transfer_t / (4. * _MASS_OF_PROTON_IN_GEV**2)

        # (3): Calculate the weighted sum of the F1 and F2:
        weighted_sum_of_form_factors = Dirac_form_factor_F1 + t_over_four_mp_squared * Pauli_form_factor_F2

        # (4): Calculate the common appearance of delta^{2} / Q^{2} = t / Q^{2}
        t_over_Q_squared = squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer

        # (5): Calculate the first term straight away:
        first_term = ((2. * t_over_four_mp_squared) - (x_Bjorken * (1. - t_over_Q_squared))) * ((1. - x_Bjorken + (x_Bjorken * t_over_Q_squared))) * sum_of_form_factors

        # (6): Calculate the second term's bracketed quantity:
        second_term_bracket_term = 1. + x_Bjorken - ((3. - 2. * x_Bjorken) * (1. + x_Bjorken * t_over_Q_squared)) - (x_Bjorken**2 * (1. + t_over_Q_squared**2) / t_over_four_mp_squared)
        
        # (7): Calculate the second term in entirety:
        second_term = weighted_sum_of_form_factors * second_term_bracket_term
        
        # (8): Calculate the overall prefactor:
        prefactor = -8. * lepton_helicity * target_polarization * x_Bjorken * lepton_energy_fraction_y * shorthand_k * np.sqrt(1. + epsilon**2) * sum_of_form_factors / (1. - t_over_four_mp_squared)

        # (13): Calculate the entire coefficient:
        c1LP_BH = prefactor * (first_term + second_term)

        # (13.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c1LP_BH to be:\n{c1LP_BH}")

        # (14): Return the coefficient:
        return c1LP_BH

    except Exception as ERROR:
        print(f"> Error in calculating c1LP for BH Amplitude Squared:\n> {ERROR}")
        return 0.