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

_TEST_VERBOSE = False

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
        for case in _TEST_CASES:
            with self.subTest(case = case):
                self.assertAlmostEqual(
                    calculate_kinematics_epsilon(
                        case["squared_q_momentum_transfer"],
                        case["x_bjorken"],
                        _TEST_VERBOSE
                    ),
                    case["expected_epsilon"]
                )
        
    def test_calculate_kinematics_lepton_energy_fraction(self):
        """
        ## Description: Test the calculation of y, lepton energy
        fraction.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        for case in _TEST_CASES:
            with self.subTest(case = case):
                self.assertAlmostEqual(
                    calculate_kinematics_lepton_energy_fraction_y(
                        case["squared_q_momentum_transfer"],
                        case["lab_kinematics_k"],
                        case["epsilon"],
                        _TEST_VERBOSE),
                case["expected_lepton_energy_fraction"])
        
    def test_calculate_skewness(self):
        """
        ## Description: Test the computation of the skewness
        parameter.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        for case in _TEST_CASES:
            with self.subTest(case = case):
                self.assertAlmostEqual(
                    calculate_kinematics_skewness_parameter(
                        case["squared_q_momentum_transfer"],
                        case["x_bjorken"],
                        case["squared_hadronic_momentum_transfer"],
                        _TEST_VERBOSE), 
                    case["skewness"])
        
    def test_calculate_t_minimum(self):
        """
        ## Description: Test the computation of t_min.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        for case in _TEST_CASES:
            with self.subTest(case = case):
                self.assertAlmostEqual(
                    calculate_kinematics_t_min(
                        case["squared_q_momentum_transfer"],
                        case["x_bjorken"],
                        case["epsilon"],
                        _TEST_VERBOSE),
                    case["expected_t_minimum"])
        
    def test_calculate_t_prime(self):
        """
        ## Description: Test the computation of t prime.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        for case in _TEST_CASES:
            with self.subTest(case = case):
                self.assertAlmostEqual(
                    calculate_kinematics_t_prime(
                        case["squared_hadronic_momentum_transfer"],
                        case["t_minimum"],
                        _TEST_VERBOSE),
                    case["expected_t_prime"])
        
    def test_calculate_k_tilde(self):
        """
        ## Description: Test the computation of K tilde.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        for case in _TEST_CASES:
            with self.subTest(case = case):
                self.assertAlmostEqual(
                    calculate_kinematics_k_tilde(
                        case["squared_q_momentum_transfer"],
                        case["x_bjorken"],
                        case["lepton_energy_fraction"],
                        case["squared_hadronic_momentum_transfer"],
                        case["epsilon"],
                        case["t_minimum"],
                        _TEST_VERBOSE),
                    case["expected_k_tilde"])
        
    def test_calculate_k_shorthand(self):
        """
        ## Description: Test the computation of K.

        ## Arguments:
        None

        ## Returns:
        None

        ## Examples:
        None
        """
        for case in _TEST_CASES:
            with self.subTest(case = case):
                self.assertAlmostEqual(
                    calculate_kinematics_k(
                        case["squared_q_momentum_transfer"],
                        case["lepton_energy_fraction"],
                        case["epsilon"],
                        case["k_tilde"],
                        _TEST_VERBOSE), 
                    case["expected_shorthand_k"])