try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

from statics.masses.particle_masses import _MASS_OF_PROTON_IN_GEV

from utilities.mathematics.complex_variables import two_complex_variable_product

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
    verbose: bool = False) -> float:
    """
    Description
    --------------
    Equation (66) of the BKM02 Formalism.

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

        # (1): Compute the recurring term 2 - xB
        two_minus_xB = Decimal("2.") - x_Bjorken

        # (2): Compute the first term in the brackets:
        first_bracket_term = compton_form_factor_hT * (two_minus_xB * compton_form_factor_e - x_Bjorken * compton_form_factor_e_tilde )

        # (3): Compute the second term in the brackets:
        second_bracket_term = Decimal("2.") * two_minus_xB * compton_form_factor_hT_tilde * compton_form_factor_hT_tilde * (compton_form_factor_h + (squared_hadronic_momentum_transfer_t * compton_form_factor_e_tilde / (Decimal("4.") * _MASS_OF_PROTON_IN_GEV**2)))

        # (4): Compute the third term in the brackets:
        third_bracket_term = Decimal("-1.0") * compton_form_factor_eT * (two_minus_xB * compton_form_factor_h - x_Bjorken * compton_form_factor_h_tilde)

        # (5): Compute the fourth term in the brackets:
        fourth_bracket_term = compton_form_factor_eT_tilde * (x_Bjorken * compton_form_factor_h + x_Bjorken * compton_form_factor_e) - two_minus_xB * compton_form_factor_h_tilde

        # (6): Compute the entire coefficient:
        c_dvcs_T_unpolarized_ff = (first_bracket_term + second_bracket_term + third_bracket_term + fourth_bracket_term) / two_minus_xB**2

        if verbose:
            print(f"> Computed c_dvcs_T_unpolarized_ff to be: {c_dvcs_T_unpolarized_ff}")

        return c_dvcs_T_unpolarized_ff


    except Exception as E:
        print(f"> Error computing c_dvcs_T_unpolarized_ff:\n> {E}")
        return Decimal("0.0")