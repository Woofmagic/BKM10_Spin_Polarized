from statics.masses.particle_masses import _MASS_OF_PROTON_IN_GEV

from utilities.mathematics.polarization import check_polarization_datatype

import numpy as np

def calculate_s_1_transversely_polarized_bh(
    lepton_helicity: float,
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    azimuthal_phi: float,
    epsilon: float,
    lepton_energy_fraction_y: float,
    shorthand_k: float,
    Dirac_form_factor_F1: float, 
    Pauli_form_factor_F2: float, 
    verbose: bool = False) -> float:
    """
    # Title: `calculate_s_1_transversely_polarized_bh`
    
    ## Description:
    Equation (42) of the BKM02 Formalism.

    Parameters
    --------------
    lepton_helicity: (float)

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

    if (check_polarization_datatype(lepton_helicity) or check_polarization_datatype(target_polarization)) is False:

        raise ValueError("> Received unacceptable polarization type.")
    
    try:
        
        # (1): Calculate the first part of the three pieces:
        first_third = np.sqrt(1. - lepton_energy_fraction_y - (lepton_energy_fraction_y**2 * epsilon**2 / 4.)) * _MASS_OF_PROTON_IN_GEV * np.power(1. + epsilon**2, 1.5) / np.sqrt(squared_Q_momentum_transfer)

        # (2): Calculate  the second third with the Fs:
        second_third = (1. - squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer) * (Dirac_form_factor_F1 + Pauli_form_factor_F2) * (Dirac_form_factor_F1 + (squared_hadronic_momentum_transfer_t * Pauli_form_factor_F2 / (4. * _MASS_OF_PROTON_IN_GEV**2)))

        # (3): Calculate the whole thing:
        s1TP_BH = 16. * lepton_helicity * np.sin(azimuthal_phi) * lepton_energy_fraction_y * x_Bjorken**2 * first_third * second_third

        # (3.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c1TP_BH to be:\n{s1TP_BH}")

        # (4): Return the coefficient:
        return s1TP_BH

    except Exception as ERROR:
        print(f"> Error in calculating s1TP_BH for BH Amplitude Squared:\n> {ERROR}")
        return 0.