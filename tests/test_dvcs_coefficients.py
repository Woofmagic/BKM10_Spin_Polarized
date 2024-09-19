import unittest

from coefficients.dvcs_coefficients.lp_polarized.bkm10.lp_polarized_curlyC_dvcs import calculate_curly_c_longitudinally_polarized_dvcs

from coefficients.dvcs_coefficients.lp_polarized.bkm10.lp_polarized_c0_dvcs import calculate_c_0_longitudinally_polarized_dvcs
from coefficients.dvcs_coefficients.lp_polarized.bkm10.lp_polarized_c1_dvcs import calculate_c_1_longitudinally_polarized_dvcs
from coefficients.dvcs_coefficients.lp_polarized.bkm10.lp_polarized_s1_dvcs import calculate_s_1_longitudinally_polarized_dvcs

from form_factors.effective_cffs import compute_cff_effective

_TEST_LEPTON_POLARIZATION = 1.0
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
_TEST_CFF_REAL_E_TILDE = 0.903
_TEST_CFF_IMAGINARY_H = 2.421
_TEST_CFF_IMAGINARY_H_TILDE = 1.131
_TEST_CFF_IMAGINARY_E = 2.207
_TEST_CFF_IMAGINARY_E_TILDE = 5.383

_TEST_VERBOSE = False

class TestDVCSCoefficients(unittest.TestCase):

    def test_calculate_curly_c_longitudinally_polarized_dvcs(self):
        """
        # Title: `test_calculate_curly_C_unpolarized_interference`

        ## Description: Test the function `calculate_curly_c_longitudinally_polarized_dvcs`.
        This is curly C DVCS for the LP case.

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
                _TEST_CFF_REAL_H,
                _TEST_CFF_REAL_H_TILDE,
                _TEST_CFF_REAL_E,
                _TEST_CFF_REAL_E_TILDE,
                _TEST_CFF_IMAGINARY_H,
                _TEST_CFF_IMAGINARY_H_TILDE,
                _TEST_CFF_IMAGINARY_E,
                _TEST_CFF_IMAGINARY_E_TILDE,
                _TEST_VERBOSE), 
            0.15380541535815)
        
    def test_calculate_c_0_longitudinally_polarized_dvcs(self):
        """
        # Title: `test_calculate_c_0_longitudinally_polarized_dvcs`

        ## Description: Test the function `calculate_c_0_longitudinally_polarized_dvcs`.
        This is the first coefficient that enters into the DVCS mode expansions, c_{0, LP}^{DVCS}.

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
                _TEST_CFF_REAL_H,
                _TEST_CFF_REAL_H_TILDE,
                _TEST_CFF_REAL_E,
                _TEST_CFF_REAL_E_TILDE,
                _TEST_CFF_IMAGINARY_H,
                _TEST_CFF_IMAGINARY_H_TILDE,
                _TEST_CFF_IMAGINARY_E,
                _TEST_CFF_IMAGINARY_E_TILDE,
                _TEST_VERBOSE), 
            0.20591565057326)
        
    def test_calculate_c_1_longitudinally_polarized_dvcs(self):
        """
        # Title: `test_calculate_c_1_longitudinally_polarized_dvcs`

        ## Description: Test the function `calculate_c_1_longitudinally_polarized_dvcs`.
        This is the first coefficient that enters into the DVCS mode expansions, c_{1, LP}^{DVCS}.

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
                _TEST_CFF_REAL_H,
                _TEST_CFF_REAL_H_TILDE,
                _TEST_CFF_REAL_E,
                _TEST_CFF_REAL_E_TILDE,
                _TEST_CFF_IMAGINARY_H,
                _TEST_CFF_IMAGINARY_H_TILDE,
                _TEST_CFF_IMAGINARY_E,
                _TEST_CFF_IMAGINARY_E_TILDE,
                _TEST_VERBOSE), 
            0.027781239111881)