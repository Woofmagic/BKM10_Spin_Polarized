"""
## Description:
Computing the Double-Spin Asymmetry (DSA) according to the BKM10 formalism.

## Notes:
    1. 2026/06/01: Moved this function to its own, dedicated file.
"""

from calculation.bkm10_cross_section import calculate_bkm10_cross_section

def calculate_bkm10_dsa(
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
    Numerically evaluates the double-spin asymmetry (DSA, or DSSA) for a given beam polarization.
    *Note: there are no polarization arguments here because the DSA calculation enforces a particular
    configuration of them.*

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

    # (1): Compute the sigma(lambda = +1, Lambda = +1/2) component of the DSA by reusing the function above:
    plus_beam_plus_lp_target_cross_section = calculate_bkm10_cross_section(
        +1.0, +0.5,
        squared_q_momentum_transfer, x_bjorken, squared_hadronic_momentum_transfer_t, lab_kinematics_k,
        azimuthal_phi,
        compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, use_ww,
        verbose, debugging)
    
    # (2): Compute the sigma(lambda = -1, Lambda = +1/2) component of the DSA by reusing the function above:
    minus_beam_plus_lp_target_cross_section = calculate_bkm10_cross_section(
        -1.0, +0.5,
        squared_q_momentum_transfer, x_bjorken, squared_hadronic_momentum_transfer_t, lab_kinematics_k,
        azimuthal_phi,
        compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, use_ww,
        verbose, debugging)
    
    # (3): Compute the sigma(lambda = +1, Lambda = -1/2) component of the DSA by reusing the function above:
    plus_beam_minus_lp_target_cross_section = calculate_bkm10_cross_section(
        +1.0, -0.5,
        squared_q_momentum_transfer, x_bjorken, squared_hadronic_momentum_transfer_t, lab_kinematics_k,
        azimuthal_phi,
        compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, use_ww,
        verbose, debugging)
    
    # (4): Compute the sigma(lambda = -1, Lambda = -1/2) component of the DSA by reusing the function above:
    minus_beam_minus_lp_target_cross_section = calculate_bkm10_cross_section(
        -1.0, -0.5,
        squared_q_momentum_transfer, x_bjorken, squared_hadronic_momentum_transfer_t, lab_kinematics_k,
        azimuthal_phi,
        compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, use_ww,
        verbose, debugging)
    
    # (5): Compute the DSA:
    dsa = (
        ((plus_beam_plus_lp_target_cross_section - plus_beam_minus_lp_target_cross_section) - (minus_beam_plus_lp_target_cross_section + minus_beam_minus_lp_target_cross_section)) /
        (plus_beam_plus_lp_target_cross_section + plus_beam_minus_lp_target_cross_section + minus_beam_plus_lp_target_cross_section + minus_beam_minus_lp_target_cross_section)
    )

    # (6): Return the DSA:
    return dsa