from statics.other.other import _ELECTRIC_FORM_FACTOR_CONSTANT

def calculate_form_factor_electric(
    squared_hadronic_momentum_transfer_t: float,
    verbose: bool = True) -> float:
    """
    Description
    --------------
    The Electric Form Factor is quite mysterious still...
    Where the fuck do these numbers come from?

    Parameters
    --------------
    squared_hadronic_momentum_transfer_t: (float)

    verbose: (bool)
        Debugging console output.

    Returns
    --------------
    form_factor_electric : (float)
        result of the operation
    
    Notes
    --------------
    """
    
    try:
        
        # (1): Calculate the mysterious denominator:
        denominator = 1. - (squared_hadronic_momentum_transfer_t / _ELECTRIC_FORM_FACTOR_CONSTANT)

        # (2): Calculate the F_{E}:
        form_factor_electric = 1. / (denominator**2)

        if verbose:
            print(f"> Calculated electric form factor as: {form_factor_electric}")

        return form_factor_electric

    except Exception as ERROR:
        print(f"> Error in calculating electric form factor:\n> {ERROR}")
        return 0.