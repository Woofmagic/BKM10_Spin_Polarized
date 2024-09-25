from coefficients.interference_coefficients.lp_polarized.pl_polarized_Spp1 import calculate_s_1_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_S0p1 import calculate_s_1_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Smp1 import calculate_s_1_minus_plus_longitudinally_polarized

from coefficients.interference_coefficients.lp_polarized.pl_polarized_Spp2 import calculate_s_2_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_S0p2 import calculate_s_2_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Smp2 import calculate_s_2_minus_plus_longitudinally_polarized

from coefficients.interference_coefficients.lp_polarized.pl_polarized_Spp3 import calculate_s_3_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Smp3 import calculate_s_3_minus_plus_longitudinally_polarized

from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_Spp import calculate_curly_S_plus_plus_longitudinally_polarized_interference
from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_S0p import calculate_curly_S_zero_plus_longitudinally_polarized_interference

from form_factors.effective_cffs import compute_cff_effective
from form_factors.effective_cffs import compute_cff_transverse

def calculate_s_1_interference_coefficient(
    n_number: int,
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float,
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float,
    skewness_parameter: float,
    t_prime: float,
    k_tilde: float,
    shorthand_k: float,
    Dirac_form_factor_F1: float,
    Pauli_form_factor_F2: float,
    compton_form_factor_h: complex,
    compton_form_factor_h_tilde: complex,
    compton_form_factor_e: complex,
    compton_form_factor_e_tilde: complex,
    verbose: bool = False) -> float:
    """
    """

    try:
            
        # (1): We compute the first part of the term: S_{++}(n = 1):
        s_plus_plus = calculate_s_1_plus_plus_longitudinally_polarized(
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            shorthand_k,
            verbose)

        # (2): The second part of the term is S_{0+}(n = 1):
        s_zero_plus = calculate_s_1_zero_plus_longitudinally_polarized(
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            k_tilde,
            verbose)
        
        # (3): The second part of the term is S_{-+}(n = 1):
        s_minus_plus = calculate_s_1_minus_plus_longitudinally_polarized(
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            shorthand_k,
            verbose)

        # (3): Calculate the curly S_{++} contribution - requires both n and the CFFs:
        curly_s_plus_plus = calculate_curly_S_plus_plus_longitudinally_polarized_interference(
            n_number,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            t_prime,
            k_tilde,
            shorthand_k,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            verbose)

        # (4): Calculate the curly S_{0+} contribution - requires both n and the CFFs:
        curly_s_zero_plus = calculate_curly_S_zero_plus_longitudinally_polarized_interference(
            n_number,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            shorthand_k,
            k_tilde,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compute_cff_effective(skewness_parameter, compton_form_factor_h),
            compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde),
            compute_cff_effective(skewness_parameter, compton_form_factor_e),
            compute_cff_effective(skewness_parameter, compton_form_factor_e_tilde),
            verbose)
        
        # (5): Calculate the curly S_{-+} contribution - requires both n and the CFFs:
        curly_s_minus_plus = calculate_curly_S_zero_plus_longitudinally_polarized_interference(
            n_number,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            shorthand_k,
            k_tilde,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compute_cff_transverse(skewness_parameter, compton_form_factor_h),
            compute_cff_transverse(skewness_parameter, compton_form_factor_h_tilde),
            compute_cff_transverse(skewness_parameter, compton_form_factor_e),
            compute_cff_transverse(skewness_parameter, compton_form_factor_e_tilde),
            verbose)
        
        # (5): Calculate the entire thing:
        # s_1_interference_coefficient = s_plus_plus * curly_s_plus_plus.imag + s_zero_plus * curly_s_zero_plus.imag + s_minus_plus * curly_s_minus_plus
        s_1_interference_coefficient = s_plus_plus * curly_s_plus_plus.imag + s_zero_plus * curly_s_zero_plus.imag

        # (): If verbose, print the output:
        if verbose:
            print(f"> Calculated s_1 interference coefficient to be:\n{s_1_interference_coefficient}")

        # (): Return the coefficient:
        return s_1_interference_coefficient
    
    except Exception as ERROR:
        print(f"> Error in s_1_interference_coefficient contribution to the interference term: \n> {ERROR}")
        return 0.
    
def calculate_s_2_interference_coefficient(
    n_number: int,
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float,
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float,
    skewness_parameter: float,
    t_prime: float,
    k_tilde: float,
    shorthand_k: float,
    Dirac_form_factor_F1: float,
    Pauli_form_factor_F2: float,
    compton_form_factor_h: complex,
    compton_form_factor_h_tilde: complex,
    compton_form_factor_e: complex,
    compton_form_factor_e_tilde: complex,
    verbose: bool = False) -> float:
    """
    """

    try:

        # (1): We compute the first part of the term: S_{++}(n = 2):
        s_plus_plus = calculate_s_2_plus_plus_longitudinally_polarized(
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            t_prime,
            k_tilde,
            verbose)

        # (2): The second part of the term is S_{0+}(n = 2):
        s_zero_plus = calculate_s_2_zero_plus_longitudinally_polarized(
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            shorthand_k,
            verbose)
        
        # (3): The second part of the term is S_{-+}(n = 2):
        s_minus_plus = calculate_s_2_minus_plus_longitudinally_polarized(
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            verbose)

        # (3): Calculate the curly S_{++} contribution - requires both n and the CFFs:
        curly_s_plus_plus = calculate_curly_S_plus_plus_longitudinally_polarized_interference(
            n_number,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            t_prime,
            k_tilde,
            shorthand_k,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            verbose)

        # (4): Calculate the curly S_{0+} contribution - requires both n and the CFFs:
        curly_s_zero_plus = calculate_curly_S_zero_plus_longitudinally_polarized_interference(
            n_number,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            shorthand_k,
            k_tilde,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compute_cff_effective(skewness_parameter, compton_form_factor_h),
            compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde),
            compute_cff_effective(skewness_parameter, compton_form_factor_e),
            compute_cff_effective(skewness_parameter, compton_form_factor_e_tilde),
            verbose)
        
        # (5): Calculate the curly S_{-+} contribution - requires both n and the CFFs:
        curly_s_minus_plus = calculate_curly_S_zero_plus_longitudinally_polarized_interference(
            n_number,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            shorthand_k,
            k_tilde,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compute_cff_transverse(skewness_parameter, compton_form_factor_h),
            compute_cff_transverse(skewness_parameter, compton_form_factor_h_tilde),
            compute_cff_transverse(skewness_parameter, compton_form_factor_e),
            compute_cff_transverse(skewness_parameter, compton_form_factor_e_tilde),
            verbose)
        
        # (5): Calculate the entire thing:
        # s_2_interference_coefficient = s_plus_plus * curly_s_plus_plus.imag + s_zero_plus * curly_s_zero_plus.imag + s_minus_plus * curly_s_minus_plus
        s_2_interference_coefficient = (s_plus_plus * curly_s_plus_plus.imag) + (s_zero_plus * curly_s_zero_plus.imag)

        # (): If verbose, print the output:
        if verbose:
            print(f"> Calculated s_2_interference_coefficient interference coefficient to be:\n{s_2_interference_coefficient}")

        # (): Return the coefficient:
        return s_2_interference_coefficient
    
    except Exception as ERROR:
        print(f"> Error in s_2_interference_coefficient contribution to the interference term: \n> {ERROR}")
        return 0.
    
def calculate_s_3_interference_coefficient(
    n_number: int,
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float,
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float,
    skewness_parameter: float,
    t_prime: float,
    k_tilde: float,
    shorthand_k: float,
    Dirac_form_factor_F1: float,
    Pauli_form_factor_F2: float,
    compton_form_factor_h: complex,
    compton_form_factor_h_tilde: complex,
    compton_form_factor_e: complex,
    compton_form_factor_e_tilde: complex,
    verbose: bool = False) -> float:
    """
    """

    s_plus_plus = 0.

    curly_s_plus_plus = 0.

    s_zero_plus = 0.

    curly_s_zero_plus = 0.

    s_minus_plus = 0.

    curly_s_minus_plus = 0.

    try:

        # (1): We compute the first part of the term: S_{++}(n = 3):
        s_plus_plus = calculate_s_3_plus_plus_longitudinally_polarized(
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            epsilon,
            lepton_energy_fraction_y,
            t_prime,
            shorthand_k,
            verbose)

        # (2): The second part of the term is S_{0+}(n = 2):
        s_zero_plus = 0.

        # (3): The second part of the term is S_{-+}(n = 3):
        s_minus_plus = calculate_s_3_minus_plus_longitudinally_polarized(
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            shorthand_k,
            verbose)

        # (3): Calculate the curly S_{++} contribution - requires both n and the CFFs:
        curly_s_plus_plus = calculate_curly_S_plus_plus_longitudinally_polarized_interference(
            n_number,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            t_prime,
            k_tilde,
            shorthand_k,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            verbose)

        # (4): Calculate the curly S_{0+} contribution - requires both n and the CFFs:
        curly_s_zero_plus = calculate_curly_S_zero_plus_longitudinally_polarized_interference(
            n_number,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            shorthand_k,
            k_tilde,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compute_cff_effective(skewness_parameter, compton_form_factor_h),
            compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde),
            compute_cff_effective(skewness_parameter, compton_form_factor_e),
            compute_cff_effective(skewness_parameter, compton_form_factor_e_tilde),
            verbose)
        
        # (5): Calculate the curly S_{-+} contribution - requires both n and the CFFs:
        curly_s_minus_plus = calculate_curly_S_zero_plus_longitudinally_polarized_interference(
            n_number,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            shorthand_k,
            k_tilde,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compute_cff_transverse(skewness_parameter, compton_form_factor_h),
            compute_cff_transverse(skewness_parameter, compton_form_factor_h_tilde),
            compute_cff_transverse(skewness_parameter, compton_form_factor_e),
            compute_cff_transverse(skewness_parameter, compton_form_factor_e_tilde),
            verbose)
        
        # (5): Calculate the entire thing:
        # s_3_interference_coefficient = s_plus_plus * curly_s_plus_plus.imag + s_zero_plus * curly_s_zero_plus.imag + s_minus_plus * curly_s_minus_plus.imag
        s_3_interference_coefficient = s_plus_plus * curly_s_plus_plus.imag + s_zero_plus * curly_s_zero_plus.imag

        # (): If verbose, print the output:
        if verbose:
            print(f"> Calculated s_3_interference_coefficient interference coefficient to be:\n{s_3_interference_coefficient}")

        # (): Return the coefficient:
        return s_3_interference_coefficient
    
    except Exception as ERROR:
        print(f"> Error in s_3_interference_coefficient contribution to the interference term: \n> {ERROR}")
        return 0.