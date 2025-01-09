import numpy as np

from coefficients.interference_coefficients.unpolarized.unpolarized_C0p0 import calculate_c_0_zero_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p0V import calculate_c_0_zero_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p0A import calculate_c_0_zero_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_C0p1 import calculate_c_1_zero_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p1V import calculate_c_1_zero_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p1A import calculate_c_1_zero_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_C0p2 import calculate_c_2_zero_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p2V import calculate_c_2_zero_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p2A import calculate_c_2_zero_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_curly_C import calculate_curly_C_unpolarized_interference
from coefficients.interference_coefficients.unpolarized.unpolarized_curly_CV import calculate_curly_C_unpolarized_interference_V
from coefficients.interference_coefficients.unpolarized.unpolarized_curly_CA import calculate_curly_C_unpolarized_interference_A

def calculate_curly_C_zero_plus_unpolarized_interference(
    n_number: int,
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
    compton_form_factor_h_eff: complex,
    compton_form_factor_h_tilde_eff: complex,
    compton_form_factor_e_eff: complex,
    verbose: bool = False) -> float:

    try:

        # (1): Calculate the prefactor: Ktilde / (2 - xb) * sqrt(2 / Q^{2})
        prefactor = sqrt(2. / squared_Q_momentum_transfer) * k_tilde / (2. - x_Bjorken)

        # (1): Calculate curly C_{unp}^{I}(F):
        curly_C_unpolarized_interference = calculate_curly_C_unpolarized_interference(
            squared_Q_momentum_transfer, 
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h_eff,
            compton_form_factor_h_tilde_eff,
            compton_form_factor_e_eff,
            verbose)
        
        # (2): Calculate curly C_{unp}^{I, V}(F):
        curly_C_V_unpolarized_interference = calculate_curly_C_unpolarized_interference_V(
            squared_Q_momentum_transfer, 
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h_eff,
            compton_form_factor_e_eff,
            verbose)
        
        # (3): Calculate curly C_{LP}^{I, A}(F):
        curly_C_A_unpolarized_interference = calculate_curly_C_unpolarized_interference_A(
            squared_Q_momentum_transfer, 
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h_tilde_eff,
            verbose)
        
        # (5): Split on the integer n:
        if n_number == 0:

            # (5.1): Calculate the C_{0+}(0) contribution
            c_zero_plus_contribution = calculate_c_0_zero_plus_unpolarized(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            # (5.2): Calculate the C_{0+}^{V}(0) contribution
            c_V_zero_plus_contribution = calculate_c_0_zero_plus_unpolarized_V(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            # (5.3): Calculate the C_{0+}^{A}(0) contribution
            c_A_zero_plus_contribution = calculate_c_0_zero_plus_unpolarized_A(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            # (6): Calculate the curly C0+ coefficient:
            curly_C_zero_plus_unpolarized_interference = prefactor * (curly_C_unpolarized_interference
            + c_V_zero_plus_contribution * curly_C_V_unpolarized_interference / c_zero_plus_contribution
            + c_A_zero_plus_contribution * curly_C_A_unpolarized_interference / c_zero_plus_contribution)

        elif n_number == 1:

            # (5.1): Calculate the C_{0+}(1) contribution
            c_zero_plus_contribution = calculate_c_1_zero_plus_unpolarized(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                verbose)

            # (5.2): Calculate the C_{0+}^{V}(1) contribution
            c_V_zero_plus_contribution = calculate_c_1_zero_plus_unpolarized_V(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)

            # (5.3): Calculate the C_{0+}^{A}(1) contribution
            c_A_zero_plus_contribution = calculate_c_1_zero_plus_unpolarized_A(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)

            # (6): Calculate the curly C0+ coefficient:
            curly_C_zero_plus_unpolarized_interference = prefactor * (curly_C_unpolarized_interference
            + c_V_zero_plus_contribution * curly_C_V_unpolarized_interference / c_zero_plus_contribution
            + c_A_zero_plus_contribution * curly_C_A_unpolarized_interference / c_zero_plus_contribution)

        elif n_number == 2:

            # (5.1): Calculate the C_{0+}(2) contribution
            c_zero_plus_contribution = calculate_c_2_zero_plus_unpolarized(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            # (5.2): Calculate the C_{0+}^{V}(2) contribution
            c_V_zero_plus_contribution = calculate_c_2_zero_plus_unpolarized_V(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            # (5.3): Calculate the C_{0+}^{A}(2) contribution
            c_A_zero_plus_contribution = calculate_c_2_zero_plus_unpolarized_A(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            # (6): Calculate the curly C0+ coefficient:
            curly_C_zero_plus_unpolarized_interference = prefactor * (curly_C_unpolarized_interference
            + c_V_zero_plus_contribution * curly_C_V_unpolarized_interference / c_zero_plus_contribution
            + c_A_zero_plus_contribution * curly_C_A_unpolarized_interference / c_zero_plus_contribution)

        elif n_number == 3:

            # (6): Calculate the curly C0+ coefficient:
            curly_C_zero_plus_unpolarized_interference = 0.
        
        # (6.1): If verbose, print the calculation:
        if verbose:
            print(f"> Calculated curly C0+ to be:\n{curly_C_zero_plus_unpolarized_interference}")

        # (7): Return the output.
        return curly_C_zero_plus_unpolarized_interference

    except Exception as ERROR:
        print(f"> Error in calculating the curly C0+ LP entire contribution: \n> {ERROR}")
        return 0.