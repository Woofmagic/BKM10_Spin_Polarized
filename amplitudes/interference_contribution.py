from decimal import Decimal
import math


from utilities.plotting.plot_customizer import PlotCustomizer

from calculation.plot_results import plot_interference_contributions

# Helper Module | Convert GeV^{-6} to nb/GeV^{4}
from utilities.mathematics.math_units import convert_to_nb_over_GeV4

from calculation.plot_results import plot_interference_contributions

import numpy as np

# Import helper modules:
from utilities.mathematics.math_units import convert_degrees_to_radians

# Coefficient | c_{0}^{I}
from coefficients.interference_coefficients.lp_polarized.lp_polarized_c_n import calculate_c_0_interference_coefficient

# Coefficient | c_{1}^{I}
from coefficients.interference_coefficients.lp_polarized.lp_polarized_c_n import calculate_c_1_interference_coefficient

# Coefficient | c_{2}^{I}
from coefficients.interference_coefficients.lp_polarized.lp_polarized_c_n import calculate_c_2_interference_coefficient

# Coefficient | c_{3}^{I}
from coefficients.interference_coefficients.lp_polarized.lp_polarized_c_n import calculate_c_3_interference_coefficient

# Coefficient | s_{1}^{I}
from coefficients.interference_coefficients.lp_polarized.lp_polarized_s_n import calculate_s_1_interference_coefficient

# Coefficient | s_{2}^{I}
from coefficients.interference_coefficients.lp_polarized.lp_polarized_s_n import calculate_s_2_interference_coefficient

# Coefficient | s_{3}^{I}
from coefficients.interference_coefficients.lp_polarized.lp_polarized_s_n import calculate_s_3_interference_coefficient

from coefficients.interference_coefficients.unpolarized.unpolarized_curly_C import calculate_curly_C_unpolarized_interference
from coefficients.interference_coefficients.unpolarized.unpolarized_curly_CV import calculate_curly_C_unpolarized_interference_V
from coefficients.interference_coefficients.unpolarized.unpolarized_curly_CA import calculate_curly_C_unpolarized_interference_A

def calculate_interference_contribution(
    lepton_helicity: float,
    target_polarization: float,
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
    compton_form_factor_h: complex,
    compton_form_factor_h_tilde: complex,
    compton_form_factor_e: complex,
    compton_form_factor_e_tilde: complex,
    use_ww: bool = False,
    verbose: bool = False) -> float:
    """
    # Title: `calculate_interference_contribution`

    ## Description:
    We calculated the BKM10-predicted contribution of the interference between
    the BH and DVCS process.

    ## Arguments:
    
        lepton_helicity: (float)

        target_polarization: (float)

        squared_Q_momentum_transfer: (float)

        x_Bjorken: (float)

        squared_hadronic_momentum_transfer_t: (float)

        lab_kinematics_k: (float)

        azimuthal_phi: (float)

        epsilon:  (float)

        lepton_energy_fraction_y: (float)

        skewness_parameter: (float)

        t_prime: (float)

        k_tilde: (float)

        shorthand_k: (float)

        lepton_propagator_p1: (float)

        lepton_propagator_p2: (float)

        Dirac_form_factor_F1: (float)

        Pauli_form_factor_F2: (float)

        compton_form_factor_h_real_part: (float)

            The real part of the Compton Form Factor (CFF) called H. We will
            write this as Re[H].

        compton_form_factor_h_tilde_real_part: (float)

            The real part of the Compton Form Factor (CFF) called Ht (H-tilde). We will
            write this as Re[HT].

        compton_form_factor_e_real_part: (float)

            The real part of the Compton Form Factor (CFF) called E. We will
            write this as Re[E].

        compton_form_factor_e_tilde_real_part: (float)

            The real part of the Compton Form Factor (CFF) called Et (E-tilde). We will
            write this as Re[Et].

        compton_form_factor_h_imaginary_part: (float)

            The imaginary/complex part of the Compton Form Factor (CFF) called H. We will
            write this as Re[H].

        compton_form_factor_h_tilde_imaginary_part: (float)

            The imaginary/complex part of the Compton Form Factor (CFF) called Ht (H-tilde). We will
            write this as Re[HT].

        compton_form_factor_e_imaginary_part: (float)

            The imaginary/complex part of the Compton Form Factor (CFF) called E. We will
            write this as Re[E].

        compton_form_factor_e_tilde_imaginary_part: (float)

            The imaginary/complex part of the Compton Form Factor (CFF) called Et (E-tilde). We will
            write this as Re[Et].

        verbose: (bool)

    ## Returns:
    
        bkm10_cross_section_in_nb_GeV4: (float)

            The four-fold differential cross section.

    ## Notes:

    ## Examples:
    """

    try:

        # (1): Calculate the prefactor:
        prefactor = 1. / (x_Bjorken * lepton_energy_fraction_y**3 * squared_hadronic_momentum_transfer_t * lepton_propagator_p1 * lepton_propagator_p2)

        # (2): Calculate c_{0}^{I}:
        # c_0_I = 0.
        c_0_I = calculate_c_0_interference_coefficient(
            0,
            lepton_helicity,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            skewness_parameter,
            t_prime,
            k_tilde,
            shorthand_k,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            use_ww,
            verbose)
        
        # (3): Calculate c_{1}^{I}:
        # c_1_I = 0.
        c_1_I = calculate_c_1_interference_coefficient(
            1,
            lepton_helicity,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            skewness_parameter,
            t_prime,
            k_tilde,
            shorthand_k,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            use_ww,
            verbose)
        
        # (4): Calculate c_{2}^{I}:
        # c_2_I = 0.
        c_2_I = calculate_c_2_interference_coefficient(
            2,
            lepton_helicity,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            skewness_parameter,
            t_prime,
            k_tilde,
            shorthand_k,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            use_ww,
            verbose)

        # (5): Calculate c_{2}^{I}:
        # c_3_I = 0.
        c_3_I = calculate_c_3_interference_coefficient(
            3,
            lepton_helicity,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            skewness_parameter,
            t_prime,
            k_tilde,
            shorthand_k,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            use_ww,
            verbose)
        
        # (6): Calculate s_{1}^{I}:
        # s_1_I = 0.
        s_1_I = calculate_s_1_interference_coefficient(
            1,
            lepton_helicity,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            skewness_parameter,
            t_prime,
            k_tilde,
            shorthand_k,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            use_ww,
            verbose)

        # (7): Calculate s_{2}^{I}:
        # s_2_I = 0.
        s_2_I = calculate_s_2_interference_coefficient(
            2,
            lepton_helicity,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            skewness_parameter,
            t_prime,
            k_tilde,
            shorthand_k,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            use_ww,
            verbose)

        # (8): Calculate s_{3}^{I}:
        # s_3_I = 0.
        s_3_I = calculate_s_3_interference_coefficient(
            3,
            lepton_helicity,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            lepton_energy_fraction_y,
            skewness_parameter,
            t_prime,
            k_tilde,
            shorthand_k,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            use_ww,
            verbose)
        
        print(f"> c0: {c_0_I[0]}")
        print(f"> c1: {c_1_I[0]}")
        print(f"> c2: {c_2_I[0]}")
        print(f"> c3: {c_3_I[0]}")
        print(f"> s1: {s_1_I[0]}")
        print(f"> s2: {s_2_I[0]}")
        print(f"> s3: {s_3_I[0]}")
        
        plot_interference_contributions(
            azimuthal_phi,
            convert_to_nb_over_GeV4(c_0_I),
            convert_to_nb_over_GeV4(c_1_I),
            convert_to_nb_over_GeV4(c_2_I),
            convert_to_nb_over_GeV4(c_3_I),
            convert_to_nb_over_GeV4(s_1_I),
            convert_to_nb_over_GeV4(s_2_I),
            convert_to_nb_over_GeV4(s_3_I))

        # (9): Calculate the interference contribution:
        interference_contribution = (prefactor * (c_0_I + 
            c_1_I * np.array([np.cos(1. * (np.pi - convert_degrees_to_radians(phi))) for phi in azimuthal_phi]) +
            c_2_I * np.array([np.cos(2. * (np.pi - convert_degrees_to_radians(phi))) for phi in azimuthal_phi]) +
            c_3_I * np.array([np.cos(3. * (np.pi - convert_degrees_to_radians(phi))) for phi in azimuthal_phi]) +
            s_1_I * np.array([np.sin(1. * (np.pi - convert_degrees_to_radians(phi))) for phi in azimuthal_phi]) +
            s_2_I * np.array([np.sin(2. * (np.pi - convert_degrees_to_radians(phi))) for phi in azimuthal_phi]) +
            s_3_I * np.array([np.sin(3. * (np.pi - convert_degrees_to_radians(phi))) for phi in azimuthal_phi])))

        # (9.1): If verbose, print the calculation:
        if verbose:
            print(f"> Calculated the interference contribution to be:\n{interference_contribution}")
            
        # (8): Return the amplitude:
        return interference_contribution
    
    except Exception as ERROR:
        print(f"> Error in calculating the interference_contribution \n> {ERROR}")
        return 0.