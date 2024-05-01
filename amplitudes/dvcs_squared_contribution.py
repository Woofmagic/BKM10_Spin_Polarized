try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

# Import helper modules:
from statics.mathematics.math_units import convert_degrees_to_radians

# c_{n}^{DVCS}
from coefficients.dvcs_coefficients.lp_polarized import calculate_c_0_longitudinally_polarized_dvcs

# s_{n}^{DVCS}
from coefficients.dvcs_coefficients.lp_polarized import calculate_c_1_longitudinally_polarized_dvcs

def calculate_dvcs_amplitude_squared_longitudinally_polarized(
    lepton_polarization: int,
    target_polarization: int,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float,
    squared_hadronic_momentum_transfer_t: float,
    azimuthal_phi: float,
    epsilon: float,
    lepton_energy_fraction_y: float,
    k_shorthand: float,
    compton_form_factor_h: float,
    compton_form_factor_h_tilde: float,
    compton_form_factor_e: float,
    compton_form_factor_e_tilde: float,
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

    if verbose:
        verbose_input = True
    else:
        verbose_input = False
        
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
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            verbose_input
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
            k_shorthand,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            verbose_input
        )

        # (4): Obtain the first coefficient in the unevaluated sum (sin n = 1 term):
        coefficient_s1_DVCS = calculate_s_1_longitudinally_polarized_dvcs(
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            k_shorthand,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            verbose_input
        )

        # (5): Compute the Fourier Mode Expansion:
        mode_expansion = coefficient_c0_DVCS 
        + (coefficient_c1_DVCS * np.cos(convert_degrees_to_radians(azimuthal_phi))) 
        + (coefficient_s1_DVCS * np.sin(convert_degrees_to_radians(azimuthal_phi)))

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