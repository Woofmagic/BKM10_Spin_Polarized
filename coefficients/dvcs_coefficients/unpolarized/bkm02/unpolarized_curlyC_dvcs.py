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
    Equation (66) of the BKM02 Formalism.

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
        
        # (1): Compute the recurring term 4*m_{p}^{2}
        four_times_proton_mass = (4. * _MASS_OF_PROTON_IN_GEV**2)

        # (2): Compute the recurring term 2 - xB
        two_minus_xB = 2. - x_Bjorken

        # (3): Calculate the first product of CFFs:
        first_term_CFFs = 4. * (1. - x_Bjorken ) *(two_complex_variable_product(
            compton_form_factor_h_real_part, 
            compton_form_factor_h_imaginary_part, 
            compton_form_factor_h_real_part, 
            -1. * compton_form_factor_h_imaginary_part)
        + two_complex_variable_product(
            compton_form_factor_h_tilde_real_part, 
            compton_form_factor_h_tilde_imaginary_part, 
            compton_form_factor_h_tilde_real_part, 
            -1. * compton_form_factor_h_tilde_imaginary_part))
        
        # (4): Calculate the second product of CFFs:
        second_term_CFFs = x_Bjorken**2 * (two_complex_variable_product(
            compton_form_factor_h_real_part, 
            compton_form_factor_h_imaginary_part, 
            compton_form_factor_e_real_part, 
            -1. * compton_form_factor_e_imaginary_part)
        + two_complex_variable_product(
            compton_form_factor_e_real_part, 
            compton_form_factor_e_imaginary_part, 
            compton_form_factor_h_real_part, 
            -1. * compton_form_factor_h_imaginary_part)
        + two_complex_variable_product(
            compton_form_factor_h_tilde_real_part, 
            compton_form_factor_h_tilde_imaginary_part, 
            compton_form_factor_e_tilde_real_part, 
            -1. * compton_form_factor_e_tilde_imaginary_part)
        + two_complex_variable_product(
            compton_form_factor_e_tilde_real_part, 
            compton_form_factor_e_tilde_imaginary_part, 
            compton_form_factor_h_tilde_real_part, 
            -1. * compton_form_factor_h_tilde_imaginary_part))
        
        # (5): Calculate the second product of CFFs:
        third_term_CFFs = (x_Bjorken**2 + two_minus_xB**2 * squared_hadronic_momentum_transfer_t / four_times_proton_mass) * two_complex_variable_product(
            compton_form_factor_e_real_part, 
            compton_form_factor_e_imaginary_part, 
            compton_form_factor_e_real_part, 
            -1. * compton_form_factor_e_imaginary_part)
        
        # (6): Calculate the second product of CFFs:
        four_term_CFFs = x_Bjorken**2 * squared_hadronic_momentum_transfer_t * two_complex_variable_product(
            compton_form_factor_e_tilde_real_part, 
            compton_form_factor_e_tilde_imaginary_part, 
            compton_form_factor_e_tilde_real_part, 
            -1. * compton_form_factor_e_tilde_imaginary_part) / four_times_proton_mass

        # (7): Return the entire thing:
        curlyCDVCS_unpolarized = (first_term_CFFs - second_term_CFFs - third_term_CFFs - four_term_CFFs) / two_minus_xB**2

        # (7.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated curlyCDVCS_unpolarized to be: {curlyCDVCS_unpolarized}")

        # (8): Return the coefficient:
        return curlyCDVCS_unpolarized

    except Exception as ERROR:
        print(f"> Error in calculating curlyCDVCS for DVCS Amplitude Squared:\n> {ERROR}")
        return 0.