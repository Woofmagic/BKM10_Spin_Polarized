def calculate_form_factor_dirac_f1(
    magnetic_form_factor: float,
    pauli_f2_form_factor: float,
    verbose: bool = True) -> float:
    """
    Description
    --------------
    We calculate the Dirac form factor, which is
    even easier to get than the Fermi one.

    Parameters
    --------------
    magnetic_form_factor: (float)

    pauli_f2_form_factor: (float)

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
    
        # (1): Calculate the Dirac form factor:
        dirac_form_factor = magnetic_form_factor - pauli_f2_form_factor

        if verbose:
            print(f"> Calculated Dirac form factor as: {dirac_form_factor}")

        return dirac_form_factor

    except Exception as ERROR:
        print(f"> Error in calculating Dirac form factor:\n> {ERROR}")
        return 0.