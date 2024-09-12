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


def calculate_c_0_unpolarized(
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
        
        # (1): Calculate the first recurrent quantity:
        two_minus_y = 2. - lepton_energy_fraction_y

        # (2): Calculate the second recurrent quantity:
        one_minus_y = 1. - lepton_energy_fraction_y

        # (3): Calculate the first term in the Re{...} brackets:
        coefficient_c_I_unpolarized = calculate_interference_coefficient_unpolarized(
            x_Bjorken, 
            squared_hadronic_momentum_transfer_t,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e
        )

        # (4): Calculate the second interference coefficient: delta_c_I:
        coefficient_delta_c_I_unpolarized = calculate_interference_coefficient_delta_unpolarized(
            x_Bjorken, 
            squared_hadronic_momentum_transfer_t,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e
        )

        # (5): Calculate the first term in the Re{...} brackets:
        first_term_in_brackets =  two_minus_y**2 * kinematic_k**2 * coefficient_c_I_unpolarized / one_minus_y

        # (6): Calculate the second term in the Re{...} brackets:
        second_term_in_brackets = squared_hadronic_momentum_transfer_t * one_minus_y * (2. - x_Bjorken) * (coefficient_c_I_unpolarized + coefficient_delta_c_I_unpolarized) / squared_Q_momentum_transfer

        # (7): Calculate the prefactor in front of the brackets:
        coefficient_prefactor = -8 * two_minus_y

        # (8): Calculate the entire coefficient:
        c_0_I_unpolarized = coefficient_prefactor * (first_term_in_brackets + second_term_in_brackets)

        if verbose:
            print(f"> Calculated c_0_I_unpolarized interference coefficient as: {c_0_I_unpolarized}")

        # (9): Return:
        return c_0_I_unpolarized

    except Exception as E:
        print(f"> Error calculating interference coefficient c_0_I_unpolarized:\n> {E}")
        return None