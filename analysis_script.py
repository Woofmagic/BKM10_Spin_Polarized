import sys

import os

from decimal import Decimal

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

    kinematics_and_cff_settings = [
        {
            "value_of_beam_energy": Decimal("5.75"),
            "value_of_Q_squared": Decimal("1.82"),
            "value_of_hadron_recoil": Decimal("-0.17"),
            "value_of_x_Bjorken": Decimal("0.34"),
            "compton_form_factor_h_real": Decimal("-0.897"),
            "compton_form_factor_h_imaginary": Decimal("2.421"),
            "compton_form_factor_h_tilde_real": Decimal("2.444"),
            "compton_form_factor_h_tilde_imaginary": Decimal("1.131"),
            "compton_form_factor_e_real": Decimal("-0.541"),
            "compton_form_factor_e_imaginary": Decimal("0.903"),
            "compton_form_factor_e_tilde_real": Decimal("2.207"),
            "compton_form_factor_e_tilde_imaginary": Decimal("5.383")
        },
        {
            "value_of_beam_energy": Decimal("10.59"),
            "value_of_Q_squared": Decimal("4.55"),
            "value_of_hadron_recoil": Decimal("-0.26"),
            "value_of_x_Bjorken": Decimal("0.37"),
            "compton_form_factor_h_real": Decimal("-0.884"),
            "compton_form_factor_h_imaginary": Decimal("1.851"),
            "compton_form_factor_h_tilde_real": Decimal("3.118"),
            "compton_form_factor_h_tilde_imaginary": Decimal("0.911"),
            "compton_form_factor_e_real": Decimal("-0.424"),
            "compton_form_factor_e_imaginary": Decimal("0.649"),
            "compton_form_factor_e_tilde_real": Decimal("2.900"),
            "compton_form_factor_e_tilde_imaginary": Decimal("3.915")
        }
    ]


    # kinematics_and_cff_settings = [
    #     {
    #         "value_of_beam_energy": 5.75,
    #         "value_of_Q_squared": 1.82,
    #         "value_of_hadron_recoil": -0.17,
    #         "value_of_x_Bjorken": 0.34,
    #         "compton_form_factor_h_real": -0.897,
    #         "compton_form_factor_h_imaginary": 2.421,
    #         "compton_form_factor_h_tilde_real": 2.444,
    #         "compton_form_factor_h_tilde_imaginary": 1.131,
    #         "compton_form_factor_e_real": -0.541,
    #         "compton_form_factor_e_imaginary": 0.903,
    #         "compton_form_factor_e_tilde_real": 2.207,
    #         "compton_form_factor_e_tilde_imaginary": 5.383
    #     },
    #     {
    #         "value_of_beam_energy": 10.59,
    #         "value_of_Q_squared": 4.55,
    #         "value_of_hadron_recoil": -0.26,
    #         "value_of_x_Bjorken": 0.37,
    #         "compton_form_factor_h_real": -0.884,
    #         "compton_form_factor_h_imaginary": 1.851,
    #         "compton_form_factor_h_tilde_real": 3.118,
    #         "compton_form_factor_h_tilde_imaginary": 0.911,
    #         "compton_form_factor_e_real": -0.424,
    #         "compton_form_factor_e_imaginary": 0.649,
    #         "compton_form_factor_e_tilde_real": 2.900,
    #         "compton_form_factor_e_tilde_imaginary": 3.915
    #     }
    # ]

    # (2): Iterate over all the testing conditions:
    for kinematic_bin_index, kinematic_bin_settings in enumerate(kinematics_and_cff_settings):

        # (3): Define a bin number by adding 1 to an index value; classic Python:
        kinematic_bin_number = kinematic_bin_index + 1
        
        # (4.1): Obtain the value of Qsquared via dictionary keys:
        value_of_Q_squared = kinematic_bin_settings["value_of_Q_squared"]

        # (4.2): Obtain the value of xB via the dictionary:
        value_of_x_Bjorken = kinematic_bin_settings["value_of_x_Bjorken"]

        # (4.3): Obtain the value of t via dictionary keys:
        value_of_hadron_recoil = kinematic_bin_settings["value_of_hadron_recoil"]

        # (4.4): Obtain the value of k via dictionary keys:
        value_of_beam_energy = kinematic_bin_settings["value_of_beam_energy"]


        squared_Q_momentum_transfer = np.array([Decimal(value_of_Q_squared) for i in range(len(np.arange(0, 361, 1.)))])

        x_Bjorken = np.array([Decimal(value_of_x_Bjorken) for i in range(len(np.arange(0, 361, 1.)))])

        squared_hadronic_momentum_transfer_t = np.array([Decimal(value_of_hadron_recoil) for i in range(len(np.arange(0, 361, 1.)))])

        lab_kinematics_k = np.array([Decimal(value_of_beam_energy) for i in range(len(np.arange(0, 361, 1.)))])

        azimuthal_phi = np.array([Decimal(float(i)) for i in range(len(np.arange(0., 361., 1.)))])

        # compton_form_factor_h_real = np.array([kinematic_bin_settings["compton_form_factor_h_real"]])
        # compton_form_factor_h_imaginary = np.array([kinematic_bin_settings["compton_form_factor_h_imaginary"]])

        # compton_form_factor_h_tilde_real = np.array([kinematic_bin_settings["compton_form_factor_h_tilde_real"]])
        # compton_form_factor_h_tilde_imaginary = np.array([kinematic_bin_settings["compton_form_factor_h_tilde_imaginary"]])

        # compton_form_factor_e_real = np.array([kinematic_bin_settings["compton_form_factor_e_real"]])
        # compton_form_factor_e_imaginary = np.array([kinematic_bin_settings["compton_form_factor_e_imaginary"]])

        # compton_form_factor_e_tilde_real = np.array([kinematic_bin_settings["compton_form_factor_e_tilde_real"]])
        # compton_form_factor_e_tilde_imaginary = np.array([kinematic_bin_settings["compton_form_factor_e_tilde_imaginary"]])

        compton_form_factor_h_real = kinematic_bin_settings["compton_form_factor_h_real"]
        compton_form_factor_h_imaginary = kinematic_bin_settings["compton_form_factor_h_imaginary"]

        compton_form_factor_h_tilde_real = kinematic_bin_settings["compton_form_factor_h_tilde_real"]
        compton_form_factor_h_tilde_imaginary = kinematic_bin_settings["compton_form_factor_h_tilde_imaginary"]

        compton_form_factor_e_real = kinematic_bin_settings["compton_form_factor_e_real"]
        compton_form_factor_e_imaginary = kinematic_bin_settings["compton_form_factor_e_imaginary"]

        compton_form_factor_e_tilde_real = kinematic_bin_settings["compton_form_factor_e_tilde_real"]
        compton_form_factor_e_tilde_imaginary = kinematic_bin_settings["compton_form_factor_e_tilde_imaginary"]
        
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

        def analyze_dvcs_unp_beam_unp_target():

            pure_dvcs_unpolarized_beam_unpolarized_target = cross_section_prefactor * (Decimal("0.5") * 
                (calculate_dvcs_amplitude_squared(
                Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False) +
                calculate_dvcs_amplitude_squared(
                -Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)))
            
            pure_dvcs_unpolarized_beam_unpolarized_target_ww = cross_section_prefactor * (Decimal("0.5") * 
                (calculate_dvcs_amplitude_squared(
                Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True) +
                calculate_dvcs_amplitude_squared(
                -Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)))
            
            jd_mathematica_pure_dvcs_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'jd_dvcs_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v2.csv',
                names = ['jd_sigma'])
            
            jd_mathematica_pure_dvcs_unpolarized_beam_unpolarized_target_ww = pd.read_csv(
                f'jd_dvcs_unpolarized_beam_unpolarized_target_ww_kinematic_bin_{kinematic_bin_number}_v2.csv',
                names = ['jd_sigma_ww'])
            
            ji_paper_bkm_pure_dvcs_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'ji_plot_bkm_dvcs_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v1.csv',
                delimiter = ',')
            
            ji_mathematica_pure_dvcs_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'ji_dvcs_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v2.csv',
                names = ['ji_sigma'])
            
            ji_paper_cov_pure_dvcs_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'ji_plot_cov_dvcs_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v1.csv',
                delimiter = ',')
            
            ji_paper_bkm_ww_pure_dvcs_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'ji_plot_bkm_ww_dvcs_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v1.csv',
                delimiter = ',')
            
            figure_pure_dvcs_unpolarized_beam_unpolarized_target = plt.figure(figsize = (13.5, 10))

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
                x_data = ji_paper_bkm_pure_dvcs_unpolarized_beam_unpolarized_target['azimuthal_phi'],
                y_data = ji_paper_bkm_pure_dvcs_unpolarized_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Ji's BKM 10 (no WW)",
                color = 'gold',
                marker = '*')

            plot_pure_dvcs_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = ji_mathematica_pure_dvcs_unpolarized_beam_unpolarized_target,
                radial_size = 1.3,
                label = "Ji's Covariant Formalism with Dima's Mathematica",
                color = 'green')

            plot_pure_dvcs_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = ji_paper_cov_pure_dvcs_unpolarized_beam_unpolarized_target['azimuthal_phi'],
                y_data = ji_paper_cov_pure_dvcs_unpolarized_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Ji's Covariant Formalism",
                color = 'cyan',
                marker = "x")

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
            
            plot_pure_dvcs_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = ji_paper_bkm_ww_pure_dvcs_unpolarized_beam_unpolarized_target['azimuthal_phi'],
                y_data = ji_paper_bkm_ww_pure_dvcs_unpolarized_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Ji's BKM 10(WW)",
                color = 'maroon',
                marker = '+')
            
            plt.savefig(
                fname = f'compared_pure_dvcs_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v4.png',
                dpi = 500)
        
        def analyze_dvcs_plus_beam_unp_target():

            pure_dvcs_plus_beam_unpolarized_target = (cross_section_prefactor * calculate_dvcs_amplitude_squared(
                +Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False))
            
            pure_dvcs_plus_beam_unpolarized_target_ww = (cross_section_prefactor * calculate_dvcs_amplitude_squared(
                +Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True))
            
            jd_mathematica_pure_dvcs_plus_beam_unpolarized_target = pd.read_csv(
                f'jd_dvcs_plus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v2.csv',
                names = ['jd_sigma'])
            
            jd_mathematica_pure_dvcs_plus_beam_unpolarized_target_ww = pd.read_csv(
                f'jd_dvcs_plus_beam_unpolarized_target_ww_kinematic_bin_{kinematic_bin_number}_v2.csv',
                names = ['jd_sigma_ww'])
            
            ji_mathematica_pure_dvcs_plus_beam_unpolarized_target = pd.read_csv(
                f'ji_dvcs_plus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v2.csv',
                names = ['ji_sigma'])
            
            figure_pure_dvcs_plus_beam_unpolarized_target = plt.figure(figsize = (13.5, 10))

            axes_pure_dvcs_plus_beam_unpolarized_target = figure_pure_dvcs_plus_beam_unpolarized_target.add_subplot(1, 1, 1)
            
            plot_pure_dvcs_plus_beam_unpolarized_target = PlotCustomizer(
                axes_pure_dvcs_plus_beam_unpolarized_target,
                title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
                    round(value_of_beam_energy, 5), 
                    round(value_of_Q_squared, 5),
                    round(value_of_hadron_recoil, 5),
                    round(value_of_x_Bjorken, 5)),
                xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
                ylabel = r"$d^{4} \sigma^{{DVCS}}_{{\mathrm{{+U}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
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
                fname = f'compared_pure_dvcs_plus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v4.png',
                dpi = 500)

        def analyze_dvcs_minus_beam_unp_target():
            pass

        def analyze_interference_unp_beam_unp_target():
                
            pure_interference_unpolarized_beam_unpolarized_target = (cross_section_prefactor * (Decimal("0.5") * 
                (calculate_interference_contribution(Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False) +
                calculate_interference_contribution(-Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False))))
            
            pure_interference_unpolarized_beam_unpolarized_target_ww = (cross_section_prefactor * (Decimal("0.5") * 
                (calculate_interference_contribution(Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True) +
                calculate_interference_contribution(-Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True))))
            
            jd_mathematica_pure_interference_unpolarized_beam_unpolarized_target = pd.read_csv(
                    f'jd_interference_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v2.csv',
                    names = ['jd_sigma'])
                
            jd_mathematica_pure_interference_unpolarized_beam_unpolarized_target_ww = pd.read_csv(
                f'jd_interference_unpolarized_beam_unpolarized_target_ww_kinematic_bin_{kinematic_bin_number}_v2.csv',
                names = ['jd_sigma_ww'])
            
            ji_paper_bkm_pure_interference_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'ji_plot_bkm_interference_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v1.csv',
                delimiter = ',')
            
            ji_mathematica_pure_interference_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'ji_interference_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v2.csv',
                names = ['ji_sigma'])
            
            ji_paper_bkm_ww_pure_interference_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'ji_plot_bkm_ww_interference_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v1.csv',
                delimiter = ',')
            
            ji_paper_cov_pure_interference_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'ji_plot_cov_interference_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v1.csv',
                delimiter = ',')
            
            figure_pure_interference_unpolarized_beam_unpolarized_target = plt.figure(figsize = (13.5, 10))

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
                x_data = ji_paper_bkm_pure_interference_unpolarized_beam_unpolarized_target['azimuthal_phi'],
                y_data = ji_paper_bkm_pure_interference_unpolarized_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Ji's BKM 10 (no WW)",
                color = 'gold',
                marker = '*')

            plot_pure_interference_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = ji_mathematica_pure_interference_unpolarized_beam_unpolarized_target,
                radial_size = 1.3,
                label = "Ji's Covariant Formalism with Dima's Mathematica",
                color = 'green')
            
            plot_pure_interference_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = ji_paper_cov_pure_interference_unpolarized_beam_unpolarized_target['azimuthal_phi'],
                y_data = ji_paper_cov_pure_interference_unpolarized_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Ji's Covariant Formalism",
                color = 'cyan',
                marker = "x")

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
            
            plot_pure_interference_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = ji_paper_bkm_ww_pure_interference_unpolarized_beam_unpolarized_target['azimuthal_phi'],
                y_data = ji_paper_bkm_ww_pure_interference_unpolarized_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Ji's BKM 10(WW)",
                color = 'maroon',
                marker = '+')

            plt.savefig(
                fname = f'compared_pure_interference_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v4.png',
                dpi = 500)
    

        def analyze_interference_plus_beam_unp_target():
            
            pure_interference_plus_beam_unpolarized_target = (cross_section_prefactor * calculate_interference_contribution(Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False))
            
            pure_interference_plus_beam_unpolarized_target_ww = (cross_section_prefactor * calculate_interference_contribution(Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True))
            
            jd_mathematica_pure_interference_plus_beam_unpolarized_target = pd.read_csv(
                    f'jd_interference_plus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v2.csv',
                    names = ['jd_sigma'])
                
            jd_mathematica_pure_interference_plus_beam_unpolarized_target_ww = pd.read_csv(
                f'jd_interference_plus_beam_unpolarized_target_ww_kinematic_bin_{kinematic_bin_number}_v2.csv',
                names = ['jd_sigma_ww'])
            
            ji_mathematica_pure_interference_plus_beam_unpolarized_target = pd.read_csv(
                f'ji_interference_plus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v2.csv',
                names = ['ji_sigma'])
            
            ji_paper_bkm_ww_pure_interference_plus_beam_unpolarized_target = pd.read_csv(
                f'ji_plot_bkm_ww_interference_plus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v1.csv',
                delimiter = ',')
            
            figure_pure_interference_plus_beam_unpolarized_target = plt.figure(figsize = (13.5, 10))

            axes_pure_interference_plus_beam_unpolarized_target = figure_pure_interference_plus_beam_unpolarized_target.add_subplot(1, 1, 1)
            
            plot_pure_interference_plus_beam_unpolarized_target = PlotCustomizer(
                axes_pure_interference_plus_beam_unpolarized_target,
                title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
                    round(value_of_beam_energy, 5), 
                    round(value_of_Q_squared, 5),
                    round(value_of_hadron_recoil, 5),
                    round(value_of_x_Bjorken, 5)),
                xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
                ylabel = r"$d^{4} \sigma^{{I}}_{{\mathrm{{+U}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
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
            
            plot_pure_interference_plus_beam_unpolarized_target.add_scatter_plot(
                x_data = ji_paper_bkm_ww_pure_interference_plus_beam_unpolarized_target['azimuthal_phi'],
                y_data = ji_paper_bkm_ww_pure_interference_plus_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Ji's BKM 10(WW)",
                color = 'maroon',
                marker = '+')
            
            plt.savefig(
                fname = f'compared_pure_interference_plus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}_v4.png',
                dpi = 500)

        print("> Beginning analysis of DVCS, unpolarized beam, unpolarized target...")
        analyze_dvcs_unp_beam_unp_target()

        print("> Beginning analysis of DVCS, (+) polarized beam, unpolarized target...")
        analyze_dvcs_plus_beam_unp_target()

        print("> Beginning analysis of DVCS, (-) polarized beam, unpolarized target...")
        analyze_dvcs_minus_beam_unp_target()
        
        print("> Beginning analysis of Interference, unpolarized beam, unpolarized target...")
        analyze_interference_unp_beam_unp_target()

        print("> Beginning analysis of Interference, (+) beam, unpolarized target...")
        analyze_interference_plus_beam_unp_target()
    
    # pure_dvcs_minus_beam_unpolarized_target = cross_section_prefactor * calculate_dvcs_amplitude_squared(
    #     -Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)
    # pure_dvcs_minus_beam_unpolarized_target_ww = cross_section_prefactor * calculate_dvcs_amplitude_squared(
    #     -Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)
    
    # jd_mathematica_pure_dvcs_minus_beam_unpolarized_target = pd.read_csv('jd_dvcs_minus_beam_unpolarized_target_kinematic_bin_1_v2.csv', names = ['jd_sigma'])
    # jd_mathematica_pure_dvcs_minus_beam_unpolarized_target_ww = pd.read_csv('jd_dvcs_minus_beam_unpolarized_target_ww_kinematic_bin_1_v2.csv', names = ['jd_sigma_ww'])
    # ji_mathematica_pure_dvcs_minus_beam_unpolarized_target = pd.read_csv('ji_dvcs_minus_beam_unpolarized_target_kinematic_bin_1_v2.csv', names = ['ji_sigma'])
    
    # figure_pure_dvcs_minus_beam_unpolarized_target = plt.figure(figsize = (13.5, 10))
    # axes_pure_dvcs_minus_beam_unpolarized_target = figure_pure_dvcs_minus_beam_unpolarized_target.add_subplot(1, 1, 1)
    # plot_pure_dvcs_minus_beam_unpolarized_target = PlotCustomizer(
    #     axes_pure_dvcs_minus_beam_unpolarized_target,
    #     title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
    #         round(value_of_beam_energy, 5), 
    #         round(value_of_Q_squared, 5),
    #         round(value_of_hadron_recoil, 5),
    #         round(value_of_x_Bjorken, 5)),
    #     xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
    #     ylabel = r"$d^{4} \sigma^{{DVCS}}_{{\mathrm{{U-}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
    #     grid = True)
    
    # plot_pure_dvcs_minus_beam_unpolarized_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = convert_to_nb_over_GeV4(pure_dvcs_minus_beam_unpolarized_target),
    #     radial_size = 1.3,
    #     label = "Dima's BKM 10 Python (no WW)",
    #     color = 'blue')
    
    # plot_pure_dvcs_minus_beam_unpolarized_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = jd_mathematica_pure_dvcs_minus_beam_unpolarized_target,
    #     radial_size = 1.3,
    #     label = "Dima's BKM10 Mathematica (no WW)",
    #     color = 'red')
    
    # plot_pure_dvcs_minus_beam_unpolarized_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = ji_mathematica_pure_dvcs_minus_beam_unpolarized_target,
    #     radial_size = 1.3,
    #     label = "Ji's Covariant Formalism with Dima's Mathematica",
    #     color = 'green')
    
    # plot_pure_dvcs_minus_beam_unpolarized_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = convert_to_nb_over_GeV4(pure_dvcs_minus_beam_unpolarized_target_ww),
    #     radial_size = 1.3,
    #     label = "Dima's BKM 10 Python (WW)",
    #     color = 'purple')
    
    # plot_pure_dvcs_minus_beam_unpolarized_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = jd_mathematica_pure_dvcs_minus_beam_unpolarized_target_ww,
    #     radial_size = 1.3,
    #     label = "Dima's BKM10 Mathematica (WW)",
    #     color = 'orange')
    
    # plt.savefig(
    #     fname = 'compared_pure_dvcs_minus_plus_unpolarized_target_kinematic_bin_1_v4.png',
    #     dpi = 500)

    # pure_dvcs_unpolarized_beam_lp_target = cross_section_prefactor * (Decimal("0.5") * 
    #     (calculate_dvcs_amplitude_squared(
    #     Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False) +
    #     calculate_dvcs_amplitude_squared(
    #     -Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)))
    # pure_dvcs_unpolarized_beam_lp_target_ww = cross_section_prefactor * (Decimal("0.5") * 
    #     (calculate_dvcs_amplitude_squared(
    #     Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True) +
    #     calculate_dvcs_amplitude_squared(
    #     -Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)))

    # jd_mathematica_pure_dvcs_unpolarized_beam_lp_target = pd.read_csv('jd_dvcs_unpolarized_beam_lp_target_kinematic_bin_1_v2.csv', names = ['jd_sigma'])
    # jd_mathematica_pure_dvcs_unpolarized_beam_lp_target_ww = pd.read_csv('jd_dvcs_unpolarized_beam_lp_target_ww_kinematic_bin_1_v2.csv', names = ['jd_sigma_ww'])
    # ji_mathematica_pure_dvcs_unpolarized_beam_lp_target = pd.read_csv('ji_dvcs_unpolarized_beam_lp_target_kinematic_bin_1_v2.csv', names = ['ji_sigma'])
    
    # figure_pure_dvcs_unpolarized_beam_lp_target = plt.figure(figsize = (13.5, 10))
    # axes_pure_dvcs_unpolarized_beam_lp_target = figure_pure_dvcs_unpolarized_beam_lp_target.add_subplot(1, 1, 1)
    # plot_pure_dvcs_unpolarized_beam_lp_target = PlotCustomizer(
    #     axes_pure_dvcs_unpolarized_beam_lp_target,
    #     title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
    #         round(value_of_beam_energy, 5), 
    #         round(value_of_Q_squared, 5),
    #         round(value_of_hadron_recoil, 5),
    #         round(value_of_x_Bjorken, 5)),
    #     xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
    #     ylabel = r"$d^{4} \sigma^{{DVCS}}_{{\mathrm{{LU}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
    #     grid = True)
    
    # plot_pure_dvcs_unpolarized_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = convert_to_nb_over_GeV4(pure_dvcs_unpolarized_beam_lp_target),
    #     radial_size = 1.3,
    #     label = "Dima's BKM 10 Python (no WW)",
    #     color = 'blue')
    
    # plot_pure_dvcs_unpolarized_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = jd_mathematica_pure_dvcs_unpolarized_beam_lp_target,
    #     radial_size = 1.3,
    #     label = "Dima's BKM10 Mathematica (no WW)",
    #     color = 'red')
    
    # plot_pure_dvcs_unpolarized_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = ji_mathematica_pure_dvcs_unpolarized_beam_lp_target,
    #     radial_size = 1.3,
    #     label = "Ji's Covariant Formalism with Dima's Mathematica",
    #     color = 'green')
    
    # plot_pure_dvcs_unpolarized_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = convert_to_nb_over_GeV4(pure_dvcs_unpolarized_beam_lp_target_ww),
    #     radial_size = 1.3,
    #     label = "Dima's BKM 10 Python (WW)",
    #     color = 'purple')
    
    # plot_pure_dvcs_unpolarized_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = jd_mathematica_pure_dvcs_unpolarized_beam_lp_target_ww,
    #     radial_size = 1.3,
    #     label = "Dima's BKM10 Mathematica (WW)",
    #     color = 'orange')
    
    # plt.savefig(
    #     fname = 'compared_pure_dvcs_unpolarized_beam_lp_target_kinematic_bin_1_v4.png',
    #     dpi = 500)
    
    # pure_dvcs_plus_beam_lp_target = cross_section_prefactor * calculate_dvcs_amplitude_squared(
    #     Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)
    # pure_dvcs_plus_beam_lp_target_ww = cross_section_prefactor * calculate_dvcs_amplitude_squared(
    #     Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False) 
    
    # jd_mathematica_pure_dvcs_plus_beam_lp_target = pd.read_csv('jd_dvcs_plus_beam_lp_target_kinematic_bin_1_v2.csv', names = ['jd_sigma'])
    # jd_mathematica_pure_dvcs_plus_beam_lp_target_ww = pd.read_csv('jd_dvcs_plus_beam_lp_target_ww_kinematic_bin_1_v2.csv', names = ['jd_sigma_ww'])
    # ji_mathematica_pure_dvcs_plus_beam_lp_target = pd.read_csv('ji_dvcs_plus_beam_lp_target_kinematic_bin_1_v2.csv', names = ['ji_sigma'])

    # figure_pure_dvcs_plus_beam_lp_target = plt.figure(figsize = (13.5, 10))
    # axes_pure_dvcs_plus_beam_lp_target = figure_pure_dvcs_plus_beam_lp_target.add_subplot(1, 1, 1)
    # plot_pure_dvcs_plus_beam_lp_target = PlotCustomizer(
    #     axes_pure_dvcs_plus_beam_lp_target,
    #     title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
    #         round(value_of_beam_energy, 5), 
    #         round(value_of_Q_squared, 5),
    #         round(value_of_hadron_recoil, 5),
    #         round(value_of_x_Bjorken, 5)),
    #     xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
    #     ylabel = r"$d^{4} \sigma^{{DVCS}}_{{\mathrm{{L+}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
    #     grid = True)
    
    # plot_pure_dvcs_plus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = convert_to_nb_over_GeV4(pure_dvcs_plus_beam_lp_target),
    #     radial_size = 1.3,
    #     label = "Dima's BKM 10 Python (no WW)",
    #     color = 'blue')
    
    # plot_pure_dvcs_plus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = jd_mathematica_pure_dvcs_plus_beam_lp_target,
    #     radial_size = 1.3,
    #     label = "Dima's BKM10 Mathematica (no WW)",
    #     color = 'red')
    
    # plot_pure_dvcs_plus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = ji_mathematica_pure_dvcs_plus_beam_lp_target,
    #     radial_size = 1.3,
    #     label = "Ji's Covariant Formalism with Dima's Mathematica",
    #     color = 'green')
    
    # plot_pure_dvcs_plus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = convert_to_nb_over_GeV4(pure_dvcs_plus_beam_lp_target_ww),
    #     radial_size = 1.3,
    #     label = "Dima's BKM 10 Python (WW)",
    #     color = 'purple')
    
    # plot_pure_dvcs_plus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = jd_mathematica_pure_dvcs_plus_beam_lp_target_ww,
    #     radial_size = 1.3,
    #     label = "Dima's BKM10 Mathematica (WW)",
    #     color = 'orange')
    
    # plt.savefig(
    #     fname = 'compared_pure_dvcs_plus_beam_lp_target_kinematic_bin_1_v4.png',
    #     dpi = 500)
    
    # pure_dvcs_minus_beam_lp_target = cross_section_prefactor * calculate_dvcs_amplitude_squared(
    #     -Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)
    # pure_dvcs_minus_beam_lp_target_ww = cross_section_prefactor * calculate_dvcs_amplitude_squared(
    #     -Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True) 

    # jd_mathematica_pure_dvcs_minus_beam_lp_target = pd.read_csv('jd_dvcs_minus_beam_lp_target_kinematic_bin_1_v2.csv', names = ['jd_sigma'])
    # jd_mathematica_pure_dvcs_minus_beam_lp_target_ww = pd.read_csv('jd_dvcs_minus_beam_lp_target_ww_kinematic_bin_1_v2.csv', names = ['jd_sigma_ww'])
    # ji_mathematica_pure_dvcs_minus_beam_lp_target = pd.read_csv('ji_dvcs_minus_beam_lp_target_kinematic_bin_1_v2.csv', names = ['ji_sigma'])

    # figure_pure_dvcs_minus_beam_lp_target = plt.figure(figsize = (13.5, 10))
    # axes_pure_dvcs_minus_beam_lp_target = figure_pure_dvcs_minus_beam_lp_target.add_subplot(1, 1, 1)
    # plot_pure_dvcs_minus_beam_lp_target = PlotCustomizer(
    #     axes_pure_dvcs_minus_beam_lp_target,
    #     title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
    #         round(value_of_beam_energy, 5), 
    #         round(value_of_Q_squared, 5),
    #         round(value_of_hadron_recoil, 5),
    #         round(value_of_x_Bjorken, 5)),
    #     xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
    #     ylabel = r"$d^{4} \sigma^{{DVCS}}_{{\mathrm{{L-}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
    #     grid = True)
    
    # plot_pure_dvcs_minus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = convert_to_nb_over_GeV4(pure_dvcs_minus_beam_lp_target),
    #     radial_size = 1.3,
    #     label = "Dima's BKM 10 Python (no WW)",
    #     color = 'blue')
    
    # plot_pure_dvcs_minus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = jd_mathematica_pure_dvcs_minus_beam_lp_target,
    #     radial_size = 1.3,
    #     label = "Dima's BKM10 Mathematica (no WW)",
    #     color = 'red')
    
    # plot_pure_dvcs_minus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = ji_mathematica_pure_dvcs_minus_beam_lp_target,
    #     radial_size = 1.3,
    #     label = "Ji's Covariant Formalism with Dima's Mathematica",
    #     color = 'green')
    
    # plot_pure_dvcs_minus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = convert_to_nb_over_GeV4(pure_dvcs_minus_beam_lp_target_ww),
    #     radial_size = 1.3,
    #     label = "Dima's BKM 10 Python (WW)",
    #     color = 'purple')
    
    # plot_pure_dvcs_minus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = jd_mathematica_pure_dvcs_minus_beam_lp_target_ww,
    #     radial_size = 1.3,
    #     label = "Dima's BKM10 Mathematica (WW)",
    #     color = 'orange')
    
    # plt.savefig(
    #     fname = 'compared_pure_dvcs_minus_beam_lp_target_kinematic_bin_1_v4.png',
    #     dpi = 500)
    
    # pure_interference_plus_beam_unpolarized_target = cross_section_prefactor * calculate_interference_contribution(Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
    #     Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)
    # pure_interference_plus_beam_unpolarized_target_ww = cross_section_prefactor * calculate_interference_contribution(Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
    #     Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)
    
    # jd_mathematica_pure_interference_plus_beam_unpolarized_target = pd.read_csv('jd_interference_plus_beam_unpolarized_target_kinematic_bin_1_v2.csv', names = ['jd_sigma'])
    # jd_mathematica_pure_interference_plus_beam_unpolarized_target_ww = pd.read_csv('jd_interference_plus_beam_unpolarized_target_ww_kinematic_bin_1_v2.csv', names = ['jd_sigma_ww'])
    # ji_mathematica_pure_interference_plus_beam_unpolarized_target = pd.read_csv('ji_interference_plus_beam_unpolarized_target_kinematic_bin_1_v2.csv', names = ['ji_sigma'])

    # figure_pure_interference_plus_beam_unpolarized_target = plt.figure(figsize = (13.5, 10))
    # axes_pure_interference_plus_beam_unpolarized_target = figure_pure_interference_plus_beam_unpolarized_target.add_subplot(1, 1, 1)
    # plot_pure_interference_plus_beam_unpolarized_target = PlotCustomizer(
    #     axes_pure_interference_plus_beam_unpolarized_target,
    #     title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
    #         round(value_of_beam_energy, 5), 
    #         round(value_of_Q_squared, 5),
    #         round(value_of_hadron_recoil, 5),
    #         round(value_of_x_Bjorken, 5)),
    #     xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
    #     ylabel = r"$d^{4} \sigma^{{I}}_{{\mathrm{{UU}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
    #     grid = True)
    
    # plot_pure_interference_plus_beam_unpolarized_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = convert_to_nb_over_GeV4(pure_interference_plus_beam_unpolarized_target),
    #     radial_size = 1.3,
    #     label = "Dima's BKM 10 Python (no WW)",
    #     color = 'blue')
    
    # plot_pure_interference_plus_beam_unpolarized_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = jd_mathematica_pure_interference_plus_beam_unpolarized_target,
    #     radial_size = 1.3,
    #     label = "Dima's BKM10 Mathematica (no WW)",
    #     color = 'red')
    
    # plot_pure_interference_plus_beam_unpolarized_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = ji_mathematica_pure_interference_plus_beam_unpolarized_target,
    #     radial_size = 1.3,
    #     label = "Ji's Covariant Formalism with Dima's Mathematica",
    #     color = 'green')
    
    # plot_pure_interference_plus_beam_unpolarized_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = convert_to_nb_over_GeV4(pure_interference_plus_beam_unpolarized_target_ww),
    #     radial_size = 1.3,
    #     label = "Dima's BKM 10 Python (WW)",
    #     color = 'purple')
    
    # plot_pure_interference_plus_beam_unpolarized_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = jd_mathematica_pure_interference_plus_beam_unpolarized_target_ww,
    #     radial_size = 1.3,
    #     label = "Dima's BKM10 Mathematica (WW)",
    #     color = 'orange')
    
    # plt.savefig(
    #     fname = 'compared_pure_interference_plus_beam_unpolarized_target_kinematic_bin_1_v4.png',
    #     dpi = 500)
    
    # pure_interference_minus_beam_unpolarized_target = cross_section_prefactor * calculate_interference_contribution(-Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
    #     Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)
    # pure_interference_minus_beam_unpolarized_target_ww = cross_section_prefactor * calculate_interference_contribution(-Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
    #     Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)
    
    # jd_mathematica_pure_interference_minus_beam_unpolarized_target = pd.read_csv('jd_interference_minus_beam_unpolarized_target_kinematic_bin_1_v2.csv', names = ['jd_sigma'])
    # jd_mathematica_pure_interference_minus_beam_unpolarized_target_ww = pd.read_csv('jd_interference_minus_beam_unpolarized_target_ww_kinematic_bin_1_v2.csv', names = ['jd_sigma_ww'])
    # ji_mathematica_pure_interference_minus_beam_unpolarized_target = pd.read_csv('ji_interference_minus_beam_unpolarized_target_kinematic_bin_1_v2.csv', names = ['ji_sigma'])
    
    # figure_pure_interference_minus_beam_unpolarized_target = plt.figure(figsize = (13.5, 10))
    # axes_pure_interference_minus_beam_unpolarized_target = figure_pure_interference_minus_beam_unpolarized_target.add_subplot(1, 1, 1)
    # plot_pure_interference_minus_beam_unpolarized_target = PlotCustomizer(
    #     axes_pure_interference_minus_beam_unpolarized_target,
    #     title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
    #         round(value_of_beam_energy, 5), 
    #         round(value_of_Q_squared, 5),
    #         round(value_of_hadron_recoil, 5),
    #         round(value_of_x_Bjorken, 5)),
    #     xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
    #     ylabel = r"$d^{4} \sigma^{{I}}_{{\mathrm{{UU}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
    #     grid = True)
    
    # plot_pure_interference_minus_beam_unpolarized_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = convert_to_nb_over_GeV4(pure_interference_minus_beam_unpolarized_target),
    #     radial_size = 1.3,
    #     label = "Dima's BKM 10 Python (no WW)",
    #     color = 'blue')
    
    # plot_pure_interference_minus_beam_unpolarized_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = jd_mathematica_pure_interference_minus_beam_unpolarized_target,
    #     radial_size = 1.3,
    #     label = "Dima's BKM10 Mathematica (no WW)",
    #     color = 'red')
    
    # plot_pure_interference_minus_beam_unpolarized_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = ji_mathematica_pure_interference_minus_beam_unpolarized_target,
    #     radial_size = 1.3,
    #     label = "Ji's Covariant Formalism with Dima's Mathematica",
    #     color = 'green')
    
    # plot_pure_interference_minus_beam_unpolarized_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = convert_to_nb_over_GeV4(pure_interference_minus_beam_unpolarized_target_ww),
    #     radial_size = 1.3,
    #     label = "Dima's BKM 10 Python (WW)",
    #     color = 'purple')
    
    # plot_pure_interference_minus_beam_unpolarized_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = jd_mathematica_pure_interference_minus_beam_unpolarized_target_ww,
    #     radial_size = 1.3,
    #     label = "Dima's BKM10 Mathematica (WW)",
    #     color = 'orange')
    
    # plt.savefig(
    #     fname = 'compared_pure_interference_minus_beam_unpolarized_target_kinematic_bin_1_v4.png',
    #     dpi = 500)
    
    # pure_interference_unpolarized_beam_lp_target = cross_section_prefactor * (Decimal("0.5") * 
    #     (calculate_interference_contribution(Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
    #     Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False) +
    #     calculate_interference_contribution(-Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
    #     Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)))
    # pure_interference_unpolarized_beam_lp_target_ww = cross_section_prefactor * (Decimal("0.5") * 
    #     (calculate_interference_contribution(Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
    #     Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True) +
    #     calculate_interference_contribution(-Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
    #     Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)))
    
    # jd_mathematica_pure_interference_unpolarized_beam_lp_target = pd.read_csv('jd_interference_unpolarized_beam_lp_target_kinematic_bin_1_v2.csv', names = ['jd_sigma'])
    # jd_mathematica_pure_interference_unpolarized_beam_lp_target_ww = pd.read_csv('jd_interference_unpolarized_beam_lp_target_ww_kinematic_bin_1_v2.csv', names = ['jd_sigma_ww'])
    # ji_mathematica_pure_interference_unpolarized_beam_lp_target = pd.read_csv('ji_interference_unpolarized_beam_lp_target_kinematic_bin_1_v2.csv', names = ['ji_sigma'])

    # figure_pure_interference_unpolarized_beam_lp_target = plt.figure(figsize = (13.5, 10))
    # axes_pure_interference_unpolarized_beam_lp_target = figure_pure_interference_unpolarized_beam_lp_target.add_subplot(1, 1, 1)
    # plot_pure_interference_unpolarized_beam_lp_target = PlotCustomizer(
    #     axes_pure_interference_unpolarized_beam_lp_target,
    #     title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
    #         round(value_of_beam_energy, 5), 
    #         round(value_of_Q_squared, 5),
    #         round(value_of_hadron_recoil, 5),
    #         round(value_of_x_Bjorken, 5)),
    #     xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
    #     ylabel = r"$d^{4} \sigma^{{I}}_{{\mathrm{{UU}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
    #     grid = True)
    
    # plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = convert_to_nb_over_GeV4(pure_interference_unpolarized_beam_lp_target),
    #     radial_size = 1.3,
    #     label = "Dima's BKM 10 Python (no WW)",
    #     color = 'blue')
    
    # plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = jd_mathematica_pure_interference_unpolarized_beam_lp_target,
    #     radial_size = 1.3,
    #     label = "Dima's BKM10 Mathematica (no WW)",
    #     color = 'red')
    
    # plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = ji_mathematica_pure_interference_unpolarized_beam_lp_target,
    #     radial_size = 1.3,
    #     label = "Ji's Covariant Formalism with Dima's Mathematica",
    #     color = 'green')
    
    # plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = convert_to_nb_over_GeV4(pure_interference_unpolarized_beam_lp_target_ww),
    #     radial_size = 1.3,
    #     label = "Dima's BKM 10 Python (WW)",
    #     color = 'purple')
    
    # plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = jd_mathematica_pure_interference_unpolarized_beam_lp_target_ww,
    #     radial_size = 1.3,
    #     label = "Dima's BKM10 Mathematica (WW)",
    #     color = 'orange')
    
    # plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
    #     x_data = np.array([0., 50.31660231660232, 100.35521235521236, 150.11583011583014, 200.98841698841696, 249.91505791505787, 299.95366795366795, 350.2702702702703, 359.72200772200773, 25.019305019305037, 75.33590733590734, 126.48648648648651, 176.2471042471042, 227.39768339768344, 277.1583011583012, 330.5328185328185]),
    #     y_data = np.array([0.00007220216606498159, 0.011624548736462088, 0.01326113116726835, 0.006089049338146808, -0.004404332129963899, -0.012442839951865223, -0.012683513838748498, -0.002478941034897715, 0.000024067388688327196, 0.006714801444043319, 0.013838748495788204, 0.010324909747292423, 0.0007942238267147975, -0.009410348977135984, -0.01383874849578821, -0.0075330926594464505]),
    #     radial_size = 11.5,
    #     label = "Ji's Covariant Formalism",
    #     color = 'cyan',
    #     marker = "x")
    
    # plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
    #     x_data = np.array([0., 50.31660231660232, 100.07722007722005, 150.11583011583014, 200.98841698841696, 249.35907335907334, 299.95366795366795, 350.2702702702703, 359.72200772200773, 25.019305019305037, 75.33590733590734, 126.76447876447878, 176.2471042471042, 227.95366795366797, 277.1583011583012, 330.5328185328185]),
    #     y_data = np.array([0.00007220216606498159, 0.011624548736462088, 0.01326113116726835, 0.006089049338146808, -0.004404332129963899, -0.012250300842358609, -0.012683513838748498, -0.002478941034897715, 0.000024067388688327196, 0.006714801444043319, 0.013838748495788204, 0.010132370637785802, 0.0007942238267147975, -0.009362214199759328, -0.01383874849578821, -0.0075330926594464505]),
    #     radial_size = 11.5,
    #     label = "Ji's BKM 10(WW)",
    #     color = 'maroon',
    #     marker = '+')
    
    # plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
    #     x_data = np.array([0.5607476635513796, 51.58878504672895, 98.97196261682242, 151.40186915887847, 198.22429906542058, 249.81308411214948, 300.8411214953271, 348.22429906542055, 360., 25.79439252336447, 73.73831775700933, 123.08411214953269, 173.83177570093454, 226.5420560747663, 279.53271028037375, 326.0747663551402]),
    #     y_data = np.array([0.0000968523002421312, 0.014274616195272306, 0.011671710626265038, 0.004165657357499901, -0.0027350690347519094, -0.01042272036647104, -0.014660008502064262, -0.004793180414897196, -0.00008474576271187001, 0.009674131933771087, 0.014395681570574966, 0.008463478180744458, 0.0008363595366766563, -0.0068512917950424735, -0.013752018187294284, -0.01175443949480034]),
    #     radial_size = 11.5,
    #     label = "Ji's Lightcone Formalism",
    #     color = 'gray',
    #     marker = "d")
    
    # plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
    #     x_data = np.array([0.5607476635513796, 50.186915887850446, 100.09345794392522, 149.99999999999997, 199.62616822429905, 250.0934579439252, 299.99999999999994, 350.46728971962614, 360., 24.95327102803736, 75.70093457943925, 125.04672897196261, 174.9532710280374, 225.4205607476635, 275.0467289719626, 325.5140186915888, 325.5140186915888]),
    #     y_data = np.array([0.0000968523002421312, 0.015230024213075056, 0.012324455205811134, 0.004334140435835354, -0.0028087167070217946, -0.010859564164648911, -0.015762711864406784, -0.004140435835351088, -0.00008474576271187001, 0.010084745762711865, 0.015169491525423722, 0.008389830508474576, 0.0008232445520581153, -0.006743341404358354, -0.014309927360774816, -0.012615012106537534, -0.012615012106537534]),
    #     radial_size = 11.5,
    #     label = "Ji's BKM 10 (no WW)",
    #     color = 'gold',
    #     marker = '*')
    
    # # BELOW IS FOR KINEMATIC BIN 2

    # # plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
    # #     x_data = np.array([0.2767102229054543, 51.468101460415056, 99.89239046887012, 150.5303612605688, 201.72175249807842, 252.63643351268252, 299.67717140661034, 348.65488086087623, 360., 26.01076095311298, 74.98847040737895, 128.11683320522673, 175.71099154496542, 225.5188316679477, 277.2636433512683, 324.85780169100696]),
    # #     y_data = np.array([0.000004878048780487506, 0.0013560975609756098, 0.0010878048780487803, 0.0003902439024390245, -0.0002975609756097565, -0.0009853658536585366, -0.0013951219512195127, -0.00043414634146341467, -0.000014634146341463818, 0.0009219512195121952, 0.0013414634146341467, 0.0007170731707317076, 0.0000536585365853656, -0.0006097560975609753, -0.0012878048780487806, -0.0011463414634146347]),
    # #     radial_size = 11.5,
    # #     label = "Ji's Lightcone Formalism",
    # #     color = 'gray',
    # #     marker = "d")
    
    # # plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
    # #     x_data = np.array([0.2767102229054543, 50.36126056879324, 100.16910069177557, 150.5303612605688, 199.7847809377402, 250.14604150653344, 300.23059185242124, 350.0384319754035, 360., 24.903920061491167, 75.2651806302844, 125.34973097617215, 175.1575710991545, 224.41199077632595, 275.3266717909301, 325.1345119139124]),
    # #     y_data = np.array([0.000004878048780487506, 0.0013804878048780489, 0.001102439024390244, 0.00039512195121951224, -0.0002682926829268293, -0.000965853658536586, -0.001419512195121952, -0.00039512195121951257, -0.000014634146341463818, 0.000902439024390244, 0.0013707317073170734, 0.0007463414634146341, 0.00006341463414634148, -0.000604878048780488, -0.0012829268292682927, -0.00115609756097561]),
    # #     radial_size = 11.5,
    # #     label = "Ji's BKM 10 (no WW)",
    # #     color = 'gold',
    # #     marker = '*')
    
    # plt.savefig(
    #     fname = 'compared_pure_interference_unpolarized_beam_lp_target_kinematic_bin_1_v4.png',
    #     dpi = 500)
    
    # pure_interference_plus_beam_lp_target = cross_section_prefactor * calculate_interference_contribution(Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
    #     Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)
    # pure_interference_plus_beam_lp_target_ww = cross_section_prefactor * calculate_interference_contribution(Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
    #     Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)
    
    # jd_mathematica_pure_interference_plus_beam_lp_target = pd.read_csv('jd_interference_plus_beam_lp_target_kinematic_bin_1_v2.csv', names = ['jd_sigma'])
    # jd_mathematica_pure_interference_plus_beam_lp_target_ww = pd.read_csv('jd_interference_plus_beam_lp_target_ww_kinematic_bin_1_v2.csv', names = ['jd_sigma_ww'])
    # ji_mathematica_pure_interference_plus_beam_lp_target = pd.read_csv('ji_interference_plus_beam_lp_target_kinematic_bin_1_v2.csv', names = ['ji_sigma'])

    # figure_pure_interference_plus_beam_lp_target = plt.figure(figsize = (13.5, 10))
    # axes_pure_interference_plus_beam_lp_target = figure_pure_interference_plus_beam_lp_target.add_subplot(1, 1, 1)
    # plot_pure_interference_plus_beam_lp_target = PlotCustomizer(
    #     axes_pure_interference_plus_beam_lp_target,
    #     title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
    #         round(value_of_beam_energy, 5), 
    #         round(value_of_Q_squared, 5),
    #         round(value_of_hadron_recoil, 5),
    #         round(value_of_x_Bjorken, 5)),
    #     xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
    #     ylabel = r"$d^{4} \sigma^{{I}}_{{\mathrm{{UU}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
    #     grid = True)
    
    # plot_pure_interference_plus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = convert_to_nb_over_GeV4(pure_interference_plus_beam_lp_target),
    #     radial_size = 1.3,
    #     label = "Dima's BKM 10 Python (no WW)",
    #     color = 'blue')
    
    # plot_pure_interference_plus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = jd_mathematica_pure_interference_plus_beam_lp_target,
    #     radial_size = 1.3,
    #     label = "Dima's BKM10 Mathematica (no WW)",
    #     color = 'red')
    
    # plot_pure_interference_plus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = ji_mathematica_pure_interference_plus_beam_lp_target,
    #     radial_size = 1.3,
    #     label = "Ji's Covariant Formalism with Dima's Mathematica",
    #     color = 'green')
    
    # plot_pure_interference_plus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = convert_to_nb_over_GeV4(pure_interference_plus_beam_lp_target_ww),
    #     radial_size = 1.3,
    #     label = "Dima's BKM 10 Python (WW)",
    #     color = 'purple')
    
    # plot_pure_interference_plus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = jd_mathematica_pure_interference_plus_beam_lp_target_ww,
    #     radial_size = 1.3,
    #     label = "Dima's BKM10 Mathematica (WW)",
    #     color = 'orange')
    
    # plt.savefig(
    #     fname = 'compared_pure_interference_plus_beam_lp_target_kinematic_bin_1_v4.png',
    #     dpi = 500)
    
    # pure_interference_minus_beam_lp_target = cross_section_prefactor * calculate_interference_contribution(-Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
    #     Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)
    # pure_interference_minus_beam_lp_target_ww = cross_section_prefactor * calculate_interference_contribution(-Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
    #     epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
    #     Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)
    
    # jd_mathematica_pure_interference_minus_beam_lp_target = pd.read_csv('jd_interference_minus_beam_lp_target_kinematic_bin_1_v2.csv', names = ['jd_sigma'])
    # jd_mathematica_pure_interference_minus_beam_lp_target_ww = pd.read_csv('jd_interference_minus_beam_lp_target_ww_kinematic_bin_1_v2.csv', names = ['jd_sigma_ww'])
    # ji_mathematica_pure_interference_minus_beam_lp_target = pd.read_csv('ji_interference_minus_beam_lp_target_kinematic_bin_1_v2.csv', names = ['ji_sigma'])

    # figure_pure_interference_minus_beam_lp_target = plt.figure(figsize = (13.5, 10))
    # axes_pure_interference_minus_beam_lp_target = figure_pure_interference_minus_beam_lp_target.add_subplot(1, 1, 1)
    # plot_pure_interference_minus_beam_lp_target = PlotCustomizer(
    #     axes_pure_interference_minus_beam_lp_target,
    #     title = r"$E = {} \mathrm{{GeV}}, Q^{{2}} = {} \mathrm{{GeV}}^{{2}}, t = {} \mathrm{{GeV}}^{{2}}, x_{{\mathrm{{B}}}}= {}$".format(
    #         round(value_of_beam_energy, 5), 
    #         round(value_of_Q_squared, 5),
    #         round(value_of_hadron_recoil, 5),
    #         round(value_of_x_Bjorken, 5)),
    #     xlabel = r"$\phi \left[ \mathrm{{deg}} \right]$",
    #     ylabel = r"$d^{4} \sigma^{{I}}_{{\mathrm{{UU}}}} \left[ \mathrm{{nb}} / \mathrm{{GeV}}^{4} \right]$",
    #     grid = True)
    
    # plot_pure_interference_minus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = convert_to_nb_over_GeV4(pure_interference_minus_beam_lp_target),
    #     radial_size = 1.3,
    #     label = "Dima's BKM 10 Python (no WW)",
    #     color = 'blue')
    
    # plot_pure_interference_minus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = jd_mathematica_pure_interference_minus_beam_lp_target,
    #     radial_size = 1.3,
    #     label = "Dima's BKM10 Mathematica (no WW)",
    #     color = 'red')
    
    # plot_pure_interference_minus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = ji_mathematica_pure_interference_minus_beam_lp_target,
    #     radial_size = 1.3,
    #     label = "Ji's Covariant Formalism with Dima's Mathematica",
    #     color = 'green')
    
    # plot_pure_interference_minus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = convert_to_nb_over_GeV4(pure_interference_minus_beam_lp_target_ww),
    #     radial_size = 1.3,
    #     label = "Dima's BKM 10 Python (WW)",
    #     color = 'purple')
    
    # plot_pure_interference_minus_beam_lp_target.add_scatter_plot(
    #     x_data = azimuthal_phi,
    #     y_data = jd_mathematica_pure_interference_minus_beam_lp_target_ww,
    #     radial_size = 1.3,
    #     label = "Dima's BKM10 Mathematica (WW)",
    #     color = 'orange')
    
    # plt.savefig(
    #     fname = 'compared_pure_interference_minus_beam_lp_target_kinematic_bin_1_v4.png',
    #     dpi = 500)



if __name__ == "__main__":

    try:
        analysis()
    except Exception as ERROR:
        print(f"> Error running the analysis script: {ERROR}")
        sys.exit(0)

# pure_bh_unpolarized_beam_unpolarized_target = (Decimal("0.5") * (
# calculate_bh_amplitude_squared(Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
#     lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose) + 
# calculate_bh_amplitude_squared(
#     -Decimal("0.5"), 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
#     lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose)))

# # jd_mathematica_pure_bh_unpolarized_beam_unpolarized_target = pd.read_csv('jd_interference_bh_beam_unpolarized_target_kinematic_bin_1_v2.csv', names = ['jd_sigma'])
# # ji_mathematica_pure_bh_unpolarized_beam_unpolarized_target = pd.read_csv('ji_interference_bh_beam_unpolarized_target_kinematic_bin_1_v2.csv', names = ['ji_sigma'])

# pure_bh_plus_beam_unpolarized_target = calculate_bh_amplitude_squared(
#     Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
#     lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose)

# # jd_mathematica_pure_bh_plus_beam_unpolarized_target = pd.read_csv('jd_bh_plus_beam_unpolarized_target_kinematic_bin_1_v2.csv', names = ['jd_sigma'])
# # ji_mathematica_pure_bh_plus_beam_unpolarized_target = pd.read_csv('ji_bh_plus_beam_unpolarized_target_kinematic_bin_1_v2.csv', names = ['ji_sigma'])

# pure_bh_minus_beam_unpolarized_target = calculate_bh_amplitude_squared(
#     -Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
#     lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose)

# # jd_mathematica_pure_bh_minus_beam_unpolarized_target = pd.read_csv('jd_bh_minus_beam_unpolarized_target_kinematic_bin_1_v2.csv', names = ['jd_sigma'])
# # ji_mathematica_pure_bh_minus_beam_unpolarized_target = pd.read_csv('ji_bh_minus_beam_unpolarized_target_kinematic_bin_1_v2.csv', names = ['ji_sigma'])

# pure_bh_unpolarized_beam_lp_target = (Decimal("0.5") * (
# calculate_bh_amplitude_squared(Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
#     lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose) + 
# calculate_bh_amplitude_squared(
#     -Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
#     lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose)))

# # jd_mathematica_pure_bh_unpolarized_beam_lp_target = pd.read_csv('jd_bh_unpolarized_beam_lp_target_kinematic_bin_1_v2.csv', names = ['jd_sigma'])
# # ji_mathematica_pure_bh_unpolarized_beam_lp_target = pd.read_csv('ji_bh_unpolarized_beam_lp_target_kinematic_bin_1_v2.csv', names = ['ji_sigma'])

# pure_bh_plus_beam_unpolarized_target = calculate_bh_amplitude_squared(Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
#     lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose)

# # jd_mathematica_pure_bh_plus_beam_lp_target = pd.read_csv('jd_bh_plus_beam_lp_target_kinematic_bin_1_v2.csv', names = ['jd_sigma'])
# # ji_mathematica_pure_bh_plus_beam_lp_target = pd.read_csv('ji_bh_plus_beam_lp_target_kinematic_bin_1_v2.csv', names = ['ji_sigma'])

# pure_bh_minus_beam_lp_target = calculate_bh_amplitude_squared(
#     -Decimal("0.5"), 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
#     lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose)

# # jd_mathematica_pure_bh_minus_beam_lp_target = pd.read_csv('jd_bh_plus_minus_lp_target_kinematic_bin_1_v2.csv', names = ['jd_sigma'])
# # ji_mathematica_pure_bh_minus_beam_lp_target = pd.read_csv('ji_bh_plus_minus_lp_target_kinematic_bin_1_v2.csv', names = ['ji_sigma'])

# # We now calculate the pure DVCS squared term for the UNPOLARIZED target/UNPOLARIZED beam: