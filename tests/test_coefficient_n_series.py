import unittest

from coefficients.interference_coefficients.lp_polarized.lp_polarized_c_n import calculate_c_0_interference_coefficient
from coefficients.interference_coefficients.lp_polarized.lp_polarized_c_n import calculate_c_1_interference_coefficient
from coefficients.interference_coefficients.lp_polarized.lp_polarized_c_n import calculate_c_2_interference_coefficient

from coefficients.interference_coefficients.lp_polarized.lp_polarized_s_n import calculate_s_1_interference_coefficient
from coefficients.interference_coefficients.lp_polarized.lp_polarized_s_n import calculate_s_2_interference_coefficient
from coefficients.interference_coefficients.lp_polarized.lp_polarized_s_n import calculate_s_3_interference_coefficient

_TEST_LEPTON_POLARIZATION = 0.5
_TEST_TARGET_POLARIZATION = 1.0

_TEST_SQUARED_Q_MOMENTUM_TRANSFER = 1.8200000524520876
_TEST_X_BJORKEN = 0.3429999947547912
_TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER = -0.1720000058412552
_TEST_EPSILON = 0.4771085571437671
_TEST_LEPTON_ENERGY_FRACTION = 0.4917571121010006

_TEST_K_TILDE = 0.1573963123403191
_TEST_SHORTHAND_K = 0.08429388311190095
_TEST_T_PRIME = -0.0337889264367002
_TEST_SKEWNESS = 0.20115437410625225

_TEST_ELECTRIC_FORM_FACTOR_FE = 0.6482376115457034
_TEST_MAGNETIC_FORM_FACTOR_FG = 1.8104286920947112
_TEST_DIRAC_FORM_FACTOR_F1 = 0.7023600720564278
_TEST_PAULI_FORM_FACTOR_F2 = 1.1080686200382834

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

class TestCurlyCLongitudinallyPolarizedSeriesCoefficients(unittest.TestCase):

    def test_calculate_c_0_interference_coefficient(self):
        """
        # Title: `test_calculate_c_0_interference_coefficient`

        ## Description: Test the function `calculate_c_0_interference_coefficient`.
        This is a major function that computes for us the c_{n}^{I} coefficients that
        are directly present in the Fourier sum. We test the c_{n = 0}^{I} contribution
        here.
        """
        self.assertAlmostEqual(
            calculate_c_0_interference_coefficient(
                0,
                0.5,
                1.0,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SKEWNESS,
                _TEST_T_PRIME,
                _TEST_K_TILDE,
                _TEST_SHORTHAND_K,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_CFF_H,
                _TEST_CFF_H_TILDE,
                _TEST_CFF_E,
                _TEST_CFF_E_TILDE,
                _TEST_VERBOSE), 
            0.10348803802959823)
        
    def test_calculate_c_1_interference_coefficient(self):
        """
        # Title: `test_calculate_c_1_interference_coefficient`

        ## Description: Test the function `calculate_c_1_interference_coefficient`.
        This is a major function that computes for us the c_{n}^{I} coefficients that
        are directly present in the Fourier sum. We test the c_{n = 1}^{I} contribution
        here.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_interference_coefficient(
                1,
                0.5,
                1.0,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SKEWNESS,
                _TEST_T_PRIME,
                _TEST_K_TILDE,
                _TEST_SHORTHAND_K,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_CFF_H,
                _TEST_CFF_H_TILDE,
                _TEST_CFF_E,
                _TEST_CFF_E_TILDE,
                _TEST_VERBOSE), 
            -0.20896781080933297)
        
    def test_calculate_c_2_interference_coefficient(self):
        """
        # Title: `test_calculate_c_2_interference_coefficient`

        ## Description: Test the function `calculate_c_2_interference_coefficient`.
        This is a major function that computes for us the c_{n}^{I} coefficients that
        are directly present in the Fourier sum. We test the c_{n = 2}^{I} contribution
        here.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_2_interference_coefficient(
                2,
                0.5,
                1.0,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SKEWNESS,
                _TEST_T_PRIME,
                _TEST_K_TILDE,
                _TEST_SHORTHAND_K,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_CFF_H,
                _TEST_CFF_H_TILDE,
                _TEST_CFF_E,
                _TEST_CFF_E_TILDE,
                _TEST_VERBOSE), 
            0.0075524977153990066)
    
    def test_calculate_s_1_interference_coefficient(self):
        """
        # Title: `test_calculate_s_1_interference_coefficient`

        ## Description: Test the function `calculate_s_1_interference_coefficient`.
        This is a major function that computes for us the s_{n}^{I} coefficients that
        are directly present in the Fourier sum. We test the s_{n = 1}^{I} contribution
        here.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_interference_coefficient(
                1,
                0.5,
                1.0,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SKEWNESS,
                _TEST_T_PRIME,
                _TEST_K_TILDE,
                _TEST_SHORTHAND_K,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_CFF_H,
                _TEST_CFF_H_TILDE,
                _TEST_CFF_E,
                _TEST_CFF_E_TILDE,
                _TEST_VERBOSE), 
            1.028806355631669)
        
    def test_calculate_s_2_interference_coefficient(self):
        """
        # Title: `test_calculate_s_2_interference_coefficient`

        ## Description: Test the function `calculate_s_2_interference_coefficient`.
        This is a major function that computes for us the s_{n}^{I} coefficients that
        are directly present in the Fourier sum. We test the s_{n = 2}^{I} contribution
        here.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_2_interference_coefficient(
                2,
                0.5,
                1.0,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SKEWNESS,
                _TEST_T_PRIME,
                _TEST_K_TILDE,
                _TEST_SHORTHAND_K,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_CFF_H,
                _TEST_CFF_H_TILDE,
                _TEST_CFF_E,
                _TEST_CFF_E_TILDE,
                _TEST_VERBOSE), 
            -0.037171780108828066)
        
    def test_calculate_s_3_interference_coefficient(self):
        """
        # Title: `test_calculate_s_3_interference_coefficient`

        ## Description: Test the function `calculate_s_3_interference_coefficient`.
        This is a major function that computes for us the s_{n}^{I} coefficients that
        are directly present in the Fourier sum. We test the s_{n = 3}^{I} contribution
        here.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_3_interference_coefficient(
                3,
                0.5,
                1.0,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SKEWNESS,
                _TEST_T_PRIME,
                _TEST_K_TILDE,
                _TEST_SHORTHAND_K,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_CFF_H,
                _TEST_CFF_H_TILDE,
                _TEST_CFF_E,
                _TEST_CFF_E_TILDE,
                _TEST_VERBOSE), 
            0.000494100323503276)