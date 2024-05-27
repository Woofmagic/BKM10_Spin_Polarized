try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

# Import helper modules:
from statics.mathematics.math_units import convert_degrees_to_radians

# c_{n}^{I}
from coefficients.interference_coefficients.lp_polarized import calculate_c_interference_coefficient

# s_{n}^{I}
from coefficients.interference_coefficients.lp_polarized import calculate_s_interference_coefficient

def calculate_interference_contribution_longitudinally_polarized(
    lepton_polarization: int,
    target_polarization: int,
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
    compton_form_factor_h: float,
    compton_form_factor_h_tilde: float,
    compton_form_factor_e: float,
    compton_form_factor_e_tilde: float,
    verbose: bool = True) -> float:
    """
    """

    try:

        # (1): Calculate the prefactor:
        prefactor = 1. / (x_Bjorken * lepton_energy_fraction_y**3 * squared_hadronic_momentum_transfer_t * lepton_propagator_p1 * lepton_propagator_p2)

        # (2): Calculate c_{0}^{I}:
        c_0_I = calculate_c_interference_coefficient(
            0,
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
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            verbose)
        
        # (3): Calculate c_{1}^{I}:
        c_1_I = calculate_c_interference_coefficient(
            1,
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
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            verbose)
        
        # (4): Calculate c_{2}^{I}:
        c_2_I = calculate_c_interference_coefficient(
            2,
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
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            verbose)
        
        # (5): Calculate c_{3}^{I}:
        c_3_I = calculate_c_interference_coefficient(
            3,
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
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            verbose)

        # (6): Calculate s_{1}^{I}:
        s_1_I = calculate_s_interference_coefficient(
            1,
            lepton_polarization,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            skewness_parameter,
            t_prime,
            k_tilde,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            verbose)
        
        # (7): Calculate s_{2}^{I}:
        s_2_I = calculate_s_interference_coefficient(
            2,
            lepton_polarization,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            skewness_parameter,
            t_prime,
            k_tilde,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            verbose)
        
        # (8): Calculate s_{3}^{I}:
        s_3_I = calculate_s_interference_coefficient(
            3,
            lepton_polarization,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            skewness_parameter,
            t_prime,
            k_tilde,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            verbose)

        # (9): Calculate the interference contribution:
        interference_contribution = prefactor * (
            c_0_I
            + c_1_I * np.cos(np.pi - 1. * (convert_degrees_to_radians(azimuthal_phi)))
            + c_2_I * np.cos(np.pi - 2. * (convert_degrees_to_radians(azimuthal_phi)))
            + c_3_I * np.cos(np.pi - 3. * (convert_degrees_to_radians(azimuthal_phi)))
            + s_1_I * np.sin(np.pi - 1. * (convert_degrees_to_radians(azimuthal_phi)))
            + s_2_I * np.sin(np.pi - 2. * (convert_degrees_to_radians(azimuthal_phi)))
            + s_3_I * np.sin(np.pi - 3. * (convert_degrees_to_radians(azimuthal_phi)))
            )

        # (9.1): If verbose, print the calculation:
        if verbose:
            print(f"> Calculated the interference contribution to be: {interference_contribution}")
            
        # (8): Return the amplitude:
        return interference_contribution
    
    except Exception as ERROR:
        print(f"> Error in calculating the interference_contribution \n> {ERROR}")
        return 0.