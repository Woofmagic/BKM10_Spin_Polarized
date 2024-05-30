def compute_cff_effective(
    skewness_parameter: float,
    compton_form_factor: float,
    verbose: bool = True) -> float:
    """
    Description
    --------------
    The CFF_{effective} is not actually easy to compute, but
    we are going to pretend it is and compute it as below. (All
    it needs is the skewness parameter.)

    Parameters
    --------------
    skewness_parameter: (float)

    compton_form_factor: (flaot)

    verbose: (bool)
        Debugging console output.

    Returns
    --------------
    cff_effective : (float)
        the effective CFF
    
    Notes
    --------------
    """

    try:

        # (1): Do the calculation in one line:
        cff_effective = -2. * skewness_parameter * compton_form_factor / (1. + skewness_parameter)

        # (1.1): If verbose, log the output:
        if verbose:
            print(f"> Computed the CFF effective to be:\n{cff_effective}")

        # (2): Return the output:
        return cff_effective

    except Exception as ERROR:
        print(f"> Error in calculating F_effective:\n> {ERROR}")
        return 0.