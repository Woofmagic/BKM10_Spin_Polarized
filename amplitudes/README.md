# Amplitude Squared Contributions

There are three contributions.

## Bethe-Heitler Process:

## Deeply-Virtual Compton Scattering (DVCS) Process:

## Interference:

The contribution from the interference terms are a major pain. We have to iterate through $n \in \left{ 0, 1, 2, 3 \right}$ and compute $s_{n}^{I}$.

The chronology of the calculation is the following:

1. Calculate the prefactor: $$\frac{1}{x_{B} y^{3} t P_{1} (\phi) P_{2} (\phi)}.$$

Please note that we do not include the electric charge $e$ because it gets canceled out in the overall prefactor of the amplitude. (The sign still matters!) Proof is an exercise for the reader.

2. Calculate $c_{0}^{I}$. This coefficient is always here and does not require any fancy iteration. This calls `calculate_c_interference_coefficient` with $n = 0$.

    1. Calculates $C_{++}(n = 0)$.
    2. Calculates $C_{0+}(n = 0)$.
    3. Calculates $C_{-+}(n = 0)$.
    4. Calculates $\mathcal{C}_{++}^{I}(n = 0 | \mathcal{F})$, passing in $\text{Re}[\mathcal{F}]$ only.
    5. Calculates $\mathcal{C}_{0+}^{I}(n = 0 | \mathcal{F}_{\text{Eff}})$, passing in $\text{Re}[\mathcal{F}_{\text{Eff}}]$ only.
    6. Calculates $\mathcal{C}_{-+}^{I}(n = 0 | \mathcal{F}_{\text{T}})$, passing in $\text{Re}[\mathcal{F}_{\text{T}}]$ only.

3. Calculate $c_{1}^{I}$. Again, this calls `calculate_c_interference_coefficient` with $n = 1$.

    1. Calculates $C_{++}(n = 1)$.
    2. Calculates $C_{0+}(n = 1)$.
    3. Calculates $C_{-+}(n = 1)$.
    4. Calculates $\mathcal{C}_{++}^{I}(n = 1 | \mathcal{F})$, passing in $\text{Re}[\mathcal{F}]$ only.
    5. Calculates $\mathcal{C}_{0+}^{I}(n = 1 | \mathcal{F}_{\text{Eff}})$, passing in $\text{Re}[\mathcal{F}_{\text{Eff}}]$ only.
    6. Calculates $\mathcal{C}_{-+}^{I}(n = 1 | \mathcal{F}_{\text{T}})$, passing in $\text{Re}[\mathcal{F}_{\text{T}}]$ only.

4. Calculate $c_{2}^{I}$. This calls `calculate_c_interference_coefficient` with $n = 2$.

    1. Calculates $C_{++}(n = 2)$.
    2. Calculates $C_{0+}(n = 2)$.
    3. Calculates $C_{-+}(n = 2)$.
    4. Calculates $\mathcal{C}_{++}^{I}(n = 2 | \mathcal{F})$, passing in $\text{Re}[\mathcal{F}]$ only.
    5. Calculates $\mathcal{C}_{0+}^{I}(n = 2 | \mathcal{F}_{\text{Eff}})$, passing in $\text{Re}[\mathcal{F}_{\text{Eff}}]$ only.
    6. Calculates $\mathcal{C}_{-+}^{I}(n = 2 | \mathcal{F}_{\text{T}})$, passing in $\text{Re}[\mathcal{F}_{\text{T}}]$ only.

5. Calculate $c_{3}^{I}$. This calls `calculate_c_interference_coefficient` with $n = 3$.

    1. Calculates $C_{++}(n = 3) = 0$.
    2. Calculates $C_{0+}(n = 3) = 0$.
    3. Calculates $C_{-+}(n = 3) = 0$.
    4. Calculates $\mathcal{C}_{++}^{I}(n = 3 | \mathcal{F})$, passing in $\text{Re}[\mathcal{F}]$ only.
    5. Calculates $\mathcal{C}_{0+}^{I}(n = 3 | \mathcal{F}_{\text{Eff}})$, passing in $\text{Re}[\mathcal{F}_{\text{Eff}}]$ only.
    6. Calculates $\mathcal{C}_{-+}^{I}(n = 3 | \mathcal{F}_{\text{T}})$, passing in $\text{Re}[\mathcal{F}_{\text{T}}]$ only.

6. Calculate $s_{1}^{I}$. This calls `calculate_s_interference_coefficient` with $n = 1$.

    1. Calculates $S_{++}(n = 1)$.
    2. Calculates $S_{0+}(n = 1)$.
    3. Calculates $S_{-+}(n = 1)$.

7. Calculate $s_{2}^{I}$. This calls `calculate_s_interference_coefficient` with $n = 2$.

    1. Calculates $S_{++}(n = 2)$.
    2. Calculates $S_{0+}(n = 2)$.
    3. Calculates $S_{-+}(n = 2)$.

8. Calculate $s_{3}^{I}$. This calls `calculate_s_interference_coefficient` with $n = 3$.

    1. Calculates $S_{++}(n = 3)$.
    2. Calculates $S_{0+}(n = 3)$.
    3. Calculates $S_{-+}(n = 3)$.