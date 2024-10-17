try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

from form_factors.effective_cffs import compute_cff_effective

from coefficients.dvcs_coefficients.unpolarized.bkm10.unpolarized_curlyC_dvcs import calculate_curly_c_unpolarized_dvcs

def calculate_c_0_unpolarized_dvcs(
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
    verbose: bool = False) -> float:
    """
    """

    try:

        # (1): Calculate the first term's prefactor:
        first_term_prefactor = 2. * ( 2. - 2. * lepton_energy_fraction_y + lepton_energy_fraction_y**2 + (epsilon**2 * lepton_energy_fraction_y**2 / 2.)) / (1. + epsilon**2)

        # (2): Calcualte the second term's prefactor:
        second_term_prefactor = 16. * shorthand_k**2 / ((2. - x_Bjorken)**2 * (1. + epsilon**2))

        # (3): Calculate the first term's Curly C contribution:
        first_term_curlyC_unp_DVCS = calculate_curly_c_unpolarized_dvcs(
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            compton_form_factor_h.conjugate(),
            compton_form_factor_h_tilde.conjugate(),
            compton_form_factor_e.conjugate(),
            compton_form_factor_e_tilde.conjugate(),
            verbose)
        
        # (4): Calculate the second terms' Curly C contribution:
        second_term_curlyC_unp_DVCS_effective_cffs = calculate_curly_c_unpolarized_dvcs(
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            compute_cff_effective(skewness_parameter, compton_form_factor_h),
            compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde),
            compute_cff_effective(skewness_parameter, compton_form_factor_e),
            compute_cff_effective(skewness_parameter, compton_form_factor_e_tilde),
            compute_cff_effective(skewness_parameter, compton_form_factor_h).conjugate(),
            compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde).conjugate(),
            compute_cff_effective(skewness_parameter, compton_form_factor_e).conjugate(),
            compute_cff_effective(skewness_parameter, compton_form_factor_e_tilde).conjugate(),
            verbose)

        # (5): Calculate the entire coefficient:
        c0_dvcs_unpolarized_coefficient = first_term_prefactor * first_term_curlyC_unp_DVCS + second_term_prefactor * second_term_curlyC_unp_DVCS_effective_cffs
        
        if verbose:
            print(f"> Calculated c0_dvcs_unpolarized_coefficient to be: {c0_dvcs_unpolarized_coefficient}")

        return c0_dvcs_unpolarized_coefficient
    
    except Exception as E:
        print(f"> Error in computing c0_dvcs_unpolarized_coefficient:\n> {E}")
        return 0.