

##################
# HELPER MODULES #
##################

# Helper Module | Convert GeV^{-6} to nb/GeV^{4}
from utilities.mathematics.math_units import convert_to_nb_over_GeV4

from calculation.plot_results import plot_cross_section
from calculation.plot_results import plot_beam_spin_asymmetry
from calculation.plot_results import plot_coefficient_contributions

######################
# DERIVED KINEMATICS #
######################

# Derived Kinematics | Epsilon | ε
from derived_kinematics.epsilon import calculate_kinematics_epsilon

# Derived Kinematics | Lepton Energy Fraction | y
from derived_kinematics.lepton_energy_fraction import calculate_kinematics_lepton_energy_fraction_y

# Derived Kinematics | Skewness | ξ
from derived_kinematics.skewness import calculate_kinematics_skewness_parameter

# Derived Kinematics | Minimum t | t_{min}
from derived_kinematics.t_minimum import calculate_kinematics_t_min

# Derived Kinematics | t Prime | t'
from derived_kinematics.t_prime import calculate_kinematics_t_prime

# Derived Kinematics | K Tilde | Ḱ
from derived_kinematics.k_tilde import calculate_kinematics_k_tilde

# Derived Kinematics | K | K
from derived_kinematics.shorthand_K import calculate_kinematics_k

# Derived Kinematics | k dot Delta | k ⋅ Δ 
from derived_kinematics.k_dot_delta import calculate_k_dot_delta

# Derived Kinematics | Lepton Propagator P1 | P_{1}(φ)
from derived_kinematics.lepton_propagator_p1 import calculate_lepton_propagator_p1

# Derived Kinematics | Lepton Propagator P2 | P_{1}(φ)
from derived_kinematics.lepton_propagator_p2 import calculate_lepton_propagator_p2

################
# FORM FACTORS #
################

# Form Factors | Electric Form Factor | F_{E}
from form_factors.electric_form_factor import calculate_form_factor_electric

# Form Factors | Magnetic Form Factor | F_{M}
from form_factors.magnetic_form_factor import calculate_form_factor_magnetic

# Form Factors | Pauli Form Factor | F_{2}
from form_factors.pauli_form_factor import calculate_form_factor_pauli_f2

# Form Factors | Dirac Form Factor | F_{1}
from form_factors.dirac_form_factor import calculate_form_factor_dirac_f1

###########################
# AMPLITUDE CONTRIBUTIONS #
###########################

# Amplitude Contributions | BKM10 Prefactor
from amplitudes.cross_section_prefactor import calculate_bkm10_cross_section_prefactor

# Amplitude Contributions | Bethe-Heitler | |M_{BH}|^{2}
from amplitudes.bh_squared_contribution import calculate_bh_amplitude_squared

# Amplitude Contributions | Deeply-Virtual Compton Scattering | |M_{DVCS}|^{2}
from amplitudes.dvcs_squared_contribution import calculate_dvcs_amplitude_squared_longitudinally_polarized

# Amplitude Contributions | Interference | I
from amplitudes.interference_contribution import calculate_interference_contribution_longitudinally_polarized

import numpy as np

def calculate_bkm10_cross_section(
    lepton_helicity: float,
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float,
    squared_hadronic_momentum_transfer_t: float,
    lab_kinematics_k: float,
    azimuthal_phi: float,
    compton_form_factor_h: complex,
    compton_form_factor_h_tilde: complex,
    compton_form_factor_e: complex,
    compton_form_factor_e_tilde: complex,
    verbose: bool = False) -> float:
    """
    # Title: `calculate_bkm10_cross_section`

    ## Description:
    Numerically evaluates the four-fold cross-section for the electroproduction
    of photons.

    ## Arguments:
    
        lepton_helicity: (float)

        target_polarization: (float)

        squared_Q_momentum_transfer: (float)

        x_Bjorken: (float)

        squared_hadronic_momentum_transfer_t: (float)

        lab_kinematics_k: (float)

        azimuthal_phi: (float)

        compton_form_factor_h_real_part: (complex)

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

        # (1): Calculate Epsilon:
        epsilon = calculate_kinematics_epsilon(
            squared_Q_momentum_transfer,
            x_Bjorken,
            verbose)

        # (2): Calculate the Lepton Energy Fraction:
        lepton_energy_fraction_y = calculate_kinematics_lepton_energy_fraction_y(
            squared_Q_momentum_transfer,
            lab_kinematics_k,
            epsilon,
            verbose)

        # (3): Calculate the Skewness Parameter:
        skewness_parameter = calculate_kinematics_skewness_parameter(
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            verbose)

        # (4): Calculate t_minimum
        squared_hadronic_momentum_transfer_t_minimum = calculate_kinematics_t_min(
            squared_Q_momentum_transfer,
            x_Bjorken,
            epsilon,
            verbose)

        # (5): Calculate t_prime:
        t_prime = calculate_kinematics_t_prime(
            squared_hadronic_momentum_transfer_t,
            squared_hadronic_momentum_transfer_t_minimum,
            verbose)

        # (6): Calculate K_tilde:
        k_tilde = calculate_kinematics_k_tilde(
            squared_Q_momentum_transfer,
            x_Bjorken,
            lepton_energy_fraction_y,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            squared_hadronic_momentum_transfer_t_minimum,
            verbose)

        # (7): Calculate K Squared:
        shorthand_k = calculate_kinematics_k(
            squared_Q_momentum_transfer,
            lepton_energy_fraction_y,
            epsilon,
            k_tilde,
            verbose)

        # (8): Calculate k_dot_delta:
        k_dot_delta = calculate_k_dot_delta(
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            azimuthal_phi,
            epsilon,
            lepton_energy_fraction_y,
            shorthand_k,
            verbose)

        # (9): Calculate Lepton Propagator 1:
        lepton_propagator_p1 = calculate_lepton_propagator_p1(
            squared_Q_momentum_transfer,
            k_dot_delta,
            verbose)
        
        # (10): Calculate Lepton Propagator 2:
        lepton_propagator_p2 = calculate_lepton_propagator_p2(
            squared_Q_momentum_transfer,
            squared_hadronic_momentum_transfer_t,
            k_dot_delta,
            verbose)
        
        # (11): Calculate the Electric Form Factor
        electric_form_factor = calculate_form_factor_electric(
            squared_hadronic_momentum_transfer_t, 
            verbose)

        # (12): Calculate the Magnetic Form Factor
        magnetic_form_factor = calculate_form_factor_magnetic(
            electric_form_factor, 
            verbose) 

        # (13): Calculate the Pauli Form Factor, F2:
        Pauli_form_factor_F2 = calculate_form_factor_pauli_f2(
            squared_hadronic_momentum_transfer_t,
            electric_form_factor,
            magnetic_form_factor,
            verbose)

        # (14): Calculate the Dirac Form Factor, F1:
        Dirac_form_factor_F1 = calculate_form_factor_dirac_f1(
            magnetic_form_factor,
            Pauli_form_factor_F2,
            verbose)

        # (15): Calculate the cross-section prefactor:
        cross_section_prefactor = calculate_bkm10_cross_section_prefactor(
            squared_Q_momentum_transfer,
            x_Bjorken,
            epsilon,
            lepton_energy_fraction_y,
            verbose)
        
        # (16): Compute the BH Amplitude Squared
        bh_amplitude_squared = 0.
        # bh_amplitude_squared = calculate_bh_amplitude_squared(
        #     lepton_helicity,
        #     target_polarization,
        #     squared_Q_momentum_transfer,
        #     x_Bjorken,
        #     squared_hadronic_momentum_transfer_t,
        #     azimuthal_phi,
        #     epsilon,
        #     lepton_energy_fraction_y,
        #     shorthand_k,
        #     lepton_propagator_p1,
        #     lepton_propagator_p2,
        #     Dirac_form_factor_F1,
        #     Pauli_form_factor_F2,
        #     verbose)

        # (17): Compute the DVCS Amplitude Squared
        dvcs_amplitude_squared = 0.

        if lepton_helicity == 0.0: 

            dvcs_amplitude_squared = 0.5 * (calculate_dvcs_amplitude_squared_longitudinally_polarized(
            1.0,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            azimuthal_phi,
            epsilon,
            lepton_energy_fraction_y,
            skewness_parameter,
            shorthand_k,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            verbose) + calculate_dvcs_amplitude_squared_longitudinally_polarized(
            -1.0,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            azimuthal_phi,
            epsilon,
            lepton_energy_fraction_y,
            skewness_parameter,
            shorthand_k,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            verbose))

        else:

            dvcs_amplitude_squared = calculate_dvcs_amplitude_squared_longitudinally_polarized(
            lepton_helicity,
            target_polarization,
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            azimuthal_phi,
            epsilon,
            lepton_energy_fraction_y,
            skewness_parameter,
            shorthand_k,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            verbose)

        # (18): Compute the BH Amplitude Squared
        interference_contribution = 0.
        
        if lepton_helicity == 0.0: 

            interference_contribution = (calculate_interference_contribution_longitudinally_polarized(
                1.0,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                azimuthal_phi,
                epsilon,
                lepton_energy_fraction_y,
                skewness_parameter,
                t_prime,
                k_tilde,
                shorthand_k,
                lepton_propagator_p1,
                lepton_propagator_p2,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                compton_form_factor_h,
                compton_form_factor_h_tilde,
                compton_form_factor_e,
                compton_form_factor_e_tilde,
                verbose) + calculate_interference_contribution_longitudinally_polarized(
                -1.0,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                azimuthal_phi,
                epsilon,
                lepton_energy_fraction_y,
                skewness_parameter,
                t_prime,
                k_tilde,
                shorthand_k,
                lepton_propagator_p1,
                lepton_propagator_p2,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                compton_form_factor_h,
                compton_form_factor_h_tilde,
                compton_form_factor_e,
                compton_form_factor_e_tilde,
                verbose)) / 2.

        else:

            interference_contribution = calculate_interference_contribution_longitudinally_polarized(
                lepton_helicity,
                target_polarization,
                squared_Q_momentum_transfer,
                x_Bjorken,
                squared_hadronic_momentum_transfer_t,
                azimuthal_phi,
                epsilon,
                lepton_energy_fraction_y,
                skewness_parameter,
                t_prime,
                k_tilde,
                shorthand_k,
                lepton_propagator_p1,
                lepton_propagator_p2,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                compton_form_factor_h,
                compton_form_factor_h_tilde,
                compton_form_factor_e,
                compton_form_factor_e_tilde,
                verbose)

        # (18): Calculate the total cross section
        bkm10_cross_section = cross_section_prefactor * (bh_amplitude_squared + dvcs_amplitude_squared + interference_contribution)

        # (18.1): If verbose, print the output:
        if verbose:
            print(f"> Calculated BKM10 differential cross section longitudinally polarized target to be:\n{bkm10_cross_section}")

        # (19): Convert to nb/GeV^{4}:
        bkm10_cross_section_in_nb_GeV4 = convert_to_nb_over_GeV4(bkm10_cross_section)
        
        # (19.1): If verbose, print the conversion:
        if verbose:
            print(f"> Converted BKM10 differential cross section to {bkm10_cross_section_in_nb_GeV4} nb/GeV4")

        plot_cross_section(
            lab_azimuthal_phi = azimuthal_phi,
            value_of_beam_energy = np.array(lab_kinematics_k)[0],
            value_of_Q_squared = np.array(squared_Q_momentum_transfer)[0],
            value_of_hadron_recoil = np.array(squared_hadronic_momentum_transfer_t)[0], 
            value_of_x_Bjorken = np.array(x_Bjorken)[0],
            calculated_cross_section = bkm10_cross_section_in_nb_GeV4)

        # plot_beam_spin_asymmetry(
        #     lab_azimuthal_phi = azimuthal_phi,
        #     value_of_beam_energy = np.array(lab_kinematics_k)[0],
        #     value_of_Q_squared = np.array(squared_Q_momentum_transfer)[0],
        #     value_of_hadron_recoil = np.array(squared_hadronic_momentum_transfer_t)[0], 
        #     value_of_x_Bjorken = np.array(x_Bjorken)[0],
        #     bsa_data = (beam_spin_asymmetry))

        # (20): Return the cross section.
        return bkm10_cross_section_in_nb_GeV4

    except Exception as ERROR:
        print(f"> Error in calculating the entire cross section:\n> {ERROR}")
        return 0.
