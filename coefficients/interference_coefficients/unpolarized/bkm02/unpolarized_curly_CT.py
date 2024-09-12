import numpy as np

from coefficients.interference_coefficients.lp_polarized.lp_polarized_C0p0 import calculate_c_0_zero_plus_longitudinally_polarized

from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_CLP import calculate_curly_C_longitudinally_polarized_interference
from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_CLPV import calculate_curly_C_longitudinally_polarized_interference_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_CLPA import calculate_curly_C_longitudinally_polarized_interference_A

from coefficients.interference_coefficients.lp_polarized.pl_polarized_C0p0V import calculate_c_0_zero_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.pl_polarized_C0p0A import calculate_c_0_zero_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.pl_polarized_C0p1 import calculate_c_1_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_C0p1V import calculate_c_1_zero_plus_longitudinally_polarized_V

from coefficients.interference_coefficients.lp_polarized.pl_polarized_C0p2 import calculate_c_2_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_C0p2V import calculate_c_2_zero_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.pl_polarized_C0p2A import calculate_c_2_zero_plus_longitudinally_polarized_A


def calculate_curly_CT_unpolarized_interference(
    n_number: int,
    lepton_helicity: float,
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float,
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float,
    k_tilde: float,
    shorthand_k: float,
    Dirac_form_factor_F1: float,
    Pauli_form_factor_F2: float,
    compton_form_factor_h_eff: float,
    compton_form_factor_h_tilde_eff: float,
    compton_form_factor_e_eff: float,
    compton_form_factor_e_tilde_eff: float,
    verbose: bool = False) -> float:

    try:

        # (1): Calculate the recurrent quantity:
        two_minus_x_b = 2. - x_Bjorken

        # (2): Calculate the first term in the brackets:
        first_term_in_brackets = compton_form_factor_h * (two_minus_x_b * compton_form_factor_e - x_Bjorken * compton_form_factor_e)

        # (3): Calculate the second term in the brackets:
        second_term_in_brackets = -2. * two_minus_x_b * compton_form_factor_h_tilde * (compton_form_factor_h + (squared_hadronic_momentum_transfer_t * compton_form_factor_e / (4. * _MASS_OF_PROTON_IN_GEV**2)))

        # (4): Calculate the third term in the brackets:
        third_term_in_brackets = -1. * compton_form_factor_e * (two_minus_x_b * compton_form_factor_h - x_Bjorken * compton_form_factor_h_tilde)

        # (5): Calculate the fourth term in the brackets:
        fourth_term_in_brackets = compton_form_factor_e * (x_Bjorken * (compton_form_factor_h + compton_form_factor_e) - two_minus_x_b * compton_form_factor_h_tilde)

        # (6): Calculate the whole coefficient:
        c_I_T_unpolarized = (first_term_in_brackets + second_term_in_brackets + third_term_in_brackets + fourth_term_in_brackets) / two_minus_x_b**2

        if verbose:
            print(f"> Computed coefficient c_I_T_unpolarized to be: {c_I_T_unpolarized}")

        # (5): Return:
        return c_I_T_unpolarized
    
    except Exception as E:
        print(f"> Error computing coefficient c_I_T_unpolarized:\n> {E}")
        return None