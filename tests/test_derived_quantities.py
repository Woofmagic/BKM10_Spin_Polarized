import unittest

from derived_kinematics.epsilon import calculate_kinematics_epsilon
from derived_kinematics.lepton_energy_fraction import calculate_kinematics_lepton_energy_fraction_y
from derived_kinematics.skewness import calculate_kinematics_skewness_parameter
from derived_kinematics.t_minimum import calculate_kinematics_t_min
from derived_kinematics.t_prime import calculate_kinematics_t_prime
from derived_kinematics.k_tilde import calculate_kinematics_k_tilde
from derived_kinematics.shorthand_K import calculate_kinematics_k
from derived_kinematics.k_dot_delta import calculate_k_dot_delta
from derived_kinematics.lepton_propagator_p1 import calculate_lepton_propagator_p1
from derived_kinematics.lepton_propagator_p2 import calculate_lepton_propagator_p2

from form_factors.electric_form_factor import calculate_form_factor_electric
from form_factors.magnetic_form_factor import calculate_form_factor_magnetic
from form_factors.pauli_form_factor import calculate_form_factor_pauli_f2
from form_factors.dirac_form_factor import calculate_form_factor_dirac_f1

from amplitudes.cross_section_prefactor import calculate_bkm10_cross_section_prefactor

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

class TestDerivedKinematics(unittest.TestCase):

    def test_calculate_kinematics_epsilon(self):
        """
        ## Description: Test the calculation of epsilon.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        self.assertAlmostEqual(
            calculate_kinematics_epsilon(
                _TEST_SQUARED_Q_MOMENTUM_TRANSFER,
                _TEST_X_BJORKEN,
                _TEST_VERBOSE), 
            0.47293561004973345)