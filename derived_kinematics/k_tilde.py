try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install NumPy to use this script.")

def calculate_kinematics_k_tilde(
    squared_Q_momentum_transfer: float, 
    x_Bjorken: float,
    lepton_energy_fraction_y: float,
    squared_hadronic_momentum_transfer_t: float,
    epsilon: float, 
    squared_hadronic_momentum_transfer_t_minimum: float,
    verbose: bool = True) -> float:
    """
    Description
    --------------

    Parameters
    --------------
    epsilon: (float)

    squared_Q_momentum_transfer: (float)

    x_Bjorken: (float)

    lepton_energy_fraction_y: (float)

    squared_hadronic_momentum_transfer_t: (float)

    squared_hadronic_momentum_transfer_t_minimum: (float)

    verbose: (bool)
        Debugging console output.

    Returns
    --------------
    k_tilde : (float)
        result of the operation
    
    Notes
    --------------
    """
    
    try:

        # (1): Calculate recurring quantity t_{min} - t
        tmin_minus_t = squared_hadronic_momentum_transfer_t_minimum - squared_hadronic_momentum_transfer_t

        # (2): Calculate the duplicate quantity 1 - x_{B}
        one_minus_xb = 1. - x_Bjorken

        # (3): Calculate the crazy root quantity:
        second_root_quantity = (one_minus_xb * np.sqrt(1. + epsilon**2)) + ((tmin_minus_t * (epsilon**2 + (4. * one_minus_xb * x_Bjorken))) / (4. * squared_Q_momentum_transfer))
    
        # (4): Calculate the first annoying root quantity:
        first_root_quantity = np.sqrt(1. - lepton_energy_fraction_y - lepton_energy_fraction_y**2 * epsilon**2 / 4.)

        # (5): Calculate the second annoying root quantity:
        second_root_quantity = np.sqrt(1. - lepton_energy_fraction_y + lepton_energy_fraction_y**2 * epsilon**2 / 4.)
        
        # (6): Calculate K_tilde
        k_tilde = np.sqrt(tmin_minus_t) * np.sqrt(second_root_quantity) * first_root_quantity / second_root_quantity

        # (6.1): Print the result of the calculation:
        if verbose:
            print(f"> Calculated k_tilde to be:\n{k_tilde}")

        # (7) Return:
        return k_tilde

    except Exception as ERROR:
        print(f"> Error in calculating K_tilde:\n> {ERROR}")
        return 0.