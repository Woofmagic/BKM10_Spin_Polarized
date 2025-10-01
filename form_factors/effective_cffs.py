"""
## Description: 
Provides a simple script that computes F_{eff}: the effective from factor.

## Notes:
1. 2025/09/01: Initiated some clean-up on these scripts.
"""

def compute_cff_effective(
    skewness_parameter: float,
    compton_form_factor: complex,
    use_ww: bool = False,
    verbose: bool = False) -> complex:
    """
    ## Description:
    The CFF_{effective} is not actually easy to compute, but
    we are going to pretend it is and compute it as below. (All
    it needs is the skewness parameter and the WW conditon on or off.)

    :param float skewness_parameter:

    :param complex compton_form_factor:

    :param bool verbose:
        Debugging console output.

    :returns: cff_effective (float): The effective CFF.
    
    ## Notes:
    None!
    """

    # (1): Initiate a try/except block:
    try:

        # (1.1): If the WW relations are on...
        if use_ww:

            # (1.1.1): ... compute F_{eff} using the prescribed formula:
            cff_effective = 2. * compton_form_factor / (1. + skewness_parameter)
        
        # (1.2): If the WW relations are off...
        else:

            # (1.2.1): ... compute F_{eff} according to a different formula:
            cff_effective = -2. * skewness_parameter * compton_form_factor / (1. + skewness_parameter)

        # (1.3): If verbose, log the output:
        if verbose:
            print(f"> Computed the CFF effective to be:\n{cff_effective}")

        # (1.4): Return the output:
        return cff_effective

    # (2): If there's a problem in computing F_{eff}...
    except Exception as ERROR:

        # (2.1): ... tell the user that this happened:
        print(f"> Error in calculating F_effective:\n> {ERROR}")

        # (2.2): And freak out and return 0:
        return 0.
    
def compute_cff_transverse(
    compton_form_factor: float,
    verbose: bool = False) -> float:
    """
    ## Description: 
    Calculates what is called $\mathcal{F}_{T}$: the transverse Compton Form Factors.

    :param complex compton_form_factor:

    :param bool verbose:
        Debugging console output.
    
    :returns: ???

    ## Notes:
    """
    return compton_form_factor