try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

# Helper Modules | Convert Degrees to Radians
from utilities.mathematics.math_units import convert_degrees_to_radians

# c_{0}^{DVCS}
from coefficients.dvcs_coefficients.lp_polarized.lp_polarized_c0_dvcs import calculate_c_0_longitudinally_polarized_dvcs

# c_{1}^{DVCS}
from coefficients.dvcs_coefficients.lp_polarized.lp_polarized_c1_dvcs import calculate_c_1_longitudinally_polarized_dvcs

# s_{1}^{DVCS}
from coefficients.dvcs_coefficients.lp_polarized.lp_polarized_s1_dvcs import calculate_s_1_longitudinally_polarized_dvcs

def calculate_dvcs_amplitude_squared_longitudinally_polarized(
    lepton_polarization: int,
    target_polarization: int,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float,
    squared_hadronic_momentum_transfer_t: float,
    azimuthal_phi: float,
    epsilon: float,
    lepton_energy_fraction_y: float,
    skewness_parameter: float,
    k_shorthand: float,
    compton_form_factor_h_real_part: float,
    compton_form_factor_h_tilde_real_part: float,
    compton_form_factor_e_real_part: float,
    compton_form_factor_e_tilde_real_part: float,
    compton_form_factor_h_imaginary_part: float,
    compton_form_factor_h_tilde_imaginary_part: float,
    compton_form_factor_e_imaginary_part: float,
    compton_form_factor_e_tilde_imaginary_part: float,
    verbose: bool = True):
    """
    Description
    --------------
    We now calculate the DVCS amplitude squared.

    Parameters
    --------------
    lepton_polarization: (int)

    target_polarization: (int)

    squared_Q_momentum_transfer: (float)

    x_Bjorken: (float)

    squared_hadronic_momentum_transfer_t: (float)

    lab_kinematics_k: (float)

    azimuthal_phi: (float)

    epsilon: (float)

    lepton_energy_fraction_y: (float)

    k_shorthand: (float)

    compton_form_factor_h: (float)

    compton_form_factor_h_tilde: (float)

    compton_form_factor_e: float: (float)

    compton_form_factor_e_tilde: (float)

    verbose: (bool)
        Debugging console output.

    Function Flow
    --------------

    Notes
    --------------
    (1): The equation for the amplitude squared comes from
        Eq. (2.27) in the BKM10 Formalism available here:
        https://arxiv.org/pdf/1005.5209.pdf
    """
        
    try:

        # (1): Calculate the Prefactor of the Denominator:
        denominator = lepton_energy_fraction_y**2 * squared_Q_momentum_transfer

        # (2): Obtain the first coefficient in the sum:
        coefficient_c0_DVCS = calculate_c_0_longitudinally_polarized_dvcs(
            lepton_polarization,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            compton_form_factor_h_real_part,
            compton_form_factor_h_tilde_real_part,
            compton_form_factor_e_real_part,
            compton_form_factor_e_tilde_real_part,
            compton_form_factor_h_imaginary_part,
            compton_form_factor_h_tilde_imaginary_part,
            compton_form_factor_e_imaginary_part,
            compton_form_factor_e_tilde_imaginary_part,
            verbose
        )

        # (3): Obtain the first coefficient in the unevaluated sum (cosine n = 1 term):
        coefficient_c1_DVCS = calculate_c_1_longitudinally_polarized_dvcs(
            lepton_polarization,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            skewness_parameter,
            k_shorthand,
            compton_form_factor_h_real_part,
            compton_form_factor_h_tilde_real_part,
            compton_form_factor_e_real_part,
            compton_form_factor_e_tilde_real_part,
            compton_form_factor_h_imaginary_part,
            compton_form_factor_h_tilde_imaginary_part,
            compton_form_factor_e_imaginary_part,
            compton_form_factor_e_tilde_imaginary_part,
            verbose
        )

        # (4): Obtain the first coefficient in the unevaluated sum (sin n = 1 term):
        coefficient_s1_DVCS = calculate_s_1_longitudinally_polarized_dvcs(
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            skewness_parameter,
            k_shorthand,
            compton_form_factor_h_real_part,
            compton_form_factor_h_tilde_real_part,
            compton_form_factor_e_real_part,
            compton_form_factor_e_tilde_real_part,
            compton_form_factor_h_imaginary_part,
            compton_form_factor_h_tilde_imaginary_part,
            compton_form_factor_e_imaginary_part,
            compton_form_factor_e_tilde_imaginary_part,
            verbose
        )

        # (5): Compute the Fourier Mode Expansion:
        mode_expansion = coefficient_c0_DVCS 
        + (coefficient_c1_DVCS * np.cos(np.pi - convert_degrees_to_radians(azimuthal_phi))) 
        + (coefficient_s1_DVCS * np.sin(np.pi - convert_degrees_to_radians(azimuthal_phi)))

        # (6): Compute the numerator of the amplitude:
        numerator = mode_expansion

        # (7): The entire amplitude:
        dvcs_amplitude_squared = numerator / denominator

        # (7.1): If verbose, then print the output:
        if verbose:
            print(f"> Calculated DVCS amplitude squared as: {dvcs_amplitude_squared}")

        # (8): Return the amplitude:
        return dvcs_amplitude_squared
    
    except Exception as ERROR:
        print(f"> Error in calculating the DVCS amplitude squared\n> {ERROR}")
        return 0.