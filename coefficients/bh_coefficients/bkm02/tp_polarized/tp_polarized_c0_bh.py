from statics.masses.particle_masses import _MASS_OF_PROTON_IN_GEV

from utilities.mathematics.polarization import check_polarization_datatype

try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_c_0_transversely_polarized_bh(
    lepton_polarization: float,
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    azimuthal_phi: float,
    epsilon: float,
    lepton_energy_fraction_y: float,
    k_shorthand: float,
    Dirac_form_factor_F1: float, 
    Pauli_form_factor_F2: float, 
    verbose: bool = False) -> float:
    """
    # Title: `calculate_c_0_transversely_polarized_bh`
    
    ## Description:
    Equation (40) of the BKM02 Formalism.

    ## Arguments:
    lepton_polarization: (float)

    target_polarization: (float)

    squared_Q_momentum_transfer: (float)

    x_Bjorken: (float)

    squared_hadronic_momentum_transfer_t: (float)

    epsilon: (float)

    lepton_energy_fraction_y: (float)

    Dirac_form_factor_F1: (float)

    Pauli_form_factor_F2: (float)

    verbose: (bool)
        Debugging console output.

    ## Returns:

    ## Function Flow:

    ## Notes:
    (1): This coefficient is in Equation (40) from
        the BKM02 Formalism, available here:
        https://arxiv.org/pdf/hep-ph/0112108.pdf
    """

    if (check_polarization_datatype(lepton_polarization) or check_polarization_datatype(target_polarization)) is False:

        raise ValueError("> Received unacceptable polarization type.")
    
    try:
        
        # (1): Calculate the common appearance of F1 + F2:
        sum_of_form_factors = (Dirac_form_factor_F1 + Pauli_form_factor_F2)

        # (2): Calculate the frequent appearance of 1 - t/Q^{2}
        t_over_Q_squared = 1. - squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer

        # (3): Calculate the first term in the brackets:
        first_bracket_term = x_Bjorken**3 * _MASS_OF_PROTON_IN_GEV**2 * t_over_Q_squared * sum_of_form_factors / squared_Q_momentum_transfer

        # (4): Calculate the second part of the second bracket term:
        second_part_second_bracket_term = x_Bjorken**2 * _MASS_OF_PROTON_IN_GEV**2 * t_over_Q_squared * Dirac_form_factor_F1 / squared_hadronic_momentum_transfer_t + x_Bjorken * Pauli_form_factor_F2 / 2.

        # (5): Calculate the second bracket term by multiplying a prefactor to the "second part" of it above:
        second_bracket_term = (1. - (1. - x_Bjorken) * squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer) *  second_part_second_bracket_term

        # (6): Calculate crazy prefactor thing:
        epsilon_prefactor = np.sqrt(1. - epsilon**2) * k_shorthand * sum_of_form_factors / np.sqrt(1. - lepton_energy_fraction_y - (epsilon**2 * lepton_energy_fraction_y**2 / 4.))

        # (7): Calculate the rest of the prefactor:
        remaining_prefactor = -8. * lepton_polarization * np.cos(azimuthal_phi) * (2. - lepton_energy_fraction_y) * lepton_energy_fraction_y * np.sqrt(squared_Q_momentum_transfer) / _MASS_OF_PROTON_IN_GEV

        # (8): Piece together all of the factors:
        c0TP_BH = remaining_prefactor * epsilon_prefactor * (first_bracket_term + second_bracket_term)

        # (8.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c0TP_BH to be:\n{c0TP_BH}")

        # (9): Return the coefficient:
        return c0TP_BH

    except Exception as ERROR:
        print(f"> Error in calculating c0TP_BH for BH Amplitude Squared:\n> {ERROR}")
        return 0.