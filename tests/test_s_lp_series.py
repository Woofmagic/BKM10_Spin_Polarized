import unittest

from coefficients.interference_coefficients.lp_polarized.pl_polarized_Spp1 import calculate_s_1_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_Spp1V import calculate_s_1_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.pl_polarized_Spp1A import calculate_s_1_plus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.pl_polarized_Spp2 import calculate_s_2_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_Spp2V import calculate_s_2_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.pl_polarized_Spp2A import calculate_s_2_plus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.pl_polarized_Spp3 import calculate_s_3_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_Spp3V import calculate_s_3_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.pl_polarized_Spp3A import calculate_s_3_plus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.pl_polarized_S0p1 import calculate_s_1_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_S0p1V import calculate_s_1_zero_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.pl_polarized_S0p1A import calculate_s_1_zero_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.pl_polarized_S0p2 import calculate_s_2_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_S0p2V import calculate_s_2_zero_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.pl_polarized_S0p2A import calculate_s_2_zero_plus_longitudinally_polarized_A

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

class TestSLPSeriesCoefficients(unittest.TestCase):

    def test_calculate_s_1_plus_plus_longitudinally_polarized(self):
        """
        # Title: `calculate_s_1_plus_plus_longitudinally_polarized`

        ## Description: Test the function `calculate_s_1_plus_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{LP}(n = 1)$.
        We call it "SLPPP1" for S (series) LP (longitudinally polarized [target]) PP (++) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_plus_plus_longitudinally_polarized(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            0.645538)
        
    def test_calculate_s_1_plus_plus_longitudinally_polarized_V(self):
        """
        # Title: `test_calculate_s_1_plus_plus_longitudinally_polarized_V`

        ## Description: Test the function `calculate_s_1_plus_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{LP, V}(n = 1)$.
        We call it "SLPPP1" for S (series) LP (longitudinally polarized [target]) V (vector) PP (++) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_plus_plus_longitudinally_polarized_V(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.107439)
        
    def test_calculate_s_1_plus_plus_longitudinally_polarized_A(self):
        """
        # Title: `test_calculate_s_1_plus_plus_longitudinally_polarized_A`

        ## Description: Test the function `calculate_s_1_plus_plus_longitudinally_polarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{LP, A}(n = 1)$.
        We call it "SLPPP1" for S (series) LP (longitudinally polarized [target]) A (axial vector) PP (++) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_plus_plus_longitudinally_polarized_A(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.0243094)
        
    def test_calculate_s_2_plus_plus_longitudinally_polarized(self):
        """
        # Title: `test_calculate_s_2_plus_plus_longitudinally_polarized`

        ## Description: Test the function `calculate_s_2_plus_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{LP}(n = 2)$.
        We call it "SLPPP2" for S (series) LP (longitudinally polarized [target]) PP (++) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_2_plus_plus_longitudinally_polarized(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            0.0048104884071469)
        
    def test_calculate_s_2_plus_plus_longitudinally_polarized_V(self):
        """
        # Title: `test_calculate_s_2_plus_plus_longitudinally_polarized_V`

        ## Description: Test the function `calculate_s_2_plus_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{LP, V}(n = 2)$.
        We call it "SLPPP1" for S (series) LP (longitudinally polarized [target]) V (vector) PP (++) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_2_plus_plus_longitudinally_polarized_V(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            -0.0046153430454031)
        
    def test_calculate_s_2_plus_plus_longitudinally_polarized_A(self):
        """
        # Title: `test_calculate_s_2_plus_plus_longitudinally_polarized_A`

        ## Description: Test the function `calculate_s_2_plus_plus_longitudinally_polarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{LP, A}(n = 2)$.
        We call it "SLPPP1" for S (series) LP (longitudinally polarized [target]) A (axial vector) PP (++) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_2_plus_plus_longitudinally_polarized_A(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            -0.0047273060125334)
        
    def test_calculate_s_3_plus_plus_longitudinally_polarized(self):
        """
        # Title: `calculate_s_3_plus_plus_longitudinally_polarized`

        ## Description: Test the function `calculate_s_3_plus_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{LP}(n = 3)$.
        We call it "SLPPP3" for S (series) LP (longitudinally polarized [target]) PP (++) 3 (n = 3).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_3_plus_plus_longitudinally_polarized(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            0.00025690082629607)
        
    def test_calculate_s_3_plus_plus_longitudinally_polarized_V(self):
        """
        # Title: `test_calculate_s_3_plus_plus_longitudinally_polarized_V`

        ## Description: Test the function `calculate_s_3_plus_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{LP, V}(n = 3)$.
        We call it "SLPPP3" for S (series) LP (longitudinally polarized [target]) V (vector) PP (++) 3 (n = 3).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_3_plus_plus_longitudinally_polarized_V(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            0.00017851247673089)
        
    def test_calculate_s_3_plus_plus_longitudinally_polarized_A(self):
        """
        # Title: `test_calculate_s_3_plus_plus_longitudinally_polarized_A`

        ## Description: Test the function `calculate_s_3_plus_plus_longitudinally_polarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{LP, A}(n = 3)$.
        We call it "SLPPP3" for S (series) LP (longitudinally polarized [target]) A (axial vector) PP (++) 3 (n = 3).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_3_plus_plus_longitudinally_polarized_A(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            0.00015423393697809)
        
    def test_calculate_s_1_zero_plus_longitudinally_polarized(self):
        """
        # Title: `test_calculate_s_1_zero_plus_longitudinally_polarized`

        ## Description: Test the function `calculate_s_1_zero_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{0+}^{LP}(n = 1)$.
        We call it "SLP0P1" for S (series) LP (longitudinally polarized [target]) 0P (0+) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_zero_plus_longitudinally_polarized(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            -0.52226678511777)
        
    def test_calculate_s_1_zero_plus_longitudinally_polarized_V(self):
        """
        # Title: `test_calculate_s_1_zero_plus_longitudinally_polarized_V`

        ## Description: Test the function `calculate_s_1_zero_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{0+}^{LP, V}(n = 1)$.
        We call it "SLPV0PP1" for S (series) LP (longitudinally polarized [target]) V (vector) 0P (0+) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_zero_plus_longitudinally_polarized_V(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            0.79822543528701)
        
    def test_calculate_s_1_zero_plus_longitudinally_polarized_A(self):
        """
        # Title: `test_calculate_s_1_zero_plus_longitudinally_polarized_A`

        ## Description: Test the function `calculate_s_1_zero_plus_longitudinally_polarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{0+}^{LP, A}(n = 1)$.
        We call it "SLPA0PP1" for S (series) LP (longitudinally polarized [target]) A (axial vector) 0P (0+) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_zero_plus_longitudinally_polarized_A(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_VERBOSE), 
            0.14240509455834)
        
    def test_calculate_s_2_zero_plus_longitudinally_polarized(self):
        """
        # Title: `test_calculate_s_2_zero_plus_longitudinally_polarized`

        ## Description: Test the function `calculate_s_2_zero_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{0+}^{LP}(n = 2)$.
        We call it "SLP0P2" for S (series) LP (longitudinally polarized [target]) 0P (0+) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_2_zero_plus_longitudinally_polarized(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            0.58609108135492)
        
    def test_calculate_s_2_zero_plus_longitudinally_polarized_V(self):
        """
        # Title: `test_calculate_s_2_zero_plus_longitudinally_polarized_V`

        ## Description: Test the function `calculate_s_2_zero_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{0+}^{LP, V}(n = 2)$.
        We call it "SLPV0P2" for S (series) LP (longitudinally polarized [target]) V (vector) 0P (0+) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_2_zero_plus_longitudinally_polarized_V(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            0.037609589418397)