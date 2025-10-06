"""
A centralized source of truth for the entire script.

## Notes:
1. All of the variables defined here may be regarded equivalently as "parameters," "control parameters," 
or "model parameters." They are, depending who you ask, also equivalent to "hyperparameters."
"""

# Directory | base > data
_DIRECTORY_DATA = 'data'

# Directory | base > extractions
_DIRECTORY_EXTRACTIONS = 'data'

# Directory | base > extractions > models
_DIRECTORY_EXTRACTIONS_MODELS_ = 'models'

# Directory | base > extractions > models > _DIRECTORY_EXTRACTIONS__MODELS_KINEMATIC_SETS
_DIRECTORY_EXTRACTIONS__MODELS_KINEMATIC_SETS = 'kinematic_sets'

# (1): argparser's description:
_ARGPARSE_DESCRIPTION = "An analysis script that takes a dataframe and shows you what the predicted BKM10/02 cross section"

# (2): argparers *argument flag* for the datafile:
_ARGPARSE_ARGUMENT_INPUT_DATAFILE = '--input-datafile'

# (3): argparser's description for the argument `input-datafile`:
_ARGPARSE_ARGUMENT_DESCRIPTION_INPUT_DATAFILE = 'Path to the input CSV file.'

# (4): argparer's *argument flag* for the datafile:
_ARGPARSE_ARGUMENT_KINEMATIC_SET_NUMBER = '--kinematic-set'

# (5): argparser's description for the argument `kinematic-set`:
_ARGPARSE_ARGUMENT_DESCRIPTION_KINEMATIC_SET_NUMBER = 'An integer specifying which kinematic set to analyze.'

# (6): argparser's argument flag for the formalism, either "bkm10" or "bkm02"
_ARGPARSE_ARGUMENT_FORMALISM_VERSION = '--formalism'

# (7): argparser's description for the argument `formalism`:
_ARGPARSE_ARGUMENT_DESCRIPTION_FORMALISM_VERSION = 'The version of the formalism that we are using to analyze the cross section. Usually, it is BKM10.'

# (8): argparser's argument flag for the formalism, either "positive" or "negative"
_ARGPARSE_ARGUMENT_LEPTON_HELICITY = '--lepton-helicity'

# (9): argparser's description for the argument `lepton-helicity`:
_ARGPARSE_ARGUMENT_DESCRIPTION_LEPTON_HELICITY = 'The incoming lepton helicitiy: positive or negative.'

# (9): argparser's argument flag for the target polarization, either "unpolarized" or "polarized"
_ARGPARSE_ARGUMENT_TARGET_POLARIZATION = '--target-polarization'

# (10): argparser's description for the argument `target-polarization`:
_ARGPARSE_ARGUMENT_DESCRIPTION_TARGET_POLARIZATION = 'The nucleon target polarization: unpolarized or polarized.'

# (11): argparer's *argument flag* for the datafile:
_ARGPARSE_ARGUMENT_VERBOSE = '--verbose'

# (12): argparer's *argument flag* for the datafile:
_ARGPARSE_ARGUMENT_DESCRIPTION_VERBOSE = 'Enable verbose logging.'

# (13): argparer's *argument flag* for the datafile:
_ARGPARSE_ARGUMENT_DEBUGGING = '--debugging'

# (14): argparer's *argument flag* for the datafile:
_ARGPARSE_ARGUMENT_DESCRIPTION_DEBUGGING = 'Enable insane debugging logging (everything gets printed).'

# (15): "Generalized" column name for kinematic set:
_COLUMN_NAME_KINEMATIC_SET = "set"

# (16): "Generalized" column name for lepton beam energy:
_COLUMN_NAME_LEPTON_MOMENTUM = "k"

# (17): "Generalized" column name for Q^{2}:
_COLUMN_NAME_Q_SQUARED = "q_squared"

# (18): "Generalized" column name for t (hadronic momentum transfer):
_COLUMN_NAME_T_MOMENTUM_CHANGE = "t"

# (19): "Generalized" column name for x_Bjokren:
_COLUMN_NAME_X_BJORKEN = "x_b"

# (20): "Generalized" column name for azimuthal phi angle:
_COLUMN_NAME_AZIMUTHAL_PHI = "phi"

# (21): "Generalized" column name for the real part of the CFF H:
_COLUMN_NAME_CFF_REAL_H = "Re[H]"

# (22): "Generalized" column name for the imaginary part of the CFF H:
_COLUMN_NAME_CFF_IMAG_H = "Im[H]"

# (23): "Generalized" column name for the real part of the CFF E:
_COLUMN_NAME_CFF_REAL_E = "Re[E]"

# (24): "Generalized" column name for the imaginary part of the CFF E:
_COLUMN_NAME_CFF_IMAG_E = "Im[E]"

# (25): "Generalized" column name for the real part of the CFF H-tilde:
_COLUMN_NAME_CFF_REAL_H_TILDE = "Re[Ht]"

# (26): "Generalized" column name for the imaginary part of the CFF H-tilde:
_COLUMN_NAME_CFF_IMAG_H_TILDE = "Im[Ht]"

# (27): "Generalized" column name for the real part of the CFF E-tilde:
_COLUMN_NAME_CFF_REAL_E_TILDE = "Re[Et]"

# (28): "Generalized" column name for the imaginary part of the CFF E-tilde:
_COLUMN_NAME_CFF_IMAG_E_TILDE = "Im[Et]"

# TEMPORARY!
_COLUMN_NAME_CROSS_SECTION = "sigma"
_COLUMN_NAME_CROSS_SECTION_ERROR = "sigma_stat_plus"

# (X): The string literal representing an encapsulate postscripe-type --- helpful for Overleaf!
_FIGURE_FORMAT_EPS = "eps"

# (X): The string literal representing scalable vector graphics-type images:
_FIGURE_FORMAT_SVG = "svg"

# (X): The string literal representing portable network graphics-type images:
_FIGURE_FORMAT_PNG = "png"

# (X): The string literal representing a comma-separated-values file, popular in data science:
_FILE_FORMAT_CSV = "csv"