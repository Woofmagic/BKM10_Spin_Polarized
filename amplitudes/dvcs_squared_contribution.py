"""
## Description:
We compute the |DVCS|^{2} contribution to the BKM02/10 formalism parametrization
of the DVCS cross section.

## Notes:
1. 2025/09/01: Removed the `math` and `Decimal` libraries at the top. Not used anymore.
"""

from calculation.plot_results import plot_dvcs_contributions

# Helper Module | Convert GeV^{-6} to nb/GeV^{4}
from utilities.mathematics.math_units import convert_to_nb_over_GeV4

import numpy as np

# Helper Modules | Convert Degrees to Radians
from utilities.mathematics.math_units import convert_degrees_to_radians

from form_factors.effective_cffs import compute_cff_effective

# Amplitude Contributions | BKM10 Prefactor
from amplitudes.cross_section_prefactor import calculate_bkm10_cross_section_prefactor

# c_{0, unp}^{DVCS}
from coefficients.dvcs_coefficients.unpolarized.bkm10.unpolarized_c0_dvcs import calculate_c_0_unpolarized_dvcs

# c_{1, unp}^{DVCS}
from coefficients.dvcs_coefficients.unpolarized.bkm10.unpolarized_c1_dvcs import calculate_c_1_unpolarized_dvcs

# s_{1, unp}^{DVCS}
from coefficients.dvcs_coefficients.unpolarized.bkm10.unpolarized_s1_dvcs import calculate_s_1_unpolarized_dvcs

# c_{0, LP}^{DVCS}
from coefficients.dvcs_coefficients.lp_polarized.bkm10.lp_polarized_c0_dvcs import calculate_c_0_longitudinally_polarized_dvcs

# c_{1, LP}^{DVCS}
from coefficients.dvcs_coefficients.lp_polarized.bkm10.lp_polarized_c1_dvcs import calculate_c_1_longitudinally_polarized_dvcs

# s_{1, LP}^{DVCS}
from coefficients.dvcs_coefficients.lp_polarized.bkm10.lp_polarized_s1_dvcs import calculate_s_1_longitudinally_polarized_dvcs

def calculate_dvcs_amplitude_squared(
    lepton_helicity: float,
    target_polarization: float,
    squared_Q_momentum_transfer: float,
    x_Bjorken: float,
    squared_hadronic_momentum_transfer_t: float,
    azimuthal_phi: float,
    epsilon: float,
    lepton_energy_fraction_y: float,
    skewness_parameter: float,
    shorthand_k: float,
    compton_form_factor_h: complex,
    compton_form_factor_h_tilde: complex,
    compton_form_factor_e: complex,
    compton_form_factor_e_tilde: complex,
    use_ww: bool = False,
    verbose: bool = False):
    """
    ## Description:
    We now calculate the DVCS amplitude squared.

    :param float lepton_helicity:

    :param float target_polarization:

    :param float squared_Q_momentum_transfer:

    :param float x_Bjorken:

    :param float squared_hadronic_momentum_transfer_t:

    :param float lab_kinematics_k:

    :param float azimuthal_phi:

    :param complex compton_form_factor_h:
        The Compton Form Factor (CFF) called H.

    :param complex compton_form_factor_h_tilde:
        The Compton Form Factor (CFF) called Ht (H-tilde)

    :param complex compton_form_factor_e: 
        The Compton Form Factor (CFF) called E.

    :param complex compton_form_factor_e_tilde:
        The Compton Form Factor (CFF) called Et (E-tilde).

    :param verbose: (bool)

    :returns: bkm10_cross_section_in_nb_gev4: (float)
        The four-fold differential cross section.

    ## Notes:
        1. The equation for the amplitude squared comes from Eq. (2.27) in the
        BKM10 Formalism available here: https://arxiv.org/pdf/1005.5209.pdf
    """
        
    try:

        # (1): Calculate the Prefactor of the Denominator:
        denominator = lepton_energy_fraction_y**2 * squared_Q_momentum_transfer

        if target_polarization == 0.0:

            if verbose:
                print(f"> Now evaluating LP target DVCS amplitude squared because target polarization was set to: {target_polarization}")

            # (2): Obtain the first coefficient in the sum:
            coefficient_c0_DVCS = calculate_c_0_unpolarized_dvcs(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                skewness_parameter,
                shorthand_k,
                compton_form_factor_h,
                compton_form_factor_h_tilde,
                compton_form_factor_e,
                compton_form_factor_e_tilde,
                use_ww,
                verbose)

            # (3): Obtain the first coefficient in the unevaluated sum (cosine n = 1 term):
            coefficient_c1_DVCS = calculate_c_1_unpolarized_dvcs(
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                skewness_parameter,
                shorthand_k,
                compton_form_factor_h,
                compton_form_factor_h_tilde,
                compton_form_factor_e,
                compton_form_factor_e_tilde,
                use_ww,
                verbose)

            # (4): Obtain the first coefficient in the unevaluated sum (np.sin n = 1 term):
            coefficient_s1_DVCS = calculate_s_1_unpolarized_dvcs(
                lepton_helicity,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                skewness_parameter,
                shorthand_k,
                compton_form_factor_h,
                compton_form_factor_h_tilde,
                compton_form_factor_e,
                compton_form_factor_e_tilde,
                use_ww,
                verbose)

        elif target_polarization != 0.0:

            if verbose:
                print(f"> Now evaluating LP target DVCS amplitude squared because target polarization was set to: {target_polarization}")

            # (2): Obtain the first coefficient in the sum:
            coefficient_c0_DVCS = calculate_c_0_longitudinally_polarized_dvcs(
                lepton_helicity,
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
                use_ww,
                verbose)

            # (3): Obtain the first coefficient in the unevaluated sum (cosine n = 1 term):
            coefficient_c1_DVCS = calculate_c_1_longitudinally_polarized_dvcs(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                skewness_parameter,
                shorthand_k,
                compton_form_factor_h,
                compton_form_factor_h_tilde,
                compton_form_factor_e,
                compton_form_factor_e_tilde,
                use_ww,
                verbose)

            # (4): Obtain the first coefficient in the unevaluated sum (np.sin n = 1 term):
            coefficient_s1_DVCS = calculate_s_1_longitudinally_polarized_dvcs(
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                skewness_parameter,
                shorthand_k,
                compton_form_factor_h,
                compton_form_factor_h_tilde,
                compton_form_factor_e,
                compton_form_factor_e_tilde,
                use_ww,
                verbose)
            
        else:

            raise ValueError("[ERROR]: Unknown value for the target polarization.")

        # print(coefficient_c0_DVCS[0])
        # print(coefficient_c1_DVCS[0])
        # print(coefficient_s1_DVCS[0])

        # plot_dvcs_contributions(
        #     azimuthal_phi,
        #     convert_to_nb_over_GeV4(coefficient_c0_DVCS),
        #     convert_to_nb_over_GeV4(coefficient_c1_DVCS),
        #     convert_to_nb_over_GeV4(coefficient_s1_DVCS))

        # (5): Compute the Fourier Mode Expansion:
        mode_expansion = (coefficient_c0_DVCS +
            coefficient_c1_DVCS * np.cos(1. * (np.pi - azimuthal_phi)) +
            coefficient_s1_DVCS * np.sin(1. * (np.pi - azimuthal_phi)))

        # (6): The entire amplitude:
        dvcs_amplitude_squared = mode_expansion / denominator

        # (6.1): If verbose, then print the output:
        if verbose:
            print(f"> Calculated DVCS amplitude squared as: {dvcs_amplitude_squared}")

        # (7): Return the amplitude:
        return dvcs_amplitude_squared
    
    except Exception as ERROR:
        print(f"[ERROR]: Error in calculating the DVCS amplitude squared\n> {ERROR}")
        return 0.