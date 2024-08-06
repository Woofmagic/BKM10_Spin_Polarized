from statics.masses.particle_masses import _MASS_OF_PROTON_IN_GEV

from utilities.mathematics.polarization import check_polarization_datatype

try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_c_0_longitudinally_polarized_bh(
    lepton_polarization: float,
    target_polarization: float,
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    lepton_energy_fraction_y: float, 
    Dirac_form_factor_F1: float, 
    Pauli_form_factor_F2: float, 
    verbose: bool = True) -> float:
    """
    # Title: `calculate_c_0_longitudinally_polarized_bh`
    
    ## Description:
    Equation (38) of the **BKM02 Formalism**.

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
    
    ## Notes
    (1): This coefficient is in Equation (38) from
        the BKM02 Formalism, available here:
        https://arxiv.org/pdf/hep-ph/0112108.pdf
    """

    if (check_polarization_datatype(lepton_polarization) or check_polarization_datatype(target_polarization)) is False:

        raise ValueError("> Received unacceptable polarization type.")
    
    try:
        
        # (1): Calculate the common appearance of F1 + F2:
        sum_of_form_factors = (Dirac_form_factor_F1 + Pauli_form_factor_F2)

        # (2): Calculate the frequent appearance of t/4mp
        t_over_four_mp_squared = squared_hadronic_momentum_transfer_t / (4. * _MASS_OF_PROTON_IN_GEV**2)

        # (3): Calculate the weighted sum of the F1 and F2:
        weighted_sum_of_form_factors = Dirac_form_factor_F1 + t_over_four_mp_squared * Pauli_form_factor_F2

        # (4): Calculate the recurrent appearance of 1 - xb:
        one_minus_xb = 1. - x_Bjorken

        # (5): Calculate the common appearance of delta^{2} / Q^{2} = t / Q^{2}
        t_over_Q_squared = squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer

        # (6): Calculate the derived quantity 1 - t/Q^{2}:
        one_minus_t_over_Q_squared = 1. - t_over_Q_squared

        # (7): Calculate the first term's first bracketed term:
        first_term_first_bracket = 0.5 * x_Bjorken * (one_minus_t_over_Q_squared) - t_over_four_mp_squared

        # (8): Calculate the first term's second bracketed term:
        first_term_second_bracket = 2. - x_Bjorken - (2. * (one_minus_xb)**2 * t_over_Q_squared) + (epsilon**2 * one_minus_t_over_Q_squared) - (x_Bjorken * (1. - 2. * x_Bjorken) * t_over_Q_squared**2)

        # (9): Calculate the first term (includes prefactor)
        first_term = 0.5 * sum_of_form_factors * first_term_first_bracket * first_term_second_bracket

        # (10): Calculate the first bracketed term in the second term:
        second_term_first_bracket = x_Bjorken**2 * (1. + t_over_Q_squared)**2 / (4. * t_over_four_mp_squared) + ((1. - x_Bjorken) * (1. + x_Bjorken * t_over_Q_squared))

        # (11): Calculate the second term (including prefactor):
        second_term = (1. - (1. - x_Bjorken) * t_over_Q_squared) * weighted_sum_of_form_factors * second_term_first_bracket

        # (12): Calculate the overall prefactor:
        prefactor = 8. * float(lepton_polarization) * float(target_polarization) * x_Bjorken * (2. - lepton_energy_fraction_y) * lepton_energy_fraction_y * np.sqrt(1. + epsilon**2) * sum_of_form_factors / (1. - t_over_four_mp_squared)

        # (13): Calculate the entire coefficient:
        c0LP_BH = prefactor * (first_term + second_term)

        # (13.1): If verbose, log the output:
        if verbose:
            print(f"> Calculated c0LP_BH to be:\n{c0LP_BH}")

        # (14): Return the coefficient:
        return c0LP_BH

    except Exception as ERROR:
        print(f"> Error in calculating c0LP for BH Amplitude Squared:\n> {ERROR}")
        return 0.