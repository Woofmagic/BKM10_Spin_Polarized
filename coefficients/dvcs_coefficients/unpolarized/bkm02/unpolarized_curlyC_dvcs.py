try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

from statics.masses.particle_masses import _MASS_OF_PROTON_IN_GEV

from statics.mathematics.complex_variables import two_complex_variable_product

def calculate_curly_c_unpolarized_dvcs(
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
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
    Description
    --------------
    Equation (2.23) of the BKM10 Formalism.

    Parameters
    --------------
    lepton_polarization: (float)

    target_polarization: (float)

    squared_Q_momentum_transfer: (float)

    x_Bjorken: (float)

    squared_hadronic_momentum_transfer_t: (float)

    epsilon: (float)

    lepton_energy_fraction_y: (float)

    shorthand_K: (float)

    compton_form_factor_h: (float)

    compton_form_factor_h_tilde: (float)

    compton_form_factor_e: (float)

    compton_form_factor_e_tilde: (float)

    verbose: (bool)
        Debugging console output.

    Notes
    --------------
    (1): This coefficient is in Equation (2.23) from
        the BKM10 Formalism, available here:
        https://arxiv.org/pdf/1005.5209.pdf
    """
    
    try:
        
        # (1): Calculate the appearance of Q^{2} + x_{B} t:
        sum_Q_squared_xb_t = squared_Q_momentum_transfer + x_Bjorken * squared_hadronic_momentum_transfer_t

        # (2): Calculate 2 - x_{B}:
        two_minus_xb = 2. - x_Bjorken

        # (3) Calculuate (2 - x_{B}) * Q^{2} + x_{B} t:
        weighted_sum_Q_squared_xb_t = two_minus_xb * squared_Q_momentum_transfer + x_Bjorken * squared_hadronic_momentum_transfer_t

        # (4): Calculate the first product of CFFs:
        first_term_CFFs = two_complex_variable_product(
            compton_form_factor_h_real_part, 
            compton_form_factor_h_imaginary_part, 
            compton_form_factor_h_tilde_real_part, 
            -1. * compton_form_factor_h_tilde_imaginary_part)
        + two_complex_variable_product(
            compton_form_factor_h_tilde_real_part, 
            compton_form_factor_h_tilde_imaginary_part, 
            compton_form_factor_h_real_part, 
            -1. * compton_form_factor_h_imaginary_part)

        # (5): Calculate the second product of CFFs:
        second_term_CFFs = two_complex_variable_product(
            compton_form_factor_h_real_part, 
            compton_form_factor_h_imaginary_part, 
            compton_form_factor_e_tilde_real_part, 
            -1. * compton_form_factor_e_tilde_imaginary_part)
        + two_complex_variable_product(
            compton_form_factor_e_tilde_real_part, 
            compton_form_factor_e_tilde_imaginary_part, 
            compton_form_factor_h_real_part, 
            -1. * compton_form_factor_h_imaginary_part)
        + two_complex_variable_product(
            compton_form_factor_h_tilde_real_part, 
            compton_form_factor_h_tilde_imaginary_part, 
            compton_form_factor_e_real_part, 
            -1. * compton_form_factor_e_imaginary_part)
        + two_complex_variable_product(
            compton_form_factor_e_real_part, 
            compton_form_factor_e_imaginary_part, 
            compton_form_factor_h_tilde_real_part, 
            -1. * compton_form_factor_h_tilde_imaginary_part)

        # (6): Calculate the third product of CFFs:
        third_term_CFFs = two_complex_variable_product(
            compton_form_factor_h_tilde_real_part, 
            compton_form_factor_h_tilde_imaginary_part, 
            compton_form_factor_e_real_part, 
            -1. * compton_form_factor_e_imaginary_part)
        + two_complex_variable_product(
            compton_form_factor_e_real_part, 
            compton_form_factor_e_imaginary_part, 
            compton_form_factor_h_tilde_real_part, 
            -1. * compton_form_factor_h_tilde_imaginary_part)

        # (7): Calculate the fourth product of CFFs:
        fourth_term_CFFs = two_complex_variable_product(
            compton_form_factor_e_real_part, 
            compton_form_factor_e_imaginary_part, 
            compton_form_factor_e_tilde_real_part, 
            -1. * compton_form_factor_e_tilde_imaginary_part)
        + two_complex_variable_product(
            compton_form_factor_e_tilde_real_part, 
            compton_form_factor_e_tilde_imaginary_part, 
            compton_form_factor_e_real_part, 
            -1. * compton_form_factor_e_imaginary_part)

        # (8): Calculate the first term's prefactor:
        first_term_prefactor = 4. * (1. - x_Bjorken + (epsilon**2 * ((3. - 2. * x_Bjorken) * squared_Q_momentum_transfer + squared_hadronic_momentum_transfer_t)) / (4. * sum_Q_squared_xb_t))

        # (9): Calculate the second term's prefactor:
        second_term_prefactor = x_Bjorken**2 * (squared_Q_momentum_transfer - (x_Bjorken * squared_hadronic_momentum_transfer_t * (1. - 2. * x_Bjorken))) / sum_Q_squared_xb_t

        # (10): Calculate the third term's prefactor:
        third_term_prefactor = x_Bjorken * ((4. * (1. - x_Bjorken) * sum_Q_squared_xb_t * squared_hadronic_momentum_transfer_t) + (epsilon**2 * (squared_Q_momentum_transfer + squared_hadronic_momentum_transfer_t)**2)) / (2. * squared_Q_momentum_transfer * sum_Q_squared_xb_t)

        # (11): Calculate the first part of the fourth term's perfactor:
        fourth_term_prefactor_first_part = weighted_sum_Q_squared_xb_t / sum_Q_squared_xb_t
        
        # (12): Calculate the second part of the fourth term's perfactor:
        fourth_term_prefactor_second_part = (x_Bjorken**2 * (squared_Q_momentum_transfer + squared_hadronic_momentum_transfer_t)**2 / (2. * squared_Q_momentum_transfer * weighted_sum_Q_squared_xb_t)) + (squared_hadronic_momentum_transfer_t / (4. * _MASS_OF_PROTON_IN_GEV**2))
        
        # (13): Finish the fourth-term prefactor
        fourth_term_prefactor = x_Bjorken * fourth_term_prefactor_first_part * fourth_term_prefactor_second_part

        # (14): Calculate the curly-bracket term:
        curly_bracket_term = first_term_CFFs * first_term_prefactor - second_term_CFFs * second_term_prefactor - third_term_CFFs * third_term_prefactor - fourth_term_CFFs * fourth_term_prefactor
        
        # (15): Calculate the prefactor:
        prefactor = squared_Q_momentum_transfer * sum_Q_squared_xb_t / (np.sqrt(1. + epsilon**2) * weighted_sum_Q_squared_xb_t**2)

        # (16): Return the entire thing:
        c1LP_BH = prefactor * curly_bracket_term

        # (13.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c1LP_BH to be: {c1LP_BH}")

        # (14): Return the coefficient:
        return c1LP_BH

    except Exception as ERROR:
        print(f"> Error in calculating c1LP for BH Amplitude Squared:\n> {ERROR}")
        return 0.