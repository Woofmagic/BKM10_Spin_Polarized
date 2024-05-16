try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

from lp_polarized_curlyC_dvcs import calculate_curly_c_longitudinally_polarized_dvcs

from form_factors.effective_cffs import compute_cff_effective

def calculate_s_1_longitudinally_polarized_dvcs(
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float, 
    skewness_parameter: float,
    k_shorthand: float,
    compton_form_factor_h_real_part: float,
    compton_form_factor_h_tilde_real_part: float,
    compton_form_factor_e_real_part: float,
    compton_form_factor_e_tilde_real_part: float,
    compton_form_factor_h_imaginary_part: float,
    compton_form_factor_h_tilde_imaginary_part: float,
    compton_form_factor_e_imaginary_part: float,
    compton_form_factor_e_tilde_imaginary_part: float,
    verbose: bool = True) -> float:
    """
    """

    try:
        
        # (1): Calculate the prefactor
        prefactor = -8. * target_polarization * k_shorthand * (2. - lepton_energy_fraction_y) / ((2. - x_Bjorken) * (1. + epsilon**2))

        # (2): Calculate the F_{eff}:
        compton_form_factor_h_effective = compute_cff_effective(skewness_parameter, compton_form_factor_h_real_part)
        compton_form_factor_h_tilde_effective = compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde_real_part)
        compton_form_factor_e_effective = compute_cff_effective(skewness_parameter, compton_form_factor_e_real_part)
        compton_form_factor_e_tilde_effective = compute_cff_effective(skewness_parameter, compton_form_factor_e_tilde_real_part)
        
        # (3): Return the entire thing:
        s1LP_DVCS = prefactor * calculate_curly_c_longitudinally_polarized_dvcs(
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            compton_form_factor_h_real_part,
            compton_form_factor_h_tilde_real_part,
            compton_form_factor_e_real_part,
            compton_form_factor_e_tilde_real_part,
            compton_form_factor_h_imaginary_part,
            compton_form_factor_h_tilde_imaginary_part,
            compton_form_factor_e_imaginary_part,
            compton_form_factor_e_tilde_imaginary_part,
            verbose
        )

        # (2.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated s1LP_DVCS to be: {s1LP_DVCS}")

        # (4): Return the coefficient:
        return s1LP_DVCS

    except Exception as ERROR:
        print(f"> Error in calculating s1LP for DVCS Amplitude Squared:\n> {ERROR}")
        return 0.