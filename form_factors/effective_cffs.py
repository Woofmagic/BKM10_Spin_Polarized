from decimal import Decimal

def compute_cff_effective(
    skewness_parameter: float,
    compton_form_factor: complex,
    use_ww: bool = False,
    verbose: bool = False) -> complex:
    """
    ## Description:
    The CFF_{effective} is not actually easy to compute, but
    we are going to pretend it is and compute it as below. (All
    it needs is the skewness parameter.)

    ## Arguments:

        skewness_parameter: (float)

        compton_form_factor: (complex)

        verbose: (bool)
            Debugging console output.

    ## Returns:

        cff_effective : (float)
            the effective CFF
    
    ## Notes:
    """

    try:

        # (1): Do the calculation in one line:
        if use_ww:
            cff_effective = 2. * compton_form_factor / (1. + skewness_parameter)
        else:
            cff_effective = -2. * skewness_parameter * compton_form_factor / (1. + skewness_parameter)

        # (1.1): If verbose, log the output:
        if verbose:
            print(f"> Computed the CFF effective to be:\n{cff_effective}")

        # (2): Return the output:
        return cff_effective

    except Exception as ERROR:
        print(f"> Error in calculating F_effective:\n> {ERROR}")
        return 0.
    
def compute_cff_transverse(
    compton_form_factor: float,
    verbose: bool = False) -> float:
    """
    # Title: `compute_cff_transverse`

    ## Description: 
    Calculates what is called $\mathcal{F}_{T}$: the transverse
    Compton Form Factors.

    ## Arguments:

        compton_form_factor: (float)

        verbose: (bool)
            Debugging console output.
    
    ## Returns:
    NOT KNOWN YET
    """
    return compton_form_factor