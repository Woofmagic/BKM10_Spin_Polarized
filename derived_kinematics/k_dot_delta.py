from decimal import Decimal
import math
from utilities.mathematics.trigonometric import cos

import numpy as np

# Helper Modules | Convert Degrees to Radians
from utilities.mathematics.math_units import convert_degrees_to_radians

def calculate_k_dot_delta(
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float, 
    squared_hadronic_momentum_transfer_t: float,
    azimuthal_phi: float,
    epsilon: float, 
    lepton_energy_fraction_y: float,
    kinematic_k: float,
    verbose: bool = False):
    """
    Description
    --------------
    Equation (29) in the BKM Formalism, available
    at this link: https://arxiv.org/pdf/hep-ph/0112108.pdf

    Parameters
    --------------
    kinematic_k: (float)
    
    epsilon: (float)

    squared_Q_momentum_transfer: (float)

    x_Bjorken: (float)

    lepton_energy_fraction_y: (float)

    squared_hadronic_momentum_transfer_t: (float)

    azimuthal_phi: (float)

    verbose: (bool)
        Debugging console output.

    Returns
    --------------
    k_dot_delta_result : (float)
        result of the operation
    
    Notes
    --------------
    (1): k-dot-delta shows up in computing the lepton
        propagators. It is Eq. (29) in the following
        paper: https://arxiv.org/pdf/hep-ph/0112108.pdf
    """

    try:
    
        # (1): The prefactor: \frac{Q^{2}}{2 y (1 + \varepsilon^{2})}
        prefactor = squared_Q_momentum_transfer / (Decimal("2.") * lepton_energy_fraction_y * (Decimal("1.") + epsilon**2))

        # (2): Second term in parentheses: Phi-Dependent Term: 2 K cos(\phi)
        phi_dependence = Decimal("2.") * kinematic_k * cos(Decimal(math.pi) - convert_degrees_to_radians(azimuthal_phi))
        
        # (3): Prefactor of third term in parentheses: \frac{t}{Q^{2}}
        ratio_delta_to_q_squared = squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer

        # (4): Second term in the third term's parentheses: x_{B} (2 - y)
        bjorken_scaling = x_Bjorken * (Decimal("2.") - lepton_energy_fraction_y)

        # (5): Third term in the third term's parentheses: \frac{y \varepsilon^{2}}{2}
        ratio_y_epsilon = lepton_energy_fraction_y * epsilon**2 / Decimal("2.0")

        # (6): Adding up all the "correction" pieces to the prefactor, written as (1 + correction)
        correction = phi_dependence - (ratio_delta_to_q_squared * (Decimal("1.") - bjorken_scaling + ratio_y_epsilon)) + (ratio_y_epsilon)

        # (7): Writing it explicitly as "1 + correction"
        in_parentheses = Decimal("1.") + correction

        # (8): The actual equation:
        k_dot_delta_result = Decimal("-1.0") * prefactor * in_parentheses

        # (8.1): If verbose, print the output:
        if verbose:
            print(f"> Calculated k dot delta: {k_dot_delta_result}")

        # (9): Return the number:
        return k_dot_delta_result
    
    except Exception as E:
        print(f"> Error in calculating k.Delta:\n> {E}")
        return Decimal("0.0")