try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

from coefficients.dvcs_coefficients.lp_polarized.bkm10.lp_polarized_curlyC_dvcs import calculate_curly_c_longitudinally_polarized_dvcs

from form_factors.effective_cffs import compute_cff_effective

def calculate_c_1_longitudinally_polarized_dvcs(
    lepton_helicity: float,
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float, 
    skewness_parameter: float,
    shorthand_k: float,
    compton_form_factor_h_real_part: float,
    compton_form_factor_h_tilde_real_part: float,
    compton_form_factor_e_real_part: float,
    compton_form_factor_e_tilde_real_part: float,
    compton_form_factor_h_imaginary_part: float,
    compton_form_factor_h_tilde_imaginary_part: float,
    compton_form_factor_e_imaginary_part: float,
    compton_form_factor_e_tilde_imaginary_part: float,
    verbose: bool = False) -> float:
    """
    """

    try:
        
        # (1): Calculate the prefactor
        prefactor = 8. * lepton_helicity * target_polarization * shorthand_k * lepton_energy_fraction_y / (np.sqrt(1. + epsilon**2) * (2. - x_Bjorken))

        # (2): Calculate the F_{eff}:
        compton_form_factor_h_effective = compute_cff_effective(skewness_parameter, compton_form_factor_h_real_part)
        compton_form_factor_h_tilde_effective = compute_cff_effective(skewness_parameter, compton_form_factor_h_tilde_real_part)
        compton_form_factor_e_effective = compute_cff_effective(skewness_parameter, compton_form_factor_e_real_part)
        compton_form_factor_e_tilde_effective = compute_cff_effective(skewness_parameter, compton_form_factor_e_tilde_real_part)
        
        # (3): Return the entire thing:
        c1LP_DVCS = prefactor * calculate_curly_c_longitudinally_polarized_dvcs(
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            compton_form_factor_h_real_part,
            compton_form_factor_h_tilde_real_part,
            compton_form_factor_e_real_part,
            compton_form_factor_e_tilde_real_part,
            compton_form_factor_h_imaginary_part,
            compton_form_factor_h_tilde_imaginary_part,
            compton_form_factor_e_imaginary_part,
            compton_form_factor_e_tilde_imaginary_part,
            verbose
        )

        # (3.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c1LP_DVCS to be:\n{c1LP_DVCS}")

        # (4): Return the coefficient:
        return c1LP_DVCS

    except Exception as ERROR:
        print(f"> Error in calculating c1LP for DVCS Amplitude Squared:\n> {ERROR}")
        return 0.