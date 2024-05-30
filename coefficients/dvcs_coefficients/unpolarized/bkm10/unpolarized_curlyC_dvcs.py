try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

from statics.masses.particle_masses import _MASS_OF_PROTON_IN_GEV

from utilities.mathematics.complex_variables import two_complex_variable_product

def calculate_curly_c_unpolarized_dvcs(
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float,
    compton_form_factor_h_real_part: float,
    compton_form_factor_h_tilde_real_part: float,
    compton_form_factor_e_real_part: float,
    compton_form_factor_e_tilde_real_part: float,
    compton_form_factor_h_imaginary_part: float,
    compton_form_factor_h_tilde_imaginary_part: float,
    compton_form_factor_e_imaginary_part: float,
    compton_form_factor_e_tilde_imaginary_part: float,
    verbose: bool = True) -> float:
    """
    Description
    --------------
    Equation (2.23) of the BKM10 Formalism.

    Parameters
    --------------
    lepton_polarization: (float)

    target_polarization: (float)

    squared_Q_momentum_transfer: (float)

    x_Bjorken: (float)

    squared_hadronic_momentum_transfer_t: (float)

    epsilon: (float)

    lepton_energy_fraction_y: (float)

    shorthand_K: (float)

    compton_form_factor_h: (float)

    compton_form_factor_h_tilde: (float)

    compton_form_factor_e: (float)

    compton_form_factor_e_tilde: (float)

    verbose: (bool)
        Debugging console output.

    Notes
    --------------
    (1): This coefficient is in Equation (2.23) from
        the BKM10 Formalism, available here:
        https://arxiv.org/pdf/1005.5209.pdf
    """

    try:

        # (1): Calculate the "a" factor:
        a_factor = squared_hadronic_momentum_transfer_t / (4. * _MASS_OF_PROTON_IN_GEV**2)
        
        if verbose:
            print(f"> [{__name__}]: Calculated `a_factor` to be: {a_factor}")

        # (2): Calculate the "b" factor:
        b_factor = 1. - x_Bjorken

        if verbose:
            print(f"> [{__name__}]: Calculated `b_factor` to be: {b_factor}")

        # (3): Calculate the "c" factor:
        c_factor = squared_Q_momentum_transfer + x_Bjorken * squared_hadronic_momentum_transfer_t

        if verbose:
            print(f"> [{__name__}]: Calculated `c_factor` to be: {c_factor}")

        # (4): Calculate the "d" factor:
        d_factor = squared_hadronic_momentum_transfer_t * c_factor

        if verbose:
            print(f"> [{__name__}]: Calculated `d_factor` to be: {d_factor}")

        # (5): Calculate the "e" factor:
        e_factor = (2. - x_Bjorken) * squared_Q_momentum_transfer + x_Bjorken * squared_hadronic_momentum_transfer_t

        if verbose:
            print(f"> [{__name__}]: Calculated `e_factor` to be: {e_factor}")

        # (6): Calculate the "f" factor:
        f_factor = squared_Q_momentum_transfer + squared_hadronic_momentum_transfer_t

        if verbose:
            print(f"> [{__name__}]: Calculated `f_factor` to be: {f_factor}")

        # (7): Calculate the prefactor:
        prefactor = d_factor / e_factor**2

        if verbose:
            print(f"> [{__name__}]: Calculated `prefactor` to be: {prefactor}")

        # (8): Calculate the scaling on the H and H-tilde CFFs:
        cff_h_h_tilde_contribution_first_term = 4. * b_factor * compton_form_factor_h * compton_form_factor_h

        if verbose:
            print(f"> [{__name__}]: Calculated `cff_h_h_tilde_contribution_first_term` to be: {cff_h_h_tilde_contribution_first_term}")


        # (9): Calculate the scaling on the H and H-tilde CFFs:
        cff_h_h_tilde_contribution_second_term = 4. * compton_form_factor_h_tilde * compton_form_factor_h_tilde * (b_factor + ((2. * squared_Q_momentum_transfer + squared_hadronic_momentum_transfer_t) * epsilon) / (4. * c_factor)) 

        if verbose:
            print(f"> [{__name__}]: Calculated `cff_h_h_tilde_contribution_second_term` to be: {cff_h_h_tilde_contribution_second_term}")
        
        # (10): Calculate the scaling on mixing H and E CFFs (with relative complex-conjugation):
        cff_e_h_mixing_contribution = -1. * x_Bjorken * f_factor**2 * (compton_form_factor_h * compton_form_factor_e + compton_form_factor_h * compton_form_factor_e) / d_factor

        if verbose:
            print(f"> [{__name__}]: Calculated `cff_e_h_mixing_contribution` to be: {cff_e_h_mixing_contribution}")
        
        # (11): Calculate the scaling on mixing H-Tilde and E-Tilde CFFs:
        cff_e_tilde_h_tilde_mixing_contribution = -1. * x_Bjorken * squared_Q_momentum_transfer * (compton_form_factor_h_tilde * compton_form_factor_e_tilde + compton_form_factor_h_tilde * compton_form_factor_e_tilde) / c_factor

        if verbose:
            print(f"> [{__name__}]: Calculated `cff_e_tilde_h_tilde_mixing_contribution` to be: {cff_e_tilde_h_tilde_mixing_contribution}")
        
        # (12): Calculate the scaling on E/EStar CFFs:
        cff_e_estar_contribution = -1. * (x_Bjorken * f_factor**2 / d_factor + e_factor**2 * a_factor / d_factor) * compton_form_factor_e * compton_form_factor_e

        if verbose:
            print(f"> [{__name__}]: Calculated `cff_e_estar_contribution` to be: {cff_e_estar_contribution}")
        
        # (13): Calculate the scaling on E-Tilde/E-TildeStar CFFs:
        cff_e_tilde_e_tilde_star_contribution = -1. * x_Bjorken * squared_Q_momentum_transfer * a_factor * c_factor * compton_form_factor_e_tilde * compton_form_factor_e_tilde

        if verbose:
            print(f"> [{__name__}]: Calculated `cff_e_tilde_e_tilde_star_contribution` to be: {cff_e_tilde_e_tilde_star_contribution}")
        
        # (14): Put together everything
        C_function_of_CFFs_unpolarized = prefactor * (cff_h_h_tilde_contribution_first_term + cff_h_h_tilde_contribution_second_term + cff_e_h_mixing_contribution + cff_e_tilde_h_tilde_mixing_contribution + cff_e_estar_contribution + cff_e_tilde_e_tilde_Star_contribution)

        if verbose:
            print(f"> [{__name__}]: Calculated `C_function_of_CFFs_unpolarized` to be: {C_function_of_CFFs_unpolarized}")

        # (15): Return the huge number:
        return C_function_of_CFFs_unpolarized

    except Exception as E:
        print(f"> Error computing C_function_of_CFFs_unpolarized:\n> {E}")  
        return None