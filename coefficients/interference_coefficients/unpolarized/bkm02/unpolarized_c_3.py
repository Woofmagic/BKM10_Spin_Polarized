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


def calculate_c_3_unpolarized(
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
        
        # (1): Calculate the prefactor:
        coefficient_prefactor = -Decimal("8. ") * squared_Q_momentum_transfer * kinematic_k**3 / (_MASS_OF_PROTON_IN_GEV**2 * (Decimal("2.") - x_Bjorken)**2)

        # (2): Calculate the Re{...} brackets:
        # THIS NEEDS TO BE F_T
        coefficient_c_I_T_unpolarized = calculate_interference_coefficient_T_unpolarized(
            x_Bjorken, 
            squared_hadronic_momentum_transfer_t,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e
        )

        # (3): Calculate the entire coefficient:
        c_3_I_unpolarized = coefficient_prefactor * coefficient_c_I_T_unpolarized

        if verbose:
            print(f"> Calculated c_3_I_unpolarized interference coefficient as: {c_3_I_unpolarized}")

        # (9): Return:
        return c_3_I_unpolarized

    except Exception as E:
        print(f"> Error calculating interference coefficient c_3_I_unpolarized:\n> {E}")
        return Decimal("0.0")