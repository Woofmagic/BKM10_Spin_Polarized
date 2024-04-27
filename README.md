# BKM10_Spin_Polarized
BKM10 four-fold cross section parametrization for a spin-polarized target.

## The Four-Fold Cross Section

What we are numerically calculating is a four-fold (meaning, we need to do four integrals) cross section. We need to integrate over four variables: $Q^{2}, x_{\text{B}}, t, \phi$. By the way, the first three quantities are called the \textit{kinematics}, and $\phi$ is an azimuthal angle that is measured in a chosen reference frame. However, the function actually requires a bit more detail. It is a function of several different things -- schematically, we express this as:

$$d^{4}\sigma = d^{4}\sigma ( \lambda, \Lambda ; Q^{2}, x_{\text{B}}, t, \phi ; \{ \mathcal{F} \} ).$$

Elaborating a bit more on what these mean follows below:

## "Chronology of Arguments"

Each function has a "chronology" of arguments so that we don't get confused, because everything is multidimensional and impossible. The chronology must be:

$$f = f(\lambda, \Lambda; Q^{2}, x_{\text{B}}, k, \phi; \epsilon, y, \xi, t_{\text{min}}, t', K, \tilde{K}; F_{E}, F_{M}, F_{1}, F_{2}; \{ \mathcal{F} \}).$$

Regarding the set of CFFs, $\{ \mathcal{F} \}$, so far it comes in the "chronology" of

$$\mathcal{H}, \tilde{\mathcal{H}}, \mathcal{E}, \tilde{\mathcal{E}}.$$

### Bethe-Heitler Contribuition:

#### Unpolarized Target:

#### Longitudinally-Polarized Target:

For the polarized target, we have two contributions:

$$c_{0}^{\text{BH}}, c_{1}^{\text{BH}}.$$

### DVCS Contribution:

#### Unpolarized Target:

#### Longitudinally-Polarized Target:

For the polarized target, we have four contributions:

$$c_{0,\text{LP}}^{\text{DVCS}}, c_{1,\text{LP}}^{\text{DVCS}}, s_{1,\text{LP}}^{\text{DVCS}}.$$

### Interference Contribution:

#### Unpolarized Target:

#### Longitudinally-Polarized Target:

For the polarized target, we have too many goddamn contributions. We will break them up like so:

##### C-Modes:

###### Helicity-Preserving:

$$C_{++}^{\text{LP}}(n = 0)$$

$$C_{++}^{\text{LP}, V}(n = 0)$$

$$C_{++}^{\text{LP}, A}(n = 0)$$

$$C_{++}^{\text{LP}}(n = 1)$$

$$C_{++}^{\text{LP}, V}(n = 1)$$

$$C_{++}^{\text{LP}, A}(n = 1)$$

$$C_{++}^{\text{LP}}(n = 2)$$

$$C_{++}^{\text{LP}, V}(n = 2)$$

$$C_{++}^{\text{LP}, A}(n = 2)$$

###### Helicity Flip by One Unit

$$C_{0+}^{\text{LP}}(n = 0)$$

$$C_{0+}^{\text{LP}, V}(n = 0)$$

$$C_{0+}^{\text{LP}, A}(n = 0)$$

$$C_{0+}^{\text{LP}}(n = 1)$$

$$C_{0+}^{\text{LP}, V}(n = 1)$$

$$C_{0+}^{\text{LP}}(n = 2)$$

$$C_{0+}^{\text{LP}, V}(n = 2)$$

$$C_{0+}^{\text{LP}, A}(n = 2)$$

###### Helicity Flip by Two Units

Not done yet.

##### S-Modes

###### Helicity-Preserving

$$S_{++}^{\text{LP}}(n = 1)$$

$$S_{++}^{\text{LP}, V}(n = 1)$$

$$S_{++}^{\text{LP}, A}(n = 1)$$

$$S_{++}^{\text{LP}}(n = 2)$$

$$C_{++}^{\text{LP}, V}(n = 2)$$

$$C_{++}^{\text{LP}, A}(n = 2)$$

$$S_{++}^{\text{LP}}(n = 3)$$

$$S_{++}^{\text{LP}, V}(n = 3)$$

$$S_{++}^{\text{LP}, A}(n = 3)$$

###### Helicity Flip by One Unit

$$S_{0+}^{\text{LP}}(n = 1)$$

$$S_{0+}^{\text{LP}, V}(n = 1)$$

$$S_{0+}^{\text{LP}}(n = 2)$$

$$S_{0+}^{\text{LP}}(n = 2)$$

$$S_{0+}^{\text{LP}, V}(n = 2)$$

$$S_{0+}^{\text{LP}, A}(n = 2)$$


###### Helicity Flip by Two Units

Not done yet.
