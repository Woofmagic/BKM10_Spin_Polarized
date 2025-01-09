import numpy as np

from coefficients.dvcs_coefficients.lp_polarized.bkm10.lp_polarized_curlyC_dvcs import calculate_curly_c_longitudinally_polarized_dvcs

def calculate_c_2_unpolarized_dvcs(
    lepton_helicity: float,
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
    verbose: bool = False) -> float:
    """
    """

    try:

        # (1): Calculate the prefactor of the coefficient:
        coefficient_prefactor = -1. * squared_Q_momentum_transfer * shorthand_k**2 / (_MASS_OF_PROTON_IN_GEV**2 * (2. - x_Bjorken))

        # (2): Calculate the insane coefficient with the Form Factors:
        insane_coefficient = calculate_dvcs_coefficient_T_unpolarized_form_factors(
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_hT,
            compton_form_factor_hT_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            compton_form_factor_eT,
            compton_form_factor_eT_tilde,
        )

        # (3): Calculate the entire coefficient:
        c2_dvcs_unpolarized_coefficient = coefficient_prefactor * insane_coefficient
        
        if verbose:
            print(f"> Calculated c2_dvcs_unpolarized_coefficient to be: {c2_dvcs_unpolarized_coefficient}")

        return c2_dvcs_unpolarized_coefficient
    
    except Exception as E:
        print(f"> Error in computing c2_dvcs_unpolarized_coefficient:\n> {E}")
        return 0.