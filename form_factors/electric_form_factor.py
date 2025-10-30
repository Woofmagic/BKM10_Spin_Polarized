from decimal import Decimal

from statics.other.other import _ELECTRIC_FORM_FACTOR_CONSTANT

def calculate_form_factor_electric(
    squared_hadronic_momentum_transfer_t: float,
    verbose: bool = False) -> float:
    """
    Calculate F_{E}.

    :param squared_hadronic_momentum_transfer_t float:

    :param verbose bool:
        Debugging console output.

    :returns: form_factor_electric
    :rtype: float

    """
    
    try:
        
        # (1): Calculate the mysterious denominator:
        denominator = 1. - (squared_hadronic_momentum_transfer_t / _ELECTRIC_FORM_FACTOR_CONSTANT)

        # (2): Calculate the F_{E}:
        form_factor_electric = 1. / (denominator**2)

        if verbose:
            print(f"> Calculated electric form factor as: {form_factor_electric}")

        return form_factor_electric

    except Exception as error:
        print(f"> Error in calculating electric form factor:\n> {error}")
        return 0.