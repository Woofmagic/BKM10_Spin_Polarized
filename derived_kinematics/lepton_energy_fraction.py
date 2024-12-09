from decimal import Decimal

try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_kinematics_lepton_energy_fraction_y(
    squared_Q_momentum_transfer: float, 
    lab_kinematics_k: float,
    epsilon: float, 
    verbose: bool = False) -> float:
    """
    Description
    --------------
    Calculate y, which measures the lepton energy fraction.
    y^{2} := \frac{ \sqrt{Q^{2}} }{ \sqrt{\epsilon^{2}} k }

    Parameters
    --------------
    epsilon: (float)
        derived kinematics

    squared_Q_momentum_transfer: (float)
        Q^{2} momentum transfer to the hadron

    lab_kinematics_k: (float)
        lepton momentum loss

    verbose: (bool)
        Debugging console output.

    Notes
    --------------

    """
    try:

        # (1): Calculate the y right away:
        lepton_energy_fraction_y = squared_Q_momentum_transfer.sqrt() / (epsilon * lab_kinematics_k)

        # (1.1): If verbose output, then print the result:
        if verbose:
            print(f"> Calculated y to be:\n{lepton_energy_fraction_y}")

        # (2): Return the calculation:
        return lepton_energy_fraction_y
    
    except Exception as ERROR:
        print(f"> Error in computing lepton_energy_fraction_y:\n> {ERROR}")
        return Decimal("0.0")