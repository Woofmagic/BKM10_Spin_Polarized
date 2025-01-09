import math
from decimal import Decimal

import numpy as np

# Statics | EM Coupling
from statics.couplings.couplings import _ELECTROMAGNETIC_FINE_STRUCTURE_CONSTANT

def calculate_bkm10_cross_section_prefactor(
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    epsilon: float, 
    lepton_energy_fraction_y: float, 
    verbose: bool = False) -> float:
    """
    Description
    --------------

    Parameters
    --------------
    squared_Q_momentum_transfer: (float)

    x_Bjorken: (float)

    epsilon: (float)

    lepton_energy_fraction_y: (float)

    verbose: (bool)
        Debugging console output.


    Notes
    --------------
    """

    try:

        # (1): Calculate the numerator of the prefactor
        numerator = _ELECTROMAGNETIC_FINE_STRUCTURE_CONSTANT**3 * lepton_energy_fraction_y**2 * x_Bjorken

        # (2): Calculate the denominator of the prefactor:
        denominator = Decimal("8. ") * Decimal(math.pi) * squared_Q_momentum_transfer**2 * (Decimal("1.") + epsilon**2).sqrt()

        # (3): Construct the prefactor:
        prefactor = numerator / denominator

        if verbose:
            print(f"> Calculated BKM10 cross-section prefactor to be:\n{prefactor}")

        # (4): Return the prefactor:
        return prefactor

    except Exception as ERROR:
        print(f"> Error calculating BKM10 cross section prefactor:\n> {ERROR}")
        return 0