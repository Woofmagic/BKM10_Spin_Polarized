try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

from form_factors.effective_cffs import compute_cff_effective

from coefficients.dvcs_coefficients.unpolarized.bkm10.unpolarized_curlyC_dvcs import calculate_curly_c_unpolarized_dvcs

def calculate_s_1_unpolarized_dvcs(
    lepton_helicity: float,
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float, 
    skewness_parameter: float,
    shorthand_k: float,
    compton_form_factor_h_real_part: float,
    compton_form_factor_h_tilde_real_part: float,
    compton_form_factor_e_real_part: float,
    compton_form_factor_e_tilde_real_part: float,
    compton_form_factor_h_imaginary_part: float,
    compton_form_factor_h_tilde_imaginary_part: float,
    compton_form_factor_e_imaginary_part: float,
    compton_form_factor_e_tilde_imaginary_part: float,
    verbose: bool = False) -> float:
    """
    """

    try:

        # (1): Calculate the first term's prefactor:
        prefactor = -8. * shorthand_k * lepton_helicity * lepton_energy_fraction_y * np.sqrt(1. + epsilon**2) / ((2. - x_Bjorken) * (1. + epsilon**2))
        
        # (2): Calculate the second terms' Curly C contribution:
        curlyC_unp_DVCS = calculate_curly_c_unpolarized_dvcs(
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
        ).imag

        # (3): Calculate the entire coefficient:
        s1_dvcs_unpolarized_coefficient = prefactor * curlyC_unp_DVCS
        
        if verbose:
            print(f"> Calculated s1_dvcs_unpolarized_coefficient to be: {s1_dvcs_unpolarized_coefficient}")

        return s1_dvcs_unpolarized_coefficient
    
    except Exception as E:
        print(f"> Error in computing s1_dvcs_unpolarized_coefficient:\n> {E}")
        return 0.