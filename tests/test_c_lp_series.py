import unittest

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp0 import calculate_c_0_plus_plus_longitudinally_polarized
from coefficients.interference_coefficients.lp_polarized.pl_polarized_Cpp0V import calculate_c_0_plus_plus_longitudinally_polarized_V
from coefficients.interference_coefficients.lp_polarized.pl_polarized_Cpp0A import calculate_c_0_plus_plus_longitudinally_polarized_A

class TestCLPSeriesCoefficients(unittest.TestCase):

    def test_calculate_c_0_plus_plus_longitudinally_polarized(self):
        self.assertAlmostEqual(
            calculate_c_0_plus_plus_longitudinally_polarized(
                1.0,
                1.0,
                1.82,
                0.343,
                -0.172,
                0.477109,
                0.491757,
                0.157396,
                False), 
            0.119359)
        
    def test_calculate_c_0_plus_plus_longitudinally_polarized_V(self):
        self.assertAlmostEqual(
            calculate_c_0_plus_plus_longitudinally_polarized_V(
                1.0,
                1.0,
                1.82,
                0.343,
                -0.172,
                0.477109,
                0.491757,
                0.157396,
                False), 
            -0.22258
        )