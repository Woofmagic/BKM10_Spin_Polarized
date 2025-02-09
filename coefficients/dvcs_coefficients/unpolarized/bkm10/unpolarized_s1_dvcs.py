from decimal import Decimal

import numpy as np

from form_factors.effective_cffs import compute_cff_effective

from coefficients.dvcs_coefficients.unpolarized.bkm10.unpolarized_curlyC_dvcs import calculate_curly_c_unpolarized_dvcs

def calculate_s_1_unpolarized_dvcs(
    lepton_helicity: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float, 
    skewness_parameter: float,
    shorthand_k: float,
    compton_form_factor_h: complex,
    compton_form_factor_h_tilde: complex,
    compton_form_factor_e: complex,
    compton_form_factor_e_tilde: complex,
    use_ww: bool = False,
    verbose: bool = False) -> float:
    """
    """

    try:

        # (1): Calculate the first term's prefactor:
        prefactor = Decimal("8. ") * shorthand_k * lepton_helicity * lepton_energy_fraction_y * (Decimal("1.") + epsilon**2).sqrt() / ((Decimal("2.") - x_Bjorken) * (Decimal("1.") + epsilon**2))

        # (2): Calculate the second terms' Curly C contribution:
        curlyC_unp_DVCS = calculate_curly_c_unpolarized_dvcs(
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            compute_cff_effective(skewness_parameter, compton_form_factor_h, use_ww),
            compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde, use_ww),
            compute_cff_effective(skewness_parameter, compton_form_factor_e, use_ww),
            compute_cff_effective(skewness_parameter, compton_form_factor_e_tilde, use_ww),
            compton_form_factor_h.conjugate(),
            compton_form_factor_h_tilde.conjugate(),
            compton_form_factor_e.conjugate(),
            compton_form_factor_e_tilde.conjugate(),
        ).imag

        # (3): Calculate the entire coefficient:
        s1_dvcs_unpolarized_coefficient = prefactor * curlyC_unp_DVCS
        
        if verbose:
            print(f"> Calculated s1_dvcs_unpolarized_coefficient to be: {s1_dvcs_unpolarized_coefficient}")

        return s1_dvcs_unpolarized_coefficient
    
    except Exception as E:
        print(f"> Error in computing s1_dvcs_unpolarized_coefficient:\n> {E}")
        return Decimal("0.0")