from decimal import Decimal

def calculate_lepton_propagator_p2(
    squared_Q_momentum_transfer: float, 
    squared_hadronic_momentum_transfer_t: float,
    k_dot_delta: float,
    verbose: bool = False) -> float:
    """
    Description
    --------------
    Equation (28) [second equation] divided through by
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
        p2_propagator = (-Decimal("2.") * (k_dot_delta / squared_Q_momentum_transfer)) + (squared_hadronic_momentum_transfer_t / squared_Q_momentum_transfer)
        
        if verbose:
            print(f"> Computed the P2 propagator to be:\n{p2_propagator}")

        return p2_propagator
    
    except Exception as E:
        print(f"> Error in computing p2 propagator:\n> {E}")
        return Decimal("0.0")