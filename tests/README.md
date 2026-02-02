

All of the numbers that we compare against are found in the Mathematica notebook entitled `bkm10_test.nb`, which is under `/mathematica/bkm10_test.nb`.


## Test File: `test_derived_quantites.py`

Tests $\epsilon$, $y$, $x_{\text{B}}$, $\xi$, $t_{\text{min}}$, $t'$, and $\tilde{K}$.

Last verified: 20260121

## Test File: `test_form_factors.py`

Tests the operation of computing effective form factors ($\mathcal{F}_{\text{eff}}$). Pretty straightforward.

Last verified: 20260121

## Test File: `test_bh_coefficients.py`

Tests $c_{0}^{\text{BH}}$, $c_{1}^{\text{BH}}$, and $s_{1}^{\text{BH}}$; tests $c_{0, \text{LP}}^{\text{BH}}$, $c_{1, \text{LP}}^{\text{BH}}$, and $s_{1, \text{LP}}^{\text{BH}}$.

Last verified: 20260121.

## Test File: `test_dvcs_coefficients.py`

Tests $c_{0}^{\text{DVCS}}$, $c_{1}^{\text{DVCS}}$, and $s_{1}^{\text{DVCS}}$; tests $c_{0, \text{LP}}^{\text{DVCS}}$, $c_{1, \text{LP}}^{\text{DVCS}}$, and $s_{1, \text{LP}}^{\text{DVCS}}$.

Last verified: 20260201.        

## Test File: `test_curly_c_unp_series.py`

Tests the three main "curly C" cofficients $\mathcal{C}^{I}_{\text{unp}}(\mathcal{F})$, $\mathcal{C}^{I, V}_{\text{unp}}(\mathcal{F})$, and $\mathcal{C}^{I, A}_{\text{unp}}(\mathcal{F})$, but does it for all possible combinations of CFFs: $\mathcal{F}$ with and without the WW-relations, and t hen $\mathcal{F}_{\text{eff}}$. Note that is it only $\mathcal{F}_{\text{eff}}$ that requires deciding if WW-relations are on or off, so the total number of possible tests here is 9, not 12.

Last verified: 20260121