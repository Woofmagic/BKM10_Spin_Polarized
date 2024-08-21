from statics.masses.particle_masses import _MASS_OF_PROTON_IN_GEV

def calculate_form_factor_pauli_f2(
    squared_hadronic_momentum_transfer_t: float,
    electric_form_factor: float,
    magnetic_form_factor: float,
    verbose: bool = False) -> float:
    """
    Description
    --------------
    We calculate the Pauli form factor, which is just a
    particular linear combination of the electromagnetic
    form factors.

    Parameters
    --------------
    squared_hadronic_momentum_transfer_t: (float)

    electric_form_factor: (float)

    magnetic_form_factor: (float)

    verbose: (bool)
        Debugging console output.

    Returns
    --------------
    pauli_form_factor : (float)
        result of the operation
    
    Notes
    --------------
    """
    
    try:

        # (1): Calculate tau:
        tau = -1. * squared_hadronic_momentum_transfer_t / (4. * _MASS_OF_PROTON_IN_GEV**2)

        # (2): Calculate the numerator:
        numerator = magnetic_form_factor - electric_form_factor

        # (3): Calculate the denominator:
        denominator = 1. + tau
    
        # (4): Calculate the Pauli form factor:
        pauli_form_factor = numerator / denominator

        if verbose:
            print(f"> Calculated Fermi form factor as: {pauli_form_factor}")

        return pauli_form_factor

    except Exception as ERROR:
        print(f"> Error in calculating Fermi form factor:\n> {ERROR}")
        return 0.