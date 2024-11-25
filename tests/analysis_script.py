import sys

import os

print(os.getcwd())

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from utilities.plotting.plot_customizer import PlotCustomizer

# Helper Module | Convert GeV^{-6} to nb/GeV^{4}
from utilities.mathematics.math_units import convert_to_nb_over_GeV4

# Derived Kinematics | Epsilon | ε
from derived_kinematics.epsilon import calculate_kinematics_epsilon

# Derived Kinematics | Lepton Energy Fraction | y
from derived_kinematics.lepton_energy_fraction import calculate_kinematics_lepton_energy_fraction_y

# Derived Kinematics | Skewness | ξ
from derived_kinematics.skewness import calculate_kinematics_skewness_parameter

# Derived Kinematics | Minimum t | t_{min}
from derived_kinematics.t_minimum import calculate_kinematics_t_min

# Derived Kinematics | t Prime | t'
from derived_kinematics.t_prime import calculate_kinematics_t_prime

# Derived Kinematics | K Tilde | Ḱ
from derived_kinematics.k_tilde import calculate_kinematics_k_tilde

# Derived Kinematics | K | K
from derived_kinematics.shorthand_K import calculate_kinematics_k

# Derived Kinematics | k dot Delta | k ⋅ Δ 
from derived_kinematics.k_dot_delta import calculate_k_dot_delta

# Derived Kinematics | Lepton Propagator P1 | P_{1}(φ)
from derived_kinematics.lepton_propagator_p1 import calculate_lepton_propagator_p1

# Derived Kinematics | Lepton Propagator P2 | P_{1}(φ)
from derived_kinematics.lepton_propagator_p2 import calculate_lepton_propagator_p2

# Form Factors | Electric Form Factor | F_{E}
from form_factors.electric_form_factor import calculate_form_factor_electric

# Form Factors | Magnetic Form Factor | F_{M}
from form_factors.magnetic_form_factor import calculate_form_factor_magnetic

# Form Factors | Pauli Form Factor | F_{2}
from form_factors.pauli_form_factor import calculate_form_factor_pauli_f2

# Form Factors | Dirac Form Factor | F_{1}
from form_factors.dirac_form_factor import calculate_form_factor_dirac_f1

# Amplitude Contributions | BKM10 Prefactor
from amplitudes.cross_section_prefactor import calculate_bkm10_cross_section_prefactor

# Amplitude Contributions | Bethe-Heitler | |M_{BH}|^{2}
from amplitudes.bh_squared_contribution import calculate_bh_amplitude_squared

# Amplitude Contributions | Deeply-Virtual Compton Scattering | |M_{DVCS}|^{2}
from amplitudes.dvcs_squared_contribution import calculate_dvcs_amplitude_squared

# Amplitude Contributions | Interference | I
from amplitudes.interference_contribution import calculate_interference_contribution

def analysis():
    """
    """

    verbose = False

    value_of_beam_energy = 5.75
    value_of_Q_squared = 1.8200000524520876
    value_of_hadron_recoil = -0.1720000058412552
    value_of_x_Bjorken = 0.3429999947547912

    squared_Q_momentum_transfer = np.array([value_of_Q_squared for i in range(len(np.arange(0, 361, 1.)))])
    x_Bjorken = np.array([value_of_x_Bjorken for i in range(len(np.arange(0, 361, 1.)))])
    squared_hadronic_momentum_transfer_t = np.array([value_of_hadron_recoil for i in range(len(np.arange(0, 361, 1.)))])
    lab_kinematics_k = np.array([value_of_beam_energy for i in range(len(np.arange(0, 361, 1.)))])
    azimuthal_phi = np.arange(0, 361, 1.)

    compton_form_factor_h_real = -0.897
    compton_form_factor_h_imaginary = 2.421

    compton_form_factor_h_tilde_real = 2.444
    compton_form_factor_h_tilde_imaginary = 1.131

    compton_form_factor_e_real = -0.541
    compton_form_factor_e_imaginary = 0.903

    compton_form_factor_e_tilde_real = 2.207
    compton_form_factor_e_tilde_imaginary = 5.383
    
    compton_form_factor_h = complex(compton_form_factor_h_real, compton_form_factor_h_imaginary)
    compton_form_factor_h_tilde = complex(compton_form_factor_h_tilde_real, compton_form_factor_h_tilde_imaginary)
    compton_form_factor_e = complex(compton_form_factor_e_real, compton_form_factor_e_imaginary)
    compton_form_factor_e_tilde = complex(compton_form_factor_e_tilde_real, compton_form_factor_e_tilde_imaginary)

    # (1): Calculate Epsilon:
    epsilon = calculate_kinematics_epsilon(
        squared_Q_momentum_transfer,
        x_Bjorken,
        verbose)

    # (2): Calculate the Lepton Energy Fraction:
    lepton_energy_fraction_y = calculate_kinematics_lepton_energy_fraction_y(
        squared_Q_momentum_transfer,
        lab_kinematics_k,
        epsilon,
        verbose)

    # (3): Calculate the Skewness Parameter:
    skewness_parameter = calculate_kinematics_skewness_parameter(
        squared_Q_momentum_transfer,
        x_Bjorken,
        squared_hadronic_momentum_transfer_t,
        verbose)

    # (4): Calculate t_minimum
    squared_hadronic_momentum_transfer_t_minimum = calculate_kinematics_t_min(
        squared_Q_momentum_transfer,
        x_Bjorken,
        epsilon,
        verbose)

    # (5): Calculate t_prime:
    t_prime = calculate_kinematics_t_prime(
        squared_hadronic_momentum_transfer_t,
        squared_hadronic_momentum_transfer_t_minimum,
        verbose)

    # (6): Calculate K_tilde:
    k_tilde = calculate_kinematics_k_tilde(
        squared_Q_momentum_transfer,
        x_Bjorken,
        lepton_energy_fraction_y,
        squared_hadronic_momentum_transfer_t,
        epsilon,
        squared_hadronic_momentum_transfer_t_minimum,
        verbose)

    # (7): Calculate K Squared:
    shorthand_k = calculate_kinematics_k(
        squared_Q_momentum_transfer,
        lepton_energy_fraction_y,
        epsilon,
        k_tilde,
        verbose)

    # (8): Calculate k_dot_delta:
    k_dot_delta = calculate_k_dot_delta(
        squared_Q_momentum_transfer,
        x_Bjorken,
        squared_hadronic_momentum_transfer_t,
        azimuthal_phi,
        epsilon,
        lepton_energy_fraction_y,
        shorthand_k,
        verbose)

    # (9): Calculate Lepton Propagator 1:
    lepton_propagator_p1 = calculate_lepton_propagator_p1(
        squared_Q_momentum_transfer,
        k_dot_delta,
        verbose)
    
    # (10): Calculate Lepton Propagator 2:
    lepton_propagator_p2 = calculate_lepton_propagator_p2(
        squared_Q_momentum_transfer,
        squared_hadronic_momentum_transfer_t,
        k_dot_delta,
        verbose)
    
    # (11): Calculate the Electric Form Factor
    electric_form_factor = calculate_form_factor_electric(
        squared_hadronic_momentum_transfer_t, 
        verbose)

    # (12): Calculate the Magnetic Form Factor
    magnetic_form_factor = calculate_form_factor_magnetic(
        electric_form_factor, 
        verbose) 

    # (13): Calculate the Pauli Form Factor, F2:
    Pauli_form_factor_F2 = calculate_form_factor_pauli_f2(
        squared_hadronic_momentum_transfer_t,
        electric_form_factor,
        magnetic_form_factor,
        verbose)

    # (14): Calculate the Dirac Form Factor, F1:
    Dirac_form_factor_F1 = calculate_form_factor_dirac_f1(
        magnetic_form_factor,
        Pauli_form_factor_F2,
        verbose)

    # (15): Calculate the cross-section prefactor:
    cross_section_prefactor = calculate_bkm10_cross_section_prefactor(
        squared_Q_momentum_transfer,
        x_Bjorken,
        epsilon,
        lepton_energy_fraction_y,
        verbose)
    
    pure_bh_unpolarized_beam_unpolarized_target = (0.5 * (
        calculate_bh_amplitude_squared(0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
            lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose) + 
        calculate_bh_amplitude_squared(
            -0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
            lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose)))
    
    # jd_mathematica_pure_bh_unpolarized_beam_unpolarized_target = pd.read_csv('jd_interference_bh_beam_unpolarized_target_v1.csv', names = ['jd_sigma'])
    # ji_mathematica_pure_bh_unpolarized_beam_unpolarized_target = pd.read_csv('ji_interference_bh_beam_unpolarized_target_v1.csv', names = ['ji_sigma'])
    
    pure_bh_plus_beam_unpolarized_target = calculate_bh_amplitude_squared(
            0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
            lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose)
    
    # jd_mathematica_pure_bh_plus_beam_unpolarized_target = pd.read_csv('jd_bh_plus_beam_unpolarized_target_v1.csv', names = ['jd_sigma'])
    # ji_mathematica_pure_bh_plus_beam_unpolarized_target = pd.read_csv('ji_bh_plus_beam_unpolarized_target_v1.csv', names = ['ji_sigma'])
    
    pure_bh_minus_beam_unpolarized_target = calculate_bh_amplitude_squared(
            -0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
            lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose)
    
    # jd_mathematica_pure_bh_minus_beam_unpolarized_target = pd.read_csv('jd_bh_minus_beam_unpolarized_target_v1.csv', names = ['jd_sigma'])
    # ji_mathematica_pure_bh_minus_beam_unpolarized_target = pd.read_csv('ji_bh_minus_beam_unpolarized_target_v1.csv', names = ['ji_sigma'])
    
    pure_bh_unpolarized_beam_lp_target = (0.5 * (
        calculate_bh_amplitude_squared(0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
            lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose) + 
        calculate_bh_amplitude_squared(
            -0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
            lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose)))
    
    # jd_mathematica_pure_bh_unpolarized_beam_lp_target = pd.read_csv('jd_bh_unpolarized_beam_lp_target_v1.csv', names = ['jd_sigma'])
    # ji_mathematica_pure_bh_unpolarized_beam_lp_target = pd.read_csv('ji_bh_unpolarized_beam_lp_target_v1.csv', names = ['ji_sigma'])
    
    pure_bh_plus_beam_unpolarized_target = calculate_bh_amplitude_squared(0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
            lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose)
    
    # jd_mathematica_pure_bh_plus_beam_lp_target = pd.read_csv('jd_bh_plus_beam_lp_target_v1.csv', names = ['jd_sigma'])
    # ji_mathematica_pure_bh_plus_beam_lp_target = pd.read_csv('ji_bh_plus_beam_lp_target_v1.csv', names = ['ji_sigma'])

    pure_bh_minus_beam_lp_target = calculate_bh_amplitude_squared(
            -0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
            lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose)
    
    # jd_mathematica_pure_bh_minus_beam_lp_target = pd.read_csv('jd_bh_plus_minus_lp_target_v1.csv', names = ['jd_sigma'])
    # ji_mathematica_pure_bh_minus_beam_lp_target = pd.read_csv('ji_bh_plus_minus_lp_target_v1.csv', names = ['ji_sigma'])
    
    pure_dvcs_unpolarized_beam_unpolarized_target = cross_section_prefactor * (0.5 * 
        (calculate_dvcs_amplitude_squared(
        0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False) +
        calculate_dvcs_amplitude_squared(
        -0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)))
    pure_dvcs_unpolarized_beam_unpolarized_target_ww = cross_section_prefactor * (0.5 * 
        (calculate_dvcs_amplitude_squared(
        0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True) +
        calculate_dvcs_amplitude_squared(
        -0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)))
    
    jd_mathematica_pure_dvcs_unpolarized_beam_unpolarized_target = pd.read_csv('jd_dvcs_unpolarized_beam_unpolarized_target_v1.csv', names = ['jd_sigma'])
    jd_mathematica_pure_dvcs_unpolarized_beam_unpolarized_target_ww = pd.read_csv('jd_dvcs_unpolarized_beam_unpolarized_target_ww_v1.csv', names = ['jd_sigma_ww'])
    ji_mathematica_pure_dvcs_unpolarized_beam_unpolarized_target = pd.read_csv('ji_dvcs_unpolarized_beam_unpolarized_target_v1.csv', names = ['ji_sigma'])

    figure_pure_dvcs_unpolarized_beam_unpolarized_target = plt.figure(figsize = (10.5, 7))
    axes_pure_dvcs_unpolarized_beam_unpolarized_target = figure_pure_dvcs_unpolarized_beam_unpolarized_target.add_subplot(1, 1, 1)
    plot_pure_dvcs_unpolarized_beam_unpolarized_target = PlotCustomizer(
        axes_pure_dvcs_unpolarized_beam_unpolarized_target,
        title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
            round(value_of_beam_energy, 5), 
            round(value_of_Q_squared, 5),
            round(value_of_hadron_recoil, 5),
            round(value_of_x_Bjorken, 5)),
        xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
        ylabel = r"$d^{4} \sigma^{{DVCS}}_{{\mathrm{{UU}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
        grid = True)
    
    plot_pure_dvcs_unpolarized_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_dvcs_unpolarized_beam_unpolarized_target),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (no WW)",
        color = 'blue')
    
    plot_pure_dvcs_unpolarized_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_dvcs_unpolarized_beam_unpolarized_target,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (no WW)",
        color = 'red')
    
    plot_pure_dvcs_unpolarized_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = ji_mathematica_pure_dvcs_unpolarized_beam_unpolarized_target,
        radial_size = 1.3,
        label = "Ji's Covariant Formalism with Dima's Mathematica",
        color = 'green')
    
    plot_pure_dvcs_unpolarized_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_dvcs_unpolarized_beam_unpolarized_target_ww),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (WW)",
        color = 'purple')
    
    plot_pure_dvcs_unpolarized_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_dvcs_unpolarized_beam_unpolarized_target_ww,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (WW)",
        color = 'orange')
    
    plt.savefig(
        fname = 'compared_pure_dvcs_unpolarized_beam_unpolarized_target_v1.png',
        dpi = 500)
    
    pure_dvcs_plus_beam_unpolarized_target = cross_section_prefactor * calculate_dvcs_amplitude_squared(
        0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)
    pure_dvcs_plus_beam_unpolarized_target_ww = cross_section_prefactor * calculate_dvcs_amplitude_squared(
        0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)
    
    jd_mathematica_pure_dvcs_plus_beam_unpolarized_target = pd.read_csv('jd_dvcs_plus_beam_unpolarized_target_v1.csv', names = ['jd_sigma'])
    jd_mathematica_pure_dvcs_plus_beam_unpolarized_target_ww = pd.read_csv('jd_dvcs_plus_beam_unpolarized_target_ww_v1.csv', names = ['jd_sigma_ww'])
    ji_mathematica_pure_dvcs_plus_beam_unpolarized_target = pd.read_csv('ji_dvcs_plus_beam_unpolarized_target_v1.csv', names = ['ji_sigma'])
    
    figure_pure_dvcs_plus_beam_unpolarized_target = plt.figure(figsize = (10.5, 7))
    axes_pure_dvcs_plus_beam_unpolarized_target = figure_pure_dvcs_plus_beam_unpolarized_target.add_subplot(1, 1, 1)
    plot_pure_dvcs_plus_beam_unpolarized_target = PlotCustomizer(
        axes_pure_dvcs_plus_beam_unpolarized_target,
        title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
            round(value_of_beam_energy, 5), 
            round(value_of_Q_squared, 5),
            round(value_of_hadron_recoil, 5),
            round(value_of_x_Bjorken, 5)),
        xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
        ylabel = r"$d^{4} \sigma^{{DVCS}}_{{\mathrm{{U+}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
        grid = True)
    
    plot_pure_dvcs_plus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_dvcs_plus_beam_unpolarized_target),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (no WW)",
        color = 'blue')
    
    plot_pure_dvcs_plus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_dvcs_plus_beam_unpolarized_target,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (no WW)",
        color = 'red')
    
    plot_pure_dvcs_plus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = ji_mathematica_pure_dvcs_plus_beam_unpolarized_target,
        radial_size = 1.3,
        label = "Ji's Covariant Formalism with Dima's Mathematica",
        color = 'green')
    
    plot_pure_dvcs_plus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_dvcs_plus_beam_unpolarized_target_ww),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (WW)",
        color = 'purple')
    
    plot_pure_dvcs_plus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_dvcs_plus_beam_unpolarized_target_ww,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (WW)",
        color = 'orange')
    
    plt.savefig(
        fname = 'compared_pure_dvcs_plus_beam_unpolarized_target_v1.png',
        dpi = 500)
    
    pure_dvcs_minus_beam_unpolarized_target = cross_section_prefactor * calculate_dvcs_amplitude_squared(
        -0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)
    pure_dvcs_minus_beam_unpolarized_target_ww = cross_section_prefactor * calculate_dvcs_amplitude_squared(
        -0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)
    
    jd_mathematica_pure_dvcs_minus_beam_unpolarized_target = pd.read_csv('jd_dvcs_minus_beam_unpolarized_target_v1.csv', names = ['jd_sigma'])
    jd_mathematica_pure_dvcs_minus_beam_unpolarized_target_ww = pd.read_csv('jd_dvcs_minus_beam_unpolarized_target_ww_v1.csv', names = ['jd_sigma_ww'])
    ji_mathematica_pure_dvcs_minus_beam_unpolarized_target = pd.read_csv('ji_dvcs_minus_beam_unpolarized_target_v1.csv', names = ['ji_sigma'])
    
    figure_pure_dvcs_minus_beam_unpolarized_target = plt.figure(figsize = (10.5, 7))
    axes_pure_dvcs_minus_beam_unpolarized_target = figure_pure_dvcs_minus_beam_unpolarized_target.add_subplot(1, 1, 1)
    plot_pure_dvcs_minus_beam_unpolarized_target = PlotCustomizer(
        axes_pure_dvcs_minus_beam_unpolarized_target,
        title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
            round(value_of_beam_energy, 5), 
            round(value_of_Q_squared, 5),
            round(value_of_hadron_recoil, 5),
            round(value_of_x_Bjorken, 5)),
        xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
        ylabel = r"$d^{4} \sigma^{{DVCS}}_{{\mathrm{{U-}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
        grid = True)
    
    plot_pure_dvcs_minus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_dvcs_minus_beam_unpolarized_target),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (no WW)",
        color = 'blue')
    
    plot_pure_dvcs_minus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_dvcs_minus_beam_unpolarized_target,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (no WW)",
        color = 'red')
    
    plot_pure_dvcs_minus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = ji_mathematica_pure_dvcs_minus_beam_unpolarized_target,
        radial_size = 1.3,
        label = "Ji's Covariant Formalism with Dima's Mathematica",
        color = 'green')
    
    plot_pure_dvcs_minus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_dvcs_minus_beam_unpolarized_target_ww),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (WW)",
        color = 'purple')
    
    plot_pure_dvcs_minus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_dvcs_minus_beam_unpolarized_target_ww,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (WW)",
        color = 'orange')
    
    plt.savefig(
        fname = 'compared_pure_dvcs_minus_plus_unpolarized_target_v1.png',
        dpi = 500)

    pure_dvcs_unpolarized_beam_lp_target = cross_section_prefactor * (0.5 * 
        (calculate_dvcs_amplitude_squared(
        0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False) +
        calculate_dvcs_amplitude_squared(
        -0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)))
    pure_dvcs_unpolarized_beam_lp_target_ww = cross_section_prefactor * (0.5 * 
        (calculate_dvcs_amplitude_squared(
        0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True) +
        calculate_dvcs_amplitude_squared(
        -0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)))

    jd_mathematica_pure_dvcs_unpolarized_beam_lp_target = pd.read_csv('jd_dvcs_unpolarized_beam_lp_target_v1.csv', names = ['jd_sigma'])
    jd_mathematica_pure_dvcs_unpolarized_beam_lp_target_ww = pd.read_csv('jd_dvcs_unpolarized_beam_lp_target_ww_v1.csv', names = ['jd_sigma_ww'])
    ji_mathematica_pure_dvcs_unpolarized_beam_lp_target = pd.read_csv('ji_dvcs_unpolarized_beam_lp_target_v1.csv', names = ['ji_sigma'])
    
    figure_pure_dvcs_unpolarized_beam_lp_target = plt.figure(figsize = (10.5, 7))
    axes_pure_dvcs_unpolarized_beam_lp_target = figure_pure_dvcs_unpolarized_beam_lp_target.add_subplot(1, 1, 1)
    plot_pure_dvcs_unpolarized_beam_lp_target = PlotCustomizer(
        axes_pure_dvcs_unpolarized_beam_lp_target,
        title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
            round(value_of_beam_energy, 5), 
            round(value_of_Q_squared, 5),
            round(value_of_hadron_recoil, 5),
            round(value_of_x_Bjorken, 5)),
        xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
        ylabel = r"$d^{4} \sigma^{{DVCS}}_{{\mathrm{{LU}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
        grid = True)
    
    plot_pure_dvcs_unpolarized_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_dvcs_unpolarized_beam_lp_target),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (no WW)",
        color = 'blue')
    
    plot_pure_dvcs_unpolarized_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_dvcs_unpolarized_beam_lp_target,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (no WW)",
        color = 'red')
    
    plot_pure_dvcs_unpolarized_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = ji_mathematica_pure_dvcs_unpolarized_beam_lp_target,
        radial_size = 1.3,
        label = "Ji's Covariant Formalism with Dima's Mathematica",
        color = 'green')
    
    plot_pure_dvcs_unpolarized_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_dvcs_unpolarized_beam_lp_target_ww),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (WW)",
        color = 'purple')
    
    plot_pure_dvcs_unpolarized_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_dvcs_unpolarized_beam_lp_target_ww,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (WW)",
        color = 'orange')
    
    plt.savefig(
        fname = 'compared_pure_dvcs_unpolarized_beam_lp_target_v1.png',
        dpi = 500)
    
    pure_dvcs_plus_beam_lp_target = cross_section_prefactor * calculate_dvcs_amplitude_squared(
        0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)
    pure_dvcs_plus_beam_lp_target_ww = cross_section_prefactor * calculate_dvcs_amplitude_squared(
        0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False) 
    
    jd_mathematica_pure_dvcs_plus_beam_lp_target = pd.read_csv('jd_dvcs_plus_beam_lp_target_v1.csv', names = ['jd_sigma'])
    jd_mathematica_pure_dvcs_plus_beam_lp_target_ww = pd.read_csv('jd_dvcs_plus_beam_lp_target_ww_v1.csv', names = ['jd_sigma_ww'])
    ji_mathematica_pure_dvcs_plus_beam_lp_target = pd.read_csv('ji_dvcs_plus_beam_lp_target_v1.csv', names = ['ji_sigma'])

    figure_pure_dvcs_plus_beam_lp_target = plt.figure(figsize = (10.5, 7))
    axes_pure_dvcs_plus_beam_lp_target = figure_pure_dvcs_plus_beam_lp_target.add_subplot(1, 1, 1)
    plot_pure_dvcs_plus_beam_lp_target = PlotCustomizer(
        axes_pure_dvcs_plus_beam_lp_target,
        title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
            round(value_of_beam_energy, 5), 
            round(value_of_Q_squared, 5),
            round(value_of_hadron_recoil, 5),
            round(value_of_x_Bjorken, 5)),
        xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
        ylabel = r"$d^{4} \sigma^{{DVCS}}_{{\mathrm{{L+}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
        grid = True)
    
    plot_pure_dvcs_plus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_dvcs_plus_beam_lp_target),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (no WW)",
        color = 'blue')
    
    plot_pure_dvcs_plus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_dvcs_plus_beam_lp_target,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (no WW)",
        color = 'red')
    
    plot_pure_dvcs_plus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = ji_mathematica_pure_dvcs_plus_beam_lp_target,
        radial_size = 1.3,
        label = "Ji's Covariant Formalism with Dima's Mathematica",
        color = 'green')
    
    plot_pure_dvcs_plus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_dvcs_plus_beam_lp_target_ww),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (WW)",
        color = 'purple')
    
    plot_pure_dvcs_plus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_dvcs_plus_beam_lp_target_ww,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (WW)",
        color = 'orange')
    
    plt.savefig(
        fname = 'compared_pure_dvcs_plus_beam_lp_target_v1.png',
        dpi = 500)
    
    pure_dvcs_minus_beam_lp_target = cross_section_prefactor * calculate_dvcs_amplitude_squared(
        -0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)
    pure_dvcs_minus_beam_lp_target_ww = cross_section_prefactor * calculate_dvcs_amplitude_squared(
        -0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True) 

    jd_mathematica_pure_dvcs_minus_beam_lp_target = pd.read_csv('jd_dvcs_minus_beam_lp_target_v1.csv', names = ['jd_sigma'])
    jd_mathematica_pure_dvcs_minus_beam_lp_target_ww = pd.read_csv('jd_dvcs_minus_beam_lp_target_ww_v1.csv', names = ['jd_sigma_ww'])
    ji_mathematica_pure_dvcs_minus_beam_lp_target = pd.read_csv('ji_dvcs_minus_beam_lp_target_v1.csv', names = ['ji_sigma'])

    figure_pure_dvcs_minus_beam_lp_target = plt.figure(figsize = (10.5, 7))
    axes_pure_dvcs_minus_beam_lp_target = figure_pure_dvcs_minus_beam_lp_target.add_subplot(1, 1, 1)
    plot_pure_dvcs_minus_beam_lp_target = PlotCustomizer(
        axes_pure_dvcs_minus_beam_lp_target,
        title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
            round(value_of_beam_energy, 5), 
            round(value_of_Q_squared, 5),
            round(value_of_hadron_recoil, 5),
            round(value_of_x_Bjorken, 5)),
        xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
        ylabel = r"$d^{4} \sigma^{{DVCS}}_{{\mathrm{{L-}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
        grid = True)
    
    plot_pure_dvcs_minus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_dvcs_minus_beam_lp_target),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (no WW)",
        color = 'blue')
    
    plot_pure_dvcs_minus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_dvcs_minus_beam_lp_target,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (no WW)",
        color = 'red')
    
    plot_pure_dvcs_minus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = ji_mathematica_pure_dvcs_minus_beam_lp_target,
        radial_size = 1.3,
        label = "Ji's Covariant Formalism with Dima's Mathematica",
        color = 'green')
    
    plot_pure_dvcs_minus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_dvcs_minus_beam_lp_target_ww),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (WW)",
        color = 'purple')
    
    plot_pure_dvcs_minus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_dvcs_minus_beam_lp_target_ww,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (WW)",
        color = 'orange')
    
    plt.savefig(
        fname = 'compared_pure_dvcs_minus_beam_lp_target_v1.png',
        dpi = 500)
    
    pure_interference_unpolarized_beam_unpolarized_target = cross_section_prefactor * (0.5 * 
        (calculate_interference_contribution(0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
        Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False) +
        calculate_interference_contribution(-0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
        Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)))
    pure_interference_unpolarized_beam_unpolarized_target_ww = cross_section_prefactor * (0.5 * 
        (calculate_interference_contribution(0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
        Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True) +
        calculate_interference_contribution(-0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
        Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)))
    
    jd_mathematica_pure_interference_unpolarized_beam_unpolarized_target = pd.read_csv('jd_interference_unpolarized_beam_unpolarized_target_v1.csv', names = ['jd_sigma'])
    jd_mathematica_pure_interference_unpolarized_beam_unpolarized_target_ww = pd.read_csv('jd_interference_unpolarized_beam_unpolarized_target_ww_v1.csv', names = ['jd_sigma_ww'])
    ji_mathematica_pure_interference_unpolarized_beam_unpolarized_target = pd.read_csv('ji_interference_unpolarized_beam_unpolarized_target_v1.csv', names = ['ji_sigma'])

    figure_pure_interference_unpolarized_beam_unpolarized_target = plt.figure(figsize = (10.5, 7))
    axes_pure_interference_unpolarized_beam_unpolarized_target = figure_pure_interference_unpolarized_beam_unpolarized_target.add_subplot(1, 1, 1)
    plot_pure_interference_unpolarized_beam_unpolarized_target = PlotCustomizer(
        axes_pure_interference_unpolarized_beam_unpolarized_target,
        title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
            round(value_of_beam_energy, 5), 
            round(value_of_Q_squared, 5),
            round(value_of_hadron_recoil, 5),
            round(value_of_x_Bjorken, 5)),
        xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
        ylabel = r"$d^{4} \sigma^{{I}}_{{\mathrm{{UU}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
        grid = True)
    
    plot_pure_interference_unpolarized_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_interference_unpolarized_beam_unpolarized_target),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (no WW)",
        color = 'blue')
    
    plot_pure_interference_unpolarized_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_interference_unpolarized_beam_unpolarized_target,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (no WW)",
        color = 'red')
    
    plot_pure_interference_unpolarized_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = ji_mathematica_pure_interference_unpolarized_beam_unpolarized_target,
        radial_size = 1.3,
        label = "Ji's Covariant Formalism with Dima's Mathematica",
        color = 'green')
    
    plot_pure_interference_unpolarized_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_interference_unpolarized_beam_unpolarized_target_ww),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (WW)",
        color = 'purple')
    
    plot_pure_interference_unpolarized_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_interference_unpolarized_beam_unpolarized_target_ww,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (WW)",
        color = 'orange')
    
    plt.savefig(
        fname = 'compared_pure_interference_unpolarized_beam_unpolarized_target_v1.png',
        dpi = 500)
    
    pure_interference_plus_beam_unpolarized_target = cross_section_prefactor * calculate_interference_contribution(0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
        Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)
    pure_interference_plus_beam_unpolarized_target_ww = cross_section_prefactor * calculate_interference_contribution(0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
        Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)
    
    jd_mathematica_pure_interference_plus_beam_unpolarized_target = pd.read_csv('jd_interference_plus_beam_unpolarized_target_v1.csv', names = ['jd_sigma'])
    jd_mathematica_pure_interference_plus_beam_unpolarized_target_ww = pd.read_csv('jd_interference_plus_beam_unpolarized_target_ww_v1.csv', names = ['jd_sigma_ww'])
    ji_mathematica_pure_interference_plus_beam_unpolarized_target = pd.read_csv('ji_interference_plus_beam_unpolarized_target_v1.csv', names = ['ji_sigma'])

    figure_pure_interference_plus_beam_unpolarized_target = plt.figure(figsize = (10.5, 7))
    axes_pure_interference_plus_beam_unpolarized_target = figure_pure_interference_plus_beam_unpolarized_target.add_subplot(1, 1, 1)
    plot_pure_interference_plus_beam_unpolarized_target = PlotCustomizer(
        axes_pure_interference_plus_beam_unpolarized_target,
        title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
            round(value_of_beam_energy, 5), 
            round(value_of_Q_squared, 5),
            round(value_of_hadron_recoil, 5),
            round(value_of_x_Bjorken, 5)),
        xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
        ylabel = r"$d^{4} \sigma^{{I}}_{{\mathrm{{UU}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
        grid = True)
    
    plot_pure_interference_plus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_interference_plus_beam_unpolarized_target),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (no WW)",
        color = 'blue')
    
    plot_pure_interference_plus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_interference_plus_beam_unpolarized_target,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (no WW)",
        color = 'red')
    
    plot_pure_interference_plus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = ji_mathematica_pure_interference_plus_beam_unpolarized_target,
        radial_size = 1.3,
        label = "Ji's Covariant Formalism with Dima's Mathematica",
        color = 'green')
    
    plot_pure_interference_plus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_interference_plus_beam_unpolarized_target_ww),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (WW)",
        color = 'purple')
    
    plot_pure_interference_plus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_interference_plus_beam_unpolarized_target_ww,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (WW)",
        color = 'orange')
    
    plt.savefig(
        fname = 'compared_pure_interference_plus_beam_unpolarized_target_v1.png',
        dpi = 500)
    
    pure_interference_minus_beam_unpolarized_target = cross_section_prefactor * calculate_interference_contribution(-0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
        Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)
    pure_interference_minus_beam_unpolarized_target_ww = cross_section_prefactor * calculate_interference_contribution(-0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
        Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)
    
    jd_mathematica_pure_interference_minus_beam_unpolarized_target = pd.read_csv('jd_interference_minus_beam_unpolarized_target_v1.csv', names = ['jd_sigma'])
    jd_mathematica_pure_interference_minus_beam_unpolarized_target_ww = pd.read_csv('jd_interference_minus_beam_unpolarized_target_ww_v1.csv', names = ['jd_sigma_ww'])
    ji_mathematica_pure_interference_minus_beam_unpolarized_target = pd.read_csv('ji_interference_minus_beam_unpolarized_target_v1.csv', names = ['ji_sigma'])
    
    figure_pure_interference_minus_beam_unpolarized_target = plt.figure(figsize = (10.5, 7))
    axes_pure_interference_minus_beam_unpolarized_target = figure_pure_interference_minus_beam_unpolarized_target.add_subplot(1, 1, 1)
    plot_pure_interference_minus_beam_unpolarized_target = PlotCustomizer(
        axes_pure_interference_minus_beam_unpolarized_target,
        title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
            round(value_of_beam_energy, 5), 
            round(value_of_Q_squared, 5),
            round(value_of_hadron_recoil, 5),
            round(value_of_x_Bjorken, 5)),
        xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
        ylabel = r"$d^{4} \sigma^{{I}}_{{\mathrm{{UU}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
        grid = True)
    
    plot_pure_interference_minus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_interference_minus_beam_unpolarized_target),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (no WW)",
        color = 'blue')
    
    plot_pure_interference_minus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_interference_minus_beam_unpolarized_target,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (no WW)",
        color = 'red')
    
    plot_pure_interference_minus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = ji_mathematica_pure_interference_minus_beam_unpolarized_target,
        radial_size = 1.3,
        label = "Ji's Covariant Formalism with Dima's Mathematica",
        color = 'green')
    
    plot_pure_interference_minus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_interference_minus_beam_unpolarized_target_ww),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (WW)",
        color = 'purple')
    
    plot_pure_interference_minus_beam_unpolarized_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_interference_minus_beam_unpolarized_target_ww,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (WW)",
        color = 'orange')
    
    plt.savefig(
        fname = 'compared_pure_interference_minus_beam_unpolarized_target_v1.png',
        dpi = 500)
    
    pure_interference_unpolarized_beam_lp_target = cross_section_prefactor * (0.5 * 
        (calculate_interference_contribution(0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
        Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False) +
        calculate_interference_contribution(-0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
        Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)))
    pure_interference_unpolarized_beam_lp_target_ww = cross_section_prefactor * (0.5 * 
        (calculate_interference_contribution(0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
        Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True) +
        calculate_interference_contribution(-0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
        Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)))
    
    jd_mathematica_pure_interference_unpolarized_beam_lp_target = pd.read_csv('jd_interference_unpolarized_beam_lp_target_v1.csv', names = ['jd_sigma'])
    jd_mathematica_pure_interference_unpolarized_beam_lp_target_ww = pd.read_csv('jd_interference_unpolarized_beam_lp_target_ww_v1.csv', names = ['jd_sigma_ww'])
    ji_mathematica_pure_interference_unpolarized_beam_lp_target = pd.read_csv('ji_interference_unpolarized_beam_lp_target_v1.csv', names = ['ji_sigma'])

    figure_pure_interference_unpolarized_beam_lp_target = plt.figure(figsize = (10.5, 7))
    axes_pure_interference_unpolarized_beam_lp_target = figure_pure_interference_unpolarized_beam_lp_target.add_subplot(1, 1, 1)
    plot_pure_interference_unpolarized_beam_lp_target = PlotCustomizer(
        axes_pure_interference_unpolarized_beam_lp_target,
        title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
            round(value_of_beam_energy, 5), 
            round(value_of_Q_squared, 5),
            round(value_of_hadron_recoil, 5),
            round(value_of_x_Bjorken, 5)),
        xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
        ylabel = r"$d^{4} \sigma^{{I}}_{{\mathrm{{UU}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
        grid = True)
    
    plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_interference_unpolarized_beam_lp_target),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (no WW)",
        color = 'blue')
    
    plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_interference_unpolarized_beam_lp_target,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (no WW)",
        color = 'red')
    
    plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = ji_mathematica_pure_interference_unpolarized_beam_lp_target,
        radial_size = 1.3,
        label = "Ji's Covariant Formalism with Dima's Mathematica",
        color = 'green')
    
    plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_interference_unpolarized_beam_lp_target_ww),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (WW)",
        color = 'purple')
    
    plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_interference_unpolarized_beam_lp_target_ww,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (WW)",
        color = 'orange')
    
    plt.savefig(
        fname = 'compared_pure_interference_unpolarized_beam_lp_target_v1.png',
        dpi = 500)
    
    pure_interference_plus_beam_lp_target = cross_section_prefactor * calculate_interference_contribution(0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
        Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)
    pure_interference_plus_beam_lp_target_ww = cross_section_prefactor * calculate_interference_contribution(0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
        Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)
    
    jd_mathematica_pure_interference_plus_beam_lp_target = pd.read_csv('jd_interference_plus_beam_lp_target_v1.csv', names = ['jd_sigma'])
    jd_mathematica_pure_interference_plus_beam_lp_target_ww = pd.read_csv('jd_interference_plus_beam_lp_target_ww_v1.csv', names = ['jd_sigma_ww'])
    ji_mathematica_pure_interference_plus_beam_lp_target = pd.read_csv('ji_interference_plus_beam_lp_target_v1.csv', names = ['ji_sigma'])

    figure_pure_interference_plus_beam_lp_target = plt.figure(figsize = (10.5, 7))
    axes_pure_interference_plus_beam_lp_target = figure_pure_interference_plus_beam_lp_target.add_subplot(1, 1, 1)
    plot_pure_interference_plus_beam_lp_target = PlotCustomizer(
        axes_pure_interference_plus_beam_lp_target,
        title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
            round(value_of_beam_energy, 5), 
            round(value_of_Q_squared, 5),
            round(value_of_hadron_recoil, 5),
            round(value_of_x_Bjorken, 5)),
        xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
        ylabel = r"$d^{4} \sigma^{{I}}_{{\mathrm{{UU}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
        grid = True)
    
    plot_pure_interference_plus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_interference_plus_beam_lp_target),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (no WW)",
        color = 'blue')
    
    plot_pure_interference_plus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_interference_plus_beam_lp_target,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (no WW)",
        color = 'red')
    
    plot_pure_interference_plus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = ji_mathematica_pure_interference_plus_beam_lp_target,
        radial_size = 1.3,
        label = "Ji's Covariant Formalism with Dima's Mathematica",
        color = 'green')
    
    plot_pure_interference_plus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_interference_plus_beam_lp_target_ww),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (WW)",
        color = 'purple')
    
    plot_pure_interference_plus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_interference_plus_beam_lp_target_ww,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (WW)",
        color = 'orange')
    
    plt.savefig(
        fname = 'compared_pure_interference_plus_beam_lp_target_v1.png',
        dpi = 500)
    
    pure_interference_minus_beam_lp_target = cross_section_prefactor * calculate_interference_contribution(-0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
        Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)
    pure_interference_minus_beam_lp_target_ww = cross_section_prefactor * calculate_interference_contribution(-0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
        epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
        Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)
    
    jd_mathematica_pure_interference_minus_beam_lp_target = pd.read_csv('jd_interference_minus_beam_lp_target_v1.csv', names = ['jd_sigma'])
    jd_mathematica_pure_interference_minus_beam_lp_target_ww = pd.read_csv('jd_interference_minus_beam_lp_target_ww_v1.csv', names = ['jd_sigma_ww'])
    ji_mathematica_pure_interference_minus_beam_lp_target = pd.read_csv('ji_interference_minus_beam_lp_target_v1.csv', names = ['ji_sigma'])

    figure_pure_interference_minus_beam_lp_target = plt.figure(figsize = (10.5, 7))
    axes_pure_interference_minus_beam_lp_target = figure_pure_interference_minus_beam_lp_target.add_subplot(1, 1, 1)
    plot_pure_interference_minus_beam_lp_target = PlotCustomizer(
        axes_pure_interference_minus_beam_lp_target,
        title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
            round(value_of_beam_energy, 5), 
            round(value_of_Q_squared, 5),
            round(value_of_hadron_recoil, 5),
            round(value_of_x_Bjorken, 5)),
        xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
        ylabel = r"$d^{4} \sigma^{{I}}_{{\mathrm{{UU}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
        grid = True)
    
    plot_pure_interference_minus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_interference_minus_beam_lp_target),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (no WW)",
        color = 'blue')
    
    plot_pure_interference_minus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_interference_minus_beam_lp_target,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (no WW)",
        color = 'red')
    
    plot_pure_interference_minus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = ji_mathematica_pure_interference_minus_beam_lp_target,
        radial_size = 1.3,
        label = "Ji's Covariant Formalism with Dima's Mathematica",
        color = 'green')
    
    plot_pure_interference_minus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = convert_to_nb_over_GeV4(pure_interference_minus_beam_lp_target_ww),
        radial_size = 1.3,
        label = "Dima's BKM 10 Python (WW)",
        color = 'purple')
    
    plot_pure_interference_minus_beam_lp_target.add_scatter_plot(
        x_data = azimuthal_phi,
        y_data = jd_mathematica_pure_interference_minus_beam_lp_target_ww,
        radial_size = 1.3,
        label = "Dima's BKM10 Mathematica (WW)",
        color = 'orange')
    
    plt.savefig(
        fname = 'compared_pure_interference_minus_beam_lp_target_v1.png',
        dpi = 500)



if __name__ == "__main__":

    try:
        analysis()
    except Exception as ERROR:
        print(f"> Error running the analysis script: {ERROR}")
        sys.exit(0)