try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

# Import helper modules:
from statics.mathematics.math_units import convert_degrees_to_radians

# c_{n}^{DVCS}
from coefficients.bh_coefficients.lp_polarized import calculate_c_0_longitudinally_polarized_bh

# s_{n}^{DVCS}
from coefficients.bh_coefficients.lp_polarized import calculate_c_1_longitudinally_polarized_bh

def calculate_bh_amplitude_squared_longitudinally_polarized(
    lepton_polarization: int,
    target_polarization: int,
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
    verbose: bool = True) -> float:
    """
    Description
    --------------
    We finally put everything together and calculate the Bethe-Heitler
    Amplitude squared. This amplitude contains ten billion different
    contributions that we coded earlier. This amplitude requires 
    essentially every kinematic variable and derived kinematic
    variable, and even needs F1 and F2.

    Parameters
    --------------
    lepton_polarization: (int)

    target_polarization: (int)

    squared_Q_momentum_transfer: (float)

    x_Bjorken: (float)

    squared_hadronic_momentum_transfer_t: (float)

    k_shorthand: (float)

    azimuthal_phi: (float)

    verbose: (bool)
        Debugging console output.

    Function Flow
    --------------

    Notes
    --------------
    (1): The equation for the amplitude squared comes from
        Eq. (25) in this paper:
        https://arxiv.org/pdf/hep-ph/0112108.pdf
    """

    try:

        # (1): Calculate the Prefactor of the Denominator:
        denominator_prefactor = x_Bjorken**2 * lepton_energy_fraction_y**2 * (1. + epsilon**2)**2 * squared_hadronic_momentum_transfer_t

        # (2): Calculate the lepton propagator contribution to the denominator:
        denominator_propagators = lepton_propagator_p1 * lepton_propagator_p2
        
        # (3): Stitch together the two calculated pieces:
        denominator = denominator_prefactor * denominator_propagators
        
        # (4): Obtain the first coefficient in the sum:
        coefficient_0_BH = calculate_c_0_longitudinally_polarized_bh(
            lepton_polarization,
            target_polarization,
            squared_Q_momentum_transfer, 
            x_Bjorken, 
            squared_hadronic_momentum_transfer_t, 
            epsilon,
            lepton_energy_fraction_y,
            Dirac_form_factor_F1,
            Pauli_form_factor_F2,
            verbose
        )

        # (5): Obtain the first coefficient in the unevaluated sum (cosine n = 1 term):
        coefficient_1_BH = calculate_c_1_longitudinally_polarized_bh(
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
            verbose
        )

        # (5): Compute the Fourier Mode Expansion:
        mode_expansion = coefficient_0_BH + (coefficient_1_BH * np.cos(np.pi - convert_degrees_to_radians(azimuthal_phi)))

        # (6): Compute the numerator of the amplitude:
        numerator = mode_expansion

        # (7): The entire amplitude:
        bh_amplitude_squared = numerator / denominator

        if verbose:
            print(f"> Calculated BH amplitude squared as: {bh_amplitude_squared}")

        # (8): Return the amplitude:
        
        return bh_amplitude_squared
    
    except Exception as ERROR:
        print(f"> Error in calculating the BH amplitude squared\n> {ERROR}")
        return 0.