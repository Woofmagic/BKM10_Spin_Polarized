"""
Compute the interference contribution to the cross-section according to
the BKM formalism
"""

import numpy as np

from utilities.plotting.plot_customizer import PlotCustomizer

from calculation.plot_results import plot_interference_contributions

# Helper Module | Convert GeV^{-6} to nb/GeV^{4}
from utilities.mathematics.math_units import convert_to_nb_over_GeV4

from calculation.plot_results import plot_interference_contributions

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
    squared_q_momentum_transfer: float,
    x_bjorken: float,
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
    dirac_form_factor_f1: float,
    pauli_form_factor_f2: float,
    compton_form_factor_h: complex,
    compton_form_factor_h_tilde: complex,
    compton_form_factor_e: complex,
    compton_form_factor_e_tilde: complex,
    use_ww: bool = False,
    verbose: bool = False,
    debugging: bool = False) -> float:
    """
    ## Description:
    We calculated the BKM10-predicted contribution of the interference between
    the BH and DVCS process.
    
    :param str lepton_helicity:
        (See BKM formalism.) Either `"positive"`, `"negative"`, or `"none"`. Nothing else! Specifies the helicity of the incoming
        lepton. The strings specifying the polarization are chosen with respect to the coordinate frame chosen in the BKM10 formalism.

    :param str target_polarization:
        (See BKM formalism.) Either `"polarized"` or `"unpolarized"`. Nothing else! 

    :param float squared_q_momentum_transfer: 
        The virtuality of the DVCS photon.

    :param float x_bjorken:
        Partonic momentum fraction of hadron.

    :param float squared_hadronic_momentum_transfer_t:
        Difference between final and initial hadron momentum (Mandelstam t).

    :param float lab_kinematics_k: 
        Incident lepton beam energy.

    :param np.ndarray azimuthal_phi: 
        An *array* of LAB azimuthal angles **in radians, not degrees**.

    :param float epsilon: 
        Dimensionless, simplifying parameter in the BKM10 formalism.

    :param float lepton_energy_fraction_y: 
        Inelasticity variable: describes the fraction of the initial lepton's energy lost to the virtual photon.

    :param float skewness_parameter: 
        Skewness parmaeter: describes the asymmetry in the distribution of partons in the hadron.

    :param float t_prime: 
        LATER!

    :param float k_tilde: 
        LATER!

    :param float shorthand_k: 
        LATER!

    :param np.ndarray lepton_propagator_p1:
        An *array* of azimuthally-modulating propagators in the denominator of the BH amplitude squared.

    :param np.ndarray lepton_propagator_p2:
        Another *array* of azimuthally-modulating propagators in the denominator of the BH amplitude squared.

    :param np.ndarray dirac_form_factor_f1:
        The Dirac Form Factor F_{1}: describes charge distribution in the hadron.

    :param np.ndarray pauli_form_factor_f2:
        The Pauli Form Factor F_{2}: describes theanomalous magnetic moment distribution in a hadron.

    :param complex compton_form_factor_h:
        The Compton Form Factor (CFF) called H.

    :param complex compton_form_factor_h_tilde:
        The Compton Form Factor (CFF) called Ht (H-tilde)

    :param complex compton_form_factor_e: 
        The Compton Form Factor (CFF) called E.

    :param complex compton_form_factor_e_tilde:
        The Compton Form Factor (CFF) called Et (E-tilde).
    
    :param bool verbose:
        If `True`, will print to inform user "where" in the code the program is.

    :param bool debugging:
        Do not turn this on! It will print *every step and computed piece of data in the code*.
    
    :returns bkm10_cross_section_in_nb_GeV4: (float)

            The four-fold differential cross section.

    ## Notes:

    ## Examples:
    """

    try:

        # (1): Calculate the prefactor:
        prefactor = 1. / (x_bjorken * lepton_energy_fraction_y**3 * squared_hadronic_momentum_transfer_t * lepton_propagator_p1 * lepton_propagator_p2)

        if verbose:
            print("[VERBOSE]: Computed Interference amplitude prefactor")

        if debugging:
            print(f"[DEBUG]: Computed Interference amplitude prefactor: {prefactor} ({type(prefactor)})")

        # (2): Initialize the Fourier coefficients:
        c_0_interference_coefficient = 0.
        
        if verbose:
            print("[VERBOSE]: Initialized Interference c0 coefficient.")

        if debugging:
            print(f"[DEBUG]: Initialized Interference c0 coefficient: {c_0_interference_coefficient} ({type(c_0_interference_coefficient)})")
            
        c_1_interference_coefficient = 0.

        if verbose:
            print("[VERBOSE]: Initialized Interference c1 coefficient.")

        if debugging:
            print(f"[DEBUG]: Initialized Interference c1 coefficient: {c_1_interference_coefficient} ({type(c_1_interference_coefficient)})")
            
        c_2_interference_coefficient = 0.

        if verbose:
            print("[VERBOSE]: Initialized Interference c2 coefficient.")

        if debugging:
            print(f"[DEBUG]: Initialized Interference c2 coefficient: {c_2_interference_coefficient} ({type(c_2_interference_coefficient)})")

        c_3_interference_coefficient = 0.

        if verbose:
            print("[VERBOSE]: Initialized Interference c3 coefficient.")

        if debugging:
            print(f"[DEBUG]: Initialized Interference c3 coefficient: {c_3_interference_coefficient} ({type(c_3_interference_coefficient)})")

        s_1_interference_coefficient = 0.

        if verbose:
            print("[VERBOSE]: Initialized Interference s1 coefficient.")

        if debugging:
            print(f"[DEBUG]: Initialized Interference s1 coefficient: {s_1_interference_coefficient} ({type(s_1_interference_coefficient)})")

        s_2_interference_coefficient = 0.

        if verbose:
            print("[VERBOSE]: Initialized Interference s2 coefficient.")

        if debugging:
            print(f"[DEBUG]: Initialized Interference s2 coefficient: {s_2_interference_coefficient} ({type(s_2_interference_coefficient)})")

        s_3_interference_coefficient = 0.

        if verbose:
            print("[VERBOSE]: Initialized Interference s3 coefficient.")

        if debugging:
            print(f"[DEBUG]: Initialized Interference s3 coefficient: {s_3_interference_coefficient} ({type(s_3_interference_coefficient)})")

        if target_polarization == 0.:

            curly_C_unpolarized_interference_for_pp = calculate_curly_C_unpolarized_interference(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                compton_form_factor_h,
                compton_form_factor_h_tilde,
                compton_form_factor_e,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed curly C++.")
            
            if debugging:
                print(f"[DEBUG]: Computed curly C++ {curly_C_unpolarized_interference_for_pp}")

            curly_C_V_unpolarized_interference_for_pp = calculate_curly_C_unpolarized_interference_V(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                compton_form_factor_h,
                compton_form_factor_e,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed curly CV++.")
            
            if debugging:
                print(f"[DEBUG]: Computed curly CV++ {curly_C_V_unpolarized_interference_for_pp}")

            curly_C_A_unpolarized_interference_for_pp = calculate_curly_C_unpolarized_interference_A(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                compton_form_factor_h_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed curly CA++.")
            
            if debugging:
                print(f"[DEBUG]: Computed curly CA++ {curly_C_A_unpolarized_interference_for_pp}")

            curly_C_unpolarized_interference_for_0p = calculate_curly_C_unpolarized_interference(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                compute_cff_effective(skewness_parameter, compton_form_factor_h, use_ww),
                compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde, use_ww),
                compute_cff_effective(skewness_parameter, compton_form_factor_e, use_ww),
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed curly C0+.")
            
            if debugging:
                print(f"[DEBUG]: Computed curly C0+ {curly_C_unpolarized_interference_for_0p}")

            curly_C_V_unpolarized_interference_for_0p = calculate_curly_C_unpolarized_interference_V(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                compute_cff_effective(skewness_parameter, compton_form_factor_h, use_ww),
                compute_cff_effective(skewness_parameter, compton_form_factor_e, use_ww),
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed curly CV0+.")
            
            if debugging:
                print(f"[DEBUG]: Computed curly CV0+ {curly_C_V_unpolarized_interference_for_0p}")

            curly_C_A_unpolarized_interference_for_0p = calculate_curly_C_unpolarized_interference_A(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde, use_ww),
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed curly CA0+.")
            
            if debugging:
                print(f"[DEBUG]: Computed curly CA0+ {curly_C_A_unpolarized_interference_for_0p}")

            C0_pp_unpolarized = calculate_c_0_plus_plus_unpolarized(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C++(n=0).")
            
            if debugging:
                print(f"[DEBUG]: Computed C++(n=0): {C0_pp_unpolarized}")

            C0V_pp_unpolarized = calculate_c_0_plus_plus_unpolarized_V(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C++V(n=0).")

            if debugging:
                print(f"[DEBUG]: Computed C++V(n=0): {C0V_pp_unpolarized}")

            C0A_pp_unpolarized = calculate_c_0_plus_plus_unpolarized_A(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C++A(n=0).")

            if debugging:
                print(f"[DEBUG]: Computed C++A(n=0): {C0A_pp_unpolarized}")

            C0_0p_unpolarized = calculate_c_0_zero_plus_unpolarized(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C0+(n=0).")

            if debugging:
                print(f"[DEBUG]: Computed C0+(n=0): {C0_0p_unpolarized}")

            C0V_0p_unpolarized = calculate_c_0_zero_plus_unpolarized_V(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C0+V(n=0).")

            if debugging:
                print(f"[DEBUG]: Computed C0+V(n=0): {C0V_0p_unpolarized}")

            C0A_0p_unpolarized = calculate_c_0_zero_plus_unpolarized_A(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C0+A(n=0).")

            if debugging:
                print(f"[DEBUG]: Computed C0+A(n=0): {C0A_0p_unpolarized}")

            C1_pp_unpolarized = calculate_c_1_plus_plus_unpolarized(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C++(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed C++(n=1): {C1_pp_unpolarized}")

            C1V_pp_unpolarized = calculate_c_1_plus_plus_unpolarized_V(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C++V(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed C++V(n=1): {C1V_pp_unpolarized}")

            C1A_pp_unpolarized = calculate_c_1_plus_plus_unpolarized_A(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C++A(n=1).")
            
            if debugging:
                print(f"[DEBUG]: Computed C++A(n=1): {C1A_pp_unpolarized}")

            C1_0p_unpolarized = calculate_c_1_zero_plus_unpolarized(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C0+(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed C0+(n=1): {C1_0p_unpolarized}")


            C1V_0p_unpolarized = calculate_c_1_zero_plus_unpolarized_V(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C0+A(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed C0+A(n=1): {C1V_0p_unpolarized}")

            C1A_0p_unpolarized = calculate_c_1_zero_plus_unpolarized_A(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C0+A(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed C0+A(n=1): {C1A_0p_unpolarized}")

            C2_pp_unpolarized = calculate_c_2_plus_plus_unpolarized(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                k_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C++(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed C++(n=2): {C2_pp_unpolarized}")

            C2V_pp_unpolarized = calculate_c_2_plus_plus_unpolarized_V(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                k_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C++V(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed C++V(n=2): {C2V_pp_unpolarized}")

            C2A_pp_unpolarized = calculate_c_2_plus_plus_unpolarized_A(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                k_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C++A(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed C++A(n=2): {C2A_pp_unpolarized}")

            C2_0p_unpolarized = calculate_c_2_zero_plus_unpolarized(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C0+(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed C0+(n=2): {C2_0p_unpolarized}")

            C2V_0p_unpolarized = calculate_c_2_zero_plus_unpolarized_V(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C0+V(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed C0+V(n=2): {C2V_0p_unpolarized}")

            C2A_0p_unpolarized = calculate_c_2_zero_plus_unpolarized_A(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C0+A(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed C0+A(n=2): {C2A_0p_unpolarized}")

            C3_pp_unpolarized = calculate_c_3_plus_plus_unpolarized(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C++(n=3).")

            if debugging:
                print(f"[DEBUG]: Computed C++(n=3): {C3_pp_unpolarized}")

            C3V_pp_unpolarized = calculate_c_3_plus_plus_unpolarized_V(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C++V(n=3).")

            if debugging:
                print(f"[DEBUG]: Computed C++V(n=3): {C3V_pp_unpolarized}")

            C3A_pp_unpolarized = calculate_c_3_plus_plus_unpolarized_A(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed C++A(n=3).")

            if debugging:
                print(f"[DEBUG]: Computed C++A(n=3): {C3A_pp_unpolarized}")

            C3_0p_unpolarized = 0.

            if verbose:
                print("[VERBOSE]: Computed C0+(n=3).")

            if debugging:
                print(f"[DEBUG]: Computed C0+(n=3): {C3_0p_unpolarized}")

            C3V_0p_unpolarized = 0.

            if verbose:
                print("[VERBOSE]: Computed CV0+(n=3).")

            if debugging:
                print(f"[DEBUG]: Computed CV0+(n=3): {C3V_0p_unpolarized}")

            C3A_0p_unpolarized = 0.

            if verbose:
                print("[VERBOSE]: Computed CA0+(n=3).")

            if debugging:
                print(f"[DEBUG]: Computed CA0+(n=3): {C3A_0p_unpolarized}")

            S1_pp_unpolarized = calculate_s_1_plus_plus_unpolarized(
                lepton_helicity,
                squared_q_momentum_transfer,
                x_bjorken,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed S++(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed S++(n=1): {S1_pp_unpolarized}")

            S1V_pp_unpolarized = calculate_s_1_plus_plus_unpolarized_V(
                lepton_helicity,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed S1++V(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed S++V(n=1): {S1V_pp_unpolarized}")

            S1A_pp_unpolarized = calculate_s_1_plus_plus_unpolarized_A(
                lepton_helicity,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed S++A(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed S++A(n=1): {S1A_pp_unpolarized}")

            S1_0p_unpolarized = calculate_s_1_zero_plus_unpolarized(
                lepton_helicity,
                squared_q_momentum_transfer,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed S0+(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed S0+(n=1): {S1_0p_unpolarized}")

            S1V_0p_unpolarized = calculate_s_1_zero_plus_unpolarized_V(
                lepton_helicity,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed S0+V(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed S0+V(n=1): {S1V_0p_unpolarized}")

            S1A_0p_unpolarized = calculate_s_1_zero_plus_unpolarized_A(
                lepton_helicity,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed S0+A(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed S0+A(n=1): {S1A_0p_unpolarized}")

            S2_pp_unpolarized = calculate_s_2_plus_plus_unpolarized(
                lepton_helicity,
                squared_q_momentum_transfer,
                x_bjorken,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed S++(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed S++(n=2): {S2_pp_unpolarized}")

            S2V_pp_unpolarized = calculate_s_2_plus_plus_unpolarized_V(
                lepton_helicity,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed S++V(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed S++V(n=2): {S2V_pp_unpolarized}")

            S2A_pp_unpolarized = calculate_s_2_plus_plus_unpolarized_A(
                lepton_helicity,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed S++A(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed S++A(n=2): {S2A_pp_unpolarized}")

            S2_0p_unpolarized = calculate_s_2_zero_plus_unpolarized(
                lepton_helicity,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed S0+(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed S0+(n=2): {S2_0p_unpolarized}")

            S2V_0p_unpolarized = calculate_s_2_zero_plus_unpolarized_V(
                lepton_helicity,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed S0+V(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed S0+V(n=2): {S2V_0p_unpolarized}")

            S2A_0p_unpolarized = calculate_s_2_zero_plus_unpolarized_A(
                lepton_helicity,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed S0+A(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed S0+A(n=2): {S2A_0p_unpolarized}")
            
            curly_C_0_pp_int =  (curly_C_unpolarized_interference_for_pp
                        + (C0V_pp_unpolarized * curly_C_V_unpolarized_interference_for_pp / C0_pp_unpolarized)
                        + (C0A_pp_unpolarized * curly_C_A_unpolarized_interference_for_pp / C0_pp_unpolarized))
            
            if verbose:
                print("[VERBOSE]: Computed curly C++(0).")

            if debugging:
                print(f"[DEBUG]: Computed curly C++(0): {curly_C_0_pp_int}")

            curly_C_0_0p_int =  ((np.sqrt(2. / squared_q_momentum_transfer) * k_tilde / (2. - x_bjorken)) * (curly_C_unpolarized_interference_for_0p
                        + (C0V_0p_unpolarized * curly_C_V_unpolarized_interference_for_0p / C0_0p_unpolarized)
                        + (C0A_0p_unpolarized * curly_C_A_unpolarized_interference_for_0p / C0_0p_unpolarized)))
            
            if verbose:
                print("[VERBOSE]: Computed curly C0+(0).")

            if debugging:
                print(f"[DEBUG]: Computed curly C0+(0): {curly_C_0_0p_int}")
            
            curly_C_1_pp_int =  (curly_C_unpolarized_interference_for_pp
                        + (C1V_pp_unpolarized * curly_C_V_unpolarized_interference_for_pp / C1_pp_unpolarized)
                        + (C1A_pp_unpolarized * curly_C_A_unpolarized_interference_for_pp / C1_pp_unpolarized))
            
            if verbose:
                print("[VERBOSE]: Computed curly C++(1).")

            if debugging:
                print(f"[DEBUG]: Computed curly C++(1): {curly_C_1_pp_int}")

            curly_C_1_0p_int =  ((np.sqrt(2. / squared_q_momentum_transfer) * k_tilde / (2. - x_bjorken)) * (curly_C_unpolarized_interference_for_0p
                        + (C1V_0p_unpolarized * curly_C_V_unpolarized_interference_for_0p / C1_0p_unpolarized)
                        + (C1A_0p_unpolarized * curly_C_A_unpolarized_interference_for_0p / C1_0p_unpolarized)))
            
            if verbose:
                print("[VERBOSE]: Computed curly C0+(1).")

            if debugging:
                print(f"[DEBUG]: Computed curly C0+(1): {curly_C_1_0p_int}")
            
            curly_C_2_pp_int =  (curly_C_unpolarized_interference_for_pp
                        + (C2V_pp_unpolarized * curly_C_V_unpolarized_interference_for_pp / C2_pp_unpolarized)
                        + (C2A_pp_unpolarized * curly_C_A_unpolarized_interference_for_pp / C2_pp_unpolarized))
            
            if verbose:
                print("[VERBOSE]: Computed curly C++(2).")

            if debugging:
                print(f"[DEBUG]: Computed curly C++(2): {curly_C_2_pp_int}")

            curly_C_2_0p_int =  ((np.sqrt(2. / squared_q_momentum_transfer) * k_tilde / (2. - x_bjorken)) * (curly_C_unpolarized_interference_for_0p
                        + (C2V_0p_unpolarized * curly_C_V_unpolarized_interference_for_0p / C2_0p_unpolarized)
                        + (C2A_0p_unpolarized * curly_C_A_unpolarized_interference_for_0p / C2_0p_unpolarized)))
            
            if verbose:
                print("[VERBOSE]: Computed curly C0+(2).")

            if debugging:
                print(f"[DEBUG]: Computed curly C0+(2): {curly_C_2_0p_int}")
            
            curly_C_3_pp_int =  (curly_C_unpolarized_interference_for_pp
                        + (C3V_pp_unpolarized * curly_C_V_unpolarized_interference_for_pp / C3_pp_unpolarized)
                        + (C3A_pp_unpolarized * curly_C_A_unpolarized_interference_for_pp / C3_pp_unpolarized))
            
            if verbose:
                print("[VERBOSE]: Computed curly C++(3).")

            if debugging:
                print(f"[DEBUG]: Computed curly C++(3): {curly_C_3_pp_int}")

            curly_C_3_0p_int =  ((np.sqrt(2. / squared_q_momentum_transfer) * k_tilde / (2. - x_bjorken)) * (curly_C_unpolarized_interference_for_0p))

            if verbose:
                print("[VERBOSE]: Computed curly C0+(3).")

            if debugging:
                print(f"[DEBUG]: Computed curly C0+(3): {curly_C_3_0p_int}")

            curly_S_1_pp_int =  (curly_C_unpolarized_interference_for_pp
                        + (S1V_pp_unpolarized * curly_C_V_unpolarized_interference_for_pp / S1_pp_unpolarized)
                        + (S1A_pp_unpolarized * curly_C_A_unpolarized_interference_for_pp / S1_pp_unpolarized))
            
            if verbose:
                print("[VERBOSE]: Computed curly S++(1).")

            if debugging:
                print(f"[DEBUG]: Computed curly S++(1): {curly_S_1_pp_int}")

            curly_S_1_0p_int =  ((np.sqrt(2. / squared_q_momentum_transfer) * k_tilde / (2. - x_bjorken)) * (curly_C_unpolarized_interference_for_0p
                        + (S1V_0p_unpolarized * curly_C_V_unpolarized_interference_for_0p / S1_0p_unpolarized)
                        + (S1A_0p_unpolarized * curly_C_A_unpolarized_interference_for_0p / S1_0p_unpolarized)))
            
            if verbose:
                print("[VERBOSE]: Computed curly S0+(1).")

            if debugging:
                print(f"[DEBUG]: Computed curly S0+(1): {curly_S_1_0p_int}")

            curly_S_2_pp_int =  (curly_C_unpolarized_interference_for_pp
                        + (S2V_pp_unpolarized * curly_C_V_unpolarized_interference_for_pp / S2_pp_unpolarized)
                        + (S2A_pp_unpolarized * curly_C_A_unpolarized_interference_for_pp / S2_pp_unpolarized))
            
            if verbose:
                print("[VERBOSE]: Computed curly S++(2).")

            if debugging:
                print(f"[DEBUG]: Computed curly S++(2): {curly_S_2_pp_int}")

            curly_S_2_0p_int =  ((np.sqrt(2. / squared_q_momentum_transfer) * k_tilde / (2. - x_bjorken)) * (curly_C_unpolarized_interference_for_0p
                        + (S2V_0p_unpolarized * curly_C_V_unpolarized_interference_for_0p / S2_0p_unpolarized)
                        + (S2A_0p_unpolarized * curly_C_A_unpolarized_interference_for_0p / S2_0p_unpolarized)))
            
            if verbose:
                print("[VERBOSE]: Computed curly S0+(2).")

            if debugging:
                print(f"[DEBUG]: Computed curly S0+(2): {curly_S_2_0p_int}")
            
            c_0_interference_coefficient = C0_pp_unpolarized * curly_C_0_pp_int.real + C0_0p_unpolarized * curly_C_0_0p_int.real

            if verbose:
                print("[VERBOSE]: Computed Interference c0 coefficient.")

            if debugging:
                print(f"[DEBUG]: Computed Interference c0 coefficient: {c_0_interference_coefficient}")

            c_1_interference_coefficient = C1_pp_unpolarized * curly_C_1_pp_int.real + C1_0p_unpolarized * curly_C_1_0p_int.real

            if verbose:
                print("[VERBOSE]: Computed Interference c1 coefficient.")

            if debugging:
                print(f"[DEBUG]: Computed Interference c1 coefficient: {c_1_interference_coefficient}")

            c_2_interference_coefficient = C2_pp_unpolarized * curly_C_2_pp_int.real + C2_0p_unpolarized * curly_C_2_0p_int.real

            if verbose:
                print("[VERBOSE]: Computed Interference c2 coefficient.")

            if debugging:
                print(f"[DEBUG]: Computed Interference c2 coefficient: {c_2_interference_coefficient}")

            c_3_interference_coefficient = C3_pp_unpolarized * curly_C_3_pp_int.real + C3_0p_unpolarized * curly_C_3_0p_int.real

            if verbose:
                print("[VERBOSE]: Computed Interference c3 coefficient.")

            if debugging:
                print(f"[DEBUG]: Computed Interference c3 coefficient: {c_3_interference_coefficient}")

            s_1_interference_coefficient = S1_pp_unpolarized * curly_S_1_pp_int.imag + S1_0p_unpolarized * curly_S_1_0p_int.imag

            if verbose:
                print("[VERBOSE]: Computed Interference s1 coefficient.")

            if debugging:
                print(f"[DEBUG]: Computed Interference s1 coefficient: {s_1_interference_coefficient}")
                
            s_2_interference_coefficient = S2_pp_unpolarized * curly_S_2_pp_int.imag + S2_0p_unpolarized * curly_S_2_0p_int.imag

            if verbose:
                print("[VERBOSE]: Computed Interference s2 coefficient.")

            if debugging:
                print(f"[DEBUG]: Computed Interference s2 coefficient: {s_2_interference_coefficient}")

            s_3_interference_coefficient = 0.

            if verbose:
                print("[VERBOSE]: Computed Interference s3 coefficient.")

            if debugging:
                print(f"[DEBUG]: Computed Interference s3 coefficient: {s_3_interference_coefficient}")

        elif target_polarization != 0.0:

            curly_C_lp_polarized_interference_for_pp = calculate_curly_C_longitudinally_polarized_interference(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                compton_form_factor_h,
                compton_form_factor_h_tilde,
                compton_form_factor_e,
                compton_form_factor_e_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed curly CLP++.")
            
            if debugging:
                print(f"[DEBUG]: Computed curly CLP++: {curly_C_lp_polarized_interference_for_pp}")           

            curly_C_V_lp_polarized_interference_for_pp = calculate_curly_C_longitudinally_polarized_interference_V(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                compton_form_factor_h,
                compton_form_factor_e,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed curly CLPV++.")
            
            if debugging:
                print(f"[DEBUG]: Computed curly CLPV++: {curly_C_V_lp_polarized_interference_for_pp}")    

            curly_C_A_lp_polarized_interference_for_pp = calculate_curly_C_longitudinally_polarized_interference_A(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                compton_form_factor_h_tilde,
                compton_form_factor_e_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed curly CLPA++.")
            
            if debugging:
                print(f"[DEBUG]: Computed curly CLPA++: {curly_C_A_lp_polarized_interference_for_pp}")

            curly_C_lp_polarized_interference_for_0p = calculate_curly_C_longitudinally_polarized_interference(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                compute_cff_effective(skewness_parameter, compton_form_factor_h, use_ww),
                compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde, use_ww),
                compute_cff_effective(skewness_parameter, compton_form_factor_e, use_ww),
                compute_cff_effective(skewness_parameter, compton_form_factor_e_tilde, use_ww),
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed curly CLP0+.")
            
            if debugging:
                print(f"[DEBUG]: Computed curly CLP0+: {curly_C_lp_polarized_interference_for_0p}")

            curly_C_V_lp_polarized_interference_for_0p = calculate_curly_C_longitudinally_polarized_interference_V(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                compute_cff_effective(skewness_parameter, compton_form_factor_h, use_ww),
                compute_cff_effective(skewness_parameter, compton_form_factor_e, use_ww),
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed curly CLPV0+.")
            
            if debugging:
                print(f"[DEBUG]: Computed curly CLPV0+: {curly_C_V_lp_polarized_interference_for_0p}")

            curly_C_A_lp_polarized_interference_for_0p = calculate_curly_C_longitudinally_polarized_interference_A(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde, use_ww),
                compute_cff_effective(skewness_parameter, compton_form_factor_e_tilde, use_ww),
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed curly CLPA0+.")
            
            if debugging:
                print(f"[DEBUG]: Computed curly CLPA0+: {curly_C_A_lp_polarized_interference_for_0p}")
            
            C0_pp_lp_polarized = calculate_c_0_plus_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed CLP++(n=0).")

            if debugging:
                print(f"[DEBUG]: Computed CLP++(n=0): {C0_pp_lp_polarized}")

            C0V_pp_lp_polarized = calculate_c_0_plus_plus_longitudinally_polarized_V(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed CLP++V(n=0).")

            if debugging:
                print(f"[DEBUG]: Computed CLP++V(n=0): {C0V_pp_lp_polarized}")

            C0A_pp_lp_polarized = calculate_c_0_plus_plus_longitudinally_polarized_A(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed CLP++A(n=0).")

            if debugging:
                print(f"[DEBUG]: Computed CLP++A(n=0): {C0A_pp_lp_polarized}")

            C0_0p_lp_polarized = calculate_c_0_zero_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed CLP0+(n=0).")

            if debugging:
                print(f"[DEBUG]: Computed CLP0+(n=0): {C0_0p_lp_polarized}")

            C0V_0p_lp_polarized = calculate_c_0_zero_plus_longitudinally_polarized_V(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed CLP0+V(n=0).")

            if debugging:
                print(f"[DEBUG]: Computed CLP0+V(n=0): {C0V_0p_lp_polarized}")

            C0A_0p_lp_polarized = calculate_c_0_zero_plus_longitudinally_polarized_A(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed CLP0+A(n=0).")

            if debugging:
                print(f"[DEBUG]: Computed CLP0+A(n=0): {C0A_0p_lp_polarized}")
            
            C1_pp_lp_polarized = calculate_c_1_plus_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed CLP++(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed CLP++(n=1): {C1_pp_lp_polarized}")

            C1V_pp_lp_polarized = calculate_c_1_plus_plus_longitudinally_polarized_V(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed CLP++V(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed CLP++V(n=1): {C1V_pp_lp_polarized}")

            C1A_pp_lp_polarized = calculate_c_1_plus_plus_longitudinally_polarized_A(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed CLP++A(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed CLP++A(n=1): {C1A_pp_lp_polarized}")

            C1_0p_lp_polarized = calculate_c_1_zero_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed CLP0+(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed CLP0+(n=1): {C1_0p_lp_polarized}")

            C1V_0p_lp_polarized = calculate_c_1_zero_plus_longitudinally_polarized_V(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed CLP0+V(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed CLP0+V(n=1): {C1V_0p_lp_polarized}")
            
            C1A_0p_lp_polarized = 0.

            if verbose:
                print("[VERBOSE]: Computed CLP0+A(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed CLP0+A(n=1): {C1A_0p_lp_polarized}")

            C2_pp_lp_polarized = calculate_c_2_plus_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed CLP++(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed CLP++(n=2): {C2_pp_lp_polarized}")

            C2V_pp_lp_polarized = calculate_c_2_plus_plus_longitudinally_polarized_V(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed CLP++V(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed CLP++V(n=2): {C2V_pp_lp_polarized}")

            C2A_pp_lp_polarized = calculate_c_2_plus_plus_longitudinally_polarized_A(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed CLP++A(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed CLP++A(n=2): {C2A_pp_lp_polarized}")

            C2_0p_lp_polarized = calculate_c_2_zero_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed CLP0+(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed CLP0+(n=2): {C2_0p_lp_polarized}")

            C2V_0p_lp_polarized = calculate_c_2_zero_plus_longitudinally_polarized_V(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed CLP0+V(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed CLP0+V(n=2): {C2V_0p_lp_polarized}")

            C2A_0p_lp_polarized = calculate_c_2_zero_plus_longitudinally_polarized_A(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed CLP0+A(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed CLP0+A(n=2): {C2A_0p_lp_polarized}")
            
            S1_pp_lp_polarized = calculate_s_1_plus_plus_longitudinally_polarized(
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed SLP++(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed SLP++(n=1): {S1_pp_lp_polarized}")

            S1V_pp_lp_polarized = calculate_s_1_plus_plus_longitudinally_polarized_V(
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed SLP++V(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed SLP++V(n=1): {S1V_pp_lp_polarized}")

            S1A_pp_lp_polarized = calculate_s_1_plus_plus_longitudinally_polarized_A(
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed SLP++A(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed SLP++A(n=1): {S1A_pp_lp_polarized}")

            S1_0p_lp_polarized = calculate_s_1_zero_plus_longitudinally_polarized(
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed SLP0+(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed SLP0+(n=1): {S1_0p_lp_polarized}")
            
            S1V_0p_lp_polarized = calculate_s_1_zero_plus_longitudinally_polarized_V(
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed SLP0+V(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed SLP0+V(n=1): {S1V_0p_lp_polarized}")
            
            S1A_0p_lp_polarized = calculate_s_1_zero_plus_longitudinally_polarized_A(
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed SLP0+A(n=1).")

            if debugging:
                print(f"[DEBUG]: Computed SLP0+A(n=1): {S1A_0p_lp_polarized}")

            S2_pp_lp_polarized = calculate_s_2_plus_plus_longitudinally_polarized(
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                k_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed SLP++(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed SLP++(n=2): {S2_pp_lp_polarized}")

            S2V_pp_lp_polarized = calculate_s_2_plus_plus_longitudinally_polarized_V(
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                k_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed SLP++V(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed SLP++V(n=2): {S2V_pp_lp_polarized}")

            S2A_pp_lp_polarized = calculate_s_2_plus_plus_longitudinally_polarized_A(
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                k_tilde,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed SLP++A(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed SLP++A(n=2): {S2A_pp_lp_polarized}")

            S2_0p_lp_polarized = calculate_s_2_zero_plus_longitudinally_polarized(
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed SLP0+(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed SLP0+(n=2): {S2_0p_lp_polarized}")

            S2V_0p_lp_polarized = calculate_s_2_zero_plus_longitudinally_polarized_V(
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed SLP0+V(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed SLP0+V(n=2): {S2V_0p_lp_polarized}")
            
            S2A_0p_lp_polarized = calculate_s_2_zero_plus_longitudinally_polarized_A(
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed SLP0+A(n=2).")

            if debugging:
                print(f"[DEBUG]: Computed SLP0+A(n=2): {S2A_0p_lp_polarized}")
            
            S3_pp_lp_polarized = calculate_s_3_plus_plus_longitudinally_polarized(
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed SLP++(n=3).")

            if debugging:
                print(f"[DEBUG]: Computed SLP++(n=3): {S3_pp_lp_polarized}")

            S3V_pp_lp_polarized = calculate_s_3_plus_plus_longitudinally_polarized_V(
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed SLP++V(n=3).")

            if debugging:
                print(f"[DEBUG]: Computed SLP++V(n=3): {S3V_pp_lp_polarized}")

            S3A_pp_lp_polarized = calculate_s_3_plus_plus_longitudinally_polarized_A(
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed SLP++A(n=3).")

            if debugging:
                print(f"[DEBUG]: Computed SLP++A(n=3): {S3A_pp_lp_polarized}")

            S3_0p_lp_polarized = 0.

            if verbose:
                print("[VERBOSE]: Computed SLP0+(n=3).")

            if debugging:
                print(f"[DEBUG]: Computed SLP0+(n=3): {S3_0p_lp_polarized}")

            S3V_0p_lp_polarized = 0.

            if verbose:
                print("[VERBOSE]: Computed SLP0+V(n=3).")

            if debugging:
                print(f"[DEBUG]: Computed SLP0+V(n=3): {S3V_0p_lp_polarized}")
            
            S3A_0p_lp_polarized = 0.

            if verbose:
                print("[VERBOSE]: Computed SLP0+A(n=3).")

            if debugging:
                print(f"[DEBUG]: Computed SLP0+A(n=3): {S3A_0p_lp_polarized}")
            
            curly_C_0_pp_int =  (curly_C_lp_polarized_interference_for_pp
                        + (C0V_pp_lp_polarized * curly_C_V_lp_polarized_interference_for_pp / C0_pp_lp_polarized)
                        + (C0A_pp_lp_polarized * curly_C_A_lp_polarized_interference_for_pp / C0_pp_lp_polarized))
            
            if verbose:
                print("[VERBOSE]: Computed curly CLP++(0).")

            if debugging:
                print(f"[DEBUG]: Computed curly CLP++(0): {curly_C_0_pp_int}")

            curly_C_0_0p_int =  ((np.sqrt(2. / squared_q_momentum_transfer) * k_tilde / (2. - x_bjorken)) * (curly_C_lp_polarized_interference_for_0p
                        + (C0V_0p_lp_polarized * curly_C_V_lp_polarized_interference_for_0p / C0_0p_lp_polarized)
                        + (C0A_0p_lp_polarized * curly_C_A_lp_polarized_interference_for_0p / C0_0p_lp_polarized)))
            
            if verbose:
                print("[VERBOSE]: Computed curly CLP0+(0).")

            if debugging:
                print(f"[DEBUG]: Computed curly CLP0+(0): {curly_C_0_0p_int}")
            
            curly_C_1_pp_int =  (curly_C_lp_polarized_interference_for_pp
                        + (C1V_pp_lp_polarized * curly_C_V_lp_polarized_interference_for_pp / C1_pp_lp_polarized)
                        + (C1A_pp_lp_polarized * curly_C_A_lp_polarized_interference_for_pp / C1_pp_lp_polarized))
            
            if verbose:
                print("[VERBOSE]: Computed curly CLP++(1).")

            if debugging:
                print(f"[DEBUG]: Computed curly CLP++(1): {curly_C_1_pp_int}")

            curly_C_1_0p_int =  ((np.sqrt(2. / squared_q_momentum_transfer) * k_tilde / (2. - x_bjorken)) * (curly_C_lp_polarized_interference_for_0p
                        + (C1V_0p_lp_polarized * curly_C_V_lp_polarized_interference_for_0p / C1_0p_lp_polarized)
                        + (C1A_0p_lp_polarized * curly_C_A_lp_polarized_interference_for_0p / C1_0p_lp_polarized)))
            
            if verbose:
                print("[VERBOSE]: Computed curly CLP0+(1).")

            if debugging:
                print(f"[DEBUG]: Computed curly CLP0+(1): {curly_C_1_0p_int}")
            
            curly_C_2_pp_int =  (curly_C_lp_polarized_interference_for_pp
                        + (C2V_pp_lp_polarized * curly_C_V_lp_polarized_interference_for_pp / C2_pp_lp_polarized)
                        + (C2A_pp_lp_polarized * curly_C_A_lp_polarized_interference_for_pp / C2_pp_lp_polarized))
            
            if verbose:
                print("[VERBOSE]: Computed curly CLP++(2).")

            if debugging:
                print(f"[DEBUG]: Computed curly CLP++(2): {curly_C_2_pp_int}")

            curly_C_2_0p_int =  ((np.sqrt(2. / squared_q_momentum_transfer) * k_tilde / (2. - x_bjorken)) * (curly_C_lp_polarized_interference_for_0p
                        + (C2V_0p_lp_polarized * curly_C_V_lp_polarized_interference_for_0p / C2_0p_lp_polarized)
                        + (C2A_0p_lp_polarized * curly_C_A_lp_polarized_interference_for_0p / C2_0p_lp_polarized)))
            
            if verbose:
                print("[VERBOSE]: Computed curly CLP0+(2).")

            if debugging:
                print(f"[DEBUG]: Computed curly CLP0+(2): {curly_C_2_0p_int}")
            
            curly_C_3_pp_int = 0.

            if verbose:
                print("[VERBOSE]: Computed curly CLP++(3).")

            if debugging:
                print(f"[DEBUG]: Computed curly CLP++(3): {curly_C_3_pp_int}")

            curly_C_3_0p_int = 0.

            if verbose:
                print("[VERBOSE]: Computed curly CLP0+(3).")

            if debugging:
                print(f"[DEBUG]: Computed curly CLP0+(3): {curly_C_3_0p_int}")

            curly_S_1_pp_int =  (curly_C_lp_polarized_interference_for_pp
                        + (S1V_pp_lp_polarized * curly_C_V_lp_polarized_interference_for_pp / S1_pp_lp_polarized)
                        + (S1A_pp_lp_polarized * curly_C_A_lp_polarized_interference_for_pp / S1_pp_lp_polarized))
            
            if verbose:
                print("[VERBOSE]: Computed curly SLP++(1).")

            if debugging:
                print(f"[DEBUG]: Computed curly SLP++(1): {curly_S_1_pp_int}")

            curly_S_1_0p_int =  ((np.sqrt(2. / squared_q_momentum_transfer) * k_tilde / (2. - x_bjorken)) * (curly_C_lp_polarized_interference_for_0p
                        + (S1V_0p_lp_polarized * curly_C_V_lp_polarized_interference_for_0p / S1_0p_lp_polarized)
                        + (S1A_0p_lp_polarized * curly_C_A_lp_polarized_interference_for_0p / S1_0p_lp_polarized)))
            
            if verbose:
                print("[VERBOSE]: Computed curly SLP0+(1).")

            if debugging:
                print(f"[DEBUG]: Computed curly SLP0+(1): {curly_S_1_0p_int}")

            curly_S_2_pp_int =  (curly_C_lp_polarized_interference_for_pp
                        + (S2V_pp_lp_polarized * curly_C_V_lp_polarized_interference_for_pp / S2_pp_lp_polarized)
                        + (S2A_pp_lp_polarized * curly_C_A_lp_polarized_interference_for_pp / S2_pp_lp_polarized))
            
            if verbose:
                print("[VERBOSE]: Computed curly SLP++(2).")

            if debugging:
                print(f"[DEBUG]: Computed curly SLP++(2): {curly_S_2_pp_int}")

            curly_S_2_0p_int =  ((np.sqrt(2. / squared_q_momentum_transfer) * k_tilde / (2. - x_bjorken)) * (curly_C_lp_polarized_interference_for_0p
                        + (S2V_0p_lp_polarized * curly_C_V_lp_polarized_interference_for_0p / S2_0p_lp_polarized)
                        + (S2A_0p_lp_polarized * curly_C_A_lp_polarized_interference_for_0p / S2_0p_lp_polarized)))
            
            if verbose:
                print("[VERBOSE]: Computed curly SLP0+(2).")

            if debugging:
                print(f"[DEBUG]: Computed curly SLP0+(2): {curly_S_2_0p_int}")
            
            curly_S_3_pp_int =  (curly_C_lp_polarized_interference_for_pp
                        + (S3V_pp_lp_polarized * curly_C_V_lp_polarized_interference_for_pp / S3_pp_lp_polarized)
                        + (S3A_pp_lp_polarized * curly_C_A_lp_polarized_interference_for_pp / S3_pp_lp_polarized))
            
            if verbose:
                print("[VERBOSE]: Computed curly SLP++(3).")

            if debugging:
                print(f"[DEBUG]: Computed curly SLP++(3): {curly_S_3_pp_int}")

            curly_S_3_0p_int =  ((np.sqrt(2. / squared_q_momentum_transfer) * k_tilde / (2. - x_bjorken)) * (curly_C_lp_polarized_interference_for_0p
            + 0.
            + 0.))

            if verbose:
                print("[VERBOSE]: Computed curly SLP0+(3).")

            if debugging:
                print(f"[DEBUG]: Computed curly SLP0+(3): {curly_S_3_0p_int}")
            
            c_0_interference_coefficient = C0_pp_lp_polarized * curly_C_0_pp_int.real + C0_0p_lp_polarized * curly_C_0_0p_int.real

            if verbose:
                print("[VERBOSE]: Computed Interference LP c0 coefficient.")

            if debugging:
                print(f"[DEBUG]: Computed Interference LP c0 coefficient: {c_0_interference_coefficient}")

            c_1_interference_coefficient = C1_pp_lp_polarized * curly_C_1_pp_int.real + C1_0p_lp_polarized * curly_C_1_0p_int.real

            if verbose:
                print("[VERBOSE]: Computed Interference LP c1 coefficient.")

            if debugging:
                print(f"[DEBUG]: Computed Interference LP c1 coefficient: {c_1_interference_coefficient}")
                
            c_2_interference_coefficient = C2_pp_lp_polarized * curly_C_2_pp_int.real + C2_0p_lp_polarized * curly_C_2_0p_int.real

            if verbose:
                print("[VERBOSE]: Computed Interference LP c2 coefficient.")

            if debugging:
                print(f"[DEBUG]: Computed Interference LP c2 coefficient: {c_2_interference_coefficient}")
                
            c_3_interference_coefficient = 0.

            if verbose:
                print("[VERBOSE]: Computed Interference LP c3 coefficient.")

            if debugging:
                print(f"[DEBUG]: Computed Interference LP c3 coefficient: {c_3_interference_coefficient}")

            s_1_interference_coefficient = S1_pp_lp_polarized * curly_S_1_pp_int.imag + S1_0p_lp_polarized * curly_S_1_0p_int.imag

            if verbose:
                print("[VERBOSE]: Computed Interference LP s1 coefficient.")

            if debugging:
                print(f"[DEBUG]: Computed Interference LP s1 coefficient: {s_1_interference_coefficient}")

            s_2_interference_coefficient = S2_pp_lp_polarized * curly_S_2_pp_int.imag + S2_0p_lp_polarized * curly_S_2_0p_int.imag

            if verbose:
                print("[VERBOSE]: Computed Interference LP s2 coefficient.")

            if debugging:
                print(f"[DEBUG]: Computed Interference LP s2 coefficient: {s_2_interference_coefficient}")

            s_3_interference_coefficient = S3_pp_lp_polarized * curly_S_3_pp_int.imag + S3_0p_lp_polarized * curly_S_3_0p_int.imag

            if verbose:
                print("[VERBOSE]: Computed Interference LP s3 coefficient.")

            if debugging:
                print(f"[DEBUG]: Computed Interference LP s3s coefficient: {s_3_interference_coefficient}")

        else:
            raise ValueError("[ERROR]: Unknown value for the target polarization.")

        interference_contribution = (prefactor * (
            c_0_interference_coefficient +
            c_1_interference_coefficient * np.cos(1. * (np.pi - azimuthal_phi)) +
            c_2_interference_coefficient * np.cos(2. * (np.pi - azimuthal_phi)) +
            c_3_interference_coefficient * np.cos(3. * (np.pi - azimuthal_phi)) +
            s_1_interference_coefficient * np.sin(1. * (np.pi - azimuthal_phi)) +
            s_2_interference_coefficient * np.sin(2. * (np.pi - azimuthal_phi)) +
            s_3_interference_coefficient * np.sin(3. * (np.pi - azimuthal_phi))))

        if verbose:
            print("[VERBOSE]: Calculated the interference contribution.")

        if debugging:
            print(f"[DEBUG]: Calculated the interference contribution to be:{interference_contribution}")
            
        # (8): Return the amplitude:
        return interference_contribution
    
    except Exception as e:
        print(f"[ERROR]: Errors in calculating the interference_contribution \n> {e}")
        return 0.
    
    