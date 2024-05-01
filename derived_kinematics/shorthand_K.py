try:
    import numpy as np
except ImportError:
    print("> NumPy is not installed. Please install NumPy to use this script.") 

def calculate_kinematics_k(
    squared_Q_momentum_transfer: float, 
    lepton_energy_fraction_y: float,
    epsilon: float,
    k_tilde: float,
    verbose: bool = True) -> float:
    """
    """

    try:

        # (1): Calculate the amazing prefactor:
        prefactor = np.sqrt((1. - lepton_energy_fraction_y + (epsilon**2 * lepton_energy_fraction_y**2 / 4.)) / squared_Q_momentum_transfer)

        # (2): Calculate the remaining part of the term:
        kinematic_k = prefactor * k_tilde

        # (2.1); If verbose, log the output:
        if verbose:
            print(f"> Calculated kinematic K to be: {kinematic_k}")

        # (3): Return the value:
        return kinematic_k

    except Exception as ERROR:
        print(f"> Error in calculating derived kinematic K:\n> {ERROR}")
        return 0.