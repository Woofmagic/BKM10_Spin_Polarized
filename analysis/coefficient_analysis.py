import numpy as np
import matplotlib.pyplot as plt

from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp0 import calculate_c_0_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp1 import calculate_c_1_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp2 import calculate_c_2_plus_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp3 import calculate_c_3_plus_plus_unpolarized

from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp0V import calculate_c_0_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp1V import calculate_c_1_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp2V import calculate_c_2_plus_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp3V import calculate_c_3_plus_plus_unpolarized_V

from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp0A import calculate_c_0_plus_plus_unpolarized_A
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp1A import calculate_c_1_plus_plus_unpolarized_A
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp2A import calculate_c_2_plus_plus_unpolarized_A
from coefficients.interference_coefficients.unpolarized.unpolarized_Cpp3A import calculate_c_3_plus_plus_unpolarized_A

from coefficients.interference_coefficients.unpolarized.unpolarized_C0p0 import calculate_c_0_zero_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p1 import calculate_c_1_zero_plus_unpolarized
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p2 import calculate_c_2_zero_plus_unpolarized

from coefficients.interference_coefficients.unpolarized.unpolarized_C0p0V import calculate_c_0_zero_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p1V import calculate_c_1_zero_plus_unpolarized_V
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p2V import calculate_c_2_zero_plus_unpolarized_V

from coefficients.interference_coefficients.unpolarized.unpolarized_C0p0A import calculate_c_0_zero_plus_unpolarized_A
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p1A import calculate_c_1_zero_plus_unpolarized_A
from coefficients.interference_coefficients.unpolarized.unpolarized_C0p2A import calculate_c_2_zero_plus_unpolarized_A

def calculate_coefficients_independently(
    lepton_polarization: float,
    target_polarization: float,
    squared_Q_momentum_transfer: float,
    x_Bjorken: float,
    squared_hadronic_momentum_transfer_t: float,
    azimuthal_phi: float,
    epsilon: float,
    lepton_energy_fraction_y: float,
    skewness_parameter: float,
    t_prime: float,
    k_tilde: float,
    shorthand_k: float,
    lepton_propagator_p1: float,
    lepton_propagator_p2: float,
    Dirac_form_factor_F1: float,
    Pauli_form_factor_F2: float,
    compton_form_factor_h: complex,
    compton_form_factor_h_tilde: complex,
    compton_form_factor_e: complex,
    compton_form_factor_e_tilde: complex,
    verbose):
    
    c_0_plus_plus = calculate_c_0_plus_plus_unpolarized(squared_Q_momentum_transfer,x_Bjorken,squared_hadronic_momentum_transfer_t,epsilon,lepton_energy_fraction_y,k_tilde,verbose)
    c_1_plus_plus = calculate_c_1_plus_plus_unpolarized(squared_Q_momentum_transfer,x_Bjorken,squared_hadronic_momentum_transfer_t,epsilon,lepton_energy_fraction_y,shorthand_k,verbose)
    c_2_plus_plus = calculate_c_2_plus_plus_unpolarized(squared_Q_momentum_transfer,x_Bjorken,squared_hadronic_momentum_transfer_t,epsilon,lepton_energy_fraction_y,t_prime,k_tilde,verbose)
    c_3_plus_plus = calculate_c_3_plus_plus_unpolarized(squared_Q_momentum_transfer,x_Bjorken,squared_hadronic_momentum_transfer_t,epsilon,lepton_energy_fraction_y,shorthand_k,verbose)
    
    c_0_V_plus_plus = calculate_c_0_plus_plus_unpolarized_V(squared_Q_momentum_transfer,x_Bjorken,squared_hadronic_momentum_transfer_t,epsilon,lepton_energy_fraction_y,k_tilde,verbose)
    c_1_V_plus_plus = calculate_c_1_plus_plus_unpolarized_V(squared_Q_momentum_transfer,x_Bjorken,squared_hadronic_momentum_transfer_t,epsilon,lepton_energy_fraction_y,t_prime,shorthand_k,verbose)
    c_2_V_plus_plus = calculate_c_2_plus_plus_unpolarized_V(squared_Q_momentum_transfer,x_Bjorken,squared_hadronic_momentum_transfer_t,epsilon,lepton_energy_fraction_y,t_prime,k_tilde,verbose)
    c_3_V_plus_plus = calculate_c_3_plus_plus_unpolarized_V(squared_Q_momentum_transfer,x_Bjorken,squared_hadronic_momentum_transfer_t,epsilon,lepton_energy_fraction_y,shorthand_k,verbose)

    c_0_A_plus_plus = calculate_c_0_plus_plus_unpolarized_A(squared_Q_momentum_transfer,x_Bjorken,squared_hadronic_momentum_transfer_t,epsilon,lepton_energy_fraction_y,k_tilde,verbose)
    c_1_A_plus_plus = calculate_c_1_plus_plus_unpolarized_A(squared_Q_momentum_transfer,x_Bjorken,squared_hadronic_momentum_transfer_t,epsilon,lepton_energy_fraction_y,t_prime,shorthand_k,verbose)
    c_2_A_plus_plus = calculate_c_2_plus_plus_unpolarized_A(squared_Q_momentum_transfer,x_Bjorken,squared_hadronic_momentum_transfer_t,epsilon,lepton_energy_fraction_y,t_prime,k_tilde,verbose)
    c_3_A_plus_plus = calculate_c_3_plus_plus_unpolarized_A(squared_Q_momentum_transfer,x_Bjorken,squared_hadronic_momentum_transfer_t,epsilon,lepton_energy_fraction_y,t_prime,shorthand_k,verbose)

    c_0_zero_plus = calculate_c_0_zero_plus_unpolarized(squared_Q_momentum_transfer,x_Bjorken,squared_hadronic_momentum_transfer_t,epsilon,lepton_energy_fraction_y,shorthand_k,verbose)
    c_1_zero_plus = calculate_c_1_zero_plus_unpolarized(squared_Q_momentum_transfer,x_Bjorken,squared_hadronic_momentum_transfer_t,epsilon,lepton_energy_fraction_y,t_prime,verbose)
    c_2_zero_plus = calculate_c_2_zero_plus_unpolarized(squared_Q_momentum_transfer,x_Bjorken,squared_hadronic_momentum_transfer_t,epsilon,lepton_energy_fraction_y,shorthand_k,verbose)
    c_3_zero_plus = 0.

    

    results = np.array([c_0_plus_plus, c_1_plus_plus, c_2_plus_plus, c_3_plus_plus])

fourier_coefficient_labels = {
    'unpolarized_coefficient_plus_plus_n_equals_0': r'$C_{++}^{unp} \left ( n = 0 \right)$',
    'unpolarized_coefficient_plus_plus_n_equals_1': r'$C_{++}^{unp} \left ( n = 1 \right)$',
    'unpolarized_coefficient_plus_plus_n_equals_2': r'$C_{++}^{unp} \left ( n = 2 \right)$',
    'unpolarized_coefficient_plus_plus_n_equals_3': r'$C_{++}^{unp} \left ( n = 3 \right)$',
    'unpolarized_coefficient_plus_plus_V_n_equals_0': r'$C_{++}^{unp, V} \left ( n = 0 \right)$',
    'unpolarized_coefficient_plus_plus_V_n_equals_1': r'$C_{++}^{unp, V} \left ( n = 1 \right)$',
    'unpolarized_coefficient_plus_plus_V_n_equals_2': r'$C_{++}^{unp, V} \left ( n = 2 \right)$',
    'unpolarized_coefficient_plus_plus_V_n_equals_3': r'$C_{++}^{unp, V} \left ( n = 3 \right)$',
    'unpolarized_coefficient_plus_plus_A_n_equals_0': r'$C_{++}^{unp, A} \left ( n = 0 \right)$',
    'unpolarized_coefficient_plus_plus_A_n_equals_1': r'$C_{++}^{unp, A} \left ( n = 1 \right)$',
    'unpolarized_coefficient_plus_plus_A_n_equals_2': r'$C_{++}^{unp, A} \left ( n = 2 \right)$',
    'unpolarized_coefficient_plus_plus_A_n_equals_3': r'$C_{++}^{unp, A} \left ( n = 3 \right)$',
    'unpolarized_coefficient_zero_plus_n_equals_0': r'$C_{0+}^{unp} \left ( n = 0 \right)$',
    'unpolarized_coefficient_zero_plus_n_equals_1': r'$C_{0+}^{unp} \left ( n = 1 \right)$',
    'unpolarized_coefficient_zero_plus_n_equals_2': r'$C_{0+}^{unp} \left ( n = 2 \right)$',
    'unpolarized_coefficient_zero_plus_V_n_equals_0': r'$C_{0+}^{unp, V} \left ( n = 0 \right)$',
    'unpolarized_coefficient_zero_plus_V_n_equals_1': r'$C_{0+}^{unp, V} \left ( n = 1 \right)$',
    'unpolarized_coefficient_zero_plus_V_n_equals_2': r'$C_{0+}^{unp, V} \left ( n = 2 \right)$',
    'unpolarized_coefficient_zero_plus_A_n_equals_0': r'$C_{0+}^{unp, A} \left ( n = 0 \right)$',
    'unpolarized_coefficient_zero_plus_A_n_equals_1': r'$C_{0+}^{unp, A} \left ( n = 1 \right)$',
    'unpolarized_coefficient_zero_plus_A_n_equals_2': r'$C_{0+}^{unp, A} \left ( n = 2 \right)$',

}

histogram_labels = [
    fourier_coefficient_labels['unpolarized_coefficient_plus_plus_n_equals_0'], 
    fourier_coefficient_labels['unpolarized_coefficient_plus_plus_n_equals_1'], 
    fourier_coefficient_labels['unpolarized_coefficient_plus_plus_n_equals_2'],
    fourier_coefficient_labels['unpolarized_coefficient_plus_plus_n_equals_3'],
    fourier_coefficient_labels['unpolarized_coefficient_plus_plus_V_n_equals_1'], 
    fourier_coefficient_labels['unpolarized_coefficient_plus_plus_V_n_equals_2'], 
    fourier_coefficient_labels['unpolarized_coefficient_plus_plus_V_n_equals_3'],
    fourier_coefficient_labels['unpolarized_coefficient_plus_plus_A_n_equals_0'],
    fourier_coefficient_labels['unpolarized_coefficient_plus_plus_A_n_equals_1'], 
    fourier_coefficient_labels['unpolarized_coefficient_plus_plus_A_n_equals_2'], 
    fourier_coefficient_labels['unpolarized_coefficient_plus_plus_A_n_equals_3'],
    fourier_coefficient_labels['unpolarized_coefficient_zero_plus_n_equals_0'],
    fourier_coefficient_labels['unpolarized_coefficient_zero_plus_n_equals_1'], 
    fourier_coefficient_labels['unpolarized_coefficient_zero_plus_n_equals_2'], 
    fourier_coefficient_labels['unpolarized_coefficient_zero_plus_V_n_equals_0'],
    fourier_coefficient_labels['unpolarized_coefficient_zero_plus_V_n_equals_1'],
    fourier_coefficient_labels['unpolarized_coefficient_zero_plus_V_n_equals_2'], 
    fourier_coefficient_labels['unpolarized_coefficient_zero_plus_A_n_equals_0'], 
    fourier_coefficient_labels['unpolarized_coefficient_zero_plus_A_n_equals_1'],
    fourier_coefficient_labels['unpolarized_coefficient_zero_plus_A_n_equals_2'],
]

plt.figure(figsize=(10, 6))
plt.bar(
    x = range(len(results)), 
    height = results, 
    tick_label = histogram_labels,
    color = plt.get_cmap("viridis").colors)

plt.xticks(rotation = 45)
plt.xlabel('Fourier Coefficients')
plt.ylabel('Numerical Value [dimensionless]')
plt.title(r'Unpolarized Fourier Coefficient Analysis, $C_{\alpha \beta}^{unp} \left( n \right)$')
plt.show()
