import unittest

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp0 import calculate_c_0_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_Cpp0V import calculate_c_0_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.pl_polarized_Cpp0A import calculate_c_0_plus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.pl_polarized_Cpp1 import calculate_c_1_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_Cpp1V import calculate_c_1_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.pl_polarized_Cpp1A import calculate_c_1_plus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.pl_polarized_C0p0 import calculate_c_0_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_C0p0V import calculate_c_0_zero_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.pl_polarized_C0p0A import calculate_c_0_zero_plus_longitudinally_polarized_A

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

_TEST_VERBOSE = False

class TestCLPSeriesCoefficients(unittest.TestCase):

    def test_calculate_c_0_plus_plus_longitudinally_polarized(self):
        """
        # Title: `test_calculate_c_0_plus_plus_longitudinally_polarized`

        ## Description: Test the function `calculate_c_0_plus_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{LP}(n = 0)$.
        We call it "CLPPP0" for C (series) LP (longitudinally polarized [target]) PP (++) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_plus_plus_longitudinally_polarized(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            0.11935918886665)
        
    def test_calculate_c_0_plus_plus_longitudinally_polarized_V(self):
        """
        # Title: `calculate_c_0_plus_plus_longitudinally_polarized_V`

        ## Description: Test the function `calculate_c_0_plus_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{LP, V}(n = 0)$.
        We call it "CLPVPP0" for C (series) LP (longitudinally polarized [target]) V (vector) PP (++) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_plus_plus_longitudinally_polarized_V(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            -0.22257983433145)
        
    def test_calculate_c_0_plus_plus_longitudinally_polarized_A(self):
        """
        # Title: `calculate_c_0_plus_plus_longitudinally_polarized_A`

        ## Description: Test the function `calculate_c_0_plus_plus_longitudinally_polarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{LP, A}(n = 0)$.
        We call it "CLPVPP0" for C (series) LP (longitudinally polarized [target]) A (axial-vector) PP (++) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_plus_plus_longitudinally_polarized_A(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            -0.041889300265988)
        
    def test_calculate_c_1_plus_plus_longitudinally_polarized(self):
        """
        # Title: `test_calculate_c_1_plus_plus_longitudinally_polarized`

        ## Description: Test the function `calculate_c_1_plus_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{LP}(n = 1)$.
        We call it "CLPPP1" for C (series) LP (longitudinally polarized [target]) PP (++) 0 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_plus_plus_longitudinally_polarized(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.27804613812563)
        
    def test_calculate_c_1_plus_plus_longitudinally_polarized_V(self):
        """
        # Title: `test_calculate_c_1_plus_plus_longitudinally_polarized_V`

        ## Description: Test the function `calculate_c_1_plus_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{LP, V}(n = 1)$.
        We call it "CLPVPP1" for C (series) LP (longitudinally polarized [target]) V (vector) PP (++) 0 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_plus_plus_longitudinally_polarized_V(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.075783256772997)
        
    def test_calculate_c_1_plus_plus_longitudinally_polarized_A(self):
        
        """
        # Title: `test_calculate_c_1_plus_plus_longitudinally_polarized_A`

        ## Description: Test the function `calculate_c_1_plus_plus_longitudinally_polarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{LP, A}(n = 1)$.
        We call it "CLPAPP1" for C (series) LP (longitudinally polarized [target]) A (axial vector) PP (++) 0 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_plus_plus_longitudinally_polarized_A(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.019994852134866)
        
    def test_calculate_c_0_plus_plus_longitudinally_polarized(self):
        """
        # Title: `test_calculate_c_0_plus_plus_longitudinally_polarized`

        ## Description: Test the function `calculate_c_0_plus_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{LP}(n = 0)$.
        We call it "CLPPP0" for C (series) LP (longitudinally polarized [target]) PP (++) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_zero_plus_longitudinally_polarized(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.013586642803901)