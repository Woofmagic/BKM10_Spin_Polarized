"""
## Description:
Computing the Transverse-Spin Asymmetry (TSA) according to the BKM10 formalism.

## Notes:
    1. 2026/06/01: Moved this function to its own, dedicated file.
"""

from calculation.bkm10_cross_section import calculate_bkm10_cross_section


def calculate_bkm10_tsa(
    lepton_helicity: float,
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
    Numerically evaluates the target-spin asymmetry (TSA) for a given beam polarization. *Note: no `target_polarization` argument
    needed here because the TSA is computed based on (+0.5) and (-0.5) target polarizations.

    :param str lepton_helicity:
        (See BKM formalism.) Either `"positive"`, `"negative"`, or `"none"`. Nothing else! Specifies the helicity of the incoming
        lepton. The strings specifying the polarization are chosen with respect to the coordinate frame chosen in the BKM10 formalism.

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

    # (1): If the lepton helicity is 0, interpret that as equal amounts of (+) and (-) beam:
    if lepton_helicity == 0.0:

        # (1.1): Compute the sigma(lambda = +1, Lambda = +1/2) component of the TSA by reusing the function above:
        plus_beam_plus_lp_target_cross_section = calculate_bkm10_cross_section(
            +1.0, +0.5,
            squared_q_momentum_transfer, x_bjorken, squared_hadronic_momentum_transfer_t, lab_kinematics_k,
            azimuthal_phi,
            compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, use_ww,
            verbose, debugging)
        
        # (1.2): Compute the sigma(lambda = -1, Lambda = +1/2) component of the TSA by reusing the function above:
        minus_beam_plus_lp_target_cross_section = calculate_bkm10_cross_section(
            -1.0, +0.5,
            squared_q_momentum_transfer, x_bjorken, squared_hadronic_momentum_transfer_t, lab_kinematics_k,
            azimuthal_phi,
            compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, use_ww,
            verbose, debugging)
        
        # (1.3): Compute the sigma(lambda = +1, Lambda = -1/2) component of the TSA by reusing the function above:
        plus_beam_minus_lp_target_cross_section = calculate_bkm10_cross_section(
            +1.0, -0.5,
            squared_q_momentum_transfer, x_bjorken, squared_hadronic_momentum_transfer_t, lab_kinematics_k,
            azimuthal_phi,
            compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, use_ww,
            verbose, debugging)
        
        # (1.4): Compute the sigma(lambda = -1, Lambda = -1/2) component of the TSA by reusing the function above:
        minus_beam_minus_lp_target_cross_section = calculate_bkm10_cross_section(
            -1.0, -0.5,
            squared_q_momentum_transfer, x_bjorken, squared_hadronic_momentum_transfer_t, lab_kinematics_k,
            azimuthal_phi,
            compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, use_ww,
            verbose, debugging)
        
        # (1.5): Compute the TSA:
        tsa = (
            ((plus_beam_plus_lp_target_cross_section + minus_beam_plus_lp_target_cross_section) - (plus_beam_minus_lp_target_cross_section + minus_beam_minus_lp_target_cross_section)) /
            (plus_beam_plus_lp_target_cross_section + minus_beam_plus_lp_target_cross_section + plus_beam_minus_lp_target_cross_section + minus_beam_minus_lp_target_cross_section)
        )

    # (2): If the lepton helicity is either all (+) or all (-) (i.e. polarized):
    elif lepton_helicity == +1.0 or lepton_helicity == -1.0:

        # (2.1): Compute the sigma(Lambda = +1/2) component of the TSA by reusing the function above:
        plus_lp_target_cross_section = calculate_bkm10_cross_section(
            lepton_helicity, +0.5,
            squared_q_momentum_transfer, x_bjorken, squared_hadronic_momentum_transfer_t, lab_kinematics_k,
            azimuthal_phi,
            compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, use_ww,
            verbose, debugging)
        
        # (2.2): Compute sigma(Lambda = -1/2) for the other half of the TSA:
        minus_lp_target_cross_section = calculate_bkm10_cross_section(
            lepton_helicity, -0.5,
            squared_q_momentum_transfer, x_bjorken, squared_hadronic_momentum_transfer_t, lab_kinematics_k,
            azimuthal_phi,
            compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, use_ww,
            verbose, debugging)
    
        # (2.3): Compute the TSA:
        tsa = (
            (plus_lp_target_cross_section - minus_lp_target_cross_section) / (plus_lp_target_cross_section + minus_lp_target_cross_section)
            )

    # (3): If something else is detected, we haven't actually coded it yet:
    # [TODO]: Code up the possibility to have different amounts of polarization in the beam, i.e. 73.4% (+) polarized:
    else:

        raise NotImplementedError("[ERROR]: Cannot parse beam and targer polarization settings.")
    
    # (4): Return the BSA:
    return tsa