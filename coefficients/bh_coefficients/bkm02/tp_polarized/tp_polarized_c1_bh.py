from statics.masses.particle_masses import _MASS_OF_PROTON_IN_GEV

from utilities.mathematics.polarization import check_polarization_datatype

try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_c_1_transversely_polarized_bh(
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
    # Title: `calculate_c_1_transversely_polarized_bh`
    
    ## Description:
    Equation (41) of the BKM02 Formalism.

    Parameters
    --------------
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

    Notes
    --------------
    (1): This coefficient is in Equation (40) from
        the BKM02 Formalism, available here:
        https://arxiv.org/pdf/hep-ph/0112108.pdf
    """

    if (check_polarization_datatype(lepton_polarization) or check_polarization_datatype(target_polarization)) is False:

        raise ValueError("> Received unacceptable polarization type.")
    
    try:
        
        # (1): Calculate the common appearance of 1 - y - e^{2} y^{2} / 4
        combination_of_y_and_epsilon = 1. - lepton_energy_fraction_y - (lepton_energy_fraction_y**2 * epsilon**2 / 4.)

        # (2): Calculate the frequent appearance of xb * (1 - t/Q^{2})
        xB_times_t_over_Q_squared = x_Bjorken * (1. - squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer)

        # (3): Calculate the first part of the first term in the brackets:
        first_part_first_bracket_term = xB_times_t_over_Q_squared * Dirac_form_factor_F1 + squared_hadronic_momentum_transfer_t * Pauli_form_factor_F2 / (4. * _MASS_OF_PROTON_IN_GEV**2)

        # (4): Calculate the second bracket term:
        second_bracket_term = (1. + epsilon**2) * xB_times_t_over_Q_squared * (Dirac_form_factor_F1 + (squared_hadronic_momentum_transfer_t * Pauli_form_factor_F2 / (4. * _MASS_OF_PROTON_IN_GEV**2)))

        # (5): Calculate the entire bracket term in one fell swoop:
        bracket_term = 2. * k_shorthand**2 * squared_Q_momentum_transfer * first_part_first_bracket_term / (squared_hadronic_momentum_transfer_t * combination_of_y_and_epsilon) + second_bracket_term

        # (6): Calculate the first part of the prefactor:
        first_part_prefactor = - 16. * lepton_polarization * np.cos(azimuthal_phi) * x_Bjorken * lepton_energy_fraction_y * np.sqrt(combination_of_y_and_epsilon)

        # (7): Piece together all of the factors:
        c1TP_BH = first_part_prefactor * _MASS_OF_PROTON_IN_GEV * np.sqrt(1. + epsilon**2) * (Dirac_form_factor_F1 + Pauli_form_factor_F2) * bracket_term / np.sqrt(squared_Q_momentum_transfer)

        # (7.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c1TP_BH to be:\n{c1TP_BH}")

        # (8): Return the coefficient:
        return c1TP_BH

    except Exception as ERROR:
        print(f"> Error in calculating c1TP_BH for BH Amplitude Squared:\n> {ERROR}")
        return 0.