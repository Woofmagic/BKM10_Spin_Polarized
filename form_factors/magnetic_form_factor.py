from statics.other.other import _PROTON_MAGNETIC_MOMENT

def calculate_form_factor_magnetic(
        electric_form_factor: float,
        verbose: bool= True) -> float:
    """
    Description
    --------------
    The Magnetic Form Factor is calculated immediately with
    the Electric Form Factor. They are only related by the 
    gyromagnetic ratio.

    Parameters
    --------------
    electric_form_factor: (float)

    verbose: (bool)
        Debugging console output.

    Returns
    --------------
    form_factor_magnetic : (float)
        result of the operation
    
    Notes
    --------------
    """
    
    try:

        # (1): Calculate the F_{M}:
        form_factor_magnetic = _PROTON_MAGNETIC_MOMENT * electric_form_factor

        if verbose:
            print(f"> Calculated magnetic form factor as: {form_factor_magnetic}")

        return form_factor_magnetic

    except Exception as ERROR:
        print(f"> Error in calculating magnetic form factor:\n> {ERROR}")
        return Decimal("0.0")