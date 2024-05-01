def calculate_lepton_propagator_p1(
    squared_Q_momentum_transfer: float, 
    k_dot_delta: float,
    verbose:bool = False) -> float:
    """
    Description
    --------------
    Equation (28) [first equation] divided through by
    Q^{2} according to the following paper:
    https://arxiv.org/pdf/hep-ph/0112108.pdf

    Parameters
    --------------
    k_dot_delta: (float)

    squared_Q_momentum_transfer: (float)

    verbose: (bool)
        Debugging console output.

    Notes
    --------------
    """
    try:
        p1_propagator = 1. + (2. * (k_dot_delta / squared_Q_momentum_transfer))
        
        if verbose:
            print(f"> Computed the P1 propagator to be: {p1_propagator}")

        return p1_propagator
    
    except Exception as E:
        print(f"> Error in computing p1 propagator:\n> {E}")
        return 0.