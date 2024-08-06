try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

from coefficients.dvcs_coefficients.lp_polarized.bkm10.lp_polarized_curlyC_dvcs import calculate_curly_c_longitudinally_polarized_dvcs

def calculate_s_1_unpolarized_dvcs(
    lepton_polarization: float,
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float, 
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

        # (1): Calculate the prefactor of the coefficient:
        coefficient_prefactor = -1. * lambda_thing * lepton_energy_fraction_y / (2. - x_Bjorken)

        # (2): Calculate the insane coefficient with the Form Factors:
        insane_coefficient = calculate_dvcs_coefficient_unpolarized_form_factors(
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde
        )

        # (3): Calculate the entire coefficient:
        s1_dvcs_unpolarized_coefficient = coefficient_prefactor * insane_coefficient
        
        if verbose:
            print(f"> Calculated s1_dvcs_unpolarized_coefficient to be: {s1_dvcs_unpolarized_coefficient}")

        return s1_dvcs_unpolarized_coefficient
    
    except Exception as E:
        print(f"> Error in computing s1_unpolarized_BH:\n> {E}")
        return 0.