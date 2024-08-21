try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

# Import helper modules:
from utilities.mathematics.math_units import convert_degrees_to_radians

# c_{0, unp}^{BH}
from coefficients.bh_coefficients.bkm02.unpolarized.unpolarized_c0_bh import calculate_c_0_unpolarized_bh

# c_{1, unp}^{BH}
from coefficients.bh_coefficients.bkm02.unpolarized.unpolarized_c1_bh import calculate_c_1_unpolarized_bh

# c_{2, unp}^{BH}
from coefficients.bh_coefficients.bkm02.unpolarized.unpolarized_c2_bh import calculate_c_2_unpolarized_bh

# c_{0, LP}^{BH}
from coefficients.bh_coefficients.bkm02.lp_polarized.lp_polarized_c0_bh import calculate_c_0_longitudinally_polarized_bh

# c_{1, LP}^{BH}
from coefficients.bh_coefficients.bkm02.lp_polarized.lp_polarized_c1_bh import calculate_c_1_longitudinally_polarized_bh

# c_{0, unp}^{BH}
from coefficients.bh_coefficients.bkm02.tp_polarized.tp_polarized_c0_bh import calculate_c_0_transversely_polarized_bh

# c_{1, unp}^{BH}
from coefficients.bh_coefficients.bkm02.tp_polarized.tp_polarized_c1_bh import calculate_c_1_transversely_polarized_bh

# c_{2, unp}^{BH}
from coefficients.bh_coefficients.bkm02.tp_polarized.tp_polarized_s1_bh import calculate_s_1_transversely_polarized_bh

def calculate_bh_amplitude_squared(
    lepton_polarization: float,
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float,
    squared_hadronic_momentum_transfer_t: float,
    azimuthal_phi: float,
    epsilon: float,
    lepton_energy_fraction_y: float,
    k_shorthand: float,
    lepton_propagator_p1: float,
    lepton_propagator_p2: float,
    Dirac_form_factor_F1: float,
    Pauli_form_factor_F2: float,
    verbose: bool = False) -> float:
    
    try:

        # (1): Calculate the Prefactor of the Denominator:
        denominator_prefactor = x_Bjorken**2 * lepton_energy_fraction_y**2 * (1. + epsilon**2)**2 * squared_hadronic_momentum_transfer_t

        # (2): Calculate the lepton propagator contribution to the denominator:
        denominator_propagators = lepton_propagator_p1 * lepton_propagator_p2
        
        # (3): Stitch together the two calculated pieces:
        denominator = denominator_prefactor * denominator_propagators

        # (4): Initialize the coefficients in the BH mode expansion:
        coefficient_c0_BH = 0.
        coefficient_c1_BH = 0.
        coefficient_c2_BH = 0.
        coefficient_s1_BH = 0.

        # (5): Calculate the coefficients based on the target polarization:
        if target_polarization == 0:

            # (5.1): Unpolarized target requires c0: Obtain the first coefficient in the sum:
            coefficient_c0_BH = calculate_c_0_unpolarized_bh(
                squared_Q_momentum_transfer, 
                x_Bjorken, 
                squared_hadronic_momentum_transfer_t, 
                epsilon,
                lepton_energy_fraction_y,
                k_shorthand,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                verbose)

            # (5.2): Unpolarized target requires c1: Obtain the first coefficient in the unevaluated sum (cosine n = 1 term):
            coefficient_c1_BH = calculate_c_1_unpolarized_bh(
                squared_Q_momentum_transfer, 
                x_Bjorken, 
                squared_hadronic_momentum_transfer_t, 
                epsilon,
                lepton_energy_fraction_y,
                k_shorthand,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                verbose)

            # (4.3): Unpolarized target required c2: Obtain the second coefficient in the unevaluated sum (cosine n = 2 term):
            coefficient_c2_BH = calculate_c_2_unpolarized_bh(
                x_Bjorken, 
                squared_hadronic_momentum_transfer_t, 
                k_shorthand,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                verbose)
        
        # (6): If the target is polarized:
        elif target_polarization == 1:

            # (6.1): Longitudinally-polarized target requires c0: Obtain the first coefficient in the sum:
            coefficient_c0_BH = calculate_c_0_longitudinally_polarized_bh(
                lepton_polarization,
                target_polarization,
                squared_Q_momentum_transfer, 
                x_Bjorken, 
                squared_hadronic_momentum_transfer_t, 
                epsilon,
                lepton_energy_fraction_y,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                verbose)

            # (6.2): Longitudinally-polarized target requires c1: Obtain the first coefficient in the unevaluated sum (cosine n = 1 term):
            coefficient_c1_BH = calculate_c_1_longitudinally_polarized_bh(
                lepton_polarization,
                target_polarization,
                squared_Q_momentum_transfer, 
                x_Bjorken, 
                squared_hadronic_momentum_transfer_t, 
                epsilon,
                lepton_energy_fraction_y,
                k_shorthand,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                verbose)
            
        # (6): If the target is tranversely-polaried:
        elif target_polarization == 2:

            # (6.1): Transversely-polarized target requires c0: Obtain the first coefficient in the sum:
            coefficient_c0_BH = calculate_c_0_transversely_polarized_bh(
                lepton_polarization,
                target_polarization,
                squared_Q_momentum_transfer, 
                x_Bjorken, 
                squared_hadronic_momentum_transfer_t, 
                azimuthal_phi,
                epsilon,
                lepton_energy_fraction_y,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                verbose)

            # (6.2): Transversely-polarized target requires c1: Obtain the first coefficient in the unevaluated sum (cosine n = 1 term):
            coefficient_c1_BH = calculate_c_1_transversely_polarized_bh(
                lepton_polarization,
                target_polarization,
                squared_Q_momentum_transfer, 
                x_Bjorken, 
                squared_hadronic_momentum_transfer_t, 
                azimuthal_phi,
                epsilon,
                lepton_energy_fraction_y,
                k_shorthand,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                verbose)
        
            # (6.3): Transversely-polarized target requires s1: Obtain the first coefficient in the unevaluated sum (cosine n = 1 term):
            coefficient_s1_BH = calculate_s_1_transversely_polarized_bh(
                lepton_polarization,
                target_polarization,
                squared_Q_momentum_transfer, 
                x_Bjorken, 
                squared_hadronic_momentum_transfer_t, 
                azimuthal_phi,
                epsilon,
                lepton_energy_fraction_y,
                k_shorthand,
                Dirac_form_factor_F1,
                Pauli_form_factor_F2,
                verbose)

        # (5): Compute the Fourier Mode Expansion:
        mode_expansion = coefficient_c0_BH + (
            coefficient_c1_BH * np.cos(1. * (np.pi - convert_degrees_to_radians(azimuthal_phi))) +
            coefficient_c2_BH * np.cos(2. * (np.pi - convert_degrees_to_radians(azimuthal_phi))) +
            coefficient_s1_BH * np.sin(1. * (np.pi - convert_degrees_to_radians(azimuthal_phi))))

        # (6): Compute the numerator of the amplitude:
        numerator = mode_expansion

        # (7): The entire amplitude:
        bh_amplitude_squared = numerator / denominator

        if verbose:
            print(f"> Calculated BH amplitude squared as: {bh_amplitude_squared}")

        # (8): Return the amplitude:
        return bh_amplitude_squared
        
    except Exception as E:
        print(f"> Error calculating the BH amplitude squared: {E}")
        return 0.