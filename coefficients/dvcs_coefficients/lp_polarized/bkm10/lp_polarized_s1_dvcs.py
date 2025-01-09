import numpy as np

from decimal import Decimal

from coefficients.dvcs_coefficients.lp_polarized.bkm10.lp_polarized_curlyC_dvcs import calculate_curly_c_longitudinally_polarized_dvcs

from form_factors.effective_cffs import compute_cff_effective

def calculate_s_1_longitudinally_polarized_dvcs(
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float, 
    skewness_parameter: float,
    shorthand_k: float,
    compton_form_factor_h: float,
    compton_form_factor_h_tilde: float,
    compton_form_factor_e: float,
    compton_form_factor_e_tilde: float,
    use_ww: bool = False,
    verbose: bool = False) -> float:
    """
    """

    try:
        
        # (1): Calculate the prefactor
        prefactor = Decimal("8. ") * target_polarization * shorthand_k * (Decimal("2.") - lepton_energy_fraction_y) / ((Decimal("2.") - x_Bjorken) * (Decimal("1.") + epsilon**2))
        
        # (3): Return the entire thing:
        s1LP_DVCS = prefactor * calculate_curly_c_longitudinally_polarized_dvcs(
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
            verbose).imag

        # (2.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated s1LP_DVCS to be:\n{s1LP_DVCS}")

        # (4): Return the coefficient:
        return s1LP_DVCS

    except Exception as ERROR:
        print(f"> Error in calculating s1LP for DVCS Amplitude Squared:\n> {ERROR}")
        return Decimal("0.0")