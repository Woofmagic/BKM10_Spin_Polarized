

from utilities.plotting.plot_customizer import PlotCustomizer

from calculation.plot_results import plot_interference_contributions

# Helper Module | Convert GeV^{-6} to nb/GeV^{4}
from utilities.mathematics.math_units import convert_to_nb_over_GeV4

from calculation.plot_results import plot_interference_contributions

import numpy as np

from form_factors.effective_cffs import compute_cff_effective

# Import helper modules:
from utilities.mathematics.math_units import convert_degrees_to_radians

from coefficients.interference_coefficients.unpolarized.unpolarized_curly_C import calculate_curly_C_unpolarized_interference
from coefficients.interference_coefficients.unpolarized.unpolarized_curly_CV import calculate_curly_C_unpolarized_interference_V
from coefficients.interference_coefficients.unpolarized.unpolarized_curly_CA import calculate_curly_C_unpolarized_interference_A

from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp0 import calculate_c_0_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp0V import calculate_c_0_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp0A import calculate_c_0_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_C0p0 import calculate_c_0_zero_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p0V import calculate_c_0_zero_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p0A import calculate_c_0_zero_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp1 import calculate_c_1_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp1V import calculate_c_1_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp1A import calculate_c_1_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_C0p1 import calculate_c_1_zero_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p1V import calculate_c_1_zero_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p1A import calculate_c_1_zero_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp2 import calculate_c_2_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp2V import calculate_c_2_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp2A import calculate_c_2_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_C0p2 import calculate_c_2_zero_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p2V import calculate_c_2_zero_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p2A import calculate_c_2_zero_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp3 import calculate_c_3_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp3V import calculate_c_3_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp3A import calculate_c_3_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_Spp1 import calculate_s_1_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Spp1V import calculate_s_1_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Spp1A import calculate_s_1_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_S0p1 import calculate_s_1_zero_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_S0p1V import calculate_s_1_zero_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_S0p1A import calculate_s_1_zero_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_Spp2 import calculate_s_2_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Spp2V import calculate_s_2_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Spp2A import calculate_s_2_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_S0p2 import calculate_s_2_zero_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_S0p2V import calculate_s_2_zero_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_S0p2A import calculate_s_2_zero_plus_unpolarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_CLP import calculate_curly_C_longitudinally_polarized_interference
from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_CLPV import calculate_curly_C_longitudinally_polarized_interference_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_CLPA import calculate_curly_C_longitudinally_polarized_interference_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp0 import calculate_c_0_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp0V import calculate_c_0_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp0A import calculate_c_0_plus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_C0p0 import calculate_c_0_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_C0p0V import calculate_c_0_zero_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_C0p0A import calculate_c_0_zero_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp1 import calculate_c_1_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp1V import calculate_c_1_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp1A import calculate_c_1_plus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_C0p1 import calculate_c_1_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_C0p1V import calculate_c_1_zero_plus_longitudinally_polarized_V

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp2 import calculate_c_2_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp2V import calculate_c_2_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp2A import calculate_c_2_plus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_C0p2 import calculate_c_2_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_C0p2V import calculate_c_2_zero_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_C0p2A import calculate_c_2_zero_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp1 import calculate_s_1_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp1V import calculate_s_1_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp1A import calculate_s_1_plus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_S0p1 import calculate_s_1_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_S0p1V import calculate_s_1_zero_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_S0p1A import calculate_s_1_zero_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp2 import calculate_s_2_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp2V import calculate_s_2_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp2A import calculate_s_2_plus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_S0p2 import calculate_s_2_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_S0p2V import calculate_s_2_zero_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_S0p2A import calculate_s_2_zero_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp3 import calculate_s_3_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp3V import calculate_s_3_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp3A import calculate_s_3_plus_plus_longitudinally_polarized_A

def calculate_interference_contribution(
    lepton_helicity: float,
    target_polarization: float,
    squared_Q_momentum_transfer: float,
    x_Bjorken: float,
    squared_hadronic_momentum_transfer_t: float,
    azimuthal_phi: float,
    epsilon: float,
    lepton_energy_fraction_y: float,
    skewness_parameter: float,
    t_prime: float,
    k_tilde: float,
    shorthand_k: float,
    lepton_propagator_p1: float,
    lepton_propagator_p2: float,
    Dirac_form_factor_F1: float,
    Pauli_form_factor_F2: float,
    compton_form_factor_h: complex,
    compton_form_factor_h_tilde: complex,
    compton_form_factor_e: complex,
    compton_form_factor_e_tilde: complex,
    use_ww: bool = False,
    verbose: bool = False) -> float:
    """
    ## Description:
    We calculated the BKM10-predicted contribution of the interference between
    the BH and DVCS process.
    
        lepton_helicity: (float)

        target_polarization: (float)

        squared_Q_momentum_transfer: (float)

        x_Bjorken: (float)

        squared_hadronic_momentum_transfer_t: (float)

        lab_kinematics_k: (float)

        azimuthal_phi: (float)

        epsilon:  (float)

        lepton_energy_fraction_y: (float)

        skewness_parameter: (float)

        t_prime: (float)

        k_tilde: (float)

        shorthand_k: (float)

        lepton_propagator_p1: (float)

        lepton_propagator_p2: (float)

        Dirac_form_factor_F1: (float)

        Pauli_form_factor_F2: (float)

        compton_form_factor_h_real_part: (float)

            The real part of the Compton Form Factor (CFF) called H. We will
            write this as Re[H].

        compton_form_factor_h_tilde_real_part: (float)

            The real part of the Compton Form Factor (CFF) called Ht (H-tilde). We will
            write this as Re[HT].

        compton_form_factor_e_real_part: (float)

            The real part of the Compton Form Factor (CFF) called E. We will
            write this as Re[E].

        compton_form_factor_e_tilde_real_part: (float)

            The real part of the Compton Form Factor (CFF) called Et (E-tilde). We will
            write this as Re[Et].

        compton_form_factor_h_imaginary_part: (float)

            The imaginary/complex part of the Compton Form Factor (CFF) called H. We will
            write this as Re[H].

        compton_form_factor_h_tilde_imaginary_part: (float)

            The imaginary/complex part of the Compton Form Factor (CFF) called Ht (H-tilde). We will
            write this as Re[HT].

        compton_form_factor_e_imaginary_part: (float)

            The imaginary/complex part of the Compton Form Factor (CFF) called E. We will
            write this as Re[E].

        compton_form_factor_e_tilde_imaginary_part: (float)

            The imaginary/complex part of the Compton Form Factor (CFF) called Et (E-tilde). We will
            write this as Re[Et].

        verbose: (bool)

    ## Returns:
    
        bkm10_cross_section_in_nb_GeV4: (float)

            The four-fold differential cross section.

    ## Notes:

    ## Examples:
    """

    try:

        # (1): Calculate the prefactor:
        prefactor = 1. / (x_Bjorken * lepton_energy_fraction_y**3 * squared_hadronic_momentum_transfer_t * lepton_propagator_p1 * lepton_propagator_p2)

        # (2): Initialize the Fourier coefficients:
        c_0_interference_coefficient = 0.
        c_1_interference_coefficient = 0.
        c_2_interference_coefficient = 0.
        c_3_interference_coefficient = 0.
        s_1_interference_coefficient = 0.
        s_2_interference_coefficient = 0.
        s_3_interference_coefficient = 0.

        if target_polarization == 0.:

            C0_pp_unpolarized = calculate_c_0_plus_plus_unpolarized(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)

            C0V_pp_unpolarized = calculate_c_0_plus_plus_unpolarized_V(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)

            C0A_pp_unpolarized = calculate_c_0_plus_plus_unpolarized_A(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)

            C0_0p_unpolarized = calculate_c_0_zero_plus_unpolarized(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            C0V_0p_unpolarized = calculate_c_0_zero_plus_unpolarized_V(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            C0A_0p_unpolarized = calculate_c_0_zero_plus_unpolarized_A(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            curly_C_unpolarized_interference_for_pp = calculate_curly_C_unpolarized_interference(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                compton_form_factor_h,
                compton_form_factor_h_tilde,
                compton_form_factor_e,
                verbose)

            curly_C_V_unpolarized_interference_for_pp = calculate_curly_C_unpolarized_interference_V(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                compton_form_factor_h,
                compton_form_factor_e,
                verbose)

            curly_C_A_unpolarized_interference_for_pp = calculate_curly_C_unpolarized_interference_A(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                compton_form_factor_h_tilde,
                verbose)

            curly_C_unpolarized_interference_for_0p = calculate_curly_C_unpolarized_interference(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                compute_cff_effective(skewness_parameter, compton_form_factor_h, use_ww),
                compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde, use_ww),
                compute_cff_effective(skewness_parameter, compton_form_factor_e, use_ww),
                verbose)

            curly_C_V_unpolarized_interference_for_0p = calculate_curly_C_unpolarized_interference_V(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                compute_cff_effective(skewness_parameter, compton_form_factor_h, use_ww),
                compute_cff_effective(skewness_parameter, compton_form_factor_e, use_ww),
                verbose)

            curly_C_A_unpolarized_interference_for_0p = calculate_curly_C_unpolarized_interference_A(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde, use_ww),
                verbose)

            C1_pp_unpolarized = calculate_c_1_plus_plus_unpolarized(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            C1V_pp_unpolarized = calculate_c_1_plus_plus_unpolarized_V(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            C1A_pp_unpolarized = calculate_c_1_plus_plus_unpolarized_A(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            C1_0p_unpolarized = calculate_c_1_zero_plus_unpolarized(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                verbose)

            C1V_0p_unpolarized = calculate_c_1_zero_plus_unpolarized_V(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)

            C1A_0p_unpolarized = calculate_c_1_zero_plus_unpolarized_A(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)

            C2_pp_unpolarized = calculate_c_2_plus_plus_unpolarized(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                k_tilde,
                verbose)

            C2V_pp_unpolarized = calculate_c_2_plus_plus_unpolarized_V(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                k_tilde,
                verbose)

            C2A_pp_unpolarized = calculate_c_2_plus_plus_unpolarized_A(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                k_tilde,
                verbose)

            C2_0p_unpolarized = calculate_c_2_zero_plus_unpolarized(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            C2V_0p_unpolarized = calculate_c_2_zero_plus_unpolarized_V(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            C2A_0p_unpolarized = calculate_c_2_zero_plus_unpolarized_A(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            C3_pp_unpolarized = calculate_c_3_plus_plus_unpolarized(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            C3V_pp_unpolarized = calculate_c_3_plus_plus_unpolarized_V(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            C3A_pp_unpolarized = calculate_c_3_plus_plus_unpolarized_A(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            C3_0p_unpolarized = 0.

            C3V_0p_unpolarized = 0.

            C3A_0p_unpolarized = 0.

            S1_pp_unpolarized = calculate_s_1_plus_plus_unpolarized(
                lepton_helicity,
                squared_Q_momentum_transfer,
                x_Bjorken,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            S1V_pp_unpolarized = calculate_s_1_plus_plus_unpolarized_V(
                lepton_helicity,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            S1A_pp_unpolarized = calculate_s_1_plus_plus_unpolarized_A(
                lepton_helicity,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            S1_0p_unpolarized = calculate_s_1_zero_plus_unpolarized(
                lepton_helicity,
                squared_Q_momentum_transfer,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)

            S1V_0p_unpolarized = calculate_s_1_zero_plus_unpolarized_V(
                lepton_helicity,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                verbose)

            S1A_0p_unpolarized = calculate_s_1_zero_plus_unpolarized_A(
                lepton_helicity,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            S2_pp_unpolarized = calculate_s_2_plus_plus_unpolarized(
                lepton_helicity,
                squared_Q_momentum_transfer,
                x_Bjorken,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                verbose)

            S2V_pp_unpolarized = calculate_s_2_plus_plus_unpolarized_V(
                lepton_helicity,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                verbose)

            S2A_pp_unpolarized = calculate_s_2_plus_plus_unpolarized_A(
                lepton_helicity,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                verbose)

            S2_0p_unpolarized = calculate_s_2_zero_plus_unpolarized(
                lepton_helicity,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            S2V_0p_unpolarized = calculate_s_2_zero_plus_unpolarized_V(
                lepton_helicity,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            S2A_0p_unpolarized = calculate_s_2_zero_plus_unpolarized_A(
                lepton_helicity,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            curly_C_0_pp_int =  (curly_C_unpolarized_interference_for_pp
                        + (C0V_pp_unpolarized * curly_C_V_unpolarized_interference_for_pp / C0_pp_unpolarized)
                        + (C0A_pp_unpolarized * curly_C_A_unpolarized_interference_for_pp / C0_pp_unpolarized))

            curly_C_0_0p_int =  ((np.sqrt(2. / squared_Q_momentum_transfer) * k_tilde / (2. - x_Bjorken)) * (curly_C_unpolarized_interference_for_0p
                        + (C0V_0p_unpolarized * curly_C_V_unpolarized_interference_for_0p / C0_0p_unpolarized)
                        + (C0A_0p_unpolarized * curly_C_A_unpolarized_interference_for_0p / C0_0p_unpolarized)))
            
            curly_C_1_pp_int =  (curly_C_unpolarized_interference_for_pp
                        + (C1V_pp_unpolarized * curly_C_V_unpolarized_interference_for_pp / C1_pp_unpolarized)
                        + (C1A_pp_unpolarized * curly_C_A_unpolarized_interference_for_pp / C1_pp_unpolarized))

            curly_C_1_0p_int =  ((np.sqrt(2. / squared_Q_momentum_transfer) * k_tilde / (2. - x_Bjorken)) * (curly_C_unpolarized_interference_for_0p
                        + (C1V_0p_unpolarized * curly_C_V_unpolarized_interference_for_0p / C1_0p_unpolarized)
                        + (C1A_0p_unpolarized * curly_C_A_unpolarized_interference_for_0p / C1_0p_unpolarized)))
            
            curly_C_2_pp_int =  (curly_C_unpolarized_interference_for_pp
                        + (C2V_pp_unpolarized * curly_C_V_unpolarized_interference_for_pp / C2_pp_unpolarized)
                        + (C2A_pp_unpolarized * curly_C_A_unpolarized_interference_for_pp / C2_pp_unpolarized))

            curly_C_2_0p_int =  ((np.sqrt(2. / squared_Q_momentum_transfer) * k_tilde / (2. - x_Bjorken)) * (curly_C_unpolarized_interference_for_0p
                        + (C2V_0p_unpolarized * curly_C_V_unpolarized_interference_for_0p / C2_0p_unpolarized)
                        + (C2A_0p_unpolarized * curly_C_A_unpolarized_interference_for_0p / C2_0p_unpolarized)))
            
            curly_C_3_pp_int =  (curly_C_unpolarized_interference_for_pp
                        + (C3V_pp_unpolarized * curly_C_V_unpolarized_interference_for_pp / C3_pp_unpolarized)
                        + (C3A_pp_unpolarized * curly_C_A_unpolarized_interference_for_pp / C3_pp_unpolarized))

            curly_C_3_0p_int =  ((np.sqrt(2. / squared_Q_momentum_transfer) * k_tilde / (2. - x_Bjorken)) * (curly_C_unpolarized_interference_for_0p))

            curly_S_1_pp_int =  (curly_C_unpolarized_interference_for_pp
                        + (S1V_pp_unpolarized * curly_C_V_unpolarized_interference_for_pp / S1_pp_unpolarized)
                        + (S1A_pp_unpolarized * curly_C_A_unpolarized_interference_for_pp / S1_pp_unpolarized))

            curly_S_1_0p_int =  ((np.sqrt(2. / squared_Q_momentum_transfer) * k_tilde / (2. - x_Bjorken)) * (curly_C_unpolarized_interference_for_0p
                        + (S1V_0p_unpolarized * curly_C_V_unpolarized_interference_for_0p / S1_0p_unpolarized)
                        + (S1A_0p_unpolarized * curly_C_A_unpolarized_interference_for_0p / S1_0p_unpolarized)))

            curly_S_2_pp_int =  (curly_C_unpolarized_interference_for_pp
                        + (S2V_pp_unpolarized * curly_C_V_unpolarized_interference_for_pp / S2_pp_unpolarized)
                        + (S2A_pp_unpolarized * curly_C_A_unpolarized_interference_for_pp / S2_pp_unpolarized))

            curly_S_2_0p_int =  ((np.sqrt(2. / squared_Q_momentum_transfer) * k_tilde / (2. - x_Bjorken)) * (curly_C_unpolarized_interference_for_0p
                        + (S2V_0p_unpolarized * curly_C_V_unpolarized_interference_for_0p / S2_0p_unpolarized)
                        + (S2A_0p_unpolarized * curly_C_A_unpolarized_interference_for_0p / S2_0p_unpolarized)))
            
            c_0_interference_coefficient = C0_pp_unpolarized * curly_C_0_pp_int.real + C0_0p_unpolarized * curly_C_0_0p_int.real
            c_1_interference_coefficient = C1_pp_unpolarized * curly_C_1_pp_int.real + C1_0p_unpolarized * curly_C_1_0p_int.real
            c_2_interference_coefficient = C2_pp_unpolarized * curly_C_2_pp_int.real + C2_0p_unpolarized * curly_C_2_0p_int.real
            c_3_interference_coefficient = C3_pp_unpolarized * curly_C_3_pp_int.real + C3_0p_unpolarized * curly_C_3_0p_int.real
            s_1_interference_coefficient = S1_pp_unpolarized * curly_S_1_pp_int.imag + S1_0p_unpolarized * curly_S_1_0p_int.imag
            s_2_interference_coefficient = S2_pp_unpolarized * curly_S_2_pp_int.imag + S2_0p_unpolarized * curly_S_2_0p_int.imag
            s_3_interference_coefficient = 0.

            # print(f"> Curly CI++: {curly_C_unpolarized_interference_for_pp[0]}")
            # print(f"> Curly CIV++: {curly_C_V_unpolarized_interference_for_pp[0]}")
            # print(f"> Curly CIA++: {curly_C_A_unpolarized_interference_for_pp[0]}")
            # print(f"> Curly CI0+: {curly_C_unpolarized_interference_for_0p[0]}")
            # print(f"> Curly CIV0+: {curly_C_V_unpolarized_interference_for_0p[0]}")
            # print(f"> Curly CIA0+: {curly_C_A_unpolarized_interference_for_0p[0]}")
            
            # print(f"> C++(n=0): {C0_pp_unpolarized[0]}")
            # print(f"> C++V(n=0): {C0V_pp_unpolarized[0]}")
            # print(f"> C++A(n=0): {C0A_pp_unpolarized[0]}")

            # print(f"> C0+(n=0): {C0_0p_unpolarized[0]}")
            # print(f"> C0+V(n=0): {C0V_0p_unpolarized[0]}")
            # print(f"> C0+A(n=0): {C0A_0p_unpolarized[0]}")

            # print(f"> C++(n=1): {C1_pp_unpolarized[0]}")
            # print(f"> C++V(n=1): {C1V_pp_unpolarized[0]}")
            # print(f"> C++A(n=1): {C1A_pp_unpolarized[0]}")

            # print(f"> C0+(n=1): {C1_0p_unpolarized[0]}")
            # print(f"> C0+V(n=1): {C1V_0p_unpolarized[0]}")
            # print(f"> C0+A(n=1): {C1A_0p_unpolarized[0]}")

            # print(f"> C++(n=2): {C2_pp_unpolarized[0]}")
            # print(f"> C++V(n=2): {C2V_pp_unpolarized[0]}")
            # print(f"> C++A(n=2): {C2A_pp_unpolarized[0]}")

            # print(f"> C0+(n=2): {C2_0p_unpolarized[0]}")
            # print(f"> C0+V(n=2): {C2V_0p_unpolarized[0]}")
            # print(f"> C0+A(n=2): {C2A_0p_unpolarized[0]}")

            # print(f"> C++(n=3): {C3_pp_unpolarized[0]}")
            # print(f"> C++V(n=3): {C3V_pp_unpolarized[0]}")
            # print(f"> C++A(n=3): {C3A_pp_unpolarized[0]}")

            # print(f"> S++(n=1): {S1_pp_unpolarized[0]}")
            # print(f"> S++V(n=1): {S1V_pp_unpolarized[0]}")
            # print(f"> S++A(n=1): {S1A_pp_unpolarized[0]}")

            # print(f"> S0+(n=1): {S1_0p_unpolarized[0]}")
            # print(f"> S0+V(n=1): {S1V_0p_unpolarized[0]}")
            # print(f"> S0+A(n=1): {S1A_0p_unpolarized[0]}")

            # print(f"> S++(n=2): {S2_pp_unpolarized[0]}")
            # print(f"> S++V(n=2): {S2V_pp_unpolarized[0]}")
            # print(f"> S++A(n=2): {S2A_pp_unpolarized[0]}")

            # print(f"> S0+(n=2): {S2_0p_unpolarized[0]}")
            # print(f"> S0+V(n=2): {S2V_0p_unpolarized[0]}")
            # print(f"> S0+A(n=2): {S2A_0p_unpolarized[0]}")

            # print(f"> Curly C++(n = 0|F): {curly_C_0_pp_int[0]}")
            # print(f"> Curly C0+(n = 0|F): {curly_C_0_0p_int[0]}")
            # print(f"> Curly C++(n = 1|F): {curly_C_1_pp_int[0]}")
            # print(f"> Curly C0+(n = 1|F): {curly_C_1_0p_int[0]}")
            # print(f"> Curly C++(n = 2|F): {curly_C_2_pp_int[0]}")
            # print(f"> Curly C0+(n = 2|F): {curly_C_2_0p_int[0]}")
            # print(f"> Curly C++(n = 3|F): {curly_C_3_pp_int[0]}")
            # print(f"> Curly C0+(n = 3|F): {curly_C_3_0p_int[0]}")

            # print(f"> Curly S++(n = 1|F): {curly_S_1_pp_int[0]}")
            # print(f"> Curly S0+(n = 1|F): {curly_S_1_0p_int[0]}")
            # print(f"> Curly S++(n = 2|F): {curly_S_2_pp_int[0]}")
            # print(f"> Curly S0+(n = 2|F): {curly_S_2_0p_int[0]}")
            
        elif target_polarization != 0.0:

            curly_C_lp_polarized_interference_for_pp = calculate_curly_C_longitudinally_polarized_interference(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                compton_form_factor_h,
                compton_form_factor_h_tilde,
                compton_form_factor_e,
                compton_form_factor_e_tilde,
                verbose)

            curly_C_V_lp_polarized_interference_for_pp = calculate_curly_C_longitudinally_polarized_interference_V(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                compton_form_factor_h,
                compton_form_factor_e,
                verbose)

            curly_C_A_lp_polarized_interference_for_pp = calculate_curly_C_longitudinally_polarized_interference_A(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                compton_form_factor_h_tilde,
                compton_form_factor_e_tilde,
                verbose)

            curly_C_lp_polarized_interference_for_0p = calculate_curly_C_longitudinally_polarized_interference(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                compute_cff_effective(skewness_parameter, compton_form_factor_h, use_ww),
                compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde, use_ww),
                compute_cff_effective(skewness_parameter, compton_form_factor_e, use_ww),
                compute_cff_effective(skewness_parameter, compton_form_factor_e_tilde, use_ww),
                verbose)

            curly_C_V_lp_polarized_interference_for_0p = calculate_curly_C_longitudinally_polarized_interference_V(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                compute_cff_effective(skewness_parameter, compton_form_factor_h, use_ww),
                compute_cff_effective(skewness_parameter, compton_form_factor_e, use_ww),
                verbose)

            curly_C_A_lp_polarized_interference_for_0p = calculate_curly_C_longitudinally_polarized_interference_A(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde, use_ww),
                compute_cff_effective(skewness_parameter, compton_form_factor_e_tilde, use_ww),
                verbose)
            
            C0_pp_lp_polarized = calculate_c_0_plus_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)

            C0V_pp_lp_polarized = calculate_c_0_plus_plus_longitudinally_polarized_V(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)

            C0A_pp_lp_polarized = calculate_c_0_plus_plus_longitudinally_polarized_A(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)

            C0_0p_lp_polarized = calculate_c_0_zero_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            C0V_0p_lp_polarized = calculate_c_0_zero_plus_longitudinally_polarized_V(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            C0A_0p_lp_polarized = calculate_c_0_zero_plus_longitudinally_polarized_A(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            C1_pp_lp_polarized = calculate_c_1_plus_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            C1V_pp_lp_polarized = calculate_c_1_plus_plus_longitudinally_polarized_V(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            C1A_pp_lp_polarized = calculate_c_1_plus_plus_longitudinally_polarized_A(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            C1_0p_lp_polarized = calculate_c_1_zero_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                shorthand_k,
                verbose)

            C1V_0p_lp_polarized = calculate_c_1_zero_plus_longitudinally_polarized_V(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)
            
            C1A_0p_lp_polarized = 0.

            C2_pp_lp_polarized = calculate_c_2_plus_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                verbose)

            C2V_pp_lp_polarized = calculate_c_2_plus_plus_longitudinally_polarized_V(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                verbose)

            C2A_pp_lp_polarized = calculate_c_2_plus_plus_longitudinally_polarized_A(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                verbose)

            C2_0p_lp_polarized = calculate_c_2_zero_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            C2V_0p_lp_polarized = calculate_c_2_zero_plus_longitudinally_polarized_V(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            C2A_0p_lp_polarized = calculate_c_2_zero_plus_longitudinally_polarized_A(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            S1_pp_lp_polarized = calculate_s_1_plus_plus_longitudinally_polarized(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            S1V_pp_lp_polarized = calculate_s_1_plus_plus_longitudinally_polarized_V(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            S1A_pp_lp_polarized = calculate_s_1_plus_plus_longitudinally_polarized_A(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            S1_0p_lp_polarized = calculate_s_1_zero_plus_longitudinally_polarized(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)
            
            S1V_0p_lp_polarized = calculate_s_1_zero_plus_longitudinally_polarized_V(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)
            
            S1A_0p_lp_polarized = calculate_s_1_zero_plus_longitudinally_polarized_A(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                verbose)

            S2_pp_lp_polarized = calculate_s_2_plus_plus_longitudinally_polarized(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                k_tilde,
                verbose)

            S2V_pp_lp_polarized = calculate_s_2_plus_plus_longitudinally_polarized_V(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                k_tilde,
                verbose)

            S2A_pp_lp_polarized = calculate_s_2_plus_plus_longitudinally_polarized_A(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                k_tilde,
                verbose)

            S2_0p_lp_polarized = calculate_s_2_zero_plus_longitudinally_polarized(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            S2V_0p_lp_polarized = calculate_s_2_zero_plus_longitudinally_polarized_V(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            S2A_0p_lp_polarized = calculate_s_2_zero_plus_longitudinally_polarized_A(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            S3_pp_lp_polarized = calculate_s_3_plus_plus_longitudinally_polarized(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            S3V_pp_lp_polarized = calculate_s_3_plus_plus_longitudinally_polarized_V(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            S3A_pp_lp_polarized = calculate_s_3_plus_plus_longitudinally_polarized_A(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            S3_0p_lp_polarized = 0.

            S3V_0p_lp_polarized = 0.
            
            S3A_0p_lp_polarized = 0.
            
            curly_C_0_pp_int =  (curly_C_lp_polarized_interference_for_pp
                        + (C0V_pp_lp_polarized * curly_C_V_lp_polarized_interference_for_pp / C0_pp_lp_polarized)
                        + (C0A_pp_lp_polarized * curly_C_A_lp_polarized_interference_for_pp / C0_pp_lp_polarized))

            curly_C_0_0p_int =  ((np.sqrt(2. / squared_Q_momentum_transfer) * k_tilde / (2. - x_Bjorken)) * (curly_C_lp_polarized_interference_for_0p
                        + (C0V_0p_lp_polarized * curly_C_V_lp_polarized_interference_for_0p / C0_0p_lp_polarized)
                        + (C0A_0p_lp_polarized * curly_C_A_lp_polarized_interference_for_0p / C0_0p_lp_polarized)))
            
            curly_C_1_pp_int =  (curly_C_lp_polarized_interference_for_pp
                        + (C1V_pp_lp_polarized * curly_C_V_lp_polarized_interference_for_pp / C1_pp_lp_polarized)
                        + (C1A_pp_lp_polarized * curly_C_A_lp_polarized_interference_for_pp / C1_pp_lp_polarized))

            curly_C_1_0p_int =  ((np.sqrt(2. / squared_Q_momentum_transfer) * k_tilde / (2. - x_Bjorken)) * (curly_C_lp_polarized_interference_for_0p
                        + (C1V_0p_lp_polarized * curly_C_V_lp_polarized_interference_for_0p / C1_0p_lp_polarized)
                        + (C1A_0p_lp_polarized * curly_C_A_lp_polarized_interference_for_0p / C1_0p_lp_polarized)))
            
            curly_C_2_pp_int =  (curly_C_lp_polarized_interference_for_pp
                        + (C2V_pp_lp_polarized * curly_C_V_lp_polarized_interference_for_pp / C2_pp_lp_polarized)
                        + (C2A_pp_lp_polarized * curly_C_A_lp_polarized_interference_for_pp / C2_pp_lp_polarized))

            curly_C_2_0p_int =  ((np.sqrt(2. / squared_Q_momentum_transfer) * k_tilde / (2. - x_Bjorken)) * (curly_C_lp_polarized_interference_for_0p
                        + (C2V_0p_lp_polarized * curly_C_V_lp_polarized_interference_for_0p / C2_0p_lp_polarized)
                        + (C2A_0p_lp_polarized * curly_C_A_lp_polarized_interference_for_0p / C2_0p_lp_polarized)))
            
            curly_C_3_pp_int = 0.

            curly_C_3_0p_int = 0.

            curly_S_1_pp_int =  (curly_C_lp_polarized_interference_for_pp
                        + (S1V_pp_lp_polarized * curly_C_V_lp_polarized_interference_for_pp / S1_pp_lp_polarized)
                        + (S1A_pp_lp_polarized * curly_C_A_lp_polarized_interference_for_pp / S1_pp_lp_polarized))

            curly_S_1_0p_int =  ((np.sqrt(2. / squared_Q_momentum_transfer) * k_tilde / (2. - x_Bjorken)) * (curly_C_lp_polarized_interference_for_0p
                        + (S1V_0p_lp_polarized * curly_C_V_lp_polarized_interference_for_0p / S1_0p_lp_polarized)
                        + (S1A_0p_lp_polarized * curly_C_A_lp_polarized_interference_for_0p / S1_0p_lp_polarized)))

            curly_S_2_pp_int =  (curly_C_lp_polarized_interference_for_pp
                        + (S2V_pp_lp_polarized * curly_C_V_lp_polarized_interference_for_pp / S2_pp_lp_polarized)
                        + (S2A_pp_lp_polarized * curly_C_A_lp_polarized_interference_for_pp / S2_pp_lp_polarized))

            curly_S_2_0p_int =  ((np.sqrt(2. / squared_Q_momentum_transfer) * k_tilde / (2. - x_Bjorken)) * (curly_C_lp_polarized_interference_for_0p
                        + (S2V_0p_lp_polarized * curly_C_V_lp_polarized_interference_for_0p / S2_0p_lp_polarized)
                        + (S2A_0p_lp_polarized * curly_C_A_lp_polarized_interference_for_0p / S2_0p_lp_polarized)))
            
            curly_S_3_pp_int =  (curly_C_lp_polarized_interference_for_pp
                        + (S3V_pp_lp_polarized * curly_C_V_lp_polarized_interference_for_pp / S3_pp_lp_polarized)
                        + (S3A_pp_lp_polarized * curly_C_A_lp_polarized_interference_for_pp / S3_pp_lp_polarized))

            curly_S_3_0p_int =  ((np.sqrt(2. / squared_Q_momentum_transfer) * k_tilde / (2. - x_Bjorken)) * (curly_C_lp_polarized_interference_for_0p
            + 0.
            + 0.))

            print(f"> Curly C++LP: {curly_C_lp_polarized_interference_for_pp[0]}")
            print(f"> Curly C++VLP: {curly_C_V_lp_polarized_interference_for_pp[0]}")
            print(f"> Curly C++ALP: {curly_C_A_lp_polarized_interference_for_pp[0]}")    
            print(f"> Curly C0+LP: {curly_C_lp_polarized_interference_for_0p[0]}")
            print(f"> Curly C0+VLP: {curly_C_V_lp_polarized_interference_for_0p[0]}")
            print(f"> Curly C0+ALP: {curly_C_A_lp_polarized_interference_for_0p[0]}")
            
            print(f"> C++(n=0): {C0_pp_lp_polarized[0]}")
            print(f"> CV++(n=0): {C0V_pp_lp_polarized[0]}")
            print(f"> CA++(n=0): {C0A_pp_lp_polarized[0]}")
            
            print(f"> C0+(n=0): {C0_0p_lp_polarized[0]}")
            print(f"> C0V+(n=0): {C0V_0p_lp_polarized[0]}")
            print(f"> C0A+(n=0): {C0A_0p_lp_polarized[0]}")
            
            print(f"> C++(n=1): {C1_pp_lp_polarized[0]}")
            print(f"> CV++(n=1): {C1V_pp_lp_polarized[0]}")
            print(f"> CA++(n=1): {C1A_pp_lp_polarized[0]}")
            
            print(f"> C0+(n=1): {C1_0p_lp_polarized[0]}")
            print(f"> C0+V(n=1): {C1V_0p_lp_polarized[0]}")
            print(f"> C0+A(n=1): {C1A_0p_lp_polarized}")
            
            print(f"> C++(n=2): {C2_pp_lp_polarized[0]}")
            print(f"> CV++(n=2): {C2V_pp_lp_polarized[0]}")
            print(f"> CA++(n=2): {C2A_pp_lp_polarized[0]}")
            
            print(f"> C0+(n=2): {C2_0p_lp_polarized[0]}")
            print(f"> C0+V(n=2): {C2V_0p_lp_polarized[0]}")
            print(f"> C0+A(n=2): {C2A_0p_lp_polarized[0]}")
            
            print(f"> S++(n=1): {S1_pp_lp_polarized[0]}")
            print(f"> S++V(n=1): {S1V_pp_lp_polarized[0]}")
            print(f"> S++A(n=1): {S1A_pp_lp_polarized[0]}")

            print(f"> S0+(n=1): {S1_0p_lp_polarized[0]}")
            print(f"> S0+V(n=1): {S1V_0p_lp_polarized[0]}")
            print(f"> S0+A(n=1): {S1A_0p_lp_polarized[0]}")
            
            print(f"> S++(n=2): {S2_pp_lp_polarized[0]}")
            print(f"> S++V(n=2): {S2V_pp_lp_polarized[0]}")
            print(f"> S++A(n=2): {S2A_pp_lp_polarized[0]}")
            
            print(f"> S0+(n=2): {S2_0p_lp_polarized[0]}")            
            print(f"> S0+V(n=2): {S2V_0p_lp_polarized[0]}")
            print(f"> S0+A(n=2): {S2A_0p_lp_polarized[0]}")

            print(f"> S++(n=3): {S3_pp_lp_polarized[0]}")
            print(f"> S++V(n=3): {S3V_pp_lp_polarized[0]}")
            print(f"> S++A(n=3): {S3A_pp_lp_polarized[0]}")

            print(f"> Curly C++(n = 0|F): {curly_C_0_pp_int[0]}")
            print(f"> Curly C0+(n = 0|F): {curly_C_0_0p_int[0]}")
            print(f"> Curly C++(n = 1|F): {curly_C_1_pp_int[0]}")
            print(f"> Curly C0+(n = 1|F): {curly_C_1_0p_int[0]}")
            print(f"> Curly C++(n = 2|F): {curly_C_2_pp_int[0]}")
            print(f"> Curly C0+(n = 2|F): {curly_C_2_0p_int[0]}")

            print(f"> Curly S++(n = 1|F): {curly_S_1_pp_int[0]}")
            print(f"> Curly S0+(n = 1|F): {curly_S_1_0p_int[0]}")
            print(f"> Curly S++(n = 2|F): {curly_S_2_pp_int[0]}")
            print(f"> Curly S0+(n = 2|F): {curly_S_2_0p_int[0]}")
            print(f"> Curly S++(n = 3|F): {curly_S_3_pp_int[0]}")
            print(f"> Curly S0+(n = 3|F): {curly_S_3_0p_int[0]}")
            
            c_0_interference_coefficient = C0_pp_lp_polarized * curly_C_0_pp_int.real + C0_0p_lp_polarized * curly_C_0_0p_int.real
            c_1_interference_coefficient = C1_pp_lp_polarized * curly_C_1_pp_int.real + C1_0p_lp_polarized * curly_C_1_0p_int.real
            c_2_interference_coefficient = C2_pp_lp_polarized * curly_C_2_pp_int.real + C2_0p_lp_polarized * curly_C_2_0p_int.real
            c_3_interference_coefficient = 0.
            s_1_interference_coefficient = S1_pp_lp_polarized * curly_S_1_pp_int.imag + S1_0p_lp_polarized * curly_S_1_0p_int.imag
            s_2_interference_coefficient = S2_pp_lp_polarized * curly_S_2_pp_int.imag + S2_0p_lp_polarized * curly_S_2_0p_int.imag
            s_3_interference_coefficient = S3_pp_lp_polarized * curly_S_3_pp_int.imag + S3_0p_lp_polarized * curly_S_3_0p_int.imag

        else:

            raise ValueError("[ERROR]: Unknown value for the target polarization.")
        
        # print(f"> c0: {c_0_interference_coefficient[0]}")
        # print(f"> c1: {c_1_interference_coefficient[0]}")
        # print(f"> c2: {c_2_interference_coefficient[0]}")
        # print(f"> c3: {c_3_interference_coefficient}")
        # print(f"> s1: {s_1_interference_coefficient[0]}")
        # print(f"> s2: {s_2_interference_coefficient[0]}")
        # print(f"> s3: {s_3_interference_coefficient[0]}")
        
        # plot_interference_contributions(
        #     azimuthal_phi,
        #     convert_to_nb_over_GeV4(c_0_interference_coefficient),
        #     convert_to_nb_over_GeV4(c_1_interference_coefficient),
        #     convert_to_nb_over_GeV4(c_2_interference_coefficient),
        #     convert_to_nb_over_GeV4(c_3_interference_coefficient),
        #     convert_to_nb_over_GeV4(s_1_interference_coefficient),
        #     convert_to_nb_over_GeV4(s_2_interference_coefficient),
        #     convert_to_nb_over_GeV4(s_3_interference_coefficient))

        interference_contribution = (prefactor * (
            c_0_interference_coefficient +
            c_1_interference_coefficient * np.cos(1. * (np.pi - azimuthal_phi)) +
            c_2_interference_coefficient * np.cos(2. * (np.pi - azimuthal_phi)) +
            c_3_interference_coefficient * np.cos(3. * (np.pi - azimuthal_phi)) +
            s_1_interference_coefficient * np.sin(1. * (np.pi - azimuthal_phi)) +
            s_2_interference_coefficient * np.sin(2. * (np.pi - azimuthal_phi)) +
            s_3_interference_coefficient * np.sin(3. * (np.pi - azimuthal_phi))))

        # (9.1): If verbose, print the calculation:
        if verbose:
            print(f"> Calculated the interference contribution to be:\n{interference_contribution}")
            
        # (8): Return the amplitude:
        return interference_contribution
    
    except Exception as ERROR:
        print(f"> Error in calculating the interference_contribution \n> {ERROR}")
        return 0.
    
    