"""
## Description:
Contains a script that calculates on the |BH||^{2} contribution to the BKM02/10 formalism parametrization
of the DVCS cross section.

## Notes:
1. 2025/09/01: Cleaned some stuff up here.
"""

# 3rd Party Library | NumPy
import numpy as np

# Import helper modules:
from utilities.mathematics.math_units import convert_degrees_to_radians

# c_{0, unp}^{BH}
from coefficients.bh_coefficients.unpolarized.unpolarized_c0_bh import calculate_c_0_unpolarized_bh

# c_{1, unp}^{BH}
from coefficients.bh_coefficients.unpolarized.unpolarized_c1_bh import calculate_c_1_unpolarized_bh

# c_{2, unp}^{BH}
from coefficients.bh_coefficients.unpolarized.unpolarized_c2_bh import calculate_c_2_unpolarized_bh

# c_{0, LP}^{BH}
from coefficients.bh_coefficients.lp_polarized.lp_polarized_c0_bh import calculate_c_0_longitudinally_polarized_bh

# c_{1, LP}^{BH}
from coefficients.bh_coefficients.lp_polarized.lp_polarized_c1_bh import calculate_c_1_longitudinally_polarized_bh

# c_{0, unp}^{BH}
from coefficients.bh_coefficients.tp_polarized.tp_polarized_c0_bh import calculate_c_0_transversely_polarized_bh

# c_{1, unp}^{BH}
from coefficients.bh_coefficients.tp_polarized.tp_polarized_c1_bh import calculate_c_1_transversely_polarized_bh

# c_{2, unp}^{BH}
from coefficients.bh_coefficients.tp_polarized.tp_polarized_s1_bh import calculate_s_1_transversely_polarized_bh

def calculate_bh_amplitude_squared(
    lepton_helicity: float,
    target_polarization: float,
    squared_q_momentum_transfer: float,
    x_bjorken: float,
    squared_hadronic_momentum_transfer_t: float,
    azimuthal_phi: np.ndarray,
    epsilon: float,
    lepton_energy_fraction_y: float,
    shorthand_k: float,
    lepton_propagator_p1: np.ndarray,
    lepton_propagator_p2: np.ndarray,
    dirac_form_factor_f1: float,
    pauli_form_factor_f2: float,
    verbose: bool = False,
    debugging: bool = False) -> float:
    """
    ## Description:
    Calculates the squared BH (Bethe-Heitler) amplitude according to the
    BKM02/BKM10 formalism.

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

    :param float epsilon: 
        Dimensionless, simplifying parameter in the BKM10 formalism.

    :param float lepton_energy_fraction_y: 
        Inelasticity variable: describes the fraction of the initial lepton's energy lost to the virtual photon. 

    :param np.ndarray lepton_propagator_p1:
        An *array* of azimuthally-modulating propagators in the denominator of the BH amplitude squared.

    :param np.ndarray lepton_propagator_p2:
        Another *array* of azimuthally-modulating propagators in the denominator of the BH amplitude squared.

    :param np.ndarray dirac_form_factor_f1:
        The Dirac Form Factor F_{1}: describes charge distribution in the hadron.

    :param np.ndarray pauli_form_factor_f2:
        The Pauli Form Factor F_{2}: describes theanomalous magnetic moment distribution in a hadron.

    :param bool verbose:
        If `True`, will print to inform user "where" in the code the program is.

    :param bool debugging:
        Do not turn this on! It will print *every step and computed piece of data in the code*.

    """
    
    try:

        # (1): Calculate the Prefactor of the Denominator:
        denominator_prefactor = x_bjorken**2 * lepton_energy_fraction_y**2 * (1. + epsilon**2)**2 * squared_hadronic_momentum_transfer_t

        if verbose:
            print("[VERBOSE]: Computed BH amplitude prefactor")

        if debugging:
            print(f"[DEBUG]: Computed BH amplitude prefactor: {denominator_prefactor} ({type(denominator_prefactor)})")

        # (2): Calculate the lepton propagator contribution to the denominator:
        denominator_propagators = lepton_propagator_p1 * lepton_propagator_p2

        if verbose:
            print("[VERBOSE]: Computed BH denominator propagators.")

        if debugging:
            print(f"[DEBUG]: Computed BH denominator propagators: {denominator_propagators} ({type(denominator_propagators)})")
        
        # (3): Stitch together the two calculated pieces:
        denominator = denominator_prefactor * denominator_propagators

        if verbose:
            print("[VERBOSE]: Computed BH denominator.")

        if debugging:
            print(f"[DEBUG]: Computed BH denominator: {denominator} ({type(denominator)})")

        # (4): Initialize the coefficients in the BH mode expansion:
        coefficient_c0_bh = 0.

        if verbose:
            print("[VERBOSE]: Initialized BH s1 coefficient.")

        if debugging:
            print(f"[DEBUG]: Initialized BH s1 coefficient: {coefficient_c0_bh} ({type(coefficient_c0_bh)})")

        coefficient_c1_bh = 0.

        if verbose:
            print("[VERBOSE]: Initialized BH s1 coefficient.")

        if debugging:
            print(f"[DEBUG]: Initialized BH s1 coefficient: {coefficient_c1_bh} ({type(coefficient_c1_bh)})")

        coefficient_c2_bh = 0.

        if verbose:
            print("[VERBOSE]: Initialized BH s1 coefficient.")

        if debugging:
            print(f"[DEBUG]: Initialized BH s1 coefficient: {coefficient_c2_bh} ({type(coefficient_c2_bh)})")

        coefficient_s1_bh = 0.

        if verbose:
            print("[VERBOSE]: Initialized BH s1 coefficient.")

        if debugging:
            print(f"[DEBUG]: Initialized BH s1 coefficient: {coefficient_s1_bh} ({type(coefficient_s1_bh)})")


        # (5): Calculate the coefficients based on the target polarization:
        if target_polarization == 0:

            # (5.1): Unpolarized target requires c0: Obtain the first coefficient in the sum:
            coefficient_c0_bh = calculate_c_0_unpolarized_bh(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed BH c0 coefficient for unpolarized-polarized target.")

            if debugging:
                print(f"[DEBUG]: Computed BH c0 coefficient for unpolarized-polarized target: {coefficient_c0_bh} ({type(coefficient_c0_bh)})")


            # (5.2): Unpolarized target requires c1: Obtain the first coefficient in the unevaluated sum (cosine n = 1 term):
            coefficient_c1_bh = calculate_c_1_unpolarized_bh(
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed BH c1 coefficient for unpolarized-polarized target.")

            if debugging:
                print(f"[DEBUG]: Computed BH c1 coefficient for unpolarized-polarized target: {coefficient_c1_bh} ({type(coefficient_c1_bh)})")

            # (4.3): Unpolarized target required c2: Obtain the second coefficient in the unevaluated sum (cosine n = 2 term):
            coefficient_c2_bh = calculate_c_2_unpolarized_bh(
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                shorthand_k,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed BH c2 coefficient for unpolarized-polarized target.")

            if debugging:
                print(f"[DEBUG]: Computed BH c2 coefficient for unpolarized-polarized target: {coefficient_c2_bh} ({type(coefficient_c2_bh)})")
        
        # (6): If the target is polarized:
        elif target_polarization == 1:

            # (6.1): Longitudinally-polarized target requires c0: Obtain the first coefficient in the sum:
            coefficient_c0_bh = calculate_c_0_longitudinally_polarized_bh(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed BH c1 coefficient for longitudinally-polarized target.")

            if debugging:
                print(f"[DEBUG]: Computed BH c1 coefficient for longitudinally-polarized target: {coefficient_c0_bh} ({type(coefficient_c0_bh)})")

            # (6.2): Longitudinally-polarized target requires c1: Obtain the first coefficient in the unevaluated sum (cosine n = 1 term):
            coefficient_c1_bh = calculate_c_1_longitudinally_polarized_bh(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed BH c1 coefficient for longitudinally-polarized target.")

            if debugging:
                print(f"[DEBUG]: Computed BH c1 coefficient for longitudinally-polarized target: {coefficient_c1_bh} ({type(coefficient_c1_bh)})")
            
        # (6): If the target is tranversely-polaried:
        elif target_polarization == 2:

            # (6.1): Transversely-polarized target requires c0: Obtain the first coefficient in the sum:
            coefficient_c0_bh = calculate_c_0_transversely_polarized_bh(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                azimuthal_phi,
                epsilon,
                lepton_energy_fraction_y,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed BH c0 coefficient for transversely-polarized target.")

            if debugging:
                print(f"[DEBUG]: Computed BH c0 coefficient for transversely-polarized target: {coefficient_c0_bh} ({type(coefficient_c0_bh)})")

            # (6.2): Transversely-polarized target requires c1: Obtain the first coefficient in the unevaluated sum (cosine n = 1 term):
            coefficient_c1_bh = calculate_c_1_transversely_polarized_bh(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                azimuthal_phi,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed BH c1 coefficient for transversely-polarized target.")

            if debugging:
                print(f"[DEBUG]: Computed BH c1 coefficient for transversely-polarized target: {coefficient_c1_bh} ({type(coefficient_c1_bh)})")
        
            # (6.3): Transversely-polarized target requires s1: Obtain the first coefficient in the unevaluated sum (cosine n = 1 term):
            coefficient_s1_bh = calculate_s_1_transversely_polarized_bh(
                lepton_helicity,
                target_polarization,
                squared_q_momentum_transfer,
                x_bjorken,
                squared_hadronic_momentum_transfer_t,
                azimuthal_phi,
                epsilon,
                lepton_energy_fraction_y,
                shorthand_k,
                dirac_form_factor_f1,
                pauli_form_factor_f2,
                verbose)
            
            if verbose:
                print("[VERBOSE]: Computed BH s1 coefficient for transversely-polarized target.")

            if debugging:
                print(f"[DEBUG]: Computed BH s1 coefficient for transversely-polarized target: {coefficient_s1_bh} ({type(coefficient_s1_bh)})")

        # (5): Compute the Fourier Mode Expansion:
        mode_expansion = (coefficient_c0_bh + (
            coefficient_c1_bh * np.cos(1. * (np.pi - azimuthal_phi)) +
            coefficient_c2_bh * np.cos(2. * (np.pi - azimuthal_phi)) +
            coefficient_s1_bh * np.sin(1. * (np.pi - azimuthal_phi))))
        
        if verbose:
            print("[VERBOSE]: Computed BH mode expansion.")

        if debugging:
            print(f"[DEBUG]: Computed BH mode expansion: {mode_expansion} ({type(mode_expansion)})")

        # (7): The entire amplitude:
        bh_amplitude_squared = mode_expansion / denominator

        if verbose:
            print("[VERBOSE]: Computed BH amplitude squared")

        if debugging:
            print(f"[DEBUG]: Computed BH amplitude squared: {bh_amplitude_squared} ({type(bh_amplitude_squared)})")

        # (8): Return the amplitude:
        return bh_amplitude_squared
        
    except Exception as e:
        print(f"[ERROR]: Error calculating the BH amplitude squared: {e}")
        return 0.