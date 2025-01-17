import unittest

from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp0 import calculate_c_0_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp0V import calculate_c_0_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp0A import calculate_c_0_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp1 import calculate_c_1_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp1V import calculate_c_1_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp1A import calculate_c_1_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp2 import calculate_c_2_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp2V import calculate_c_2_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp2A import calculate_c_2_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp3 import calculate_c_3_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp3V import calculate_c_3_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp3A import calculate_c_3_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_C0p0 import calculate_c_0_zero_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p0V import calculate_c_0_zero_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p0A import calculate_c_0_zero_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_C0p1 import calculate_c_1_zero_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p1V import calculate_c_1_zero_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p1A import calculate_c_1_zero_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_C0p2 import calculate_c_2_zero_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p2V import calculate_c_2_zero_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p2A import calculate_c_2_zero_plus_unpolarized_A

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

class TestCUnpolarizedSeriesCoefficients(unittest.TestCase):

    def test_calculate_c_0_plus_plus_unpolarized(self):
        """
        ## Description: Test the function `calculate_c_0_plus_plus_unpolarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp}(n = 0)$.
        We call it "CunpPP0" for C (series) unp (unpolarized [target]) PP (++) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_plus_plus_unpolarized(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            0.41930759273043816)
        
    def test_calculate_c_0_plus_plus_unpolarized_V(self):
        """
        ## Description: Test the function `calculate_c_0_plus_plus_unpolarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp}(n = 0)$.
        We call it "CunpVPP0" for C (series) unp (unpolarized [target]) V (vector) PP (++) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_plus_plus_unpolarized_V(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            -0.12251628051653782)
        
    def test_calculate_c_0_plus_plus_unpolarized_A(self):
        """
        ## Description: Test the function `calculate_c_0_plus_plus_unpolarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp}(n = 0)$.
        We call it "CunpVPP0" for C (series) unp (unpolarized [target]) A (axial vector) PP (++) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_plus_plus_unpolarized_A(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE),
            -0.6653497452048907)
        
    def test_calculate_c_1_plus_plus_unpolarized(self):
        """
        ## Description: Test the function `calculate_c_1_plus_plus_unpolarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp}(n = 1)$.
        We call it "CunpPP1" for C (series) unp (unpolarized [target]) PP (++) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_plus_plus_unpolarized(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.4054747518042577)

    def test_calculate_c_1_plus_plus_unpolarized_V(self):
        """
        # Title: `test_calculate_c_1_plus_plus_unpolarized_V`

        ## Description: Test the function `calculate_c_1_plus_plus_unpolarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp}(n = 1)$.
        We call it "CunpVPP1" for C (series) unp (unpolarized [target]) V (vector) PP (++) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_plus_plus_unpolarized_V(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.06051421738686888)
        
    def test_calculate_c_1_plus_plus_unpolarized_A(self):
        """
        ## Description: Test the function `calculate_c_1_plus_plus_unpolarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp, A}(n = 1)$.
        We call it "CunpAPP1" for C (series) unp (unpolarized [target]) A (axial vector) PP (++) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_plus_plus_unpolarized_A(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.18943390904546398)
        
    def test_calculate_c_2_plus_plus_unpolarized(self):
        """
        ## Description: Test the function `calculate_c_2_plus_plus_unpolarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp}(n = 2)$.
        We call it "CunpPP2" for C (series) unp (unpolarized [target]) PP (++) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_2_plus_plus_unpolarized(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            0.012752925202806235)
        
    def test_calculate_c_2_plus_plus_unpolarized_V(self):
        """
        ## Description: Test the function `calculate_c_2_plus_plus_unpolarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp}(n = 2)$.
        We call it "CunpVPP2" for C (series) unp (unpolarized [target]) V (vector) PP (++) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_2_plus_plus_unpolarized_V(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            -0.00476937398971525)
        
    def test_calculate_c_2_plus_plus_unpolarized_A(self):
        """
        ## Description: Test the function `calculate_c_2_plus_plus_unpolarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp, A}(n = 2)$.
        We call it "CunpAPP2" for C (series) unp (unpolarized [target]) A (axial vector) PP (++) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_2_plus_plus_unpolarized_A(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            -0.005182877093365479)
        
    def test_calculate_c_3_plus_plus_unpolarized(self):
        """
        ## Description: Test the function `calculate_c_3_plus_plus_unpolarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp}(n = 3)$.
        We call it "CunpPP3" for C (series) unp (unpolarized [target]) PP (++) 3 (n = 3).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_3_plus_plus_unpolarized(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE),
            0.00028845009320500685)
        
    def test_calculate_c_3_plus_plus_unpolarized_V(self):
        """
        ## Description: Test the function `calculate_c_3_plus_plus_unpolarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp, V}(n = 3)$.
        We call it "CunpVPP3" for C (series) unp (unpolarized [target]) V (vector) PP (++) 3 (n = 3).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_3_plus_plus_unpolarized_V(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.00017252488320532806)
        
    def test_calculate_c_3_plus_plus_unpolarized_A(self):
        """
        ## Description: Test the function `calculate_c_3_plus_plus_unpolarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{++}^{unp, A}(n = 3)$.
        We call it "CunpAPP3" for C (series) unp (unpolarized [target]) A (axial vector) PP (++) 3 (n = 3).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_3_plus_plus_unpolarized_A(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            0.00019946802377942044)
        
    def test_calculate_c_0_zero_plus_unpolarized(self):
        """
        ## Description: Test the function `calculate_c_0_zero_plus_unpolarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{0+}^{unp}(n = 0)$.
        We call it "Cunp0P0" for C (series) unp (unpolarized [target]) 0P (0+) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_zero_plus_unpolarized(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            0.21243317252244243)
        
    def test_calculate_c_0_zero_plus_unpolarized_V(self):
        """
        ## Description: Test the function `calculate_c_0_zero_plus_unpolarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{0+}^{unp, V}(n = 0)$.
        We call it "CunpV0P0" for C (series) unp (unpolarized [target]) V (vector) 0P (0+) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_zero_plus_unpolarized_V(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.05992954624455699)
        
    def test_calculate_c_0_zero_plus_unpolarized_A(self):
        """
        ## Description: Test the function `calculate_c_0_zero_plus_unpolarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{0+}^{unp, A}(n = 0)$.
        We call it "CunpA0P0" for C (series) unp (unpolarized [target]) A (axial vector) 0P (0+) 0 (n = 0).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_0_zero_plus_unpolarized_A(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.19946517626656324)
        
    def test_calculate_c_1_zero_plus_unpolarized(self):
        """
        ## Description: Test the function `calculate_c_1_zero_plus_unpolarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{0+}^{unp}(n = 1)$.
        We call it "Cunp0P1" for C (series) unp (unpolarized [target]) 0P (0+) 0 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_zero_plus_unpolarized(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_VERBOSE), 
            0.5951521249440364)
        
    def test_calculate_c_1_zero_plus_unpolarized_V(self):
        """
        ## Description: Test the function `calculate_c_1_zero_plus_unpolarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{0+}^{unp, V}(n = 1)$.
        We call it "CunpV0P1" for C (series) unp (unpolarized [target]) V (vector) 0P (0+) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_zero_plus_unpolarized_V(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            -0.1674768238263991)
        
    def test_calculate_c_1_zero_plus_unpolarized_A(self):
        """
        ## Description: Test the function `calculate_c_1_zero_plus_unpolarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{0+}^{unp, A}(n = 1)$.
        We call it "CunpA0P1" for C (series) unp (unpolarized [target]) A (axial vector) 0P (0+) 1 (n = 1.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_1_zero_plus_unpolarized_A(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            -0.8807587542823425)
        
    def test_calculate_c_2_zero_plus_unpolarized(self):
        """
        ## Description: Test the function `calculate_c_2_zero_plus_unpolarized`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{0+}^{unp}(n = 2)$.
        We call it "Cunp0P2" for C (series) unp (unpolarized [target]) 0P (0+) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_2_zero_plus_unpolarized(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.6532897993773489)
        
    def test_calculate_c_2_zero_plus_unpolarized_V(self):
        """
        ## Description: Test the function `calculate_c_2_zero_plus_unpolarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{0+}^{unp, V}(n = 2)$.
        We call it "CunpV0P2" for C (series) unp (unpolarized [target]) V (vector) 0P (0+) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_2_zero_plus_unpolarized_V(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.019976515414852337)
        
    def test_calculate_c_2_zero_plus_unpolarized_A(self):
        """
        ## Description: Test the function `calculate_c_2_zero_plus_unpolarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $C_{0+}^{unp, A}(n = 2)$.
        We call it "CunpA0P1" for C (series) unp (unpolarized [target]) A (axial vector) 0P (0+) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_c_2_zero_plus_unpolarized_A(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.04104505925226267)