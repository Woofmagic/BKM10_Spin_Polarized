from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_CLP import calculate_curly_C_longitudinally_polarized_interference
from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_CLPV import calculate_curly_C_longitudinally_polarized_interference_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_CLPA import calculate_curly_C_longitudinally_polarized_interference_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp1 import calculate_s_1_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp1V import calculate_s_1_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp1A import calculate_s_1_plus_plus_longitudinally_polarized_A
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp2 import calculate_s_2_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp2V import calculate_s_2_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp2A import calculate_s_2_plus_plus_longitudinally_polarized_A
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp3 import calculate_s_3_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp3V import calculate_s_3_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp3A import calculate_s_3_plus_plus_longitudinally_polarized_A

def calculate_curly_S_plus_plus_longitudinally_polarized_interference(
    n_number: int,
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float,
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float,
    t_prime: float,
    k_tilde: float,
    shorthand_k: float,
    Dirac_form_factor_F1: float,
    Pauli_form_factor_F2: float,
    compton_form_factor_h_real_part: float,
    compton_form_factor_h_tilde_real_part: float,
    compton_form_factor_e_real_part: float,
    compton_form_factor_e_tilde_real_part: float,
    verbose: bool = False) -> float:

    try:

        # (1): Calculate curly C_{LP}^{I}(F):
        curly_C_longitudinally_polarized_interference = calculate_curly_C_longitudinally_polarized_interference(
            squared_Q_momentum_transfer, 
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h_real_part,
            compton_form_factor_h_tilde_real_part,
            compton_form_factor_e_real_part,
            compton_form_factor_e_tilde_real_part,
            verbose)
        
        # (2): Calculate curly C_{LP}^{I, V}(F):
        curly_C_V_longitudinally_polarized_interference = calculate_curly_C_longitudinally_polarized_interference_V(
            squared_Q_momentum_transfer, 
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h_real_part,
            compton_form_factor_e_real_part,
            verbose)
        
        # (3): Calculate curly C_{LP}^{I, A}(F):
        curly_C_A_longitudinally_polarized_interference = calculate_curly_C_longitudinally_polarized_interference_A(
            squared_Q_momentum_transfer, 
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h_tilde_real_part,
            compton_form_factor_e_tilde_real_part,
            verbose)
        
        # (4): Split on the integer n:
        if n_number == 0:

            # (4.1): Calculate the S_{++}(0) contribution
            s_plus_plus_contribution = 0.

            # (4.2): Calculate the S_{++}^{V}(0) contribution
            s_V_plus_plus_contribution = 0.

            # (4.3): Calculate the S_{++}^{A}(0) contribution
            s_A_plus_plus_contribution = 0.

        elif n_number == 1:

            # (4.1): Calculate the S_{++}(1) contribution
            s_plus_plus_contribution = calculate_s_1_plus_plus_longitudinally_polarized(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            # (4.2): Calculate the S_{++}^{V}(1) contribution
            s_V_plus_plus_contribution = calculate_s_1_plus_plus_longitudinally_polarized_V(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            # (4.3): Calculate the S_{++}^{A}(1) contribution
            s_A_plus_plus_contribution = calculate_s_1_plus_plus_longitudinally_polarized_A(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

        elif n_number == 2:

            # (4.1): Calculate the S_{++}(2) contribution
            s_plus_plus_contribution = calculate_s_2_plus_plus_longitudinally_polarized(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                k_tilde,
                verbose)

            # (4.2): Calculate the S_{++}^{V}(2) contribution
            s_V_plus_plus_contribution = calculate_s_2_plus_plus_longitudinally_polarized_V(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                k_tilde,
                verbose)

            # (4.3): Calculate the S_{++}^{A}(2) contribution
            s_A_plus_plus_contribution = calculate_s_2_plus_plus_longitudinally_polarized_A(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                k_tilde,
                verbose)

        elif n_number == 3:

            # (4.1): Calculate the S_{++}(3) contribution
            s_plus_plus_contribution = calculate_s_3_plus_plus_longitudinally_polarized(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            # (4.2): Calculate the S_{++}^{V}(3) contribution
            s_V_plus_plus_contribution = calculate_s_3_plus_plus_longitudinally_polarized_V(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            # (4.3): Calculate the S_{++}^{A}(3) contribution
            s_A_plus_plus_contribution = calculate_s_3_plus_plus_longitudinally_polarized_A(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

        # (6): 
        curly_S_longitudinally_polarized_interference = curly_C_longitudinally_polarized_interference + (s_V_plus_plus_contribution * curly_C_V_longitudinally_polarized_interference / s_plus_plus_contribution) + (s_A_plus_plus_contribution * curly_C_A_longitudinally_polarized_interference / s_plus_plus_contribution)

        # (6.1): If verbose, print the calculation:
        if verbose:
            print(f"> Calculated curly S++ to be:\n{curly_S_longitudinally_polarized_interference}")

        # (7): Return the output.
        return curly_S_longitudinally_polarized_interference

    except Exception as ERROR:
        print(f"> Error in calculating the curly S LP entire contribution amplitude squared\n> {ERROR}")
        return 0