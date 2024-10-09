import numpy as np
import matplotlib.pyplot as plt

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

results = np.random.rand(len(histogram_labels))

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
