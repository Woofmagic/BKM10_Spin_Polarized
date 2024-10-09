import numpy as np
import matplotlib.pyplot as plt

results = np.random.rand(100)

fourier_coefficient_labels = {
    'unpolarized_coefficient_plus_plus_n_equals_0': r'$C_{++}^{unp} \left ( n = 0 \right)$',
    'unpolarized_coefficient_plus_plus_n_equals_1': r'$C_{++}^{unp} \left ( n = 1 \right)$',
    'unpolarized_coefficient_plus_plus_n_equals_2': r'$C_{++}^{unp} \left ( n = 2 \right)$',
}

histogram_labels = [
    fourier_coefficient_labels['unpolarized_coefficient_plus_plus_n_equals_0'], 
    fourier_coefficient_labels['unpolarized_coefficient_plus_plus_n_equals_0'], 
    fourier_coefficient_labels['unpolarized_coefficient_plus_plus_n_equals_0']
]

plt.figure(figsize=(10, 6))
plt.bar(
    x = range(len(results)), 
    heights = results, 
    tick_label = histogram_labels)

plt.xlabel('Subfunction')
plt.ylabel('Result')
plt.title(r'UnpolarizedFourier Coefficient Analysis, $C_{\alpha \beta}^{unp} \left( n \right)$')
plt.show()
