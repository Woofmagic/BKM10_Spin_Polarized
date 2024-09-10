import unittest

from coefficients.interference_coefficients.lp_polarized.lp_polarized_Cpp0 import calculate_c_0_plus_plus_longitudinally_polarized

class TestCLPSeriesCoefficients(unittest.TestCase):

    def test_calculate_c_0_plus_plus_longitudinally_polarized(self):
        self.assertEqual(
            calculate_c_0_plus_plus_longitudinally_polarized(
                1.0,
                1.0,
                1.82,
                0.343,
                -0.172,
                0.477109,
                0.491757,
                0.157396,
                False
            ), 
            0.119359
        )