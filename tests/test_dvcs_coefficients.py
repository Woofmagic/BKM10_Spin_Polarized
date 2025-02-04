import unittest

from coefficients.dvcs_coefficients.unpolarized.bkm10.unpolarized_curlyC_dvcs import calculate_curly_c_unpolarized_dvcs
from coefficients.dvcs_coefficients.unpolarized.bkm10.unpolarized_c0_dvcs import calculate_c_0_unpolarized_dvcs
from coefficients.dvcs_coefficients.unpolarized.bkm10.unpolarized_c1_dvcs import calculate_c_1_unpolarized_dvcs
from coefficients.dvcs_coefficients.unpolarized.bkm10.unpolarized_s1_dvcs import calculate_s_1_unpolarized_dvcs

from coefficients.dvcs_coefficients.lp_polarized.bkm10.lp_polarized_curlyC_dvcs import calculate_curly_c_longitudinally_polarized_dvcs
from coefficients.dvcs_coefficients.lp_polarized.bkm10.lp_polarized_c0_dvcs import calculate_c_0_longitudinally_polarized_dvcs
from coefficients.dvcs_coefficients.lp_polarized.bkm10.lp_polarized_c1_dvcs import calculate_c_1_longitudinally_polarized_dvcs
from coefficients.dvcs_coefficients.lp_polarized.bkm10.lp_polarized_s1_dvcs import calculate_s_1_longitudinally_polarized_dvcs

from form_factors.effective_cffs import compute_cff_effective

_TEST_LEPTON_POLARIZATION = 0.5
_TEST_TARGET_POLARIZATION = 1.0

_TEST_SQUARED_Q_MOMENTUM_TRANSFER = 1.82
_TEST_X_BJORKEN = 0.34
_TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER = -0.17

_TEST_EPSILON = 0.47293561004973345
_TEST_LEPTON_ENERGY_FRACTION = 0.49609612355928445
_TEST_K_TILDE = 0.1592415651944438
_TEST_SHORTHAND_K = 0.08492693191323883
_TEST_T_PRIME = -0.034481755270847486

_TEST_VERBOSE = False

_TEST_SKEWNESS = 0.19906188837146524

_TEST_CFF_REAL_H = -0.897
_TEST_CFF_REAL_H_TILDE = 2.444
_TEST_CFF_REAL_E = -0.541
_TEST_CFF_REAL_E_TILDE = 2.207

_TEST_CFF_IMAGINARY_H = 2.421
_TEST_CFF_IMAGINARY_H_TILDE = 1.131
_TEST_CFF_IMAGINARY_E = 0.903
_TEST_CFF_IMAGINARY_E_TILDE = 5.383

_TEST_CFF_H = complex(_TEST_CFF_REAL_H, _TEST_CFF_IMAGINARY_H)
_TEST_CFF_H_TILDE = complex(_TEST_CFF_REAL_H_TILDE, _TEST_CFF_IMAGINARY_H_TILDE)
_TEST_CFF_E = complex(_TEST_CFF_REAL_E, _TEST_CFF_IMAGINARY_E)
_TEST_CFF_E_TILDE = complex(_TEST_CFF_REAL_E_TILDE, _TEST_CFF_IMAGINARY_E_TILDE)

_TEST_VERBOSE = False

class TestDVCSCoefficients(unittest.TestCase):

    def test_calculate_curly_c_unpolarized_dvcs_normal_cffs(self):
        """
        ## Description: Test curlyC(F, F*)
        This is curly C DVCS for the unpolarized case. Please note what is being passed in as arguments!
        Notice that we're evaluating CurlyC(F, F*), not any effective stuff!
        """
        self.assertAlmostEqual(
            calculate_curly_c_unpolarized_dvcs(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_CFF_H,
                _TEST_CFF_H_TILDE,
                _TEST_CFF_E,
                _TEST_CFF_E_TILDE,
                _TEST_CFF_H.conjugate(),
                _TEST_CFF_H_TILDE.conjugate(),
                _TEST_CFF_E.conjugate(),
                _TEST_CFF_E_TILDE.conjugate(),
                _TEST_VERBOSE),
            complex(13.478125253553266, 0.))

    def test_calculate_curly_c_unpolarized_dvcs_effective_cffs_ww_off(self):
        """
        ## Description: Test curlyC(F_eff, F*_eff) *without* the WW Relations!
        This is curly C DVCS for the unpolarized case. Please note what is being passed in as arguments!
        Notice that we're evaluating CurlyC(Feff, Feff*).
        """
        self.assertAlmostEqual(
            calculate_curly_c_unpolarized_dvcs(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H, use_ww = False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE, use_ww = False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E, use_ww = False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E_TILDE, use_ww = False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H.conjugate(), use_ww = False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE.conjugate(), use_ww = False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E.conjugate(), use_ww = False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E_TILDE.conjugate(), use_ww = False),
                _TEST_VERBOSE), 
            complex(1.485875835353519, 7.91929098021258e-20))
        
    def test_calculate_curly_c_unpolarized_dvcs_effective_cffs_ww_on(self):
        """
        ## Description: Test curlyC(F_eff, F*_eff) *using* the WW Relations!
        This is curly C DVCS for the unpolarized case. Please note what is being passed in as arguments!
        Notice that we're evaluating CurlyC(Feff, Feff*).
        """
        self.assertAlmostEqual(
            calculate_curly_c_unpolarized_dvcs(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H, use_ww = True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE, use_ww = True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E, use_ww = True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E_TILDE, use_ww = True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H.conjugate(), use_ww = True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE.conjugate(), use_ww = True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E.conjugate(), use_ww = True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E_TILDE.conjugate(), use_ww = True),
                _TEST_VERBOSE),
            complex(37.49784250218004, 0.))

    def test_calculate_curly_c_unpolarized_dvcs_mixed_cffs_ww_off(self):
        """
        ## Description: Test curlyC(F_eff, F*) *without* the WW Relations!
        This is curly C DVCS for the unpolarized case. Please note what is being passed in as arguments!
        Notice that we're evaluating CurlyC(Feff, F*).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_curly_c_unpolarized_dvcs(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H, use_ww = False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE, use_ww = False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E, use_ww = False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E_TILDE, use_ww = False),
                _TEST_CFF_H.conjugate(),
                _TEST_CFF_H_TILDE.conjugate(),
                _TEST_CFF_E.conjugate(),
                _TEST_CFF_E_TILDE.conjugate(),
                _TEST_VERBOSE), 
            complex(-4.475133586846634, -1.88800852032242e-17))
        
    def test_calculate_curly_c_unpolarized_dvcs_mixed_cffs_ww_on(self):
        """
        ## Description: Test curlyC(F_eff, F*) *using* the WW Relations!
        This is curly C DVCS for the unpolarized case. Please note what is being passed in as arguments!
        Notice that we're evaluating CurlyC(Feff, F*).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_curly_c_unpolarized_dvcs(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H, use_ww = True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE, use_ww = True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E, use_ww = True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E_TILDE, use_ww = True),
                _TEST_CFF_H.conjugate(),
                _TEST_CFF_H_TILDE.conjugate(),
                _TEST_CFF_E.conjugate(),
                _TEST_CFF_E_TILDE.conjugate(),
                _TEST_VERBOSE),
            complex(22.481116920259893, 5.604782843278753e-16))
        
    def test_calculate_c_0_unpolarized_dvcs_no_ww(self):
        """
        ## Description: Testing c_{0, unp}^{DVCS} *without* WW relations.
        This is the first c coefficient that enters into the DVCS mode expansions, c_{0, unp}^{DVCS}.
        """
        self.assertAlmostEqual(
            calculate_c_0_unpolarized_dvcs(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SKEWNESS,
                _TEST_SHORTHAND_K,
                complex(_TEST_CFF_REAL_H, _TEST_CFF_IMAGINARY_H),
                complex(_TEST_CFF_REAL_H_TILDE, _TEST_CFF_IMAGINARY_H_TILDE),
                complex(_TEST_CFF_REAL_E, _TEST_CFF_IMAGINARY_E),
                complex(_TEST_CFF_REAL_E_TILDE, _TEST_CFF_IMAGINARY_E_TILDE),
                False,
                _TEST_VERBOSE),
            complex(28.27982414922643, 2.7102998542967846e-21))
        
    def test_calculate_c_0_unpolarized_dvcs_ww_on(self):
        """
        ## Description: Testing c_{0, unp}^{DVCS} *using* WW relations.
        This is the first c coefficient that enters into the DVCS mode expansions, c_{0, unp}^{DVCS}.
        """
        self.assertAlmostEqual(
            calculate_c_0_unpolarized_dvcs(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SKEWNESS,
                _TEST_SHORTHAND_K,
                complex(_TEST_CFF_REAL_H, _TEST_CFF_IMAGINARY_H),
                complex(_TEST_CFF_REAL_H_TILDE, _TEST_CFF_IMAGINARY_H_TILDE),
                complex(_TEST_CFF_REAL_E, _TEST_CFF_IMAGINARY_E),
                complex(_TEST_CFF_REAL_E_TILDE, _TEST_CFF_IMAGINARY_E_TILDE),
                True,
                _TEST_VERBOSE),
            complex(29.512298473681934, 0.))
        
    def test_calculate_c_1_unpolarized_dvcs_no_ww(self):
        """
        ## Description: Testing c_{1, unp}^{DVCS} *without* the WW relations.
        This is the second c coefficient that enters into the DVCS mode expansions, c_{1, unp}^{DVCS}.
        """
        self.assertAlmostEqual(
            calculate_c_1_unpolarized_dvcs(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SKEWNESS,
                _TEST_SHORTHAND_K,
                complex(_TEST_CFF_REAL_H, _TEST_CFF_IMAGINARY_H),
                complex(_TEST_CFF_REAL_H_TILDE, _TEST_CFF_IMAGINARY_H_TILDE),
                complex(_TEST_CFF_REAL_E, _TEST_CFF_IMAGINARY_E),
                complex(_TEST_CFF_REAL_E_TILDE, _TEST_CFF_IMAGINARY_E_TILDE),
                False,
                _TEST_VERBOSE), 
            -2.2510740484250977)
        
    def test_calculate_c_1_unpolarized_dvcs_ww_on(self):
        """
        ## Description: Testing c_{1, unp}^{DVCS} *using* the WW relations.
        This is the second c coefficient that enters into the DVCS mode expansions, c_{1, unp}^{DVCS}.
        """
        self.assertAlmostEqual(
            calculate_c_1_unpolarized_dvcs(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SKEWNESS,
                _TEST_SHORTHAND_K,
                complex(_TEST_CFF_REAL_H, _TEST_CFF_IMAGINARY_H),
                complex(_TEST_CFF_REAL_H_TILDE, _TEST_CFF_IMAGINARY_H_TILDE),
                complex(_TEST_CFF_REAL_E, _TEST_CFF_IMAGINARY_E),
                complex(_TEST_CFF_REAL_E_TILDE, _TEST_CFF_IMAGINARY_E_TILDE),
                True,
                _TEST_VERBOSE), 
            11.308413010854267)
    
    def test_calculate_s_1_unpolarized_dvcs_no_ww(self):
        """
        ## Description: Testing s_{1, unp}^{DVCS} *without* the WW relations.
        This is the first s coefficient that enters into the DVCS mode expansions, s_{1, unp}^{DVCS}.
        """
        self.assertAlmostEqual(
            calculate_s_1_unpolarized_dvcs(
                _TEST_LEPTON_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SKEWNESS,
                _TEST_SHORTHAND_K,
                complex(_TEST_CFF_REAL_H, _TEST_CFF_IMAGINARY_H),
                complex(_TEST_CFF_REAL_H_TILDE, _TEST_CFF_IMAGINARY_H_TILDE),
                complex(_TEST_CFF_REAL_E, _TEST_CFF_IMAGINARY_E),
                complex(_TEST_CFF_REAL_E_TILDE, _TEST_CFF_IMAGINARY_E_TILDE),
                False,
                _TEST_VERBOSE), 
            1.732747591893179e-18)
        
    def test_calculate_s_1_unpolarized_dvcs_ww_on(self):
        """
        ## Description: Testing s_{1, unp}^{DVCS} *using* the WW relations.
        This is the first s coefficient that enters into the DVCS mode expansions, s_{1, unp}^{DVCS}.
        """
        self.assertAlmostEqual(
            calculate_s_1_unpolarized_dvcs(
                _TEST_LEPTON_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SKEWNESS,
                _TEST_SHORTHAND_K,
                complex(_TEST_CFF_REAL_H, _TEST_CFF_IMAGINARY_H),
                complex(_TEST_CFF_REAL_H_TILDE, _TEST_CFF_IMAGINARY_H_TILDE),
                complex(_TEST_CFF_REAL_E, _TEST_CFF_IMAGINARY_E),
                complex(_TEST_CFF_REAL_E_TILDE, _TEST_CFF_IMAGINARY_E_TILDE),
                True,
                _TEST_VERBOSE), 
            -5.143871900068003e-17)

    def test_calculate_curly_c_longitudinally_polarized_dvcs_normal_cffs(self):
        """
        ## Description: Test curlyC_{LP}}(F, F^{*})
        This is curly C DVCS for the LP case. Please note what is being passed in as arguments!
        Notice that we're evaluating CurlyC(F, F*), not any effective stuff!
        """
        self.assertAlmostEqual(
            calculate_curly_c_longitudinally_polarized_dvcs(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_CFF_H,
                _TEST_CFF_H_TILDE,
                _TEST_CFF_E,
                _TEST_CFF_E_TILDE,
                _TEST_CFF_H.conjugate(),
                _TEST_CFF_H_TILDE.conjugate(),
                _TEST_CFF_E.conjugate(),
                _TEST_CFF_E_TILDE.conjugate(),
                _TEST_VERBOSE),
            complex(0.3052889600009992, 0.))
    
    def test_calculate_curly_c_longitudinally_polarized_dvcs_effective_cffs_no_ww(self):
        """
        ## Description: Test curlyC_{LP}}(F_{eff}, F^{*}) *without* the WW relations.
        This is curly C DVCS for the LP case. Please note what is being passed in as arguments!
        Notice that we're evaluating CurlyC(F_{eff}, F*), so there's an asymmetry there!
        """
        self.assertAlmostEqual(
            calculate_curly_c_longitudinally_polarized_dvcs(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H, use_ww = False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE, use_ww = False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E, use_ww = False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E_TILDE, use_ww = False),
                _TEST_CFF_H.conjugate(),
                _TEST_CFF_H_TILDE.conjugate(),
                _TEST_CFF_E.conjugate(),
                _TEST_CFF_E_TILDE.conjugate(),
                _TEST_VERBOSE),
            complex(-0.10136490445759658, 4.6168131193724e-16))
        
    def test_calculate_curly_c_longitudinally_polarized_dvcs_effective_cffs_ww_on(self):
        """
        ## Description: Test curlyC_{LP}}(F_{eff}, F^{*}) *using* the WW relations.
        This is curly C DVCS for the LP case. Please note what is being passed in as arguments!
        Notice that we're evaluating CurlyC(F_{eff}, F*), so there's an asymmetry there!
        """
        self.assertAlmostEqual(
            calculate_curly_c_longitudinally_polarized_dvcs(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H, use_ww = True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE, use_ww = True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E, use_ww = True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E_TILDE, use_ww = True),
                _TEST_CFF_H.conjugate(),
                _TEST_CFF_H_TILDE.conjugate(),
                _TEST_CFF_E.conjugate(),
                _TEST_CFF_E_TILDE.conjugate(),
                _TEST_VERBOSE),
            complex(0.5092130155444017, -1.8499274535682393e-15))
    
    def test_calculate_c_0_longitudinally_polarized_dvcs_no_ww(self):
        """
        ## Description: Test the function that computes c_{0, LP}^{DVCS} *without* WW relations.
        This is the first c coefficient that enters into the DVCS mode expansions, c_{0, LP}^{DVCS}.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_longitudinally_polarized_dvcs(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                complex(_TEST_CFF_REAL_H, _TEST_CFF_IMAGINARY_H),
                complex(_TEST_CFF_REAL_H_TILDE, _TEST_CFF_IMAGINARY_H_TILDE),
                complex(_TEST_CFF_REAL_E, _TEST_CFF_IMAGINARY_E),
                complex(_TEST_CFF_REAL_E_TILDE, _TEST_CFF_IMAGINARY_E_TILDE),
                False,
                _TEST_VERBOSE),
            0.2059041946153708)
        
    def test_calculate_c_0_longitudinally_polarized_dvcs_ww_on(self):
        """
        ## Description: Test the function that computes c_{0, LP}^{DVCS} *using* the WW relations.
        This is the first c coefficient that enters into the DVCS mode expansions, c_{0, LP}^{DVCS}.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_longitudinally_polarized_dvcs(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                complex(_TEST_CFF_REAL_H, _TEST_CFF_IMAGINARY_H),
                complex(_TEST_CFF_REAL_H_TILDE, _TEST_CFF_IMAGINARY_H_TILDE),
                complex(_TEST_CFF_REAL_E, _TEST_CFF_IMAGINARY_E),
                complex(_TEST_CFF_REAL_E_TILDE, _TEST_CFF_IMAGINARY_E_TILDE),
                True,
                _TEST_VERBOSE),
            0.2059041946153708)
    
    def test_calculate_c_1_longitudinally_polarized_dvcs_no_ww(self):
        """
        ## Description: Test the function computing c_{1, LP}^{DVCS} *without* WW relations.
        This is the second c coefficient that enters into the DVCS mode expansions, c_{1, LP}^{DVCS}.
        """
        self.assertAlmostEqual(
            calculate_c_1_longitudinally_polarized_dvcs(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SKEWNESS,
                _TEST_SHORTHAND_K,
                complex(_TEST_CFF_REAL_H, _TEST_CFF_IMAGINARY_H),
                complex(_TEST_CFF_REAL_H_TILDE, _TEST_CFF_IMAGINARY_H_TILDE),
                complex(_TEST_CFF_REAL_E, _TEST_CFF_IMAGINARY_E),
                complex(_TEST_CFF_REAL_E_TILDE, _TEST_CFF_IMAGINARY_E_TILDE),
                False,
                _TEST_VERBOSE),
            -0.00930291321309229)
        
    def test_calculate_c_1_longitudinally_polarized_dvcs_ww_on(self):
        """
        ## Description: Test the function computing c_{1, LP}^{DVCS} *using* the WW relations.
        This is the second c coefficient that enters into the DVCS mode expansions, c_{1, LP}^{DVCS}.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_longitudinally_polarized_dvcs(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SKEWNESS,
                _TEST_SHORTHAND_K,
                complex(_TEST_CFF_REAL_H, _TEST_CFF_IMAGINARY_H),
                complex(_TEST_CFF_REAL_H_TILDE, _TEST_CFF_IMAGINARY_H_TILDE),
                complex(_TEST_CFF_REAL_E, _TEST_CFF_IMAGINARY_E),
                complex(_TEST_CFF_REAL_E_TILDE, _TEST_CFF_IMAGINARY_E_TILDE),
                True,
                _TEST_VERBOSE),
            0.04673377354751275)
    
    def test_calculate_s_1_longitudinally_polarized_dvcs_no_ww(self):
        """
        ## Description: Test the function computing s_{1, LP}^{DVCS} *without* the WW relations.
        This is the third coefficient (first s-coefficient) that enters into the DVCS mode expansions, s_{1, LP}^{DVCS}
        """
        self.assertAlmostEqual(
            calculate_s_1_longitudinally_polarized_dvcs(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SKEWNESS,
                _TEST_SHORTHAND_K,
                complex(_TEST_CFF_REAL_H, _TEST_CFF_IMAGINARY_H),
                complex(_TEST_CFF_REAL_H_TILDE, _TEST_CFF_IMAGINARY_H_TILDE),
                complex(_TEST_CFF_REAL_E, _TEST_CFF_IMAGINARY_E),
                complex(_TEST_CFF_REAL_E_TILDE, _TEST_CFF_IMAGINARY_E_TILDE),
                False,
                _TEST_VERBOSE),
            -2.322341444732363e-16)
        
    def test_calculate_s_1_longitudinally_polarized_dvcs_ww_on(self):
        """
        ## Description: Test the function computing s_{1, LP}^{DVCS} *using* the WW relations.
        This is the third coefficient (first s-coefficient) that enters into the DVCS mode expansions, s_{1, LP}^{DVCS}
        """
        self.assertAlmostEqual(
            calculate_s_1_longitudinally_polarized_dvcs(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SKEWNESS,
                _TEST_SHORTHAND_K,
                complex(_TEST_CFF_REAL_H, _TEST_CFF_IMAGINARY_H),
                complex(_TEST_CFF_REAL_H_TILDE, _TEST_CFF_IMAGINARY_H_TILDE),
                complex(_TEST_CFF_REAL_E, _TEST_CFF_IMAGINARY_E),
                complex(_TEST_CFF_REAL_E_TILDE, _TEST_CFF_IMAGINARY_E_TILDE),
                True,
                _TEST_VERBOSE),
            9.305473459912834e-16)