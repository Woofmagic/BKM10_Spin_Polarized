import unittest

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp0 import calculate_c_0_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_Cpp0V import calculate_c_0_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.pl_polarized_Cpp0A import calculate_c_0_plus_plus_longitudinally_polarized_A

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
                1.0,
                1.0,
                1.8200000524520876,
                0.3429999947547912,
                -0.1720000058412552,
                0.477109,
                0.491757,
                0.157396,
                False), 
            0.119359)
        
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
                1.0,
                1.0,
                1.8200000524520876,
                0.3429999947547912,
                -0.1720000058412552,
                0.477109,
                0.491757,
                0.157396,
                False), 
            -0.22258)
        
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
                1.0,
                1.0,
                1.8200000524520876,
                0.3429999947547912,
                -0.1720000058412552,
                0.477109,
                0.491757,
                0.157396,
                False), 
            -0.0418893)