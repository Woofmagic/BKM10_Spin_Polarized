import unittest

from coefficients.interference_coefficients.lp_polarized.pl_polarized_Spp1 import calculate_s_1_plus_plus_longitudinally_polarized

class TestSLPSeriesCoefficients(unittest.TestCase):

    def test_calculate_s_1_plus_plus_longitudinally_polarized(self):
        """
        # Title: `calculate_s_1_plus_plus_longitudinally_polarized`

        ## Description: Test the function `calculate_s_1_plus_plus_longitudinally_polarized`.
        Remember, that function corresponds to the BKM10 coefficient called $S_{++}^{LP}(n = 1)$.
        We call it "SLPPP1" for S (series) LP (longitudinally polarized [target]) PP (++) 0 (n = 1).

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_s_1_plus_plus_longitudinally_polarized(
                1.0,
                1.8200000524520876,
                0.3429999947547912,
                -0.1720000058412552,
                0.477109,
                0.491757,
                0.0842939,
                False), 
            0.645538)