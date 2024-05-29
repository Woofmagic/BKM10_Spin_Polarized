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
    """
    return (.389379 * 1000000) * number