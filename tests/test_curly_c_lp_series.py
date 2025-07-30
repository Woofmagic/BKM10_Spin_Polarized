import unittest

from coefficients.interference_coefficients.unpolarized.unpolarized_curly_C import calculate_curly_C_unpolarized_interference
from coefficients.interference_coefficients.unpolarized.unpolarized_curly_CV import calculate_curly_C_unpolarized_interference_V
from coefficients.interference_coefficients.unpolarized.unpolarized_curly_CA import calculate_curly_C_unpolarized_interference_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_CLP import calculate_curly_C_longitudinally_polarized_interference
from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_CLPV import calculate_curly_C_longitudinally_polarized_interference_V
from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_CLPA import calculate_curly_C_longitudinally_polarized_interference_A

from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_Cpp import calculate_curly_C_plus_plus_longitudinally_polarized_interference
from coefficients.interference_coefficients.lp_polarized.lp_polarized_curly_C0p import calculate_curly_C_zero_plus_longitudinally_polarized_interference

from form_factors.effective_cffs import compute_cff_effective

_TEST_CASES = [
    {
        "lab_kinematics_k": 5.75,
        "squared_q_momentum_transfer": 1.82,
        "x_bjorken": 0.34,
        "squared_hadronic_momentum_transfer": -0.17,
        "epsilon": 0.47293561004973345,
        "lepton_energy_fraction": 0.49609612355928445,
        "skewness": 0.19906188837146524,
        "t_minimum": -0.13551824472915253,
        "t_prime": -0.034481755270847486,
        "k_tilde": 0.1592415651944438,
        "expected_epsilon": 0.47293561004973345,
        "expected_lepton_energy_fraction": 0.49609612355928445,
        "expected_skewness": 0.19906188837146524,
        "expected_t_minimum": -0.13551824472915253,
        "expected_t_prime": -0.034481755270847486,
        "expected_k_tilde": 0.1592415651944438,
        "expected_shorthand_k": 0.08492693191323883,
    },
    {
        "lab_kinematics_k": 10.59,
        "squared_q_momentum_transfer": 4.55,
        "x_bjorken": 0.37,
        "squared_hadronic_momentum_transfer": -0.26,
        "epsilon": 0.3255028672427054,
        "lepton_energy_fraction": 0.6188065752739715,
        "skewness": 0.2234061445569171,
        "t_minimum": -0.17914464172739256,
        "t_prime": -0.08085535827260745,
        "k_tilde": 0.2322551942737076,
        "expected_epsilon": 0.3255028672427054,
        "expected_lepton_energy_fraction": 0.6188065752739715,
        "expected_skewness": 0.2234061445569171,
        "expected_t_minimum": -0.17914464172739256,
        "expected_t_prime": -0.08085535827260745,
        "expected_k_tilde": 0.2322551942737076,
        "expected_shorthand_k": 0.06811374886346015,
    }
]

_TEST_LEPTON_POLARIZATION = 1.0
_TEST_TARGET_POLARIZATION = 0.5

_TEST_SQUARED_Q_MOMENTUM_TRANSFER = 1.82
_TEST_X_BJORKEN = 0.34
_TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER = -0.17

_TEST_EPSILON = 0.47293561004973345
_TEST_LEPTON_ENERGY_FRACTION = 0.49609612355928445
_TEST_K_TILDE = 0.1592415651944438
_TEST_SHORTHAND_K = 0.08492693191323883
_TEST_T_PRIME = -0.034481755270847486

_TEST_SKEWNESS = 0.19906188837146524

_TEST_ELECTRIC_FORM_FACTOR_FE = 0.648238
_TEST_MAGNETIC_FORM_FACTOR_FG = 1.81043
_TEST_DIRAC_FORM_FACTOR_F1 = 0.7049508167585219
_TEST_PAULI_FORM_FACTOR_F2 = 1.1137103937669304

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

class TestCurlyCLongitudinallyPolarizedSeriesCoefficients(unittest.TestCase):

    def test_calculate_curly_C_unpolarized_interference(self):
        """
        ## Description: Test the function `calculate_curly_C_unpolarized_interference`.
        This is curly C I (unpolarized)

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_curly_C_unpolarized_interference(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_CFF_REAL_H,
                _TEST_CFF_REAL_H_TILDE,
                _TEST_CFF_REAL_E,
                _TEST_VERBOSE), 
            20.024667250345)

    def test_calculate_curly_C_unpolarized_interference_V(self):
        """
        ## Description: Test the function `calculate_curly_C_unpolarized_interference_V`.
        This is curly C I V (unpolarized)

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_curly_C_unpolarized_interference_V(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_CFF_REAL_H,
                _TEST_CFF_REAL_E,
                _TEST_VERBOSE), 
            -0.54965740801746)
    
    def test_calculate_curly_C_unpolarized_interference_A(self):
        """
        ## Description: Test the function `calculate_curly_C_unpolarized_interference_A`.
        This is curly C I A (unpolarized)

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_curly_C_unpolarized_interference_A(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_CFF_REAL_H_TILDE,
                _TEST_VERBOSE), 
            0.93418825117849)
    
    def test_calculate_curly_C_longitudinally_polarized_interference(self):
        """
        ## Description: Test the function `test_calculate_curly_C_longitudinally_polarized_interference`.
        These Curly Cs don't rely on the helicity flip of the lepton or not, so they
        are easy to test.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        
        # (1): First, evaluate it with normal CFFs:
        self.assertAlmostEqual(
            calculate_curly_C_longitudinally_polarized_interference(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_CFF_H,
                _TEST_CFF_H_TILDE,
                _TEST_CFF_E,
                _TEST_CFF_E_TILDE,
                _TEST_VERBOSE),
            complex(1.5144078323497445, 1.7888998121367863))
        
        # (2): Now, we evaluate it with F_{eff} with WW = Off:
        self.assertAlmostEqual(
            calculate_curly_C_longitudinally_polarized_interference(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H, False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE, False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E, False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E_TILDE, False),
                _TEST_VERBOSE),
            complex(-0.5028278953666251, -0.5939672975428422 ))
        
        # (3): Now, we evaluate it with F_{eff} with WW = On:
        self.assertAlmostEqual(
            calculate_curly_C_longitudinally_polarized_interference(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H, True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE, True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E, True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E_TILDE, True),
                _TEST_VERBOSE),
            complex(2.525987769332864, 2.9838323267307305))
    
    def test_calculate_curly_C_longitudinally_polarized_interference_V(self):
        """
        ## Description: Test the function `calculate_curly_C_longitudinally_polarized_interference_V`.
        These Curly Cs don't rely on the helicity flip of the lepton or not, so they
        are easy to test.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """

        # (1): First, evaluate it with normal CFFs:
        self.assertAlmostEqual(
            calculate_curly_C_longitudinally_polarized_interference_V(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_CFF_H,
                _TEST_CFF_E,
                _TEST_VERBOSE),
            complex(-0.3788358951249188, 0.9831471548237565))
        
        # (2): Now, we evaluate it with F_{eff} with WW = Off:
        self.assertAlmostEqual(
            calculate_curly_C_longitudinally_polarized_interference_V(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H, False),
                compute_cff_effective(_TEST_SKEWNESS,_TEST_CFF_E, False),
                _TEST_VERBOSE),
            complex(0.12578464781143706, -0.3264337413843661))
        
        # (3): Now, we evaluate it with F_{eff} with WW = On:
        self.assertAlmostEqual(
            calculate_curly_C_longitudinally_polarized_interference_V(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                compute_cff_effective(_TEST_SKEWNESS,_TEST_CFF_H, True),
                compute_cff_effective(_TEST_SKEWNESS,_TEST_CFF_E, True),
                _TEST_VERBOSE),
            complex(-0.6318871424384005, 1.6398605682631469))
        
    def test_calculate_curly_C_longitudinally_polarized_interference_A(self):
        """
        ## Description: Test the function `calculate_curly_C_longitudinally_polarized_interference_A`.
        These Curly Cs don't rely on the helicity flip of the lepton or not, so they
        are easy to test.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        
        # (1): First, evaluate it with normal CFFs:
        self.assertAlmostEqual(
            calculate_curly_C_longitudinally_polarized_interference_A(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                _TEST_CFF_H_TILDE,
                _TEST_CFF_E_TILDE,
                _TEST_VERBOSE), 
            complex(1.3759089266214655, 0.9183117895068561))
        
        # (2): Now, we evaluate it with F_{eff} with WW = Off:
        self.assertAlmostEqual(
            calculate_curly_C_longitudinally_polarized_interference_A(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE, False),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E_TILDE, False),
                _TEST_VERBOSE),
            complex(-0.4568421894092831, -0.30490649516229673))
        
        # (3): Now, we evaluate it with F_{eff} with WW = On:
        self.assertAlmostEqual(
            calculate_curly_C_longitudinally_polarized_interference_A(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_SQUARED_HADRONIC_MOMENTUM_TRANSFER,
                _TEST_DIRAC_FORM_FACTOR_F1,
                _TEST_PAULI_FORM_FACTOR_F2,
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_H_TILDE, True),
                compute_cff_effective(_TEST_SKEWNESS, _TEST_CFF_E_TILDE, True),
                _TEST_VERBOSE), 
            complex(2.2949756638336485, 1.5317170838514154))