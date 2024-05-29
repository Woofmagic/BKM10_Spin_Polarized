from coefficients.interference_coefficients.lp_polarized.pl_polarized_Spp1 import calculate_s_1_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_S0p1 import calculate_s_1_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_Spp2 import calculate_s_2_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_S0p2 import calculate_s_2_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_Spp3 import calculate_s_3_plus_plus_longitudinally_polarized

from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_Spp import calculate_curly_S_plus_plus_longitudinally_polarized_interference
from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_S0p import calculate_curly_S_zero_plus_longitudinally_polarized_interference

from form_factors.effective_cffs import compute_cff_effective

def calculate_s_interference_coefficient(
    n_number: int,
    lepton_polarization: float,
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
    compton_form_factor_h_real_part: float,
    compton_form_factor_h_tilde_real_part: float,
    compton_form_factor_e_real_part: float,
    compton_form_factor_e_tilde_real_part: float,
    verbose: bool = True) -> float:
    """
    """

    try:

        if n_number == 0:

            # (1): We compute the first part of the term: S++, n = 0
            s_plus_plus = 0.

            # (2): The second part of the term is S0+, n = 0
            s_zero_plus_n = 0.
            
        elif n_number == 1:

            # (1): We compute the first part of the term: S++, n = 1
            s_plus_plus = calculate_s_1_plus_plus_longitudinally_polarized(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            # (2): The second part of the term is S0+, n = 1
            s_zero_plus_n = calculate_s_1_zero_plus_longitudinally_polarized(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)
            
        elif n_number == 2:

            # (1): We compute the first part of the term: S++, n = 2
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

            # (2): The second part of the term is S0+, n = 2
            s_zero_plus_n = calculate_s_2_zero_plus_longitudinally_polarized(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

        elif n_number == 3:

            # (1): We compute the first part of the term: S++, n = 3
            s_plus_plus = calculate_s_3_plus_plus_longitudinally_polarized(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            # (2): The second part of the term is S0+, n = 3
            s_zero_plus_n = 0.

        # (3): Calculate the curly S_{++} contribution - requires both n and the CFFs:
        curly_s_plus_plus = calculate_curly_S_plus_plus_longitudinally_polarized_interference(
            n_number,
            lepton_polarization,
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
            compton_form_factor_h_real_part,
            compton_form_factor_h_tilde_real_part,
            compton_form_factor_e_real_part,
            compton_form_factor_e_tilde_real_part,
            verbose)

        # (4): Calculate the curly S_{+0} contribution - requires both n and the CFFs:
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
            compute_cff_effective(skewness_parameter, compton_form_factor_h_real_part),
            compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde_real_part),
            compute_cff_effective(skewness_parameter, compton_form_factor_e_real_part),
            compute_cff_effective(skewness_parameter, compton_form_factor_e_tilde_real_part),
            verbose)
        
        # (5): Calculate the entire thing:
        print(s_plus_plus, curly_s_plus_plus, s_zero_plus_n, curly_s_zero_plus)
        s_n_interference_coefficient = s_plus_plus * curly_s_plus_plus + s_zero_plus_n * curly_s_zero_plus

        # (): If verbose, print the output:
        if verbose:
            print(f"> Calculated s_{n_number} interference coefficient to be: {s_n_interference_coefficient}")

        # (): Return the coefficient:
        return s_n_interference_coefficient
    
    except Exception as ERROR:
        print(f"> Error in s_{n_number} contribution to the interference term: \n> {ERROR}")
        return 0.