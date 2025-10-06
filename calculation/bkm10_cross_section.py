"""
## Description:
This module contains the *major function* that computes the entire four-fold
differential cross-section according to the BKM10 formulation.

## Notes:
    1. 2025/09/01: Initiated refactoring with slightly more up-to-date workflow information.
"""

# Helper Module | Convert GeV^{-6} to nb/GeV^{4}
from utilities.mathematics.math_units import convert_to_nb_over_GeV4

from calculation.plot_results import plot_cross_section

from calculation.plot_results import plot_beam_spin_asymmetry

from calculation.plot_results import plot_coefficient_contributions

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

# Form Factors | Electric Form Factor | F_{E}
from form_factors.electric_form_factor import calculate_form_factor_electric

# Form Factors | Magnetic Form Factor | F_{M}
from form_factors.magnetic_form_factor import calculate_form_factor_magnetic

# Form Factors | Pauli Form Factor | F_{2}
from form_factors.pauli_form_factor import calculate_form_factor_pauli_f2

# Form Factors | Dirac Form Factor | F_{1}
from form_factors.dirac_form_factor import calculate_form_factor_dirac_f1

# Amplitude Contributions | BKM10 Prefactor
from amplitudes.cross_section_prefactor import calculate_bkm10_cross_section_prefactor

# Amplitude Contributions | Bethe-Heitler | |M_{BH}|^{2}
from amplitudes.bh_squared_contribution import calculate_bh_amplitude_squared

# Amplitude Contributions | Deeply-Virtual Compton Scattering | |M_{DVCS}|^{2}
from amplitudes.dvcs_squared_contribution import calculate_dvcs_amplitude_squared

# Amplitude Contributions | Interference | I
from amplitudes.interference_contribution import calculate_interference_contribution

def calculate_bkm10_cross_section(
    lepton_helicity: float,
    target_polarization: float,
    squared_q_momentum_transfer: float,
    x_bjorken: float,
    squared_hadronic_momentum_transfer_t: float,
    lab_kinematics_k: float,
    azimuthal_phi: float,
    compton_form_factor_h: complex,
    compton_form_factor_h_tilde: complex,
    compton_form_factor_e: complex,
    compton_form_factor_e_tilde: complex,
    use_ww: bool = False,
    verbose: bool = False,
    debugging: bool = False) -> float:
    """
    ## Description:
    Numerically evaluates the four-fold cross-section for the electroproduction
    of photons.
    
    :param str lepton_helicity:
        (See BKM formalism.) Either `"positive"`, `"negative"`, or `"none"`. Nothing else! Specifies the helicity of the incoming
        lepton. The strings specifying the polarization are chosen with respect to the coordinate frame chosen in the BKM10 formalism.

    :param str target_polarization:
        (See BKM formalism.) Either `"polarized"` or `"unpolarized"`. Nothing else! 

    :param float squared_q_momentum_transfer: 
        The virtuality of the DVCS photon.

    :param float x_bjorken:
        Partonic momentum fraction of hadron.

    :param float squared_hadronic_momentum_transfer_t:
        Difference between final and initial hadron momentum (Mandelstam t).

    :param float lab_kinematics_k: 
        Incident lepton beam energy.

    :param np.ndarray azimuthal_phi: 
        An *array* of LAB azimuthal angles **in radians, not degrees**.

    :param complex compton_form_factor_h:
        The Compton Form Factor (CFF) called H.

    :param complex compton_form_factor_h_tilde:
            The Compton Form Factor (CFF) called Ht (H-tilde)

    :param complex compton_form_factor_e: 
        The Compton Form Factor (CFF) called E.

    :param complex compton_form_factor_e_tilde:
        The Compton Form Factor (CFF) called Et (E-tilde).

    :param bool verbose:
        If `True`, will print to inform user "where" in the code the program is.

    :param bool debugging:
        Do not turn this on! It will print *every step and computed piece of data in the code*.

    :returns: bkm10_cross_section_in_nb_gev4: (float)
        The four-fold differential cross section.

    ## Notes:
    None!
    """

    try:

        # (1): Calculate Epsilon:
        epsilon = calculate_kinematics_epsilon(
            squared_q_momentum_transfer,
            x_bjorken,
            verbose)
        
        if verbose:
            print("[VERBOSE]: Computed epsilon.")

        if debugging:
            print(f"[DEBUG]: Computed epsilon: {epsilon} ({type(epsilon)})")

        # (2): Calculate the Lepton Energy Fraction:
        lepton_energy_fraction_y = calculate_kinematics_lepton_energy_fraction_y(
            squared_q_momentum_transfer,
            lab_kinematics_k,
            epsilon,
            verbose)
        
        if verbose:
            print("[VERBOSE]: Computed y.")

        if debugging:
            print(f"[DEBUG]: Computed y: {lepton_energy_fraction_y} ({type(lepton_energy_fraction_y)})")

        # (3): Calculate the Skewness Parameter:
        skewness_parameter = calculate_kinematics_skewness_parameter(
            squared_q_momentum_transfer,
            x_bjorken,
            squared_hadronic_momentum_transfer_t,
            verbose)
        
        if verbose:
            print("[VERBOSE]: Computed xi.")

        if debugging:
            print(f"[DEBUG]: Computed xi: {skewness_parameter} ({type(skewness_parameter)})")

        # (4): Calculate t_minimum
        squared_hadronic_momentum_transfer_t_minimum = calculate_kinematics_t_min(
            squared_q_momentum_transfer,
            x_bjorken,
            epsilon,
            verbose)
        
        if verbose:
            print("[VERBOSE]: Computed t_min.")

        if debugging:
            print(f"[DEBUG]: Computed t_min: {squared_hadronic_momentum_transfer_t_minimum} ({type(squared_hadronic_momentum_transfer_t_minimum)})")

        # (5): Calculate t_prime:
        t_prime = calculate_kinematics_t_prime(
            squared_hadronic_momentum_transfer_t,
            squared_hadronic_momentum_transfer_t_minimum,
            verbose)
        
        if verbose:
            print("[VERBOSE]: Computed t'.")

        if debugging:
            print(f"[DEBUG]: Computed t': {t_prime} ({type(t_prime)})")

        # (6): Calculate K_tilde:
        k_tilde = calculate_kinematics_k_tilde(
            squared_q_momentum_transfer,
            x_bjorken,
            lepton_energy_fraction_y,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            squared_hadronic_momentum_transfer_t_minimum,
            verbose)
        
        if verbose:
            print("[VERBOSE]: Computed K-tilde.")

        if debugging:
            print(f"[DEBUG]: Computed K-tilde: {k_tilde} ({type(k_tilde)})")

        # (7): Calculate K Squared:
        shorthand_k = calculate_kinematics_k(
            squared_q_momentum_transfer,
            lepton_energy_fraction_y,
            epsilon,
            k_tilde,
            verbose)
        
        if verbose:
            print("[VERBOSE]: Computed K.")

        if debugging:
            print(f"[DEBUG]: Computed K: {shorthand_k} ({type(shorthand_k)})")


        # (8): Calculate k_dot_delta:
        k_dot_delta = calculate_k_dot_delta(
            squared_q_momentum_transfer,
            x_bjorken,
            squared_hadronic_momentum_transfer_t,
            azimuthal_phi,
            epsilon,
            lepton_energy_fraction_y,
            shorthand_k,
            verbose)
        
        if verbose:
            print("[VERBOSE]: Computed k dot Delta.")

        if debugging:
            print(f"[DEBUG]: Computed k dot Delta: {k_dot_delta} ({type(k_dot_delta)})")

        # (9): Calculate Lepton Propagator 1:
        lepton_propagator_p1 = calculate_lepton_propagator_p1(
            squared_q_momentum_transfer,
            k_dot_delta,
            verbose)
        
        if verbose:
            print("[VERBOSE]: Computed lepton propagator P_1")

        if debugging:
            print(f"[DEBUG]: Computed lepton propagator P_1: {lepton_propagator_p1} ({type(lepton_propagator_p1)})")
        
        # (10): Calculate Lepton Propagator 2:
        lepton_propagator_p2 = calculate_lepton_propagator_p2(
            squared_q_momentum_transfer,
            squared_hadronic_momentum_transfer_t,
            k_dot_delta,
            verbose)
        
        if verbose:
            print("[VERBOSE]: Computed lepton propagator P_2")

        if debugging:
            print(f"[DEBUG]: Computed lepton propagator P_2: {lepton_propagator_p2} ({type(lepton_propagator_p2)})")
        
        # (11): Calculate the Electric Form Factor
        electric_form_factor = calculate_form_factor_electric(
            squared_hadronic_momentum_transfer_t,
            verbose)
        
        if verbose:
            print("[VERBOSE]: Computed F_E")

        if debugging:
            print(f"[DEBUG]: Computed F_E: {electric_form_factor} ({type(electric_form_factor)})")

        # (12): Calculate the Magnetic Form Factor
        magnetic_form_factor = calculate_form_factor_magnetic(
            electric_form_factor,
            verbose)
        
        if verbose:
            print("[VERBOSE]: Computed F_G")

        if debugging:
            print(f"[DEBUG]: Computed F_G: {magnetic_form_factor} ({type(magnetic_form_factor)})")

        # (13): Calculate the Pauli Form Factor, F2:
        pauli_form_factor_f2 = calculate_form_factor_pauli_f2(
            squared_hadronic_momentum_transfer_t,
            electric_form_factor,
            magnetic_form_factor,
            verbose)
        
        if verbose:
            print("[VERBOSE]: Computed F_2")

        if debugging:
            print(f"[DEBUG]: Computed F_2: {pauli_form_factor_f2} ({type(pauli_form_factor_f2)})")

        # (14): Calculate the Dirac Form Factor, F1:
        dirac_form_factor_f1 = calculate_form_factor_dirac_f1(
            magnetic_form_factor,
            pauli_form_factor_f2,
            verbose)
        
        if verbose:
            print("[VERBOSE]: Computed F_1")

        if debugging:
            print(f"[DEBUG]: Computed F_1: {dirac_form_factor_f1} ({type(dirac_form_factor_f1)})")

        # (15): Calculate the cross-section prefactor:
        cross_section_prefactor = calculate_bkm10_cross_section_prefactor(
            squared_q_momentum_transfer,
            x_bjorken,
            epsilon,
            lepton_energy_fraction_y,
            verbose)
        
        if verbose:
            print("[VERBOSE]: Computed cross-section prefactor")

        if debugging:
            print(f"[DEBUG]: Computed cross-section prefactor: {cross_section_prefactor} ({type(cross_section_prefactor)})")
        
        # (16): Initialize the BH Amplitude Squared
        bh_amplitude_squared = 0.

        if verbose:
            print("[VERBOSE]: Initialized BH amplitude squared.")

        if debugging:
            print(f"[DEBUG]: Initialized BH amplitude squared. {bh_amplitude_squared} ({type(bh_amplitude_squared)})")

        # (X): If the lepton beam is unpolarized on the whole...
        if lepton_helicity == 0.0:

            if verbose:
                print("[VERBOSE]: Now evaluating unpolarized-beam DVCS amplitude squared.")

            if debugging:
                print(f"[DEBUG]: Now evaluating unpolarized-beam DVCS amplitude squared because lepton helicity was set to: {lepton_helicity}")
            
            # (X): ... compute 0/5 * (sigma(+1) + sigma(-1)), the coherent-averaged
            # | cross section for the BH term:
            bh_amplitude_squared = (0.5 * (calculate_bh_amplitude_squared(
                1.0,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                azimuthal_phi,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                lepton_propagator_p1,
                lepton_propagator_p2,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                verbose,
                debugging) + calculate_bh_amplitude_squared(
                -1.0,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                azimuthal_phi,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                lepton_propagator_p1,
                lepton_propagator_p2,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                verbose,
                debugging)))

        # (X): If the beam has a particular polarization...
        else:

            if verbose:
                print("[DEBUG]: Now evaluating polarized-beam DVCS amplitude squared.")

            if debugging:
                print(f"[DEBUG]: Now evaluating polarized-beam DVCS amplitude squared because lepton helicity was set to: {lepton_helicity}")

            # (X): ... and then calculate the BH contribution according to that beam configuration:
            bh_amplitude_squared = calculate_bh_amplitude_squared(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                azimuthal_phi,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                lepton_propagator_p1,
                lepton_propagator_p2,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                verbose)

        # (17): Initialize the DVCS Amplitude Squared
        dvcs_amplitude_squared = 0.

        if verbose:
            print("[VERBOSE]: Initialized DVCS amplitude squared.")

        if debugging:
            print(f"[DEBUG]: Initialized DVCS amplitude squared. {dvcs_amplitude_squared} ({type(dvcs_amplitude_squared)})")

        # (X): If the lepton beam is unpolarized on the whole...
        if lepton_helicity == 0.0:

            if verbose:
                print("[VERBOSE]: Now evaluating unpolarized-beam DVCS amplitude squared.")

            if debugging:
                print(f"[DEBUG]: Now evaluating unpolarized-beam DVCS amplitude squared because lepton helicity was set to: {lepton_helicity}")

            # (X): ... compute 0/5 * (sigma(+1) + sigma(-1)), the coherent-averaged
            # | cross section for the DVCS term:
            dvcs_amplitude_squared = (0.5 * (calculate_dvcs_amplitude_squared(
            1.0,
            target_polarization,
            squared_q_momentum_transfer,
            x_bjorken,
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
            use_ww,
            verbose) + calculate_dvcs_amplitude_squared(
            1.0,
            target_polarization,
            squared_q_momentum_transfer,
            x_bjorken,
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
            use_ww,
            verbose)))

        # (X): If the beam has a particular polarization...
        else:

            if verbose:
                print("[VERBOSE]: Now evaluating polarized-beam DVCS amplitude squared.")

            if debugging:
                print(f"[DEBUG]: Now evaluating polarized-beam DVCS amplitude squared because lepton helicity was set to: {lepton_helicity}")

            # (X): ... and then calculate the DVCS contribution according to that beam configuration:
            dvcs_amplitude_squared = calculate_dvcs_amplitude_squared(
            lepton_helicity,
            target_polarization,
            squared_q_momentum_transfer,
            x_bjorken,
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
            use_ww,
            verbose)

        # (18): Initialize the interference piece:
        interference_contribution = 0.

        if verbose:
            print("[VERBOSE]: Initialized Interference amplitude squared.")

        if debugging:
            print(f"[DEBUG]: Initialized Interference amplitude squared. {interference_contribution} ({type(interference_contribution)})")

        # (X): If the lepton beam is unpolarized on the whole...
        if lepton_helicity == 0.0:

            if verbose:
                print("[VERBOSE]: Now evaluating unpolarized-beam DVCS amplitude squared.")

            if debugging:
                print(f"[DEBUG]: Now evaluating unpolarized-beam DVCS amplitude squared because lepton helicity was set to: {lepton_helicity}")

            # (X): ... compute 0/5 * (sigma(+1) + sigma(-1)), the coherent-averaged
            # | cross section:
            interference_contribution = (0.5 * (
                calculate_interference_contribution(
                1.0,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
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
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                compton_form_factor_h,
                compton_form_factor_h_tilde,
                compton_form_factor_e,
                compton_form_factor_e_tilde,
                use_ww,
                verbose) +
                calculate_interference_contribution(
                -1.0,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
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
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                compton_form_factor_h,
                compton_form_factor_h_tilde,
                compton_form_factor_e,
                compton_form_factor_e_tilde,
                use_ww,
                verbose)))

        # (X): If the beam has a particular polarization...
        else:

            if verbose:
                print("[VERBOSE]: Now evaluating polarized-beam Interference amplitude squared.")

            if debugging:
                print(f"[DEBUG]: Now evaluating polarized-beam Interference amplitude squared because lepton helicity was set to: {lepton_helicity}")

            # (X): ... then run the standard function to compute the cross-section:
            interference_contribution = calculate_interference_contribution(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
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
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                compton_form_factor_h,
                compton_form_factor_h_tilde,
                compton_form_factor_e,
                compton_form_factor_e_tilde,
                use_ww,
                verbose)

        # (18): Calculate the total cross section:
        bkm10_cross_section = cross_section_prefactor * (bh_amplitude_squared + dvcs_amplitude_squared + interference_contribution)

        if verbose:
            print("[VERBOSE]: Obtained BKM cross section.")

        if debugging:
            print(f"[DEBUG]: Obtained the BKM cross section: {bkm10_cross_section}")

        # (19): Convert to nb/GeV^{4}:
        bkm10_cross_section_in_nb_gev4 = convert_to_nb_over_GeV4(bkm10_cross_section)

        if verbose:
            print("[VERBOSE]: Converted BKM10 differential cross section to nb/GeV4.")

        if debugging:
            print(f"[DEBUG]: Converted BKM10 differential cross section to {bkm10_cross_section_in_nb_gev4} nb/GeV4")
        
        
        # plot_beam_spin_asymmetry(
        #     lab_azimuthal_phi = azimuthal_phi,
        #     value_of_beam_energy = lab_kinematics_k,
        #     value_of_Q_squared = squared_q_momentum_transfer,
        #     value_of_hadron_recoil = squared_hadronic_momentum_transfer_t,
        #     value_of_x_Bjorken = x_bjorken,
        #     bsa_data = (beam_spin_asymmetry))

        # (20): Return the cross section.
        return bkm10_cross_section_in_nb_gev4

    except Exception as ERROR:
        print(f"> Error in calculating the entire cross section:\n> {ERROR}")
        return 0.
    
