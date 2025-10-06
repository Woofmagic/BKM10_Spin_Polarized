"""
## Description:
This script takes in kinematic settings and CFF data and returns what the 
four-fold differential cross-section ought to be according to the BKM10 formalism.

## Notes:
1. The paper for the BKM02 formalism is available here (as of 2025/09/01):
    https://www.sciencedirect.com/science/article/abs/pii/S055032130200144X
2. The paper for the BKM10 version is available here (as of2025/09/01):
    https://journals.aps.org/prd/abstract/10.1103/PhysRevD.82.074010
"""

# Native Library | argparse
import argparse

# Native Library | os
import os

# Native Library | sys
import sys

# 3rd Party Library | NumPy
import numpy as np

# 3rd Party Library | Matplotlib
import matplotlib.pyplot as plt

# utilities > data_handling > pandas_reading > read_csv_file_with_pandas
from utilities.data_handling.pandas_reading import read_csv_file_with_pandas

# utilities > directories > find_directory
from utilities.directories.searching_directories import find_directory

# static_strings > /data
from statics.strings.static_strings import _DIRECTORY_DATA

# static_strings > argparse > description:
from statics.strings.static_strings import _ARGPARSE_DESCRIPTION

# static_strings > argparse > -d:
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_INPUT_DATAFILE

# static_strings > argparse > -kin:
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_KINEMATIC_SET_NUMBER

# static_strings > argparse > -form:
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_FORMALISM_VERSION

# static_strings > argparse > -lep-helicity:
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_LEPTON_HELICITY

# static_strings > argparse > -target-polar:
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_TARGET_POLARIZATION

# static_strings > argparse > -v:
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_VERBOSE

# static_strings > argparse > description for -d:
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_DESCRIPTION_INPUT_DATAFILE

# static_strings > argparse > description for -kin:
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_DESCRIPTION_KINEMATIC_SET_NUMBER

# static_strings > argparse > description for -form:
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_DESCRIPTION_FORMALISM_VERSION

# static_strings > argparse > description for -lep-helicity:
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_DESCRIPTION_LEPTON_HELICITY

# static_strings > argparse > description for -target-polar
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_DESCRIPTION_TARGET_POLARIZATION

# static_strings > argparse > description for verbose:
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_DESCRIPTION_VERBOSE

# static_strings > "set"
from statics.strings.static_strings import _COLUMN_NAME_KINEMATIC_SET

# static_strings > "k"
from statics.strings.static_strings import _COLUMN_NAME_LEPTON_MOMENTUM

# static_strings > "x_b"
from statics.strings.static_strings import _COLUMN_NAME_X_BJORKEN

# static_strings > "q_squared"
from statics.strings.static_strings import _COLUMN_NAME_Q_SQUARED

# static_strings > "t"
from statics.strings.static_strings import _COLUMN_NAME_T_MOMENTUM_CHANGE

# static_strings > "phi"
from statics.strings.static_strings import _COLUMN_NAME_AZIMUTHAL_PHI

# static_strings > Re[H]
from statics.strings.static_strings import _COLUMN_NAME_CFF_REAL_H

# static_strings > Im[H]
from statics.strings.static_strings import _COLUMN_NAME_CFF_IMAG_H

# static_strings > Re[E]
from statics.strings.static_strings import _COLUMN_NAME_CFF_REAL_E

# static_strings > Im[E]
from statics.strings.static_strings import _COLUMN_NAME_CFF_IMAG_E

# static_strings > Re[Ht]
from statics.strings.static_strings import _COLUMN_NAME_CFF_REAL_H_TILDE

# static_strings > Im[Ht]
from statics.strings.static_strings import _COLUMN_NAME_CFF_IMAG_H_TILDE

# static_strings > Re[Et]
from statics.strings.static_strings import _COLUMN_NAME_CFF_REAL_E_TILDE

# static_strings > Im[ET]
from statics.strings.static_strings import _COLUMN_NAME_CFF_IMAG_E_TILDE

# static_strings > .png
from statics.strings.static_strings import _FIGURE_FORMAT_PNG

# (X): Function | calculation > bkm10_cross_section:
from calculation.bkm10_cross_section import calculate_bkm10_cross_section

def main(
    kinematics_dataframe_path: str,
    kinematic_set_number: int,
    formalism_version: str,
    lepton_helicity: str,
    target_polarization: str,
    verbose: bool = False,
    debugging: bool = True):
    """
    ## Description:
    The main function that runs computes the entire BKM[`formalism_version`] cross-section according to
    a `kinematics_dataframe_path` file of kinematic and CFF data within.

    :param str kinematics_dataframe_path:

    :param int kinematics_set_number:

    :param str formalism_version:
        Either `"bkm10"` or `"bkm02"`. Nothing else! One can compute the cross-section using either the 2002 
        formulation or the 2010 formulation. By default, this is `"bkm10"`.
        [NOTE]: Later, we wish to integrate more formalisms out there that parametrize the DVCS cross-section.

    :param str lepton_helicity:
        (See BKM formalism.) Either `"positive"`, `"negative"`, or `"none"`. Nothing else! Specifies the helicity of the incoming
        lepton. The strings specifying the polarization are chosen with respect to the coordinate frame chosen in the BKM10 formalism.

    :param str target_polarization:
        (See BKM formalism.) Either `"polarized"` or `"unpolarized"`. Nothing else! 

    :param bool verbose:
        If `True`, will print to inform user "where" in the code the program is.

    :param bool debugging:
        Do not turn this on! It will print *every step and computed piece of data in the code*.
    """

    try:
        
        # (1): Construct the filepath to the data:
        possible_data_path = f"{_DIRECTORY_DATA}/{kinematics_dataframe_path}"

        if verbose:
            print(f"[VERBOSE]: Possible data path is: {possible_data_path}")

        if debugging:
            print(f"[DEBUG]: Possible data path is: {possible_data_path}")

        # (2): Now, check if the kinematics is actually there:
        kinematics_dataframe_file_path = find_directory(os.getcwd(), possible_data_path)

        if verbose:
            print(f"[VERBOSE]: Did we find the filepath for the kinematics? {kinematics_dataframe_file_path}")

        if debugging:
            print(f"[DEBUG]: Did we find the filepath for the kinematics? {kinematics_dataframe_file_path}")

        # (3): If the file was there, turn it into a DF with Pandas:
        kinematics_dataframe = read_csv_file_with_pandas(kinematics_dataframe_file_path)

        if verbose:
            print(f"[VERBOSE]: Did we convert the kinematics file to a Pandas DF? {kinematics_dataframe is not None}")

        if debugging:
            print(f"[DEBUG]: The kinematics dataframe has been found. Printing:\n {kinematics_dataframe}")

        # (4): Partition the DF on a fixed kinematic set:
        fixed_kinematic_set_dataframe = kinematics_dataframe[kinematics_dataframe[_COLUMN_NAME_KINEMATIC_SET] == kinematic_set_number]

        if verbose:
            print(f"[VERBOSE]: Did we manage to fix to a kinematic range? {fixed_kinematic_set_dataframe is not None}")

        if debugging:
            print(f"[DEBUG]: Parititioned on a fixed kinematic setting: Printing:\n {fixed_kinematic_set_dataframe}")

        # (5): We index the DF with the column named "QQ" or something like that:
        range_of_q_squared = fixed_kinematic_set_dataframe[_COLUMN_NAME_Q_SQUARED]

        if verbose:
            print("[VERBOSE]: Successfully obtained a range of Q^2 values.")

        if debugging:
            print(f"[DEBUG]: Successfully obtained a range of Q^2 values. Printing:\n {range_of_q_squared}")

        # (5.2): We obtain the column of the DF named "x_b":
        range_of_x_bjorken = fixed_kinematic_set_dataframe[_COLUMN_NAME_X_BJORKEN]

        if verbose:
            print("[VERBOSE]: Successfully obtained a range of x_B values.")

        if debugging:
            print(f"[DEBUG]: Successfully obtained a range of x_B values. Printing:\n {range_of_x_bjorken}")

        # (5.3): We obtain the column of the DF named "t":
        range_of_hadronic_momentum_transfer_t = fixed_kinematic_set_dataframe[_COLUMN_NAME_T_MOMENTUM_CHANGE]

        if verbose:
            print("[VERBOSE]: Successfully obtained a range of t values.")

        if debugging:
            print(f"[DEBUG]: Successfully obtained a range of t values. Printing:\n {range_of_hadronic_momentum_transfer_t}")

        # (5.4): We obtain the column of the DF named "k":
        range_of_lepton_momentum_k = fixed_kinematic_set_dataframe[_COLUMN_NAME_LEPTON_MOMENTUM]

        if verbose:
            print("[VERBOSE]: Successfully obtained a range of k values.")

        if debugging:
            print(f"[DEBUG]: Successfully obtained a range of k values. Printing:\n {range_of_lepton_momentum_k}")

        # (5.5): We obtain the column of the DF named "phi_x":
        range_of_lab_azimuthal_phi = fixed_kinematic_set_dataframe[_COLUMN_NAME_AZIMUTHAL_PHI]

        if verbose:
            print("[VERBOSE]: Successfully obtained a range of phi values.")

        if debugging:
            print(f"[DEBUG]: Successfully obtained a range of phi values. Printing:\n {range_of_lab_azimuthal_phi}")

        # (X): Dynamically determine the correct float based on the string argument for lepton helicity:
        numerical_lepton_polarization = 1.0 if lepton_helicity == 'positive' else -1.0 if lepton_helicity == 'negative' else 0.0

        # (X): Same as above except for target polarization:
        numerical_target_polarization = 0.5 if target_polarization == 'polarized' else 0.0

        if verbose:
            print(f"[VERBOSE]: Obtained lepton helicity to be: {numerical_lepton_polarization}")

        if debugging:
            print(f"[DEBUG]: Obtained target polarization to be: {numerical_target_polarization}")
        
        # (X.1): Obtain the values of the Re[H]:
        compton_form_factor_h_real = fixed_kinematic_set_dataframe[_COLUMN_NAME_CFF_REAL_H].iloc[0]

        if verbose:
            print("[VERBOSE]: Obtained CFF Re[H] value.")

        if debugging:
            print(f"[DEBUG]: Obtained CFF Re[H] value to be: {compton_form_factor_h_real} ({type(compton_form_factor_h_real)})")

        # (X.2): Obtain the values of the Im[H]:
        compton_form_factor_h_imaginary = fixed_kinematic_set_dataframe[_COLUMN_NAME_CFF_IMAG_H].iloc[0]

        if verbose:
            print("[VERBOSE]: Obtained CFF Im[H] value.")

        if debugging:
            print(f"[DEBUG]: Obtained CFF Im[H] value to be: {compton_form_factor_h_imaginary} ({type(compton_form_factor_h_imaginary)})")

        # (X.3): Obtain the values of the Re[Ht]:
        compton_form_factor_h_tilde_real = fixed_kinematic_set_dataframe[_COLUMN_NAME_CFF_REAL_H_TILDE].iloc[0]

        if verbose:
            print("[VERBOSE]: Obtained CFF Re[Ht] value.")

        if debugging:
            print(f"[DEBUG]: Obtained CFF Re[Ht] value to be: {compton_form_factor_h_tilde_real} ({type(compton_form_factor_h_tilde_real)})")

        # (X.4): Obtain the values of the Im[Ht]:
        compton_form_factor_h_tilde_imaginary = fixed_kinematic_set_dataframe[_COLUMN_NAME_CFF_IMAG_H_TILDE].iloc[0]

        if verbose:
            print("[VERBOSE]: Obtained CFF Im[H] value.")

        if debugging:
            print(f"[DEBUG]: CFF Im[H] value to be: {compton_form_factor_h_tilde_imaginary} ({type(compton_form_factor_h_tilde_imaginary)})")

        # (X.5): Obtain the values of the Re[E]:
        compton_form_factor_e_real = fixed_kinematic_set_dataframe[_COLUMN_NAME_CFF_REAL_E].iloc[0]

        if verbose:
            print("[VERBOSE]: Obtained CFF Re[E] value.")

        if debugging:
            print(f"[DEBUG]: Obtained CFF Re[E] value to be: {compton_form_factor_e_real} ({type(compton_form_factor_e_real)})")

        # (X.6): Obtain the values of the Im[E]:
        compton_form_factor_e_imaginary = fixed_kinematic_set_dataframe[_COLUMN_NAME_CFF_IMAG_E].iloc[0]

        if verbose:
            print("[VERBOSE]: Obtained CFF Im[H] value.")

        if debugging:
            print(f"[DEBUG]: Obtained CFF Im[H] value to be: {compton_form_factor_e_imaginary} ({type(compton_form_factor_e_imaginary)})")

        # (X.7): Obtain the values of the Re[Et]:
        compton_form_factor_e_tilde_real = fixed_kinematic_set_dataframe[_COLUMN_NAME_CFF_REAL_E_TILDE].iloc[0]

        if verbose:
            print("[VERBOSE]: Obtained CFF Re[Et] value.")

        if debugging:
            print(f"[DEBUG]: Obtained CFF Re[Et] value to be: {compton_form_factor_e_tilde_real} ({type(compton_form_factor_e_tilde_real)})")

        # (X.8): Obtain the values of the Im[Et]:
        compton_form_factor_e_tilde_imaginary = fixed_kinematic_set_dataframe[_COLUMN_NAME_CFF_IMAG_E_TILDE].iloc[0]

        if verbose:
            print("[VERBOSE]: Obtained CFF Im[Et] value.")

        if debugging:
            print(f"[DEBUG]: Obtained CFF Im[Et] value to be: {compton_form_factor_e_tilde_imaginary} ({type(compton_form_factor_e_tilde_imaginary)})")

        # (X): Obtain a single float for Q^{2}:
        value_of_q_squared = range_of_q_squared.iloc[0]

        if verbose:
            print("[VERBOSE]: Obtained single Q^2 value from dataframe.")

        if debugging:
            print(f"[DEBUG]: Obtained single Q^2 value from dataframe: {value_of_q_squared} ({type(value_of_q_squared)})")

        # (X): Obtain a single float for x_{B}:
        value_of_x_bjorken = range_of_x_bjorken.iloc[0]

        if verbose:
            print("[VERBOSE]: Obtained single x_B value from dataframe.")

        if debugging:
            print(f"[DEBUG]: Obtained single x_B value from dataframe: {value_of_x_bjorken} ({type(value_of_x_bjorken)})")

        # (X): Obtain a single float for t:
        value_of_t = range_of_hadronic_momentum_transfer_t.iloc[0]

        if verbose:
            print("[VERBOSE]: Obtained single t value from dataframe.")

        if debugging:
            print(f"[DEBUG]: Obtained single t value from dataframe: {value_of_t} ({type(value_of_t)})")

        # (X): Obtain a single float for k:
        value_of_k = range_of_lepton_momentum_k.iloc[0]

        if verbose:
            print("[VERBOSE]: Obtained single k value from dataframe.")

        if debugging:
            print(f"[DEBUG]: Obtained single k value from dataframe: {value_of_k} ({type(value_of_k)})")

        # (8): Attempt to calculate the BKM10 Cross Section:
        computed_cross_sections = calculate_bkm10_cross_section(
            numerical_lepton_polarization,
            numerical_target_polarization,
            value_of_q_squared,
            value_of_x_bjorken,
            value_of_t,
            value_of_k,
            range_of_lab_azimuthal_phi,
            complex(compton_form_factor_h_real, compton_form_factor_h_tilde_real),
            complex(compton_form_factor_e_real, compton_form_factor_e_imaginary),
            complex(compton_form_factor_h_imaginary, compton_form_factor_h_tilde_imaginary),
            complex(compton_form_factor_e_tilde_real, compton_form_factor_e_tilde_imaginary),
            verbose)
        
        # (X): Coerce kinematic values into a string:
        title_string = (
            rf"$Q^2 = {value_of_q_squared:.2f}$ GeV$^2$, "
            rf"$x_B = {value_of_x_bjorken:.2f}$, "
            rf"$t = {value_of_t:.2f}$ GeV$^2$, "
            rf"$k = {value_of_k:.2f}$ GeV")
        
        # (X): Obtain the CFF inputs as well to display:
        cff_string = (
            rf"$\mathcal{{H}} = {complex(compton_form_factor_h_real, compton_form_factor_h_tilde_real):.3f}$, "
            rf"$\widetilde{{\mathcal{{H}}}} = {complex(compton_form_factor_e_real, compton_form_factor_e_imaginary):.3f}$, "
            rf"$\mathcal{{E}} = {complex(compton_form_factor_h_imaginary, compton_form_factor_h_tilde_imaginary):.3f}$, "
            rf"$\widetilde{{\mathcal{{E}}}} = {complex(compton_form_factor_e_tilde_real, compton_form_factor_e_tilde_imaginary):.3f}$")

        # (X): Initialize a figure:
        cross_section_figure = plt.figure(figsize = (8, 5))

        # (X): Add an Axis object to it:
        cross_section_axis = cross_section_figure.add_subplot(1, 1, 1)

        # (X): Plot the computed cross-section data:
        cross_section_axis.plot(
            range_of_lab_azimuthal_phi,
            computed_cross_sections,
            marker = ".",
            linestyle = "none",
            color = "red",
            alpha = 0.65)
        
        # (X): Set the x-label:
        cross_section_axis.set_xlabel(r"Azimuthal Angle $\phi$ (radians)")

        # (X): Set the y-label:
        cross_section_axis.set_ylabel(r"Differential Cross Section ($nb/GeV^{4}$)")

        # (X): Set the title:
        cross_section_axis.set_title(f"{title_string}\n{cff_string}")

        # (X): Add a grid:
        cross_section_axis.grid(True)

        # (X): Compute the figure title:
        figure_title = f"{formalism_version}_cross_section_v1.{_FIGURE_FORMAT_PNG}"

        # (X): Save the figure as PNG:
        cross_section_figure.savefig(
            fname = figure_title,
            format = _FIGURE_FORMAT_PNG,
            dpi = 400)

        # (X): Close the figure to avoid killing the machine's memory and etc.:
        plt.close(cross_section_figure)

        # (X): Return the numerical value of the cross section:
        return computed_cross_sections

    except KeyboardInterrupt:

        print("[ERROR]: Shutdown requested...exiting")

        sys.exit(0)
   
if __name__ == "__main__":
    
    # (1): Create an instance of the ArgumentParser
    parser = argparse.ArgumentParser(description = _ARGPARSE_DESCRIPTION)

    # (2): Enforce the path to the datafile:
    parser.add_argument(
        '-d',
        _ARGPARSE_ARGUMENT_INPUT_DATAFILE,
        type = str,
        required = True,
        help = _ARGPARSE_ARGUMENT_DESCRIPTION_INPUT_DATAFILE)
    
    # (3): Enforce the path to the datafile:
    parser.add_argument(
        '-kin',
        _ARGPARSE_ARGUMENT_KINEMATIC_SET_NUMBER,
        type = int,
        required = True,
        help = _ARGPARSE_ARGUMENT_DESCRIPTION_KINEMATIC_SET_NUMBER)
    
    # (4): Ask, but don't enforce BKM Formalism:
    parser.add_argument(
        '-form',
        _ARGPARSE_ARGUMENT_FORMALISM_VERSION,
        type = str,
        required = True,
        default = '10',
        help = _ARGPARSE_ARGUMENT_DESCRIPTION_FORMALISM_VERSION)
    
    # (5): Ask, but don't enforce lepton helicity parameter:
    parser.add_argument(
        '-lep-helicity',
        _ARGPARSE_ARGUMENT_LEPTON_HELICITY,
        type = str,
        required = False,
        default = 'none',
        choices = ['positive','none', 'negative'],
        help = _ARGPARSE_ARGUMENT_DESCRIPTION_LEPTON_HELICITY)
    
    # (5): Ask, but don't enforce target polarization parameter:
    parser.add_argument(
        '-target-polar',
        _ARGPARSE_ARGUMENT_TARGET_POLARIZATION,
        type = str,
        required = False,
        default = 'unpolarized',
        choices = ['polarized', 'unpolarized'],
        help = _ARGPARSE_ARGUMENT_DESCRIPTION_TARGET_POLARIZATION)
    
    # (6): Ask, but don't enforce verbose output:
    parser.add_argument(
        '-v',
        _ARGPARSE_ARGUMENT_VERBOSE,
        type = bool,
        required = False,
        default = False,
        help = _ARGPARSE_ARGUMENT_DESCRIPTION_VERBOSE)
    
    # (7): Parse the arguments:
    arguments = parser.parse_args()

    # (8): Run main() with the arguments:
    main(
        kinematics_dataframe_path = arguments.input_datafile,
        kinematic_set_number = arguments.kinematic_set,
        formalism_version = arguments.formalism,
        lepton_helicity = arguments.lepton_helicity,
        target_polarization = arguments.target_polarization,
        verbose = arguments.verbose)
