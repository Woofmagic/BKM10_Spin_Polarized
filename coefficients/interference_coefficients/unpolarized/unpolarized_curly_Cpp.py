from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp0 import calculate_c_0_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp0V import calculate_c_0_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp0A import calculate_c_0_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp1 import calculate_c_1_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp1V import calculate_c_1_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp1A import calculate_c_1_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp2 import calculate_c_2_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp2V import calculate_c_2_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp2A import calculate_c_2_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp3 import calculate_c_3_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp3V import calculate_c_3_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp3A import calculate_c_3_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_curly_C import calculate_curly_C_unpolarized_interference
from coefficients.interference_coefficients.unpolarized.unpolarized_curly_CV import calculate_curly_C_unpolarized_interference_V
from coefficients.interference_coefficients.unpolarized.unpolarized_curly_CA import calculate_curly_C_unpolarized_interference_A

def calculate_curly_C_plus_plus_unpolarized_interference(
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
    compton_form_factor_h_real_part: float,
    compton_form_factor_h_tilde_real_part: float,
    compton_form_factor_e_real_part: float,
    verbose: bool = False) -> float:

    try:

        # (1): Calculate curly C_{unp}^{I}(F):
        curly_C_unpolarized_interference = calculate_curly_C_unpolarized_interference(
            squared_Q_momentum_transfer, 
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h_real_part,
            compton_form_factor_h_tilde_real_part,
            compton_form_factor_e_real_part,
            verbose)
        
        # (2): Calculate curly C_{unp}^{I, V}(F):
        curly_C_V_unpolarized_interference = calculate_curly_C_unpolarized_interference_V(
            squared_Q_momentum_transfer, 
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h_real_part,
            compton_form_factor_e_real_part,
            verbose)
        
        # (3): Calculate curly C_{LP}^{I, A}(F):
        curly_C_A_unpolarized_interference = calculate_curly_C_unpolarized_interference_A(
            squared_Q_momentum_transfer, 
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h_tilde_real_part,
            verbose)
        
        # (4): Split on the integer n:
        if n_number == 0:

            # (4.1): Calculate the C_{++}(0) contribution
            c_plus_plus_contribution = calculate_c_0_plus_plus_unpolarized(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)

            # (4.2): Calculate the C_{++}^{V}(0) contribution
            c_V_plus_plus_contribution = calculate_c_0_plus_plus_unpolarized_V(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)

            # (4.3): Calculate the C_{++}^{A}(0) contribution
            c_A_plus_plus_contribution = calculate_c_0_plus_plus_unpolarized_A(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)

            # (5): Perform the calculation:
            curly_C_plus_plus_unpolarized_interference = (curly_C_unpolarized_interference
            + (c_V_plus_plus_contribution * curly_C_V_unpolarized_interference / c_plus_plus_contribution)
            + (c_A_plus_plus_contribution * curly_C_A_unpolarized_interference / c_plus_plus_contribution))

        elif n_number == 1:

            # (4.1): Calculate the C_{++}(1) contribution
            c_plus_plus_contribution = calculate_c_1_plus_plus_unpolarized(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            # (4.2): Calculate the C_{++}^{V}(1) contribution
            c_V_plus_plus_contribution = calculate_c_1_plus_plus_unpolarized_V(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            # (4.3): Calculate the C_{++}^{A}(1) contribution
            c_A_plus_plus_contribution = calculate_c_1_plus_plus_unpolarized_A(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            # (5): Perform the calculation:
            curly_C_plus_plus_unpolarized_interference = (curly_C_unpolarized_interference
            + (c_V_plus_plus_contribution * curly_C_V_unpolarized_interference / c_plus_plus_contribution)
            + (c_A_plus_plus_contribution * curly_C_A_unpolarized_interference / c_plus_plus_contribution))

        elif n_number == 2:

            # (4.1): Calculate the C_{++}(2) contribution
            c_plus_plus_contribution = calculate_c_2_plus_plus_unpolarized(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                k_tilde,
                verbose)

            # (4.2): Calculate the C_{++}^{V}(2) contribution
            c_V_plus_plus_contribution = calculate_c_2_plus_plus_unpolarized_V(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                k_tilde,
                verbose)

            # (4.3): Calculate the C_{++}^{A}(2) contribution
            c_A_plus_plus_contribution = calculate_c_2_plus_plus_unpolarized_A(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                k_tilde,
                verbose)

            # (5): Perform the calculation:
            curly_C_plus_plus_unpolarized_interference = (curly_C_unpolarized_interference
            + (c_V_plus_plus_contribution * curly_C_V_unpolarized_interference / c_plus_plus_contribution)
            + (c_A_plus_plus_contribution * curly_C_A_unpolarized_interference / c_plus_plus_contribution))

        elif n_number == 3:

            # (4.1): Calculate the C_{++}(3) contribution
            c_plus_plus_contribution = calculate_c_3_plus_plus_unpolarized(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            # (4.2): Calculate the C_{++}^{V}(3) contribution
            c_V_plus_plus_contribution = calculate_c_3_plus_plus_unpolarized_V(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            # (4.3): Calculate the C_{++}^{A}(3) contribution
            c_A_plus_plus_contribution = calculate_c_3_plus_plus_unpolarized_A(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                t_prime,
                shorthand_k,
                verbose)

            # (5): Perform the calculation:
            curly_C_plus_plus_unpolarized_interference = (curly_C_unpolarized_interference
            + (c_V_plus_plus_contribution * curly_C_V_unpolarized_interference / c_plus_plus_contribution)
            + (c_A_plus_plus_contribution * curly_C_A_unpolarized_interference / c_plus_plus_contribution))

        else:

            curly_C_plus_plus_unpolarized_interference = 0.

        # (5.1): If verbose, print the calculation:
        if verbose:
            print(f"> Calculated curly C++ to be:\n{curly_C_plus_plus_unpolarized_interference}")

        # (6): Return the output.
        return curly_C_plus_plus_unpolarized_interference

    except Exception as ERROR:
        print(f"> Error in calculating the curly C++ LP entire contribution amplitude squared\n> {ERROR}")
        return 0.