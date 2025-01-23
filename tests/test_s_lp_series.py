import unittest

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp1 import calculate_s_1_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp1V import calculate_s_1_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp1A import calculate_s_1_plus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp2 import calculate_s_2_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp2V import calculate_s_2_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp2A import calculate_s_2_plus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp3 import calculate_s_3_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp3V import calculate_s_3_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Spp3A import calculate_s_3_plus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_S0p1 import calculate_s_1_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_S0p1V import calculate_s_1_zero_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_S0p1A import calculate_s_1_zero_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_S0p2 import calculate_s_2_zero_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_S0p2V import calculate_s_2_zero_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_S0p2A import calculate_s_2_zero_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Smp1 import calculate_s_1_minus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Smp1V import calculate_s_1_minus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Smp1A import calculate_s_1_minus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Smp2 import calculate_s_2_minus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Smp2V import calculate_s_2_minus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Smp2A import calculate_s_2_minus_plus_longitudinally_polarized_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Smp3 import calculate_s_3_minus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Smp3V import calculate_s_3_minus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_Smp3A import calculate_s_3_minus_plus_longitudinally_polarized_A

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

class TestSLPSeriesCoefficients(unittest.TestCase):

    def test_calculate_s_1_plus_plus_longitudinally_polarized(self):
        """
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
            0.6506323386753146)
        
    def test_calculate_s_1_plus_plus_longitudinally_polarized_V(self):
        """
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
            -0.10726649931526153)
        
    def test_calculate_s_1_plus_plus_longitudinally_polarized_A(self):
        """
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
            -0.02402970822511508)
        
    def test_calculate_s_2_plus_plus_longitudinally_polarized(self):
        """
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
            0.005027011370588231)
        
    def test_calculate_s_2_plus_plus_longitudinally_polarized_V(self):
        """
        ## Description: Test the function `calculate_s_2_plus_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{LP, V}(n = 2)$.
        We call it "SLPPP2" for S (series) LP (longitudinally polarized [target]) V (vector) PP (++) 2 (n = 2).

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
            -0.004685318215068245)
        
    def test_calculate_s_2_plus_plus_longitudinally_polarized_A(self):
        """
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
            -0.004723867344658563)
        
    def test_calculate_s_3_plus_plus_longitudinally_polarized(self):
        """
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
            0.00026075873525180664)
        
    def test_calculate_s_3_plus_plus_longitudinally_polarized_V(self):
        """
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
            0.00018031899045680918)
        
    def test_calculate_s_3_plus_plus_longitudinally_polarized_A(self):
        """
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
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.00015596240529592618)
        
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
        
    def test_calculate_s_2_zero_plus_longitudinally_polarized_A(self):
        """
        # Title: `test_calculate_s_2_zero_plus_longitudinally_polarized_A`

        ## Description: Test the function `calculate_s_2_zero_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{0+}^{LP, A}(n = 2)$.
        We call it "SLPA0P2" for S (series) LP (longitudinally polarized [target]) A (axial vector) 0P (0+) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_2_zero_plus_longitudinally_polarized_A(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            0.017779238335062)
        
    def test_calculate_s_1_minus_plus_longitudinally_polarized(self):
        """
        # Title: `test_calculate_s_1_minus_plus_longitudinally_polarized`

        ## Description: Test the function `calculate_s_1_minus_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{-+}^{LP}(n = 1)$.
        We call it "SLPPP1" for S (series) LP (longitudinally polarized [target]) MP (-+) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_minus_plus_longitudinally_polarized(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            -0.15053635153596)
        
    def test_calculate_s_1_minus_plus_longitudinally_polarized_V(self):
        """
        # Title: `test_calculate_s_1_minus_plus_longitudinally_polarized_V`

        ## Description: Test the function `calculate_s_1_minus_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{-+}^{LP, V}(n = 1)$.
        We call it "SLPVPP1" for S (series) LP (longitudinally polarized [target]) V (vector) MP (-+) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_minus_plus_longitudinally_polarized_V(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            0.13509164613432)
        
    def test_calculate_s_1_minus_plus_longitudinally_polarized_A(self):
        """
        # Title: `test_calculate_s_1_minus_plus_longitudinally_polarized_A`

        ## Description: Test the function `calculate_s_1_minus_plus_longitudinally_polarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{-+}^{LP, A}(n = 1)$.
        We call it "SLPVPP1" for S (series) LP (longitudinally polarized [target]) A (axial vector) MP (-+) 1 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_minus_plus_longitudinally_polarized_A(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            0.045267549381737)
        
    def test_calculate_s_2_minus_plus_longitudinally_polarized(self):
        """
        # Title: `test_calculate_s_2_minus_plus_longitudinally_polarized`

        ## Description: Test the function `calculate_s_2_minus_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{-+}^{LP}(n = 2)$.
        We call it "SLPPP2" for S (series) LP (longitudinally polarized [target]) MP (-+) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_2_minus_plus_longitudinally_polarized(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_VERBOSE), 
            -0.42338955042822)
        
    def test_calculate_s_2_minus_plus_longitudinally_polarized_V(self):
        """
        # Title: `test_calculate_s_2_minus_plus_longitudinally_polarized_V`

        ## Description: Test the function `calculate_s_2_minus_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{-+}^{LP,V}(n = 2)$.
        We call it "SLPVPP2" for S (series) LP (longitudinally polarized [target]) V (vector) MP (-+) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_2_minus_plus_longitudinally_polarized_V(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            0.87645317970911)
        
    def test_calculate_s_2_minus_plus_longitudinally_polarized_A(self):
        """
        # Title: `test_calculate_s_2_minus_plus_longitudinally_polarized_A`

        ## Description: Test the function `calculate_s_2_minus_plus_longitudinally_polarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{-+}^{LP,V}(n = 2)$.
        We call it "SLPVPP2" for S (series) LP (longitudinally polarized [target]) A (axial vector) MP (-+) 2 (n = 2).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_2_minus_plus_longitudinally_polarized_A(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_K_TILDE,
                _TEST_VERBOSE), 
            0.11404596503142)
        
    def test_calculate_s_3_minus_plus_longitudinally_polarized(self):
        """
        # Title: `test_calculate_s_3_minus_plus_longitudinally_polarized`

        ## Description: Test the function `calculate_s_3_minus_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{-+}^{LP}(n = 3)$.
        We call it "SLPPP3" for S (series) LP (longitudinally polarized [target]) MP (-+) 3 (n = 3).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_3_minus_plus_longitudinally_polarized(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            0.39628257057683)
        
    def test_calculate_s_3_minus_plus_longitudinally_polarized_V(self):
        """
        # Title: `test_calculate_s_3_minus_plus_longitudinally_polarized_V`

        ## Description: Test the function `calculate_s_3_minus_plus_longitudinally_polarized_V`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{-+}^{LP,V}(n = 3)$.
        We call it "SLPVPP3" for S (series) LP (longitudinally polarized [target]) V (vector) MP (-+) 3 (n = 3).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_3_minus_plus_longitudinally_polarized_V(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_T_PRIME,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            0.025263273062887)
        
    def test_calculate_s_3_minus_plus_longitudinally_polarized_A(self):
        """
        # Title: `test_calculate_s_3_minus_plus_longitudinally_polarized_A`

        ## Description: Test the function `calculate_s_3_minus_plus_longitudinally_polarized_A`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{-+}^{LP,A}(n = 3)$.
        We call it "SLPAPP3" for S (series) LP (longitudinally polarized [target]) A (axial vector) MP (-+) 3 (n = 3).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_3_minus_plus_longitudinally_polarized_A(
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_VERBOSE), 
            0.012187607425918)