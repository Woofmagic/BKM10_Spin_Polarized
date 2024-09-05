import numpy as np

from coefficients.interference_coefficients.lp_polarized.pl_polarized_C0p0 import calculate_c_0_zero_plus_longitudinally_polarized

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


def calculate_curly_C_unpolarized_interference(
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

        # (1): Calculate the first term:
        c_I_unpolarized_first_term = Dirac_form_factor_F1 * compton_form_factor_h

        # (2): Calculate the second term:
        c_I_unpolarized_second_term = x_Bjorken * (Dirac_form_factor_F1 + Pauli_form_factor_F2) * compton_form_factor_h_tilde / (2. - x_Bjorken)

        # (3): Calculate the third term:
        c_I_unpolarized_third_term = -1. * squared_hadronic_momentum_transfer_t * Pauli_form_factor_F2 * compton_form_factor_e / (4. * _MASS_OF_PROTON_IN_GEV**2)

        # (4): Calculate the entire coefficient:
        c_I_unpolarized = c_I_unpolarized_first_term + c_I_unpolarized_second_term + c_I_unpolarized_third_term

        if verbose:
            print(f"> Computed coefficient c_I_unpolarized to be: {c_I_unpolarized}")

        # (5): Return:
        return c_I_unpolarized
    
    except Exception as E:
        print(f"> Error computing coefficient c_I_unpolarized:\n> {E}")
        return 0.