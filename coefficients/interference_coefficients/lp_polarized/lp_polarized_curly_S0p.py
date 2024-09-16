import numpy as np

from coefficients.interference_coefficients.lp_polarized.lp_polarized_C0p0 import calculate_c_0_zero_plus_longitudinally_polarized

from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_CLP import calculate_curly_C_longitudinally_polarized_interference
from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_CLPV import calculate_curly_C_longitudinally_polarized_interference_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_CLPA import calculate_curly_C_longitudinally_polarized_interference_A

from coefficients.interference_coefficients.lp_polarized.pl_polarized_S0p1 import calculate_s_1_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_S0p1V import calculate_s_1_zero_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.pl_polarized_S0p1A import calculate_s_1_zero_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.pl_polarized_S0p2 import calculate_s_2_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_S0p2V import calculate_s_2_zero_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.pl_polarized_S0p2A import calculate_s_2_zero_plus_longitudinally_polarized_A


def calculate_curly_S_zero_plus_longitudinally_polarized_interference(
    n_number: int,
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float,
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float,
    shorthand_k: float,
    k_tilde: float,
    Dirac_form_factor_F1: float,
    Pauli_form_factor_F2: float,
    compton_form_factor_h_eff: float,
    compton_form_factor_h_tilde_eff: float,
    compton_form_factor_e_eff: float,
    compton_form_factor_e_tilde_eff: float,
    verbose: bool = False) -> float:

    try:

        # (1): Calculate the prefactor: Ktilde/ (2 - xb) * sqrt(2 / Q^{2})
        prefactor = np.sqrt(2. / squared_Q_momentum_transfer) * k_tilde / (2. - x_Bjorken)

        # (2): Calculate curly C_{LP}^{I}(F):
        curly_C_longitudinally_polarized_interference = calculate_curly_C_longitudinally_polarized_interference(
            squared_Q_momentum_transfer, 
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h_eff,
            compton_form_factor_h_tilde_eff,
            compton_form_factor_e_eff,
            compton_form_factor_e_tilde_eff,
            verbose)
        
        # (3): Calculate curly C_{LP}^{I, V}(F):
        curly_C_V_longitudinally_polarized_interference = calculate_curly_C_longitudinally_polarized_interference_V(
            squared_Q_momentum_transfer, 
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h_eff,
            compton_form_factor_e_eff,
            verbose)
        
        # (4): Calculate curly C_{LP}^{I, A}(F):
        curly_C_A_longitudinally_polarized_interference = calculate_curly_C_longitudinally_polarized_interference_A(
            squared_Q_momentum_transfer, 
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h_tilde_eff,
            compton_form_factor_e_tilde_eff,
            verbose)
        
        if n_number == 0:

            # (6): Calculate the curly S0+ coefficient:
            curly_S_longitudinally_polarized_interference = 0.

        elif n_number == 1:

            # (5.1): Calculate the S_{0+}(1) contribution
            s_zero_plus_contribution = calculate_s_1_zero_plus_longitudinally_polarized(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)

            # (5.2): Calculate the S_{0+}^{V}(1) contribution
            s_V_zero_plus_contribution = calculate_s_1_zero_plus_longitudinally_polarized_V(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)

            # (5.3): Calculate the C_{S+}^{A}(1) contribution
            s_A_zero_plus_contribution = calculate_s_1_zero_plus_longitudinally_polarized_A(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                verbose)
            
            # (6): Calculate the curly S0+ coefficient:
            curly_S_longitudinally_polarized_interference = prefactor * (curly_C_longitudinally_polarized_interference + (s_V_zero_plus_contribution * curly_C_V_longitudinally_polarized_interference / s_zero_plus_contribution) + (s_A_zero_plus_contribution * curly_C_A_longitudinally_polarized_interference / s_zero_plus_contribution))

        elif n_number == 2:

            # (5.1): Calculate the S_{0+}(2) contribution
            s_zero_plus_contribution = calculate_s_2_zero_plus_longitudinally_polarized(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            # (5.2): Calculate the S_{0+}^{V}(2) contribution
            s_V_zero_plus_contribution = calculate_s_2_zero_plus_longitudinally_polarized_V(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            # (5.3): Calculate the S_{0+}^{A}(2) contribution
            s_A_zero_plus_contribution = calculate_s_2_zero_plus_longitudinally_polarized_A(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            # (6): Calculate the curly S0+ coefficient:
            curly_S_longitudinally_polarized_interference = prefactor * (curly_C_longitudinally_polarized_interference + s_V_zero_plus_contribution * curly_C_V_longitudinally_polarized_interference / s_zero_plus_contribution + s_A_zero_plus_contribution * curly_C_A_longitudinally_polarized_interference / s_zero_plus_contribution)
            
        elif n_number == 3:

            # (6): Calculate the curly S0+ coefficient:
            curly_S_longitudinally_polarized_interference = 0.

        # (6.1): If verbose, print the calculation:
        if verbose:
            print(f"> Calculated curly S0+ to be:\n{curly_S_longitudinally_polarized_interference}")

        # (7): Return the output.
        return curly_S_longitudinally_polarized_interference

    except Exception as ERROR:
        print(f"> Error in calculating the curly S0+ LP entire contribution amplitude squared\n> {ERROR}")
        return 0.
    
    