try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

from coefficients.dvcs_coefficients.lp_polarized.bkm10.lp_polarized_curlyC_dvcs import calculate_curly_c_longitudinally_polarized_dvcs

def calculate_c_0_longitudinally_polarized_dvcs(
    lepton_helicity: float,
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float, 
    compton_form_factor_h: complex,
    compton_form_factor_h_tilde: complex,
    compton_form_factor_e: complex,
    compton_form_factor_e_tilde: complex,
    use_ww: bool = False,
    verbose: bool = False) -> float:
    """
    """

    try:
        
        # (1): Calculate the prefactor
        prefactor = 2. * lepton_helicity * target_polarization * lepton_energy_fraction_y * (2. - lepton_energy_fraction_y) / np.sqrt(1. + epsilon**2)

        # (2): Calculate the Curly C contribution:
        curlyC_lp_contribution = calculate_curly_c_longitudinally_polarized_dvcs(
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            compton_form_factor_h,
            compton_form_factor_h_tilde,
            compton_form_factor_e,
            compton_form_factor_e_tilde,
            compton_form_factor_h.conjugate(),
            compton_form_factor_h_tilde.conjugate(),
            compton_form_factor_e.conjugate(),
            compton_form_factor_e_tilde.conjugate(),
            verbose)

        # (3): Return the entire thing:
        c0LP_DVCS = prefactor * curlyC_lp_contribution

        # (3.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c0LP_DVCS to be:\n{c0LP_DVCS}")

        # (4): Return the coefficient:
        return c0LP_DVCS

    except Exception as ERROR:
        print(f"> Error in calculating c0LP for DVCS Amplitude Squared:\n> {ERROR}")
        return 0.