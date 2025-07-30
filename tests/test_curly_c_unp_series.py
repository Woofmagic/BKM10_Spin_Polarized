import unittest

from coefficients.interference_coefficients.unpolarized.unpolarized_curly_C import calculate_curly_C_unpolarized_interference
from coefficients.interference_coefficients.unpolarized.unpolarized_curly_CV import calculate_curly_C_unpolarized_interference_V
from coefficients.interference_coefficients.unpolarized.unpolarized_curly_CA import calculate_curly_C_unpolarized_interference_A

from form_factors.effective_cffs import compute_cff_effective

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

_TEST_ELECTRIC_FORM_FACTOR_FE = 0.648238
_TEST_MAGNETIC_FORM_FACTOR_FG = 1.81043
_TEST_DIRAC_FORM_FACTOR_F1 = 0.7049508167585219
_TEST_PAULI_FORM_FACTOR_F2 = 1.1137103937669304

_TEST_SKEWNESS = 0.19906188837146524

_TEST_CFF_REAL_H = -0.897
_TEST_CFF_REAL_H_TILDE = 2.444
_TEST_CFF_REAL_E = -0.541
_TEST_CFF_REAL_E_TILDE = 2.207

_TEST_CFF_IMAGINARY_H = 2.421
_TEST_CFF_IMAGINARY_H_TILDE = 1.131
_TEST_CFF_IMAGINARY_E = 0.903
_TEST_CFF_IMAGINARY_E_TILDE = 5.383

_TEST_CFF_H = complex(_TEST_CFF_REAL_H, _TEST_CFF_IMAGINARY_H)
_TEST_CFF_H_TILDE = complex(_TEST_CFF_REAL_H_TILDE, _TEST_CFF_IMAGINARY_H_TILDE)
_TEST_CFF_E = complex(_TEST_CFF_REAL_E, _TEST_CFF_IMAGINARY_E)
_TEST_CFF_E_TILDE = complex(_TEST_CFF_REAL_E_TILDE, _TEST_CFF_IMAGINARY_E_TILDE)

_TEST_VERBOSE = False

class TestCurlyCUnpolarizedSeriesCoefficients(unittest.TestCase):

    def test_calculate_curly_C_unpolarized_interference_normal_cffs(self):
        """
        ## Description: Test the function computing C^{I}(F)
        These Curly Cs don't rely on the helicity flip of the lepton or not, so they
        are easy to test.
        """
        self.assertAlmostEqual(
            calculate_curly_C_unpolarized_interference(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_CFF_H,
                _TEST_CFF_H_TILDE,
                _TEST_CFF_E,
                _TEST_VERBOSE), 
            complex(0.266711013189341, 2.1847473098840733))
        
    def test_calculate_curly_C_unpolarized_interference_eff_cffs_ww_off(self):
        """
        ## Description: Test the function computing C^{I}(F_{eff}) *without* the WW Relations!
        These Curly Cs don't rely on the helicity flip of the lepton or not, so they
        are easy to test.
        """
        self.assertAlmostEqual(
            calculate_curly_C_unpolarized_interference(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H, use_ww = False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE, use_ww = False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E, use_ww = False),
                _TEST_VERBOSE), 
            complex(-0.08855589265212185, -0.7254002972451608))
        
    def test_calculate_curly_C_unpolarized_interference_eff_cffs_ww_on(self):
        """
        ## Description: Test the function computing C^{I}(F_{eff}) *using* the WW Relations!
        These Curly Cs don't rely on the helicity flip of the lepton or not, so they
        are easy to test.
        """
        self.assertAlmostEqual(
            calculate_curly_C_unpolarized_interference(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H, use_ww = True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE, use_ww = True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E, use_ww = True),
                _TEST_VERBOSE), 
            complex(0.44486613372656025, 3.6440943225229856))
        
    def test_calculate_curly_C_unpolarized_interference_V_normal_cffs(self):
        """
        ## Description: Test the function computing C^{I,V}(F) 
        """
        self.assertAlmostEqual(
            calculate_curly_C_unpolarized_interference_V(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_CFF_H,
                _TEST_CFF_E,
                _TEST_VERBOSE), 
            complex(-0.5460981666569447, 1.2623298372515186))
        
    def test_calculate_curly_C_unpolarized_interference_V_eff_cffs_ww_off(self):
        """
        ## Description: Test the function computing C^{I,V}(F) *without* the WW Relations!
        """
        self.assertAlmostEqual(
            calculate_curly_C_unpolarized_interference_V(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H, use_ww = False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E, use_ww = False),
                _TEST_VERBOSE),
            complex(0.1813206363160621, -0.41913059465548697))
        
    def test_calculate_curly_C_unpolarized_interference_V_eff_cffs_ww_on(self):
        """
        ## Description: Test the function computing C^{I,V}(F) *using* the WW Relations!
        """
        self.assertAlmostEqual(
            calculate_curly_C_unpolarized_interference_V(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H, use_ww = True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E, use_ww = True),
                _TEST_VERBOSE), 
            complex(-0.9108756969978273, 2.10552907984755))
        
    def test_calculate_curly_C_unpolarized_interference_A_normal_cffs(self):
        """
        ## Description: Test the function computing C^{I,A}(F)
        """
        self.assertAlmostEqual(
            calculate_curly_C_unpolarized_interference_A(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_CFF_H_TILDE,
                _TEST_VERBOSE),
            complex(0.9281390259454608, 0.42951114498539944))
        
    def test_calculate_curly_C_unpolarized_interference_A_eff_cffs_ww_off(self):
        """
        ## Description: Test the function computing C^{I,A}(F) *without* the WW Relations!
        """
        self.assertAlmostEqual(
            calculate_curly_C_unpolarized_interference_A(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE, use_ww = False),
                _TEST_VERBOSE),
            complex(-0.30816942639531, -0.1426103196616594))
        
    def test_calculate_curly_C_unpolarized_interference_A_eff_cffs_ww_on(self):
        """
        ## Description: Test the function computing C^{I,A}(F) *using* the WW Relations!
        """
        self.assertAlmostEqual(
            calculate_curly_C_unpolarized_interference_A(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE, use_ww = True),
                _TEST_VERBOSE),
            complex(1.5481086254956118, 0.7164119703091395))
        