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
_TEST_SQUARED_Q_MOMENTUM_TRANSFER = 1.8200000524520876
_TEST_X_BJORKEN = 0.3429999947547912
_TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER = -0.1720000058412552
_TEST_EPSILON = 0.477109
_TEST_LEPTON_ENERGY_FRACTION = 0.491757
_TEST_K_TILDE = 0.157396
_TEST_SHORTHAND_K = 0.0842939
_TEST_T_PRIME = -0.0337889

_TEST_SKEWNESS = 0.20115437410625

_TEST_ELECTRIC_FORM_FACTOR_FE = 0.648238
_TEST_MAGNETIC_FORM_FACTOR_FG = 1.81043
_TEST_DIRAC_FORM_FACTOR_F1 = -21.9835
_TEST_PAULI_FORM_FACTOR_F2 = 23.794
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
        # Title: `test_calculate_curly_c_unpolarized_dvcs_normal_cffs`

        ## Description: Test the function `calculate_curly_c_unpolarized_dvcs`.
        This is curly C DVCS for the unpolarized case. Please note what is being passed in as arguments!
        Notice that we're evaluating CurlyC(F, F*), not any effective stuff!

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
                _TEST_CFF_H,
                _TEST_CFF_H_TILDE,
                _TEST_CFF_E,
                _TEST_CFF_E_TILDE,
                _TEST_CFF_H.conjugate(),
                _TEST_CFF_H_TILDE.conjugate(),
                _TEST_CFF_E.conjugate(),
                _TEST_CFF_E_TILDE.conjugate(),
                _TEST_VERBOSE), 
            complex(13.469720827800701, 1.2719338656422867e-18))

    def test_calculate_curly_c_unpolarized_dvcs_effective_cffs(self):
        """
        # Title: `test_calculate_curly_c_unpolarized_dvcs_effective_cffs`

        ## Description: Test the function `calculate_curly_c_unpolarized_dvcs`.
        This is curly C DVCS for the unpolarized case. Please note what is being passed in as arguments!
        Notice that we're evaluating CurlyC(Feff, Feff*).

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
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E_TILDE),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H.conjugate()),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE.conjugate()),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E.conjugate()),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E_TILDE.conjugate()),
                _TEST_VERBOSE), 
            complex(1.5110536811619562, 0.))

    def test_calculate_curly_c_unpolarized_dvcs_mixed_cffs(self):
        """
        # Title: `test_calculate_curly_c_unpolarized_dvcs_mixed_cffs`

        ## Description: Test the function `calculate_curly_c_unpolarized_dvcs`.
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
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E_TILDE),
                _TEST_CFF_H.conjugate(),
                _TEST_CFF_H_TILDE.conjugate(),
                _TEST_CFF_E.conjugate(),
                _TEST_CFF_E_TILDE.conjugate(),
                _TEST_VERBOSE), 
            complex(-4.51148215568588, -1.6180643376269439e-16))
    
    def test_calculate_curly_c_longitudinally_polarized_dvcs_normal_cffs(self):
        """
        # Title: `test_calculate_curly_c_longitudinally_polarized_dvcs_normal_cffs`

        ## Description: Test the function `calculate_curly_c_longitudinally_polarized_dvcs`.
        This is curly C DVCS for the LP case. Please note what is being passed in as arguments!
        Notice that we're evaluating CurlyC(F, F*), not any effective stuff!

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
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
            complex(0.28892498828412116, 0.))
        
    def test_calculate_curly_c_longitudinally_polarized_dvcs_mixed_cffs(self):
        """
        # Title: `test_calculate_curly_c_longitudinally_polarized_dvcs_mixed_cffs`

        ## Description: Test the function `calculate_curly_c_longitudinally_polarized_dvcs`.
        This is curly C DVCS for the LP case. Notice what is being passed in! We are evaluating
        it for EFFECTIVE CFFs!

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_curly_c_longitudinally_polarized_dvcs(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E_TILDE),
                _TEST_CFF_H.conjugate(),
                _TEST_CFF_H_TILDE.conjugate(),
                _TEST_CFF_E.conjugate(),
                _TEST_CFF_E_TILDE.conjugate(),
                _TEST_VERBOSE), 
            complex(-0.09677111691025254, 4.579109351649904e-16))
        
    def test_calculate_c_0_unpolarized_dvcs(self):
        """
        # Title: `test_calculate_c_0_unpolarized_dvcs`

        ## Description: Test the function `calculate_c_0_unpolarized_dvcs`.
        This is the first c coefficient that enters into the DVCS mode expansions, c_{0, unp}^{DVCS}.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
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
                _TEST_VERBOSE), 
            28.26760257132236)
    
    def test_calculate_c_0_longitudinally_polarized_dvcs(self):
        """
        # Title: `test_calculate_c_0_longitudinally_polarized_dvcs`

        ## Description: Test the function `calculate_c_0_longitudinally_polarized_dvcs`.
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
                _TEST_VERBOSE), 
            0.1934072893040095)
        
    def test_calculate_c_1_unpolarized_dvcs(self):
        """
        # Title: `test_calculate_c_1_unpolarized_dvcs`

        ## Description: Test the function `calculate_c_1_unpolarized_dvcs`.
        This is the first c coefficient that enters into the DVCS mode expansions, c_{1, unp}^{DVCS}.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
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
                _TEST_VERBOSE), 
            -2.2557224607532707)
    
    def test_calculate_c_1_longitudinally_polarized_dvcs(self):
        """
        # Title: `test_calculate_c_1_longitudinally_polarized_dvcs`

        ## Description: Test the function `calculate_c_1_longitudinally_polarized_dvcs`.
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
                _TEST_VERBOSE), 
            -0.008739684268421938)
        
    def test_calculate_s_1_unpolarized_dvcs(self):
        """
        # Title: `test_calculate_s_1_unpolarized_dvcs`

        ## Description: Test the function `calculate_s_1_unpolarized_dvcs`.
        This is the first s coefficient that enters into the DVCS mode expansions, s_{1, unp}^{DVCS}.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
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
                _TEST_VERBOSE), 
            1.461321506702021e-17)
    
    def test_calculate_s_1_longitudinally_polarized_dvcs(self):
        """
        # Title: `test_calculate_s_1_longitudinally_polarized_dvcs`

        ## Description: Test the function `calculate_s_1_longitudinally_polarized_dvcs`.
        This is the first s coefficient that enters into the DVCS mode expansions, s_{1, LP}^{DVCS}.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_longitudinally_polarized_dvcs(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                compute_cff_effective(_TEST_SKEWNESS, complex(_TEST_CFF_REAL_H, _TEST_CFF_IMAGINARY_H)),
                compute_cff_effective(_TEST_SKEWNESS, complex(_TEST_CFF_REAL_H_TILDE, _TEST_CFF_IMAGINARY_H_TILDE)),
                compute_cff_effective(_TEST_SKEWNESS, complex(_TEST_CFF_REAL_E, _TEST_CFF_IMAGINARY_E)),
                compute_cff_effective(_TEST_SKEWNESS, complex(_TEST_CFF_REAL_E, _TEST_CFF_IMAGINARY_E_TILDE)),
                complex(_TEST_CFF_REAL_H, _TEST_CFF_IMAGINARY_H).conjugate(),
                complex(_TEST_CFF_REAL_H_TILDE, _TEST_CFF_IMAGINARY_H_TILDE).conjugate(),
                complex(_TEST_CFF_REAL_E, _TEST_CFF_IMAGINARY_E).conjugate(),
                complex(_TEST_CFF_REAL_E, _TEST_CFF_IMAGINARY_E_TILDE).conjugate(),
                _TEST_VERBOSE), 
            -2.3144012749806e-16)