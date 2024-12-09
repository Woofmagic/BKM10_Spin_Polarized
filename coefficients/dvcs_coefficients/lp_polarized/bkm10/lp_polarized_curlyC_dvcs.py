try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

from statics.masses.particle_masses import _MASS_OF_PROTON_IN_GEV

from utilities.mathematics.complex_variables import two_complex_variable_product

def calculate_curly_c_longitudinally_polarized_dvcs(
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    compton_form_factor_h: complex,
    compton_form_factor_h_tilde: complex,
    compton_form_factor_e: complex,
    compton_form_factor_e_tilde: complex,
    compton_form_factor_h_conjugate: complex,
    compton_form_factor_h_tilde_conjugate: complex,
    compton_form_factor_e_conjugate: complex,
    compton_form_factor_e_tilde_conjugate: complex,
    verbose: bool = False) -> float:
    """
    Description
    --------------
    Equation (2.23) of the BKM10 Formalism.

    Parameters
    --------------
    lepton_helicity: (float)

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
        two_minus_xb = Decimal("2.") - x_Bjorken

        # (3) Calculuate (2 - x_{B}) * Q^{2} + x_{B} t:
        weighted_sum_Q_squared_xb_t = two_minus_xb * squared_Q_momentum_transfer + x_Bjorken * squared_hadronic_momentum_transfer_t

        # (4): Calculate the first product of CFFs:
        first_term_CFFs = compton_form_factor_h * compton_form_factor_h_tilde_conjugate + compton_form_factor_h_tilde * compton_form_factor_h_conjugate

        # (5): Calculate the second product of CFFs:
        second_term_CFFs = compton_form_factor_h * compton_form_factor_e_tilde_conjugate + compton_form_factor_e_tilde * compton_form_factor_h_conjugate + compton_form_factor_h_tilde * compton_form_factor_e_conjugate + compton_form_factor_e * compton_form_factor_h_tilde_conjugate

        # (6): Calculate the third product of CFFs:
        third_term_CFFs = compton_form_factor_h_tilde * compton_form_factor_e_conjugate + compton_form_factor_e * compton_form_factor_h_tilde_conjugate

        # (7): Calculate the fourth product of CFFs:
        fourth_term_CFFs = compton_form_factor_e * compton_form_factor_e_tilde_conjugate + compton_form_factor_e_tilde * compton_form_factor_e_conjugate

        # (8): Calculate the first term's prefactor:
        first_term_prefactor = Decimal("4.") * (Decimal("1.") - x_Bjorken + (epsilon**2 * ((Decimal("3.")  - Decimal("2.") * x_Bjorken) * squared_Q_momentum_transfer + squared_hadronic_momentum_transfer_t)) / (Decimal("4.") * sum_Q_squared_xb_t))

        # (9): Calculate the second term's prefactor:
        second_term_prefactor = x_Bjorken**2 * (squared_Q_momentum_transfer - (x_Bjorken * squared_hadronic_momentum_transfer_t * (Decimal("1.") - Decimal("2.") * x_Bjorken))) / sum_Q_squared_xb_t

        # (10): Calculate the third term's prefactor:
        third_term_prefactor = x_Bjorken * ((Decimal("4.") * (Decimal("1.") - x_Bjorken) * sum_Q_squared_xb_t * squared_hadronic_momentum_transfer_t) + (epsilon**2 * (squared_Q_momentum_transfer + squared_hadronic_momentum_transfer_t)**2)) / (Decimal("2.") * squared_Q_momentum_transfer * sum_Q_squared_xb_t)

        # (11): Calculate the first part of the fourth term's perfactor:
        fourth_term_prefactor_first_part = weighted_sum_Q_squared_xb_t / sum_Q_squared_xb_t
        
        # (12): Calculate the second part of the fourth term's perfactor:
        fourth_term_prefactor_second_part = (x_Bjorken**2 * (squared_Q_momentum_transfer + squared_hadronic_momentum_transfer_t)**2 / (Decimal("2.") * squared_Q_momentum_transfer * weighted_sum_Q_squared_xb_t)) + (squared_hadronic_momentum_transfer_t / (Decimal("4.") * _MASS_OF_PROTON_IN_GEV**2))
        
        # (13): Finish the fourth-term prefactor
        fourth_term_prefactor = x_Bjorken * fourth_term_prefactor_first_part * fourth_term_prefactor_second_part

        # (14): Calculate the curly-bracket term:
        curly_bracket_term = first_term_CFFs * first_term_prefactor - second_term_CFFs * second_term_prefactor - third_term_CFFs * third_term_prefactor - fourth_term_CFFs * fourth_term_prefactor
        
        # (15): Calculate the prefactor:
        prefactor = squared_Q_momentum_transfer * sum_Q_squared_xb_t / (sqrt(Decimal("1.") + epsilon**2) * weighted_sum_Q_squared_xb_t**2)

        # (16): Return the entire thing:
        curlyCDVCS = prefactor * curly_bracket_term

        # (13.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated curlyCDVCS to be:\n{curlyCDVCS}")

        # (14): Return the coefficient:
        return curlyCDVCS

    except Exception as ERROR:
        print(f"> Error in calculating curlyCDVCS for DVCS Amplitude Squared:\n> {ERROR}")
        return Decimal("0.0")
    