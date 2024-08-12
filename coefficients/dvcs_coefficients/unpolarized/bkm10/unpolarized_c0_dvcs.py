try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

from form_factors.effective_cffs import compute_cff_effective

from coefficients.dvcs_coefficients.unpolarized.bkm10.unpolarized_curlyC_dvcs import calculate_curly_c_unpolarized_dvcs

def calculate_c_0_unpolarized_dvcs(
    lepton_polarization: float,
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

        # (1): Calculate the first term's prefactor:
        first_term_prefactor = 2. * ( 2. - 2. * lepton_energy_fraction_y + lepton_energy_fraction_y**2 + (epsilon**2 * lepton_energy_fraction_y**2 / 2.)) / (1. + epsilon**2)

        # (2): Calcualte the second term's prefactor:
        second_term_prefactor = 16. * k_shorthand**2 / ((2. - x_Bjorken)**2 * (1. + epsilon**2))

        # (3): Calculate the first term's Curly C contribution:
        first_term_curlyC_unp_DVCS = calculate_curly_c_unpolarized_dvcs(
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
            verbose)
        
        # (4): Calculate the second terms' Curly C contribution:
        first_term_curlyC_unp_DVCS = calculate_curly_c_unpolarized_dvcs(
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            compute_cff_effective(skewness_parameter, compton_form_factor_h_real_part),
            compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde_real_part),
            compute_cff_effective(skewness_parameter, compton_form_factor_e_real_part),
            compute_cff_effective(skewness_parameter, compton_form_factor_e_tilde_real_part),
            compute_cff_effective(skewness_parameter, compton_form_factor_h_imaginary_part),
            compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde_imaginary_part),
            compute_cff_effective(skewness_parameter, compton_form_factor_e_imaginary_part),
            compute_cff_effective(skewness_parameter, compton_form_factor_e_tilde_imaginary_part),
            verbose
        )

        # (5): Calculate the entire coefficient:
        c0_dvcs_unpolarized_coefficient = first_term_prefactor * first_term_curlyC_unp_DVCS + second_term_prefactor * first_term_curlyC_unp_DVCS
        
        if verbose:
            print(f"> Calculated c0_dvcs_unpolarized_coefficient to be: {c0_dvcs_unpolarized_coefficient}")

        return c0_dvcs_unpolarized_coefficient
    
    except Exception as E:
        print(f"> Error in computing c2_unpolarized_BH:\n> {E}")
        return 0.