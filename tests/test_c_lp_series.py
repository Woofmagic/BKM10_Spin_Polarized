import unittest

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp0 import calculate_c_0_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp0V import calculate_c_0_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp0A import calculate_c_0_plus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp1 import calculate_c_1_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp1V import calculate_c_1_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp1A import calculate_c_1_plus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp2 import calculate_c_2_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp2V import calculate_c_2_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp2A import calculate_c_2_plus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_C0p0 import calculate_c_0_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_C0p0V import calculate_c_0_zero_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_C0p0A import calculate_c_0_zero_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_C0p1 import calculate_c_1_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_C0p1V import calculate_c_1_zero_plus_longitudinally_polarized_V

from coefficients.interference_coefficients.lp_polarized.lp_polarized_C0p2 import calculate_c_2_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_C0p2V import calculate_c_2_zero_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_C0p2A import calculate_c_2_zero_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cmp0 import calculate_c_0_minus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cmp0V import calculate_c_0_minus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cmp0A import calculate_c_0_minus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cmp1 import calculate_c_1_minus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cmp1V import calculate_c_1_minus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cmp1A import calculate_c_1_minus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cmp2 import calculate_c_2_minus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cmp2V import calculate_c_2_minus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cmp2A import calculate_c_2_minus_plus_longitudinally_polarized_A

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

class TestCLPSeriesCoefficients(unittest.TestCase):

    def test_calculate_c_0_plus_plus_longitudinally_polarized(self):
        """
        ## Description: Test the function `calculate_c_0_plus_plus_longitudinally_polarized`.
        Test the coefficient called: $C_{++}^{LP}(n = 0)$.
        We call it "CLPPP0" for C (series) LP (longitudinally polarized [target]) PP (++) 0 (n = 0).
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
            0.057338590283762814)
        
    def test_calculate_c_0_plus_plus_longitudinally_polarized_V(self):
        """
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
            -0.11083877974118175)
        
    def test_calculate_c_0_plus_plus_longitudinally_polarized_A(self):
        """
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
            -0.020719510401278708)
        
    def test_calculate_c_1_plus_plus_longitudinally_polarized(self):
        """
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
            -0.1423854729987041)
        
    def test_calculate_c_1_plus_plus_longitudinally_polarized_V(self):
        """
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
            -0.03826898637315565)
        
    def test_calculate_c_1_plus_plus_longitudinally_polarized_A(self):
        
        """
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
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.010009435464345648)
        
    def test_calculate_c_2_plus_plus_longitudinally_polarized(self):
        """
        ## Description: Test the function `calculate_c_2_plus_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{LP}(n = 2)$.
        We call it "CLPPP2" for C (series) LP (longitudinally polarized [target]) PP (++) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_2_plus_plus_longitudinally_polarized(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_VERBOSE), 
            0.0012220373655056997)
        
    def test_calculate_c_2_plus_plus_longitudinally_polarized_V(self):
        """
        ## Description: Test the function `calculate_c_2_plus_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{LP, V}(n = 2)$.
        We call it "CLPVPP2" for C (series) LP (longitudinally polarized [target]) V (vector) PP (++) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_2_plus_plus_longitudinally_polarized_V(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_VERBOSE), 
            -0.0014399130108895203)
        
    def test_calculate_c_2_plus_plus_longitudinally_polarized_A(self):
        """
        ## Description: Test the function `calculate_c_2_plus_plus_longitudinally_polarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{LP, A}(n = 2)$.
        We call it "CLPAPP2" for C (series) LP (longitudinally polarized [target]) A (axial vector) PP (++) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_2_plus_plus_longitudinally_polarized_A(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_VERBOSE), 
            -0.00025947949074194774)
        
    def test_calculate_c_0_zero_plus_longitudinally_polarized(self):
        """
        ## Description: Test the function `calculate_c_0_zero_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{0+}^{LP}(n = 0)$.
        We call it "CLP0P0" for C (series) LP (longitudinally polarized [target]) 0P (0+) 0 (n = 0).

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
            -0.006869758061985178)
        
    def test_calculate_c_0_zero_plus_longitudinally_polarized_V(self):
        """
        ## Description: Test the function `calculate_c_0_zero_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{0+}^{LP,V}(n = 0)$.
        We call it "CLPV0P0" for C (series) LP (longitudinally polarized [target]) V (vector) 0P (0+) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_zero_plus_longitudinally_polarized_V(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.0038500841885851004)
        
    def test_calculate_c_0_zero_plus_longitudinally_polarized_A(self):
        
        """
        ## Description: Test the function `calculate_c_0_zero_plus_longitudinally_polarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{0+}^{LP, A}(n = 0)$.
        We call it "CLPA0P0" for C (series) LP (longitudinally polarized [target]) A (axial vector) 0P (0+) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_zero_plus_longitudinally_polarized_A(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            0.0032084034904875836)

    def test_calculate_c_1_zero_plus_longitudinally_polarized(self):
        """
        ## Description: Test the function `calculate_c_1_zero_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{0+}^{LP}(n = 1)$.
        We call it "CLP0P1" for C (series) LP (longitudinally polarized [target]) 0P (0+) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_zero_plus_longitudinally_polarized(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.0007823645434023494)
        
    def test_calculate_c_1_zero_plus_longitudinally_polarized_V(self):
        """
        ## Description: Test the function `calculate_c_1_zero_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{0+}^{LP,V}(n = 1)$.
        We call it "CLPV0P1" for C (series) LP (longitudinally polarized [target]) V (vector) 0P (0+) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_zero_plus_longitudinally_polarized_V(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            -0.002568110094701144)
        
    def test_calculate_c_2_zero_plus_longitudinally_polarized(self):
        """
        ## Description: Test the function `calculate_c_2_zero_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{0+}^{LP}(n = 2)$.
        We call it "CLP0P2" for C (series) LP (longitudinally polarized [target]) 0P (0+) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_2_zero_plus_longitudinally_polarized(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.1078956119147084)
        
    def test_calculate_c_2_zero_plus_longitudinally_polarized_V(self):
        """
        ## Description: Test the function `calculate_c_2_zero_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{0+}^{LP,V}(n = 2)$.
        We call it "CLPV0P2" for C (series) LP (longitudinally polarized [target]) V (vector) 0P (0+) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_2_zero_plus_longitudinally_polarized_V(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.006869758061985178)
        
    def test_calculate_c_2_zero_plus_longitudinally_polarized_A(self):
        """
        ## Description: Test the function `calculate_c_2_zero_plus_longitudinally_polarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{0+}^{LP,A}(n = 2)$.
        We call it "CLPA0P2" for C (series) LP (longitudinally polarized [target]) A (axial vector) 0P (0+) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_2_zero_plus_longitudinally_polarized_A(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.0032084034904875836)
        
    def test_calculate_c_0_minus_plus_longitudinally_polarized(self):
        """
        # Title: `test_calculate_c_0_minus_plus_longitudinally_polarized`

        ## Description: Test the function `calculate_c_0_minus_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{-+}^{LP}(n = 0)$.
        We call it "CLPMP0" for C (series) LP (longitudinally polarized [target]) MP (-+) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_minus_plus_longitudinally_polarized(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            -0.0063529167096453)
        
    def test_calculate_c_0_minus_plus_longitudinally_polarized_V(self):
        """
        # Title: `test_calculate_c_0_minus_plus_longitudinally_polarized_V`

        ## Description: Test the function `calculate_c_0_minus_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{-+}^{LP, V}(n = 0)$.
        We call it "CLPVMP0" for C (series) LP (longitudinally polarized [target]) V (vector) MP (-+) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_minus_plus_longitudinally_polarized_V(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            0.000089774829475794)
        
    def test_calculate_c_0_minus_plus_longitudinally_polarized_A(self):
        """
        # Title: `test_calculate_c_0_minus_plus_longitudinally_polarized_A`

        ## Description: Test the function `calculate_c_0_minus_plus_longitudinally_polarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{-+}^{LP, A}(n = 0)$.
        We call it "CLPVMP0" for C (series) LP (longitudinally polarized [target]) A (axial vector) MP (-+) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_minus_plus_longitudinally_polarized_A(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_VERBOSE), 
            0.0028441866111567)
        
    def test_calculate_c_1_minus_plus_longitudinally_polarized(self):
        """
        # Title: `test_calculate_c_1_minus_plus_longitudinally_polarized`

        ## Description: Test the function `calculate_c_1_minus_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{-+}^{LP}(n = 0)$.
        We call it "CLPMP0" for C (series) LP (longitudinally polarized [target]) MP (-+) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_minus_plus_longitudinally_polarized(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.063674515630947)
        
    def test_calculate_c_1_minus_plus_longitudinally_polarized_V(self):
        """
        # Title: `test_calculate_c_1_minus_plus_longitudinally_polarized_V`

        ## Description: Test the function `calculate_c_1_minus_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{-+}^{LP, V}(n = 1)$.
        We call it "CLPVMP1" for C (series) LP (longitudinally polarized [target]) V (vector) MP (-+) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_minus_plus_longitudinally_polarized_V(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_VERBOSE), 
            0.51591854160087)
        
    def test_calculate_c_1_minus_plus_longitudinally_polarized_A(self):
        """
        # Title: `test_calculate_c_1_minus_plus_longitudinally_polarized_A`

        ## Description: Test the function `calculate_c_1_minus_plus_longitudinally_polarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{-+}^{LP, A}(n = 1)$.
        We call it "CLPAMP1" for C (series) LP (longitudinally polarized [target]) A (axial vector) MP (-+) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_minus_plus_longitudinally_polarized_A(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_VERBOSE), 
            0.23720406981753)
        
    def test_calculate_c_2_minus_plus_longitudinally_polarized(self):
        """
        # Title: `test_calculate_c_2_minus_plus_longitudinally_polarized`

        ## Description: Test the function `calculate_c_2_minus_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{-+}^{LP}(n = 2)$.
        We call it "CLPMP2" for C (series) LP (longitudinally polarized [target]) MP (-+) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_2_minus_plus_longitudinally_polarized(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_VERBOSE), 
            -0.18590121965401)
        
    def test_calculate_c_2_minus_plus_longitudinally_polarized_V(self):
        """
        # Title: `test_calculate_c_2_minus_plus_longitudinally_polarized_V`

        ## Description: Test the function `calculate_c_2_minus_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{-+}^{LP, V}(n = 2)$.
        We call it "CLPVMP2" for C (series) LP (longitudinally polarized [target]) V (vector) MP (-+) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_2_minus_plus_longitudinally_polarized_V(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_VERBOSE), 
            0.21767807213023)
        
    def test_calculate_c_2_minus_plus_longitudinally_polarized_A(self):
        """
        # Title: `test_calculate_c_2_minus_plus_longitudinally_polarized_A`

        ## Description: Test the function `calculate_c_2_minus_plus_longitudinally_polarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{-+}^{LP, A}(n = 2)$.
        We call it "CLPAMP2" for C (series) LP (longitudinally polarized [target]) A (axial vector) MP (-+) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_2_minus_plus_longitudinally_polarized_A(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_VERBOSE), 
            0.039524572890599)