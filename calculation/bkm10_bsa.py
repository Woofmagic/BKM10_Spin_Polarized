"""
## Description:
Computing the Beam-Spin Asymmetry (BSA) according to the BKM10 formalism.

## Notes:
    1. 2026/02/26: Moved this function to its own, dedicated file.
"""

from calculation.bkm10_cross_section import calculate_bkm10_cross_section

def calculate_bkm10_bsa(
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
    Numerically evaluates the beam-spin asymmetry (BSA) for a given target polarization. *Note: no `lepton_polarization` argument
    needed here because the BSA is computed based on (+) and (-) beam polarizations (i.e. both are included!).

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

    # (1): Compute the sigma(lambda = +1) component of the BSA by reusing the function above:
    positive_beam_cross_section = calculate_bkm10_cross_section(
        +1.0, target_polarization,
        squared_q_momentum_transfer, x_bjorken, squared_hadronic_momentum_transfer_t, lab_kinematics_k,
        azimuthal_phi,
        compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, use_ww,
        verbose, debugging)
    
    # (2): Compute sigma(lambda = -1) for the other half of the BSA:
    negative_beam_cross_section = calculate_bkm10_cross_section(
        -1.0, target_polarization,
        squared_q_momentum_transfer, x_bjorken, squared_hadronic_momentum_transfer_t, lab_kinematics_k,
        azimuthal_phi,
        compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, use_ww,
        verbose, debugging)
    
    # (3): Compute the BSA:
    bsa = ((positive_beam_cross_section - negative_beam_cross_section) / (positive_beam_cross_section + negative_beam_cross_section))
    
    # (4): Return the BSA:
    return bsa