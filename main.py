# Native Library | argparse
import argparse

# Native Library | os
import os

# Native Library | sys
import sys

from statics.strings.static_strings import _DIRECTORY_DATA

from statics.strings.static_strings import _ARGPARSE_DESCRIPTION

from statics.strings.static_strings import _ARGPARSE_ARGUMENT_INPUT_DATAFILE
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_KINEMATIC_SET_NUMBER
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_FORMALISM_VERSION
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_LEPTON_POLARIZATION
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_TARGET_POLARIZATION
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_NUMBER_REPLICAS
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_VERBOSE

from statics.strings.static_strings import _ARGPARSE_ARGUMENT_DESCRIPTION_INPUT_DATAFILE
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_DESCRIPTION_KINEMATIC_SET_NUMBER
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_DESCRIPTION_FORMALISM_VERSION
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_DESCRIPTION_LEPTON_POLARIZATION
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_DESCRIPTION_TARGET_POLARIZATION
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_DESCRIPTION_NUMBER_REPLICAS
from statics.strings.static_strings import _ARGPARSE_ARGUMENT_DESCRIPTION_VERBOSE

# DataFrame Columns
from statics.strings.static_strings import _COLUMN_NAME_KINEMATIC_SET
from statics.strings.static_strings import _COLUMN_NAME_X_BJORKEN
from statics.strings.static_strings import _COLUMN_NAME_Q_SQUARED
from statics.strings.static_strings import _COLUMN_NAME_T_MOMENTUM_CHANGE
from statics.strings.static_strings import _COLUMN_NAME_AZIMUTHAL_PHI
from statics.strings.static_strings import _COLUMN_NAME_LEPTON_MOMENTUM

from calculation.bkm10_cross_section import calculate_bkm10_cross_section

def main(
    kinematics_dataframe_path: str,
    kinematic_set_number: int,
    formalism_version: str,
    lepton_polarization: str,
    target_polarization: str,
    verbose: bool = False):

    # utilities > data_handling > pandas_reading > read_csv_file_with_pandas
    from utilities.data_handling.pandas_reading import read_csv_file_with_pandas

    # utilities > directories > find_directory
    from utilities.directories.searching_directories import find_directory

    try:
        
        # (1): Construct the filepath to the data:
        possible_data_path = f"{_DIRECTORY_DATA}\\{kinematics_dataframe_path}"

        if verbose:
            print(f"> Possible data path is: {possible_data_path}")

        # (2): Now, check if the kinematics is actually there:
        kinematics_dataframe_file_path = find_directory(os.getcwd(), possible_data_path)

        if verbose:
            print(f"> Did we find the filepath for the kinematics? {kinematics_dataframe_file_path}")

        # (3): If the file was there, turn it into a DF with Pandas:
        kinematics_dataframe = read_csv_file_with_pandas(kinematics_dataframe_file_path)

        if verbose:
            print(f"> Did we convert the kinematics file to a Pandas DF? {kinematics_dataframe is not None}")

        # (4): Partition the DF on a fixed kinematic set:
        fixed_kinematic_set_dataframe = kinematics_dataframe[kinematics_dataframe[_COLUMN_NAME_KINEMATIC_SET] == kinematic_set_number]

        if verbose:
            print(f"> Did we manage to fix to a kinematic range? {fixed_kinematic_set_dataframe is not None}")

        # (5): Obtain the range of kinematic quantites:

        # (5.1): We index the DF with the column named "QQ" or something like that:
        range_of_Q_squared = fixed_kinematic_set_dataframe[_COLUMN_NAME_Q_SQUARED]

        # (5.2): We obtain the column of the DF named "x_b":
        range_of_x_Bjorken = fixed_kinematic_set_dataframe[_COLUMN_NAME_X_BJORKEN]

        # (5.3): We obtain the column of the DF named "t":
        range_of_hadronic_momentum_transfer_t = fixed_kinematic_set_dataframe[_COLUMN_NAME_T_MOMENTUM_CHANGE]

        # (5.4): We obtain the column of the DF named "k":
        range_of_lepton_momentum_k = fixed_kinematic_set_dataframe[_COLUMN_NAME_LEPTON_MOMENTUM]

        # (5.5): We obtain the column of the DF named "phi_x":
        range_of_lab_azimuthal_phi = fixed_kinematic_set_dataframe[_COLUMN_NAME_AZIMUTHAL_PHI]

        # (6): Obtain the polarizations -- set to 1 for now:
        numerical_lepton_polarization = 0.5 if lepton_polarization == 'polarized' else 0
        numerical_target_polarization = 1 if target_polarization == 'polarized' else 0

        if verbose:
            print(f"> Obtained lepton helicity to be: {numerical_lepton_polarization}")
            print(f"> Obtained target polarization to be: {numerical_target_polarization}")

        # (7): Obtain the values of the CFFs:
        compton_form_factor_h_real = -0.897
        compton_form_factor_h_imaginary = 2.421

        compton_form_factor_h_tilde_real = 2.444
        compton_form_factor_h_tilde_imaginary = 1.131

        compton_form_factor_e_real = -0.541
        compton_form_factor_e_imaginary = 2.207

        compton_form_factor_e_imaginary = 0.903
        compton_form_factor_e_tilde_imaginary = 5.383

        # (8): Attempt to calculate the BKM10 Cross Section:
        calculate_bkm10_cross_section(
            numerical_lepton_polarization,
            numerical_target_polarization,
            range_of_Q_squared,
            range_of_x_Bjorken,
            range_of_hadronic_momentum_transfer_t,
            range_of_lepton_momentum_k,
            range_of_lab_azimuthal_phi,
            compton_form_factor_h_real,
            compton_form_factor_h_tilde_real,
            compton_form_factor_e_real,
            compton_form_factor_e_imaginary,
            compton_form_factor_h_imaginary,
            compton_form_factor_h_tilde_imaginary,
            compton_form_factor_e_imaginary,
            compton_form_factor_e_tilde_imaginary,
            verbose)

    except KeyboardInterrupt:

        print("Shutdown requested...exiting")

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
    
    # (5): Ask, but don't enforce BKM Formalism:
    parser.add_argument(
        '-lep-polar',
        _ARGPARSE_ARGUMENT_LEPTON_POLARIZATION,
        type = str,
        required = False,
        default = 'polarized',
        choices = ['polarized', 'unpolarized'],
        help = _ARGPARSE_ARGUMENT_DESCRIPTION_LEPTON_POLARIZATION)
    
    # (5): Ask, but don't enforce BKM Formalism:
    parser.add_argument(
        '-target-polar',
        _ARGPARSE_ARGUMENT_TARGET_POLARIZATION,
        type = str,
        required = False,
        default = 'unpolarized',
        choices = ['polarized', 'unpolarized'],
        help = _ARGPARSE_ARGUMENT_DESCRIPTION_TARGET_POLARIZATION)
    
    # (5): Ask, but don't enforce debugging verbosity:
    parser.add_argument(
        '-v',
        _ARGPARSE_ARGUMENT_VERBOSE,
        type = bool,
        required = False,
        default = False,
        help = _ARGPARSE_ARGUMENT_DESCRIPTION_VERBOSE)
    
    # (5): Parse the arguments:
    arguments = parser.parse_args()

    # (6): Run main() with the arguments
    main(
        kinematics_dataframe_path = arguments.input_datafile,
        kinematic_set_number = arguments.kinematic_set,
        formalism_version = arguments.formalism,
        lepton_polarization = arguments.lepton_polarization,
        target_polarization = arguments.target_polarization,
        verbose = arguments.verbose)