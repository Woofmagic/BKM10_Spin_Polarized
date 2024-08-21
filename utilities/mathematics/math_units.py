try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")


def convert_degrees_to_radians(degrees: float) -> float:
    """
    Converts a number in degrees (0-360) to radians
    using the standard formula.
    """
    return (degrees * np.pi / 180.)

def convert_to_nb_over_GeV4(number: float) -> float:
    """
    # Title: `convert_to_nb_over_GeV4`

    ## Description:
    Convert a number in units of GeV^{-6} to nb/GeV^{4}. For reference,
    the number is 389379 or about 3.9e6 (= 4.0e6), and it is 
    multiplied by whatever `number` is passed in.

    ## Arguments:

        1. number (float)

    ## Returns:

        1. number_in_nb_over_GeV4 (float)
    """
    _CONVERSION_FACTOR = .389379 * 1000000
    number_in_nb_over_GeV4 = _CONVERSION_FACTOR * number
    return number_in_nb_over_GeV4