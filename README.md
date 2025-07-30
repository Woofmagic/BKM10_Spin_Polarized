# BKM10_Spin_Polarized
BKM10 four-fold cross section parametrization for a spin-polarized target.

## About the Program:
This script is designed to use the BKM10 formalism to compute the cross-section and cross-section-derived observables based on knowledge of the kinematic setting and CFFs in the form of a data file (see below).

To run the program, run `main.py` with the required arguments.

### Arguments:

1. `-d data_file.extension [str]`
2. `-kin kinematic set [int]`
3. `-form formalism [str: bkm02 | bkm10]`
4. `-lep-polar`
5. `-target-polar`

#### Required Arguments:

1. `-d data_file.extension [str]`
2. `-kin kinematic set [int]`

#### Optional Arguments:

1. `-form formalism [str: bkm02 | bkm10]`
2. `-lep-polar`
3. `-target-polar`

### Examples: 

```bash
python main.py -d basic_model_pseudodata_for_Jlab_kinematics.csv -kin 1 -form 10 -lep-helicity polarized -target-polar polarized
```

## The Four-Fold Differential Cross Section
Let's talk about the physics momentarily.

What we are numerically calculating is a four-fold (meaning we need to do four integrals) cross section. We need to integrate over four variables: $Q^{2}, x_{\text{B}}, t, \phi$. By the way, the first three quantities are called the \textit{kinematics}, and $\phi$ is an azimuthal angle that is measured in a chosen reference frame. However, the cross-section actually requires a bit more detail: It is a function of several different things -- schematically, we express this as:

$$d^{4}\sigma ( \lambda, \Lambda ; Q^{2}, x_{\text{B}}, t, \phi ; \{ \mathcal{F} \} ).$$

Elaborating a bit more on what these mean follows below:

## "Chronology of Arguments"

Programmatically, each sub-function that plays a role in computing the cross-section has a "chronology" of arguments so that we don't get confused. Ensure that, if you are committing to this repository, the chronology is:

$$f = f(\lambda, \Lambda; Q^{2}, x_{\text{B}}, k, \phi; \epsilon, y, \xi, t_{\text{min}}, t', K, \tilde{K}; F_{E}, F_{M}, F_{1}, F_{2}; \{ \mathcal{F} \}).$$

Regarding the set of CFFs, $\{ \mathcal{F} \}$, so far it comes in the "chronology" of $\mathcal{H}, \tilde{\mathcal{H}}, \mathcal{E}, \tilde{\mathcal{E}}.$

Note: We do use Python's `complex` type to handle the CFFs.

We will now talk about the various pieces that go into computing the cross section.

### Bethe-Heitler Contribuition:
The Bethe-Heitler (BH) process is one that has the same desired initial and final state particles, but the real photon does not come from DVCS; it is instead electromagnetic radiation as part of pure QED. Thus, this process serves as a contamination to the total cross section. Nevertheless, we must account for it when computing the amplitude squared of the process.

We will now outline the various subfunctions that go into computing the BH contribution.

#### Unpolarized Target:

For the unpolarized target, we have three contributions: $c_{0, \text{unp}}^{\text{BH}}, c_{1, \text{unp}}^{\text{BH}}, c_{2, \text{unp}}^{\text{BH}}.$

#### Polarized Target:

For the polarized target, we have two contributions: $c_{0}^{\text{BH}}, c_{1}^{\text{BH}}.$

### DVCS Contribution:
The deeply-virtual Compton scattering (DVCS) process is the one that actually probes the GPDs using a highly-virtual photon. This process is the main one of interest.

We will now outline all the subfuncitons that go into computing the DVCS (squared!) contribution.

#### Unpolarized Target:

For the unpolarized target, we have three contributions: $c_{0,\text{unp}}^{\text{DVCS}}, c_{1,\text{unp}}^{\text{DVCS}}, s_{1,\text{unp}}^{\text{DVCS}}.$

#### Polarized Target:

For the polarized target, we have three contributions: $c_{0,\text{LP}}^{\text{DVCS}}, c_{1,\text{LP}}^{\text{DVCS}}, s_{1,\text{LP}}^{\text{DVCS}}.$

### Interference Contribution:
The interference term arises due to quantum interference between the BH and DVCS process. In fact, it is an interesting term in its own right, because the CFFs appear in this term linearly instead of modulated by *themselves* in the DVCS process (bilinearly). On the other hand, this term is the biggest pain in the ass.

We will now outline all of the subfunctions that go into computing the interference contribution.

#### Unpolarized Target:

For the unpolarized target, we have:

##### Helicity-Preserving:

Regular: $C_{++}^{\text{unp}}(n = 0)$; Vector: $C_{++}^{\text{unp}, V}(n = 0)$; Axial Vector: $C_{++}^{\text{unp}, A}(n = 0).$

Regular: $C_{++}^{\text{unp}}(n = 1)$; Vector: $C_{++}^{\text{unp}, V}(n = 1)$; Axial Vector: $C_{++}^{\text{unp}, A}(n = 1).$

Regular: $C_{++}^{\text{unp}}(n = 2)$; Vector: $C_{++}^{\text{unp}, V}(n = 2)$; Axial Vector: $C_{++}^{\text{unp}, A}(n = 2).$

Regular: $C_{++}^{\text{unp}}(n = 3)$; Vector: $C_{++}^{\text{unp}, V}(n = 3)$; Axial Vector: $C_{++}^{\text{unp}, A}(n = 3).$

Regular: $S_{++}^{\text{unp}}(n = 1)$; Vector: $S_{++}^{\text{unp}, V}(n = 1)$; Axial Vector: $S_{++}^{\text{unp}, A}(n = 1).$

Regular: $S_{++}^{\text{unp}}(n = 2)$; Vector: $C_{++}^{\text{unp}, V}(n = 2)$; Axial Vector: $C_{++}^{\text{unp}, A}(n = 2).$

##### Helicity Flip by One Unit:

Regular: $C_{0+}^{\text{unp}}(n = 0)$; Vector: $C_{0+}^{\text{unp}, V}(n = 0)$; Axial Vector: $C_{0+}^{\text{unp}, A}(n = 0).$

Regular: $C_{0+}^{\text{unp}}(n = 1)$; Vector: $C_{0+}^{\text{unp}, V}(n = 1)$; Axial Vector: $C_{0+}^{\text{unp}, A}(n = 1).$

Regular: $C_{0+}^{\text{unp}}(n = 2)$; Vector: $C_{0+}^{\text{unp}, V}(n = 2)$; Axial Vector: $C_{0+}^{\text{unp}, A}(n = 2).$

Regular: $S_{0+}^{\text{unp}}(n = 1)$; Vector: $S_{0+}^{\text{unp}, V}(n = 1)$; Axial Vector: $S_{0+}^{\text{unp}, A}(n = 1).$

Regular: $S_{0+}^{\text{unp}}(n = 2)$; Vector: $C_{0+}^{\text{unp}, V}(n = 2)$; Axial Vector: $C_{0+}^{\text{unp}, A}(n = 2).$

##### Helicity Flip by Two Units:

We will code this up later. Let us know if you need these functions now.

#### Polarized Target:

For the polarized target, we have too many goddamn contributions:

##### Helicity-Preserving:

Regular: $C_{++}^{\text{LP}}(n = 0)$; Vector: $C_{++}^{\text{LP}, V}(n = 0)$; Axial Vector: $C_{++}^{\text{LP}, A}(n = 0).$

Regular: $C_{++}^{\text{LP}}(n = 1)$; Vector: $C_{++}^{\text{LP}, V}(n = 1)$; Axial Vector: $C_{++}^{\text{LP}, A}(n = 1).$

Regular: $C_{++}^{\text{LP}}(n = 2)$; Vector: $C_{++}^{\text{LP}, V}(n = 2)$; Axial Vector: $C_{++}^{\text{LP}, A}(n = 2).$

Regular: $S_{++}^{\text{LP}}(n = 1)$; Vector: $S_{++}^{\text{LP}, V}(n = 1)$; Axial Vector: $S_{++}^{\text{LP}, A}(n = 1).$

Regular: $S_{++}^{\text{LP}}(n = 2)$; Vector: $C_{++}^{\text{LP}, V}(n = 2)$; Axial Vector: $C_{++}^{\text{LP}, A}(n = 2).$

Regular: $S_{++}^{\text{LP}}(n = 3)$; Vector: $S_{++}^{\text{LP}, V}(n = 3)$; Axial Vector: $S_{++}^{\text{LP}, A}(n = 3).$

##### Helicity Flip by One Unit:

Regular: $C_{0+}^{\text{LP}}(n = 0)$; Vector: $C_{0+}^{\text{LP}, V}(n = 0)$; Axial Vector: $C_{0+}^{\text{LP}, A}(n = 0).$

Regular: $C_{0+}^{\text{LP}}(n = 1)$; Axial Vector: $C_{0+}^{\text{LP}, A}(n = 1).$

Regular: $C_{0+}^{\text{LP}}(n = 2)$; Vector: $C_{0+}^{\text{LP}, V}(n = 2)$; Axial Vector: $C_{0+}^{\text{LP}, A}(n = 2).$

Regular: $S_{0+}^{\text{LP}}(n = 1)$; Vector: $S_{0+}^{\text{LP}, V}(n = 1)$; Axial Vector: $S_{0+}^{\text{LP}, A}(n = 1).$

Regular: $S_{0+}^{\text{LP}}(n = 2)$; Vector: $C_{0+}^{\text{LP}, V}(n = 2)$; Axial Vector: $C_{0+}^{\text{LP}, A}(n = 2).$

##### Helicity Flip by Two Units:

We are not currently using these coefficients. We will do this in the future.