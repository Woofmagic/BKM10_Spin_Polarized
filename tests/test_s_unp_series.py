import unittest

from coefficients.interference_coefficients.unpolarized.unpolarized_Spp1 import calculate_s_1_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Spp1V import calculate_s_1_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Spp1A import calculate_s_1_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_Spp2 import calculate_s_2_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Spp2V import calculate_s_2_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Spp2A import calculate_s_2_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_S0p1 import calculate_s_1_zero_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_S0p1V import calculate_s_1_zero_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_S0p1A import calculate_s_1_zero_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_S0p2 import calculate_s_2_zero_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_S0p2V import calculate_s_2_zero_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_S0p2A import calculate_s_2_zero_plus_unpolarized_A

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

class TestSUnpolarizedSeriesCoefficients(unittest.TestCase):

    def test_calculate_s_1_plus_plus_unpolarized(self):
        """
        ## Description: Test the function `calculate_s_1_plus_plus_unpolarized`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{unp}(n = 1)$.
        We call it "SunpPP1" for S (series) unp (unpolarized [target]) PP (++) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_plus_plus_unpolarized(
                _TEST_LEPTON_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE),
            0.204835886952946)
        
    def test_calculate_s_1_plus_plus_unpolarized_V(self):
        """
        ## Description: Test the function `calculate_s_1_plus_plus_unpolarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{unp, V}(n = 1)$.
        We call it "SunpVPP0" for S (series) unp (unpolarized [target]) V (vector) PP (++) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_plus_plus_unpolarized_V(
                _TEST_LEPTON_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE),
            -0.00014525045555408562)
        
    def test_calculate_s_1_plus_plus_unpolarized_A(self):
        """
        ## Description: Test the function `calculate_s_1_plus_plus_unpolarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{unp, A}(n = 1)$.
        We call it "SunpAPP0" for S (series) unp (unpolarized [target]) A (axial vector) PP (++) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_plus_plus_unpolarized_A(
                _TEST_LEPTON_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.01942223795974634)
        
    def test_calculate_s_2_plus_plus_unpolarized(self):
        """
        ## Description: Test the function `calculate_s_2_plus_plus_unpolarized`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{unp}(n = 2)$.
        We call it "SunpPP2" for S (series) unp (unpolarized [target]) PP (++) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_2_plus_plus_unpolarized(
                _TEST_LEPTON_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_VERBOSE), 
            0.0013518120174947131)
        
    def test_calculate_s_2_plus_plus_unpolarized_V(self):
        """
        ## Description: Test the function `calculate_s_2_plus_plus_unpolarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{unp, V}(n = 2)$.
        We call it "SunpVP2" for S (series) unp (unpolarized [target]) V (vector) PP (++) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_2_plus_plus_unpolarized_V(
                _TEST_LEPTON_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_VERBOSE),
            -0.00028703499891201986)
        
    def test_calculate_s_2_plus_plus_unpolarized_A(self):
        """
        ## Description: Test the function `calculate_s_2_plus_plus_unpolarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{unp, A}(n = 2)$.
        We call it "SunpAPP2" for S (series) unp (unpolarized [target]) A (axial vector) PP (++) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_2_plus_plus_unpolarized_A(
                _TEST_LEPTON_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_VERBOSE),
            -0.0015964152659533244)
        
    def test_calculate_s_1_zero_plus_unpolarized(self):
        """
        ## Description: Test the function `calculate_s_1_zero_plus_unpolarized`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{0+}^{unp}(n = 1)$.
        We call it "Sunp0P1" for S (series) unp (unpolarized [target]) 0P (0+) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_zero_plus_unpolarized(
                _TEST_LEPTON_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE),
            0.027493884543271067)
        
    def test_calculate_s_1_zero_plus_unpolarized_V(self):
        """
        ## Description: Test the function `calculate_s_1_zero_plus_unpolarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{0+}^{unp, V}(n = 1)$.
        We call it "Sunp0PV2" for S (series) unp (unpolarized [target]) V (vector) 0P (0+) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_zero_plus_unpolarized_V(
                _TEST_LEPTON_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_VERBOSE),
            -0.002132993423969055)
        
    def test_calculate_s_1_zero_plus_unpolarized_A(self):
        """
        ## Description: Test the function `calculate_s_1_zero_plus_unpolarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{0+}^{unp, A}(n = 1)$.
        We call it "Sunp0PA2" for S (series) unp (unpolarized [target]) A (axial vector) 0P (0+) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_zero_plus_unpolarized_A(
                _TEST_LEPTON_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE),
            0.0004254151959084707)
        
    def test_calculate_s_2_zero_plus_unpolarized(self):
        """
        ## Description: Test the function `calculate_s_2_zero_plus_unpolarized`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{0+}^{unp}(n = 2)$.
        We call it "Sunp0P2" for S (series) unp (unpolarized [target]) 0P (0+) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_2_zero_plus_unpolarized(
                _TEST_LEPTON_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE),
            0.11919374186393569)
        
    def test_calculate_s_2_zero_plus_unpolarized_V(self):
        """
        ## Description: Test the function `calculate_s_2_zero_plus_unpolarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{0+}^{unp, V}(n = 2)$.
        We call it "Sunp0PV2" for S (series) unp (unpolarized [target]) V (vector) 0P (0+) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_2_zero_plus_unpolarized_V(
                _TEST_LEPTON_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE),
            0.0036447463651938946)
        
    def test_calculate_s_2_zero_plus_unpolarized_A(self):
        """
        ## Description: Test the function `calculate_s_2_zero_plus_unpolarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{0+}^{unp, A}(n = 2)$.
        We call it "Sunp0PA2" for S (series) unp (unpolarized [target]) A (axial vector) 0P (0+) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_2_zero_plus_unpolarized_A(
                _TEST_LEPTON_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE),
            0.006943662221072585)