def calculate_kinematics_t_prime(
    squared_hadronic_momentum_transfer_t: float,
    squared_hadronic_momentum_transfer_t_minimum: float,
    verbose: bool = False) -> float:
    """
    Description
    --------------
    Calculate t prime.

    Parameters
    --------------
    squared_hadronic_momentum_transfer_t: (float)

    squared_hadronic_momentum_transfer_t_minimum: (float)

    verbose: (float)

    Returns
    --------------
    t_prime: (float)

    Notes
    --------------
    """
    try:

        # (1): Obtain the t_prime immediately
        t_prime = squared_hadronic_momentum_transfer_t - squared_hadronic_momentum_transfer_t_minimum

        # (1.1): If verbose, print the result:
        if verbose:
            print(f"> Calculated t prime to be:\n{t_prime}")

        # (2): Return t_prime
        return t_prime

    except Exception as ERROR:
        print(f"> Error calculating t_prime:\n> {ERROR}")
        return 0.