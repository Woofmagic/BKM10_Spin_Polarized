from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp0 import calculate_c_0_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_C0p0 import calculate_c_0_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cmp0 import calculate_c_0_minus_plus_longitudinally_polarized

from coefficients.interference_coefficients.lp_polarized.pl_polarized_Cpp1 import calculate_c_1_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_C0p1 import calculate_c_1_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cmp1 import calculate_c_1_minus_plus_longitudinally_polarized

from coefficients.interference_coefficients.lp_polarized.pl_polarized_Cpp2 import calculate_c_2_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_C0p2 import calculate_c_2_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cmp2 import calculate_c_2_minus_plus_longitudinally_polarized

from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_Cpp import calculate_curly_C_plus_plus_longitudinally_polarized_interference

from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_C0p import calculate_curly_C_zero_plus_longitudinally_polarized_interference

from form_factors.effective_cffs import compute_cff_effective
from form_factors.effective_cffs import compute_cff_transverse

def calculate_c_interference_coefficient(
    n_number: int,
    lepton_helicity: float,
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
    verbose: bool = False) -> float:
    """
    """

    # (1): We initialize all terms of: c_{n}^{I} = C_{++}(n) Re[CurlyC_{++}(n|F)] + C_{0+}(n) Re[CurlyC_{0+}(n|F_{eff})] + C_{-+}(n) Re[CurlyC_{-+}(n|F_{T})]

    # (1.1): Initialize the contribution from C_{++}(n) by setting it equal to 0.:
    c_plus_plus = 0.

    # (1.2): Initialize the contribution from CurlyC_{++}(n|F):
    curly_c_plus_plus = 0.

    # (1.3): Initialize the contribution from C_{0+}(n):
    c_zero_plus = 0.

    # (1.4): Initialize the contribution from CurlyC_{0+}(n|F_{eff}):
    curly_c_zero_plus = 0.

    # (1.5): Initialize the contribution from C_{-+}(n):
    c_minus_plus = 0.

    # (1.6): Initialize the contribution from CurlyC_{-+}(n|F_{T})
    curly_c_minus_plus = 0.

    try:

        if n_number == 0:

            # (1): We compute the first part of the term: C_{++}(n = 0):
            c_plus_plus = calculate_c_0_plus_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)

            # (2): The second part of the term is C_{0+}(n = 0):
            c_zero_plus = calculate_c_0_zero_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
            # (3): The third part of the term is C_{-+}(n = 0):
            c_minus_plus = calculate_c_0_minus_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                verbose)
            
        elif n_number == 1:

            # (1): We compute the first part of the term: C++, n = 1
            c_plus_plus = calculate_c_1_plus_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            # (2): The second part of the term is C0+, n = 1
            c_zero_plus = calculate_c_1_zero_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                epsilon,
                lepton_energy_fraction_y,
                k_tilde,
                shorthand_k,
                verbose)
            
            # (3): The third part of the term is C_{-+}(n = 1):
            c_minus_plus = calculate_c_1_minus_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)
            
        elif n_number == 2:

            # (1): We compute the first part of the term: C++, n = 2
            c_plus_plus = calculate_c_2_plus_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                verbose)

            # (2): The second part of the term is C0+, n = 2
            c_zero_plus = calculate_c_2_zero_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                verbose)

            # (3): The third part of the term is C_{-+}(n = 2):
            c_minus_plus = calculate_c_2_minus_plus_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                verbose)
            
        elif n_number == 3:

            # (1): We compute the first part of the term: C++, n = 3
            c_plus_plus = 0.

            # (2): The second part of the term is C0+, n = 3
            c_zero_plus = 0.

            # (3): C_{-+}(n = 0) is 0:
            c_minus_plus = 0.

        # (3): Calculate the curly C_{++} contribution - requires both n and the CFFs:
        curly_c_plus_plus = calculate_curly_C_plus_plus_longitudinally_polarized_interference(
            n_number,
            lepton_helicity,
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


        # (4): Calculate the curly C_{0+} contribution - requires both n and the CFFs:
        curly_c_zero_plus = calculate_curly_C_zero_plus_longitudinally_polarized_interference(
            n_number,
            lepton_helicity,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            k_tilde,
            shorthand_k,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compute_cff_effective(skewness_parameter, compton_form_factor_h_real_part),
            compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde_real_part),
            compute_cff_effective(skewness_parameter, compton_form_factor_e_real_part),
            compute_cff_effective(skewness_parameter, compton_form_factor_e_tilde_real_part),
            verbose)
        
        # (5): Calculate the curly C_{-+} contribution - requires both n and the TRANSVERSE CFFs:
        curly_c_minus_plus = calculate_curly_C_zero_plus_longitudinally_polarized_interference(
            n_number,
            lepton_helicity,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            k_tilde,
            shorthand_k,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compute_cff_transverse(skewness_parameter, compton_form_factor_h_real_part),
            compute_cff_transverse(skewness_parameter, compton_form_factor_h_tilde_real_part),
            compute_cff_transverse(skewness_parameter, compton_form_factor_e_real_part),
            compute_cff_transverse(skewness_parameter, compton_form_factor_e_tilde_real_part),
            verbose)

        # (5): Calculate the entire thing:
        # c_n_interference_coefficient = c_plus_plus * curly_c_plus_plus + c_zero_plus * curly_c_zero_plus + c_minus_plus * curly_c_minus_plus
        c_n_interference_coefficient = c_plus_plus * curly_c_plus_plus + c_zero_plus * curly_c_zero_plus
        
        # (): If verbose, print the output:
        if verbose:
            print(f"> Calculated c_{n_number} interference coefficient to be:\n{c_n_interference_coefficient}")

        # (): Return the coefficient:
        return c_n_interference_coefficient
    
    except Exception as ERROR:
        print(f"> Error in c_{n_number} contribution to the interference term: \n> {ERROR}")
        return 0.