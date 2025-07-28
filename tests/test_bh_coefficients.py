"""
## Description:
A testing script for the BH (Bethe-Heitler) coefficients, both unpolarized and unpolarized.

## Notes:
    (1): all tests in this script passed on 2025/07/23.
    (2): TP (transversely-polarized) coefficients not yet implemented.
"""

import unittest

from coefficients.bh_coefficients.unpolarized.unpolarized_c0_bh import calculate_c_0_unpolarized_bh
from coefficients.bh_coefficients.unpolarized.unpolarized_c1_bh import calculate_c_1_unpolarized_bh
from coefficients.bh_coefficients.unpolarized.unpolarized_c2_bh import calculate_c_2_unpolarized_bh

from coefficients.bh_coefficients.lp_polarized.lp_polarized_c0_bh import calculate_c_0_longitudinally_polarized_bh
from coefficients.bh_coefficients.lp_polarized.lp_polarized_c1_bh import calculate_c_1_longitudinally_polarized_bh

_TEST_LEPTON_POLARIZATION = 1.0
_TEST_TARGET_POLARIZATION = 0.5

_TEST_SQUARED_Q_MOMENTUM_TRANSFER = 1.82
_TEST_X_BJORKEN = 0.34
_TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER = -0.17

_TEST_EPSILON = 0.47293561004973345
_TEST_LEPTON_ENERGY_FRACTION = 0.49609612355928445
_TEST_SHORTHAND_K = 0.08492693191323883

_TEST_DIRAC_FORM_FACTOR_F1 = 0.7049508167585219
_TEST_PAULI_FORM_FACTOR_F2 = 1.1137103937669304

_TEST_VERBOSE = False

_TEST_VERBOSE = False

class TestBHCoefficients(unittest.TestCase):
    
    def test_calculate_c0_BH_unpolarized(self):
        """
        ## Description: Test c_{0, unp}^{BH}
        This is the first coefficient in the BH mode expansion.
        """
        self.assertAlmostEqual(
            calculate_c_0_unpolarized_bh(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_VERBOSE),
            4.196441097163937)
        
    def test_calculate_c1_BH_unpolarized(self):
        """
        ## Description: Test c_{1, unp}^{BH}
        This is the first coefficient in the BH mode expansion.
        """
        self.assertAlmostEqual(
            calculate_c_1_unpolarized_bh(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_VERBOSE),
            -1.0718559129262486)

    def test_calculate_c2_BH_unpolarized(self):
        """
        ## Description: Test c_{2, unp}^{BH}
        This is the first coefficient in the BH mode expansion.
        """
        self.assertAlmostEqual(
            calculate_c_2_unpolarized_bh(
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_SHORTHAND_K,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_VERBOSE),
            -0.03281299774352729)
        
    def test_calculate_c0_BH_longitudinally_polarized(self):
        """
        ## Description: Test c_{0, LP}^{BH}
        This is the first coefficient in the BH mode expansion for LP target.
        """
        self.assertAlmostEqual(
            calculate_c_0_longitudinally_polarized_bh(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_VERBOSE),
            1.0209385078703184)

    def test_calculate_c1_BH_longitudinally_polarized(self):
        """
        ## Description: Test c_{1, LP}^{BH}
        This is the second coefficient in the BH mode expansion for LP target.
        """
        self.assertAlmostEqual(
            calculate_c_1_longitudinally_polarized_bh(
                _TEST_LEPTON_POLARIZATION,
                _TEST_TARGET_POLARIZATION,
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_EPSILON,
                _TEST_LEPTON_ENERGY_FRACTION,
                _TEST_SHORTHAND_K,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_VERBOSE),
            -0.04922677820072388)