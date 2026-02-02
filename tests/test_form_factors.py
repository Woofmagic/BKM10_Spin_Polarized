"""
## Description:
Just need to verify that the effective form factors (F_{eff}) are coming
out correctly.

## Notes:
    1. 2026/01/21
        - All tests pass.
"""

import unittest

from form_factors.effective_cffs import compute_cff_effective

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

_TEST_SKEWNESS = 0.19906188837146524

_TEST_ELECTRIC_FORM_FACTOR_FE = 0.648238
_TEST_MAGNETIC_FORM_FACTOR_FG = 1.81043
_TEST_DIRAC_FORM_FACTOR_F1 = -21.9835
_TEST_PAULI_FORM_FACTOR_F2 = 23.794
_TEST_CFF_REAL_H = -0.897
_TEST_CFF_REAL_H_TILDE = 2.444
_TEST_CFF_REAL_E = -0.541
_TEST_CFF_REAL_E_TILDE = 2.207
_TEST_CFF_IMAGINARY_H = 2.421
_TEST_CFF_IMAGINARY_H_TILDE = 1.131
_TEST_CFF_IMAGINARY_E = 0.903
_TEST_CFF_IMAGINARY_E_TILDE = 5.383

_TEST_VERBOSE = False

class TestFormFactors(unittest.TestCase):

    def test_effective_cff_real_h(self):
        """
        ## Description:
        Test Re[H]'s effective value *without WW relations on*.
        """
        self.assertAlmostEqual(
            compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_REAL_H, _TEST_VERBOSE),
            0.29783035488137793)
    
    def test_effective_cff_real_ht(self):
        """
        ## Description:
        Test Re[Ht]'s effective value *without WW relations on*.
        """

        self.assertAlmostEqual(
            compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_REAL_H_TILDE ,_TEST_VERBOSE),
            -0.8114798075028848)
    
    def test_effective_cff_real_e(self):
        """
        ## Description:
        Test Re[E]'s effective value *without WW relations on*.
        """
        self.assertAlmostEqual(
            compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_REAL_E, _TEST_VERBOSE),
            0.17962789519601502)
    
    def test_effective_cff_real_et(self):
        """
        ## Description:
        Test Re[Et]'s effective value *without WW relations on*.
        """
        self.assertAlmostEqual(
            compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_REAL_E_TILDE, _TEST_VERBOSE),
            -0.7327888441730223)
    
    def test_effective_cff_imag_h(self):
        """
        ## Description:
        Test Im[H]'s effective value *without WW relations on*.
        """
        self.assertAlmostEqual(
            compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_IMAGINARY_H, _TEST_VERBOSE),
            -0.8038431317366954)
    
    def test_effective_cff_imag_ht(self):
        """
        ## Description:
        Test Im[Ht]'s effective value *without WW relations on*.
        """
        self.assertAlmostEqual(
            compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_IMAGINARY_H_TILDE ,_TEST_VERBOSE),
            -0.37552523006782434)
    
    def test_effective_cff_imag_e(self):
        """
        ## Description:
        Test Im[E]'s effective value *without WW relations on*.
        """
        self.assertAlmostEqual(
            compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_IMAGINARY_E, _TEST_VERBOSE),
            -0.2998225311682099)
        
    def test_effective_cff_imag_et(self):
        """
        ## Description:
        Test Im[Et]'s effective value *without WW relations on*.
        """
        self.assertAlmostEqual(
            compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_IMAGINARY_E_TILDE, _TEST_VERBOSE),
            -1.787314158669406)
        
    def test_effective_cff_real_h_ww(self):
        """
        ## Description:
        Test Re[H]'s effective value *with WW relations on*.
        """
        self.assertAlmostEqual(
            compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_REAL_H, True, _TEST_VERBOSE),
            -1.4961696451186222)
    
    def test_effective_cff_real_ht_ww(self):
        """
        ## Description:
        Test Re[Ht]'s effective value *with WW relations on*.
        """

        self.assertAlmostEqual(
            compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_REAL_H_TILDE, True, _TEST_VERBOSE),
            4.0765201924971155)
    
    def test_effective_cff_real_e_ww(self):
        """
        ## Description:
        Test Re[E]'s effective value *with WW relations on*.
        """
        self.assertAlmostEqual(
            compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_REAL_E, True, _TEST_VERBOSE),
            -0.9023721048039851)
    
    def test_effective_cff_real_et_ww(self):
        """
        ## Description:
        Test Re[Et]'s effective value *with WW relations on*.
        """
        self.assertAlmostEqual(
            compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_REAL_E_TILDE, True, _TEST_VERBOSE),
            3.6812111558269773)
    
    def test_effective_cff_imag_h_ww(self):
        """
        ## Description:
        Test Im[H]'s effective value *with WW relations on*.
        """
        self.assertAlmostEqual(
            compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_IMAGINARY_H, True,_TEST_VERBOSE),
            4.038156868263304)
    
    def test_effective_cff_imag_ht_ww(self):
        """
        ## Description:
        Test Im[Ht]'s effective value *with WW relations on*.
        """
        self.assertAlmostEqual(
            compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_IMAGINARY_H_TILDE, True, _TEST_VERBOSE),
            1.8864747699321758)
    
    def test_effective_cff_imag_e_ww(self):
        """
        ## Description:
        Test Im[E]'s effective value *with WW relations on*.
        """
        self.assertAlmostEqual(
            compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_IMAGINARY_E, True, _TEST_VERBOSE),
            1.5061774688317902)
        
    def test_effective_cff_imag_et_ww(self):
        """
        ## Description:
        Test Im[Et]'s effective value *with WW relations on*.
        """
        self.assertAlmostEqual(
            compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_IMAGINARY_E_TILDE, True,  _TEST_VERBOSE),
            8.978685841330593)