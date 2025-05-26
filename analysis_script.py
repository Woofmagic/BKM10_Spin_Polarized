import sys

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
    ## Description:
    Here, we generate all the comparison plots that we need.
    """

    verbose = False

    kinematics_and_cff_settings = [
        {
            "value_of_beam_energy": 5.75,
            "value_of_Q_squared": 1.82,
            "value_of_hadron_recoil": -0.17,
            "value_of_x_Bjorken": 0.34,
            "compton_form_factor_h_real": -0.897,
            "compton_form_factor_h_imaginary": 2.421,
            "compton_form_factor_h_tilde_real": 2.444,
            "compton_form_factor_h_tilde_imaginary": 1.131,
            "compton_form_factor_e_real": -0.541,
            "compton_form_factor_e_imaginary": 0.903,
            "compton_form_factor_e_tilde_real": 2.207,
            "compton_form_factor_e_tilde_imaginary": 5.383
        },
        {
            "value_of_beam_energy": 10.59,
            "value_of_Q_squared": 4.55,
            "value_of_hadron_recoil": -0.26,
            "value_of_x_Bjorken": 0.37,
            "compton_form_factor_h_real": -0.884,
            "compton_form_factor_h_imaginary": 1.851,
            "compton_form_factor_h_tilde_real": 3.118,
            "compton_form_factor_h_tilde_imaginary": 0.911,
            "compton_form_factor_e_real": -0.424,
            "compton_form_factor_e_imaginary": 0.649,
            "compton_form_factor_e_tilde_real": 2.900,
            "compton_form_factor_e_tilde_imaginary": 3.915
        }
    ]

    # (2): Iterate over all the testing conditions:
    for kinematic_bin_index, kinematic_bin_settings in enumerate(kinematics_and_cff_settings):

        if verbose:
            print(f"> Now iterating over Kinematic Bin Setting #{kinematic_bin_index + 1}")

        # (2.1): Define a bin number by adding 1 to an index value; classic Python:
        kinematic_bin_number = kinematic_bin_index + 1
        
        # (2.2): Obtain the value of Qsquared via dictionary keys:
        value_of_Q_squared = kinematic_bin_settings["value_of_Q_squared"]

        # (2.3): Obtain the value of xB via the dictionary:
        value_of_x_Bjorken = kinematic_bin_settings["value_of_x_Bjorken"]

        # (2.4): Obtain the value of t via dictionary keys:
        value_of_hadron_recoil = kinematic_bin_settings["value_of_hadron_recoil"]

        # (2.5): Obtain the value of k via dictionary keys:
        value_of_beam_energy = kinematic_bin_settings["value_of_beam_energy"]

        # (2.6): Obtain the value of the REAL part of the CFF H with the dictionary `kinematic_bin_settings`:
        compton_form_factor_h_real = kinematic_bin_settings["compton_form_factor_h_real"]

        # (2.7): Obtain the value of the IMAGINARY part of the CFF H with the dictionary `kinematic_bin_settings`:
        compton_form_factor_h_imaginary = kinematic_bin_settings["compton_form_factor_h_imaginary"]

        # (2.8): Obtain the value of the REAL part of the CFF E with the dictionary `kinematic_bin_settings`:
        compton_form_factor_e_real = kinematic_bin_settings["compton_form_factor_e_real"]

        # (2.9): Obtain the value of the IMAGINARY part of the CFF E with the dictionary `kinematic_bin_settings`:
        compton_form_factor_e_imaginary = kinematic_bin_settings["compton_form_factor_e_imaginary"]

        # (2.10): Obtain the value of the REAL part of the CFF H-tilde with the dictionary `kinematic_bin_settings`:
        compton_form_factor_h_tilde_real = kinematic_bin_settings["compton_form_factor_h_tilde_real"]

        # (2.11): Obtain the value of the IMAGINARY part of the CFF H-tilde with the dictionary `kinematic_bin_settings`:
        compton_form_factor_h_tilde_imaginary = kinematic_bin_settings["compton_form_factor_h_tilde_imaginary"]

        # (2.12): Obtain the value of the REAL part of the CFF E-tilde with the dictionary `kinematic_bin_settings`:
        compton_form_factor_e_tilde_real = kinematic_bin_settings["compton_form_factor_e_tilde_real"]

        # (2.13): Obtain the value of the IMAGINARY part of the CFF E-tilde with the dictionary `kinematic_bin_settings`:
        compton_form_factor_e_tilde_imaginary = kinematic_bin_settings["compton_form_factor_e_tilde_imaginary"]
        
        # (X): Cast to a complex type the H CFF function at the given kinematic settings:
        compton_form_factor_h = complex(compton_form_factor_h_real, compton_form_factor_h_imaginary)

        # (X): Cast to a complex type the Htilde CFF function at the given kinematic settings:
        compton_form_factor_h_tilde = complex(compton_form_factor_h_tilde_real, compton_form_factor_h_tilde_imaginary)

        # (X): Cast to a complex type the E CFF function at the given kinematic settings:
        compton_form_factor_e = complex(compton_form_factor_e_real, compton_form_factor_e_imaginary)

        # (X): Cast to a complex type the Etilde CFF function at the given kinematic settings:
        compton_form_factor_e_tilde = complex(compton_form_factor_e_tilde_real, compton_form_factor_e_tilde_imaginary)

        # (X): Want to do element-wise operations, so iterate it our for Q^{2}:
        squared_Q_momentum_transfer = np.array([value_of_Q_squared for _ in range(len(np.arange(0, 361, 1.)))])

        # (X): Want to do element-wise operations, so iterate it our for x_{B}:
        x_Bjorken = np.array([value_of_x_Bjorken for _ in range(len(np.arange(0, 361, 1.)))])

        # (X): Want to do element-wise operations, so iterate for t:
        squared_hadronic_momentum_transfer_t = np.array([value_of_hadron_recoil for _ in range(len(np.arange(0, 361, 1.)))])

        # (X): Want to do element-wise operations, so iterate it for the beam energy (k):
        lab_kinematics_k = np.array([value_of_beam_energy for _ in range(len(np.arange(0, 361, 1.)))])
        
        # (X): This is the *crucial line* --- it says that the azimuthal phi is really why we need element-wise operations:
        azimuthal_phi = np.array([phi for phi in range(len(np.arange(0., 361., 1.)))])

        # (X): Cast the Re[H] number to an NumPy array:
        compton_form_factor_h_real = np.array([kinematic_bin_settings["compton_form_factor_h_real"]])

        # (X): Cast the Im[H] number to an NumPy array:
        compton_form_factor_h_imaginary = np.array([kinematic_bin_settings["compton_form_factor_h_imaginary"]])

        # (X): Cast the Re[Htilde] number to an NumPy array:
        compton_form_factor_h_tilde_real = np.array([kinematic_bin_settings["compton_form_factor_h_tilde_real"]])

        # (X): Cast the Im[Htilde] number to an NumPy array:
        compton_form_factor_h_tilde_imaginary = np.array([kinematic_bin_settings["compton_form_factor_h_tilde_imaginary"]])

        # (X): Cast the Re[E] number to an NumPy array:
        compton_form_factor_e_real = np.array([kinematic_bin_settings["compton_form_factor_e_real"]])

        # (X): Cast the Im[E] number to an NumPy array:
        compton_form_factor_e_imaginary = np.array([kinematic_bin_settings["compton_form_factor_e_imaginary"]])

        # (X): Cast the Re[Etilde] number to an NumPy array:
        compton_form_factor_e_tilde_real = np.array([kinematic_bin_settings["compton_form_factor_e_tilde_real"]])

        # (X): Cast the Im[Etilde] number to an NumPy array:
        compton_form_factor_e_tilde_imaginary = np.array([kinematic_bin_settings["compton_form_factor_e_tilde_imaginary"]])

        # (2.X): Calculate Epsilon:
        # - the value commented out comes from a Desmos comparison
        # epsilon = 0.472935565613
        epsilon = calculate_kinematics_epsilon(
            squared_Q_momentum_transfer,
            x_Bjorken,
            verbose)

        # (2.X): Calculate the Lepton Energy Fraction:
        # - the value commented out comes from a Desmos comparison
        # lepton_energy_fraction_y = 0.496096170172
        lepton_energy_fraction_y = calculate_kinematics_lepton_energy_fraction_y(
            squared_Q_momentum_transfer,
            lab_kinematics_k,
            epsilon,
            verbose)
        
        # (2.X): Calculate the Skewness Parameter:
        # - the value commented out comes from a Desmos comparison
        # skewness_parameter = 0.199061888371
        skewness_parameter = calculate_kinematics_skewness_parameter(
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            verbose)

        # (2.X): Calculate t_minimum:
        # - the value commented out comes from a Desmos comparison
        # squared_hadronic_momentum_transfer_t_minimum = -0.13551822229
        squared_hadronic_momentum_transfer_t_minimum = calculate_kinematics_t_min(
            squared_Q_momentum_transfer,
            x_Bjorken,
            epsilon,
            verbose)

        # (2.X): Calculate t_prime:
        # - t_prime is determined by t and t_min, so we don't need a hard-coded value
        # - from Desmos to run this simple function
        t_prime = calculate_kinematics_t_prime(
            squared_hadronic_momentum_transfer_t,
            squared_hadronic_momentum_transfer_t_minimum,
            verbose)

        # (2.X): Calculate K_tilde:
        # - the value commented out comes from a Desmos comparison
        # k_tilde = 0.153827372074
        k_tilde = calculate_kinematics_k_tilde(
            squared_Q_momentum_transfer,
            x_Bjorken,
            lepton_energy_fraction_y,
            squared_hadronic_momentum_transfer_t,
            epsilon,
            squared_hadronic_momentum_transfer_t_minimum,
            verbose)
        
        # (2.X): Calculate K:
        # - the value commented out comes from a Desmos comparison
        # shorthand_k = 0.0820394232521
        shorthand_k = calculate_kinematics_k(
            squared_Q_momentum_transfer,
            lepton_energy_fraction_y,
            epsilon,
            k_tilde,
            verbose)

        # (2.X): Calculate k_dot_delta:
        # - again, this value is derived from earlier ones and
        # - will be consistent whether calculated in Python or Desmos
        k_dot_delta = calculate_k_dot_delta(
            squared_Q_momentum_transfer,
            x_Bjorken,
            squared_hadronic_momentum_transfer_t,
            azimuthal_phi,
            epsilon,
            lepton_energy_fraction_y,
            shorthand_k,
            verbose)

        # (2.X): Calculate Lepton Propagator 1:
        lepton_propagator_p1 = calculate_lepton_propagator_p1(
            squared_Q_momentum_transfer,
            k_dot_delta,
            verbose)
        
        # (2.X): Calculate Lepton Propagator 2:
        lepton_propagator_p2 = calculate_lepton_propagator_p2(
            squared_Q_momentum_transfer,
            squared_hadronic_momentum_transfer_t,
            k_dot_delta,
            verbose)
        
        # (2.X): Calculate the Electric Form Factor
        electric_form_factor = calculate_form_factor_electric(
            squared_hadronic_momentum_transfer_t, 
            verbose)

        # (2.X): Calculate the Magnetic Form Factor
        magnetic_form_factor = calculate_form_factor_magnetic(
            electric_form_factor,
            verbose) 

        # (2.X): Calculate the Pauli Form Factor, F2:
        # - the value commented out comes from a Desmos comparison
        # Pauli_form_factor_F2 = 1.0986689028
        Pauli_form_factor_F2 = calculate_form_factor_pauli_f2(
            squared_hadronic_momentum_transfer_t,
            electric_form_factor,
            magnetic_form_factor,
            verbose)

        # (2.X): Calculate the Dirac Form Factor, F1:
        # - the value commented out comes from a Desmos comparison
        # Dirac_form_factor_F1 = 0.68565636208
        Dirac_form_factor_F1 = calculate_form_factor_dirac_f1(
            magnetic_form_factor,
            Pauli_form_factor_F2,
            verbose)
        
        # (2.X): Calculate the cross-section prefactor:
        # - the value commented out comes from a Desmos comparison
        # cross_section_prefactor = 3.5309551538e-10
        cross_section_prefactor = calculate_bkm10_cross_section_prefactor(
            squared_Q_momentum_transfer,
            x_Bjorken,
            epsilon,
            lepton_energy_fraction_y,
            verbose)
        
        def analyze_bh_unpolarized_beam_unpolarized_target():
            
            # (1): Generate the pure DVCS cross-section with: (unpolarized beam, unpolarized target, no WW)
            pure_dvcs_unpolarized_beam_unpolarized_target = (cross_section_prefactor * (0.5 *
                (calculate_bh_amplitude_squared(
                1.0, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, False) +
                calculate_bh_amplitude_squared(
                -1.0, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, False))))
            
            # (2): Read the data generated from the BKM10 code *in Mathematica* with: (unpolarized beam, unpolarized target, no WW)
            jd_mathematica_pure_dvcs_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'jd_dvcs_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma'])
            
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
                radial_size = 4.,
                label = "JD's BKM 10 Python (no WW)",
                color = 'blue',
                marker = 'x')

            plot_pure_dvcs_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_dvcs_unpolarized_beam_unpolarized_target,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (no WW)",
                color = 'red')
            
            plt.savefig(
                fname = f'compared_pure_bh_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.png',
                dpi = 500)
            
            plt.close()

        def analyze_dvcs_unpolarized_beam_unpolarized_target():
            
            # (1): Generate the pure DVCS cross-section with: (unpolarized beam, unpolarized target, no WW)
            pure_dvcs_unpolarized_beam_unpolarized_target = (cross_section_prefactor * (0.5 *
                (calculate_dvcs_amplitude_squared(
                1.0, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False) +
                calculate_dvcs_amplitude_squared(
                -1.0, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False))))
            
            # (3): Ji' s Fig. (5.a) (kin. set. #1) and (5.b) (kin. set #2) in [2109.10373] has BKM10 *without* the WW relations applied (red curve):
            lcd_desmos_bkm_dvcs_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'lcd_dvcs_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                delimiter = ',')
            
            # (3): Ji' s Fig. (5.a) (kin. set. #1) and (5.b) (kin. set #2) in [2109.10373] has BKM10 *without* the WW relations applied (red curve):
            lcd_desmos_bkm_dvcs_unpolarized_beam_unpolarized_target_ww = pd.read_csv(
                f'lcd_dvcs_unpolarized_beam_unpolarized_target_ww_kinematic_bin_{kinematic_bin_number}.csv',
                delimiter = ',')
            
            # (2): Read the data generated from the BKM10 code *in Mathematica* with: (unpolarized beam, unpolarized target, no WW)
            jd_mathematica_pure_dvcs_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'jd_dvcs_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma'])
            
            # (3): Ji' s Fig. (5.a) (kin. set. #1) and (5.b) (kin. set #2) in [2109.10373] has BKM10 *without* the WW relations applied (red curve):
            ji_paper_bkm_pure_dvcs_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'ji_plot_bkm_dvcs_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                delimiter = ',')
            
            # (4): Ji's Fig. (13.a) (kin. set. #1) and (13.b) (kin. set #2) in [2109.10373] is his own formalism *with* the WW applied (orange curve): 
            ji_paper_cov_pure_dvcs_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'ji_plot_cov_dvcs_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                delimiter = ',')
            
            # (5): Generate the pure DVCS cross-section with: (unpolarized beam, unpolarized target, WW)
            pure_dvcs_unpolarized_beam_unpolarized_target_ww = (cross_section_prefactor * (0.5 *
                (calculate_dvcs_amplitude_squared(
                1.0, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True) +
                calculate_dvcs_amplitude_squared(
                -1.0, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True))))
            
            # (6): Ji's formalism coded up in Mathematica with: (unpolarized beam, unpolarized target, WW):
            ji_mathematica_pure_dvcs_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'ji_dvcs_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['ji_sigma'])
            
            # (7): Read the data generated from the BKM10 code *in Mathematica* with: (unpolarized beam, unpolarized target, WW)
            jd_mathematica_pure_dvcs_unpolarized_beam_unpolarized_target_ww = pd.read_csv(
                f'jd_dvcs_unpolarized_beam_unpolarized_target_ww_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma_ww'])
            
            # (8): Ji' s Fig. (13.a) (kin. set. #1) and (13.b) (kin. set #2) in [2109.10373] has BKM10 *with* the WW relations applied (blue curve):
            ji_paper_bkm_ww_pure_dvcs_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'ji_plot_bkm_ww_dvcs_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                delimiter = ',')
            
            figure_pure_dvcs_unpolarized_beam_unpolarized_target = plt.figure(figsize = (15, 10))

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
                radial_size = 4.,
                label = "JD's BKM 10 Python (no WW)",
                color = 'blue',
                marker = 'x')

            plot_pure_dvcs_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_dvcs_unpolarized_beam_unpolarized_target,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (no WW)",
                color = 'red')
            
            plot_pure_dvcs_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = lcd_desmos_bkm_dvcs_unpolarized_beam_unpolarized_target['azimuthal_phi'],
                y_data = lcd_desmos_bkm_dvcs_unpolarized_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Liliet's Desmos BKM 10 (no WW)",
                color = 'turquoise',
                marker = '8')
            
            plot_pure_dvcs_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = lcd_desmos_bkm_dvcs_unpolarized_beam_unpolarized_target_ww['azimuthal_phi'],
                y_data = lcd_desmos_bkm_dvcs_unpolarized_beam_unpolarized_target_ww['cross_section'],
                radial_size = 11.5,
                label = "Liliet's Desmos BKM 10 (WW)",
                color = 'dodgerblue',
                marker = '8')

            plot_pure_dvcs_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = ji_paper_bkm_pure_dvcs_unpolarized_beam_unpolarized_target['azimuthal_phi'],
                y_data = ji_paper_bkm_pure_dvcs_unpolarized_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Ji's Paper with BKM 10 (no WW)",
                color = 'gold',
                marker = '*')

            plot_pure_dvcs_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = ji_mathematica_pure_dvcs_unpolarized_beam_unpolarized_target,
                radial_size = 1.3,
                label = "Ji's  Formalism with JD's Mathematica (WW)",
                color = 'green')

            plot_pure_dvcs_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = ji_paper_cov_pure_dvcs_unpolarized_beam_unpolarized_target['azimuthal_phi'],
                y_data = ji_paper_cov_pure_dvcs_unpolarized_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Ji's Formalism Plot (WW)",
                color = 'cyan',
                marker = "x")

            plot_pure_dvcs_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = convert_to_nb_over_GeV4(pure_dvcs_unpolarized_beam_unpolarized_target_ww),
                radial_size = 4.,
                label = "JD's BKM 10 Python (WW)",
                color = 'purple',
                marker = 'd',)

            plot_pure_dvcs_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_dvcs_unpolarized_beam_unpolarized_target_ww,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (WW)",
                color = 'orange')
            
            plot_pure_dvcs_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = ji_paper_bkm_ww_pure_dvcs_unpolarized_beam_unpolarized_target['azimuthal_phi'],
                y_data = ji_paper_bkm_ww_pure_dvcs_unpolarized_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Ji's Paper with BKM 10 (WW)",
                color = 'maroon',
                marker = '+')
            
            plt.savefig(
                fname = f'compared_pure_dvcs_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.png',
                dpi = 500)
            
            plt.close()
        
        def analyze_dvcs_plus_beam_unpolarized_target():

            # (1): Generate the pure DVCS cross-section with: ((+)-polarized) beam, unpolarized target, no WW)
            pure_dvcs_plus_beam_unpolarized_target = (cross_section_prefactor * calculate_dvcs_amplitude_squared(
                +1.0, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False))
            
            # (3): Ji' s Fig. (5.a) (kin. set. #1) and (5.b) (kin. set #2) in [2109.10373] has BKM10 *without* the WW relations applied (red curve):
            lcd_desmos_bkm_dvcs_plus_beam_unpolarized_target = pd.read_csv(
                f'lcd_dvcs_plus_beam_unpolarized_target_kinematic_bin_1.csv',
                delimiter = ',')
            
            # (2): Read the data generated from the BKM10 code *in Mathematica* with: ((+)-polarized beam, unpolarized target, no WW)
            jd_mathematica_pure_dvcs_plus_beam_unpolarized_target = pd.read_csv(
                f'jd_dvcs_plus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma'])
            
            # (3): Generate the pure DVCS cross-section with: ((+)-polarized) beam, unpolarized target, WW)
            pure_dvcs_plus_beam_unpolarized_target_ww = (cross_section_prefactor * calculate_dvcs_amplitude_squared(
                +1.0, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True))
            
            # (4): Read the data generated from the BKM10 code *in Mathematica* with: ((+)-polarized beam, unpolarized target, WW)
            jd_mathematica_pure_dvcs_plus_beam_unpolarized_target_ww = pd.read_csv(
                f'jd_dvcs_plus_beam_unpolarized_target_ww_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma_ww'])
            
            # (5): Ji's formalism coded up in Mathematica with: ((+)-polarized beam, unpolarized target, WW):
            ji_mathematica_pure_dvcs_plus_beam_unpolarized_target = pd.read_csv(
                f'ji_dvcs_plus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
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
                radial_size = 4.,
                label = "JD's BKM 10 Python (no WW)",
                color = 'blue',
                marker = 'x')
            
            plot_pure_dvcs_plus_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_dvcs_plus_beam_unpolarized_target,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (no WW)",
                color = 'red')
            
            plot_pure_dvcs_plus_beam_unpolarized_target.add_scatter_plot(
                x_data = lcd_desmos_bkm_dvcs_plus_beam_unpolarized_target['azimuthal_phi'],
                y_data = lcd_desmos_bkm_dvcs_plus_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Liliet's Desmos BKM 10 (WW)",
                color = 'dodgerblue',
                marker = '8')

            plot_pure_dvcs_plus_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = ji_mathematica_pure_dvcs_plus_beam_unpolarized_target,
                radial_size = 1.3,
                label = "Ji's  Formalism with JD's Mathematica (WW)",
                color = 'green')

            plot_pure_dvcs_plus_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = convert_to_nb_over_GeV4(pure_dvcs_plus_beam_unpolarized_target_ww),
                radial_size = 4.,
                label = "JD's BKM 10 Python (WW)",
                color = 'purple',
                marker = 'd',)

            plot_pure_dvcs_plus_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_dvcs_plus_beam_unpolarized_target_ww,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (WW)",
                color = 'orange')
            
            plt.savefig(
                fname = f'compared_pure_dvcs_plus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.png',
                dpi = 500)
            
            plt.close()

        def analyze_dvcs_minus_beam_unpolarized_target():
            
            # (1): Generate the pure DVCS cross-section with: ((-)-polarized) beam, unpolarized target, no WW)
            pure_dvcs_minus_beam_unpolarized_target = (cross_section_prefactor * calculate_dvcs_amplitude_squared(
                -1.0, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False))
            
            # (3): Ji' s Fig. (5.a) (kin. set. #1) and (5.b) (kin. set #2) in [2109.10373] has BKM10 *without* the WW relations applied (red curve):
            lcd_desmos_bkm_dvcs_minus_beam_unpolarized_target = pd.read_csv(
                f'lcd_dvcs_minus_beam_unpolarized_target_kinematic_bin_1.csv',
                delimiter = ',')
            
            # (2): Read the data generated from the BKM10 code *in Mathematica* with: ((-)-polarized beam, unpolarized target, no WW)
            jd_mathematica_pure_dvcs_minus_beam_unpolarized_target = pd.read_csv(
                f'jd_dvcs_minus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv', 
                names = ['jd_sigma'])
            
            # (3): Generate the pure DVCS cross-section with: ((-)-polarized) beam, unpolarized target, WW)
            ji_mathematica_pure_dvcs_minus_beam_unpolarized_target = pd.read_csv(
                f'ji_dvcs_minus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['ji_sigma'])
            
            # (4): Read the data generated from the BKM10 code *in Mathematica* with: ((-)-polarized beam, unpolarized target, WW)
            pure_dvcs_minus_beam_unpolarized_target_ww = (cross_section_prefactor * calculate_dvcs_amplitude_squared(
                -1.0, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True))
            
            # (5): Ji's formalism coded up in Mathematica with: ((-)-polarized beam, unpolarized target, WW):
            jd_mathematica_pure_dvcs_minus_beam_unpolarized_target_ww = pd.read_csv(
                f'jd_dvcs_minus_beam_unpolarized_target_ww_kinematic_bin_{kinematic_bin_number}.csv', 
                names = ['jd_sigma_ww'])
            
            figure_pure_dvcs_minus_beam_unpolarized_target = plt.figure(figsize = (13.5, 10))

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
                radial_size = 4.,
                label = "JD's BKM 10 Python (no WW)",
                color = 'blue',
                marker = 'x')
            
            plot_pure_dvcs_minus_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_dvcs_minus_beam_unpolarized_target,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (no WW)",
                color = 'red')
            
            plot_pure_dvcs_minus_beam_unpolarized_target.add_scatter_plot(
                x_data = lcd_desmos_bkm_dvcs_minus_beam_unpolarized_target['azimuthal_phi'],
                y_data = lcd_desmos_bkm_dvcs_minus_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Liliet's Desmos BKM 10 (WW)",
                color = 'dodgerblue',
                marker = '8')
            
            plot_pure_dvcs_minus_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = ji_mathematica_pure_dvcs_minus_beam_unpolarized_target,
                radial_size = 1.3,
                label = "Ji's  Formalism with JD's Mathematica (WW)",
                color = 'green')
            
            plot_pure_dvcs_minus_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = convert_to_nb_over_GeV4(pure_dvcs_minus_beam_unpolarized_target_ww),
                radial_size = 4.,
                label = "JD's BKM 10 Python (WW)",
                color = 'purple',
                marker = 'd',)
            
            plot_pure_dvcs_minus_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_dvcs_minus_beam_unpolarized_target_ww,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (WW)",
                color = 'orange')
            
            plt.savefig(
                fname = f'compared_pure_dvcs_minus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.png',
                dpi = 500)
            
            plt.close()

        def analyze_dvcs_unpolarized_beam_polarized_target():

            # (1): Generate the pure DVCS cross-section with: (unpolarized beam, longitudinally-polarized target, no WW)
            pure_dvcs_unpolarized_beam_lp_target = (cross_section_prefactor * (0.5 * 
                (calculate_dvcs_amplitude_squared(
                1.0, 0.5, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False) +
                calculate_dvcs_amplitude_squared(
                -1.0, 0.5, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False))))

            # (2): Read the data generated from the BKM10 code *in Mathematica* with: (unpolarized beam, longitudinally-polarized target, no WW)
            jd_mathematica_pure_dvcs_unpolarized_beam_lp_target = pd.read_csv(
                f'jd_dvcs_unpolarized_beam_lp_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma'])
            
            # (3): Generate the pure DVCS cross-section with: (unpolarized beam, longitudinally-polarized target, WW)
            pure_dvcs_unpolarized_beam_lp_target_ww = (cross_section_prefactor * (0.5 * 
                (calculate_dvcs_amplitude_squared(
                1.0, 0.5, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True) +
                calculate_dvcs_amplitude_squared(
                -1.0, 0.5, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True))))
            
            # (4): Read the data generated from the BKM10 code *in Mathematica* with: (unpolarized beam, longitudinally-polarized target, WW)
            jd_mathematica_pure_dvcs_unpolarized_beam_lp_target_ww = pd.read_csv(
                f'jd_dvcs_unpolarized_beam_lp_target_ww_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma_ww'])
            
            # (5): Ji's formalism coded up in Mathematica with: (unpolarized beam, longitudinally-polarized target, WW):
            ji_mathematica_pure_dvcs_unpolarized_beam_lp_target = pd.read_csv(
                'ji_dvcs_unpolarized_beam_lp_target_kinematic_bin_1.csv',
                names = ['ji_sigma'])
            
            figure_pure_dvcs_unpolarized_beam_lp_target = plt.figure(figsize = (13.5, 10))

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
                radial_size = 4.,
                label = "JD's BKM 10 Python (no WW)",
                color = 'blue',
                marker = 'x')
            
            plot_pure_dvcs_unpolarized_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_dvcs_unpolarized_beam_lp_target,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (no WW)",
                color = 'red')
            
            # plot_pure_dvcs_unpolarized_beam_lp_target.add_scatter_plot(
            #     x_data = azimuthal_phi,
            #     y_data = ji_mathematica_pure_dvcs_unpolarized_beam_lp_target,
            #     radial_size = 1.3,
            #     label = "Ji's  Formalism with JD's Mathematica (WW)",
            #     color = 'green')
            
            plot_pure_dvcs_unpolarized_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = convert_to_nb_over_GeV4(pure_dvcs_unpolarized_beam_lp_target_ww),
                radial_size = 4.,
                label = "JD's BKM 10 Python (WW)",
                color = 'purple',
                marker = 'd',)
            
            plot_pure_dvcs_unpolarized_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_dvcs_unpolarized_beam_lp_target_ww,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (WW)",
                color = 'orange')
            
            plt.savefig(
                fname = f'compared_pure_dvcs_unpolarized_beam_lp_target_kinematic_bin_{kinematic_bin_number}.png',
                dpi = 500)
            
            plt.close()
            
        def analyze_dvcs_plus_beam_polarized_target():

            # (1): Generate the pure DVCS cross-section with: ((+)-polarized beam, longitudinally-polarized target, no WW)
            pure_dvcs_plus_beam_lp_target = (cross_section_prefactor * calculate_dvcs_amplitude_squared(
                1.0, 0.5, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False))
            
            # (3): Ji' s Fig. (5.a) (kin. set. #1) and (5.b) (kin. set #2) in [2109.10373] has BKM10 *without* the WW relations applied (red curve):
            lcd_desmos_bkm_dvcs_plus_beam_lp_target = pd.read_csv(
                f'lcd_dvcs_plus_beam_lp_target_kinematic_bin_1.csv',
                delimiter = ',')
            
            # (2): Read the data generated from the BKM10 code *in Mathematica* with: ((+)-polarized beam, longitudinally-polarized target, no WW)
            jd_mathematica_pure_dvcs_plus_beam_lp_target = pd.read_csv(
                f'jd_dvcs_plus_beam_lp_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma'])
            
            # (3): Generate the pure DVCS cross-section with: ((+)-polarized beam, longitudinally-polarized target, WW)
            pure_dvcs_plus_beam_lp_target_ww = (cross_section_prefactor * calculate_dvcs_amplitude_squared(
                1.0, 0.5, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True))

            # (4): Read the data generated from the BKM10 code *in Mathematica* with: ((+)-polarized beam, longitudinally-polarized target, WW)
            jd_mathematica_pure_dvcs_plus_beam_lp_target_ww = pd.read_csv(
                f'jd_dvcs_plus_beam_lp_target_ww_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma_ww'])

            # (5): Ji's formalism coded up in Mathematica with: ((+)-polarized beam, longitudinally-polarized target, WW):
            ji_mathematica_pure_dvcs_plus_beam_lp_target = pd.read_csv(
                f'ji_dvcs_plus_beam_lp_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['ji_sigma'])

            figure_pure_dvcs_plus_beam_lp_target = plt.figure(figsize = (13.5, 10))

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
                radial_size = 4.,
                label = "JD's BKM 10 Python (no WW)",
                color = 'blue',
                marker = 'x')
            
            plot_pure_dvcs_plus_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_dvcs_plus_beam_lp_target,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (no WW)",
                color = 'red')
            
            plot_pure_dvcs_plus_beam_lp_target.add_scatter_plot(
                x_data = lcd_desmos_bkm_dvcs_plus_beam_lp_target['azimuthal_phi'],
                y_data = lcd_desmos_bkm_dvcs_plus_beam_lp_target['cross_section'],
                radial_size = 11.5,
                label = "Liliet's Desmos BKM 10 (WW)",
                color = 'dodgerblue',
                marker = '8')
            
            # plot_pure_dvcs_plus_beam_lp_target.add_scatter_plot(
            #     x_data = azimuthal_phi,
            #     y_data = ji_mathematica_pure_dvcs_plus_beam_lp_target,
            #     radial_size = 1.3,
            #     label = "Ji's  Formalism with JD's Mathematica (WW)",
            #     color = 'green')
            
            plot_pure_dvcs_plus_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = convert_to_nb_over_GeV4(pure_dvcs_plus_beam_lp_target_ww),
                radial_size = 4.,
                label = "JD's BKM 10 Python (WW)",
                color = 'purple',
                marker = 'd',)
            
            plot_pure_dvcs_plus_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_dvcs_plus_beam_lp_target_ww,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (WW)",
                color = 'orange')
            
            plt.savefig(
                fname = f'compared_pure_dvcs_plus_beam_lp_target_kinematic_bin_{kinematic_bin_number}.png',
                dpi = 500)
            
            plt.close()
            
        def analyze_dvcs_minus_beam_polarized_target():
            
            # (1): Generate the pure DVCS cross-section with: ((-)-polarized beam, longitudinally-polarized target, no WW)
            pure_dvcs_minus_beam_lp_target = (cross_section_prefactor * calculate_dvcs_amplitude_squared(
                -1.0, 0.5, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False))

            # (3): Ji' s Fig. (5.a) (kin. set. #1) and (5.b) (kin. set #2) in [2109.10373] has BKM10 *without* the WW relations applied (red curve):
            lcd_desmos_bkm_dvcs_minus_beam_lp_target = pd.read_csv(
                f'lcd_dvcs_minus_beam_lp_target_kinematic_bin_1.csv',
                delimiter = ',')
            
            # (2): Read the data generated from the BKM10 code *in Mathematica* with: ((-)-polarized beam, longitudinally-polarized target, no WW)
            jd_mathematica_pure_dvcs_minus_beam_lp_target = pd.read_csv(
                f'jd_dvcs_minus_beam_lp_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma'])
            
            # (3): Generate the pure DVCS cross-section with: ((-)-polarized beam, longitudinally-polarized target, WW)
            pure_dvcs_minus_beam_lp_target_ww = (cross_section_prefactor * calculate_dvcs_amplitude_squared(
                -1.0, 0.5, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, shorthand_k, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True) )
            
            # (4): Read the data generated from the BKM10 code *in Mathematica* with: ((-)-polarized beam, longitudinally-polarized target, WW)
            jd_mathematica_pure_dvcs_minus_beam_lp_target_ww = pd.read_csv(
                f'jd_dvcs_minus_beam_lp_target_ww_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma_ww'])

            # (5): Ji's formalism coded up in Mathematica with: ((-)-polarized beam, longitudinally-polarized target, WW):
            ji_mathematica_pure_dvcs_minus_beam_lp_target = pd.read_csv(
                f'ji_dvcs_minus_beam_lp_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['ji_sigma'])


            figure_pure_dvcs_minus_beam_lp_target = plt.figure(figsize = (13.5, 10))

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
                radial_size = 4.,
                label = "JD's BKM 10 Python (no WW)",
                color = 'blue',
                marker = 'x')
            
            plot_pure_dvcs_minus_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_dvcs_minus_beam_lp_target,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (no WW)",
                color = 'red')
            
            plot_pure_dvcs_minus_beam_lp_target.add_scatter_plot(
                x_data = lcd_desmos_bkm_dvcs_minus_beam_lp_target['azimuthal_phi'],
                y_data = lcd_desmos_bkm_dvcs_minus_beam_lp_target['cross_section'],
                radial_size = 11.5,
                label = "Liliet's Desmos BKM 10 (WW)",
                color = 'dodgerblue',
                marker = '8')
            
            # plot_pure_dvcs_minus_beam_lp_target.add_scatter_plot(
            #     x_data = azimuthal_phi,
            #     y_data = ji_mathematica_pure_dvcs_minus_beam_lp_target,
            #     radial_size = 1.3,
            #     label = "Ji's  Formalism with JD's Mathematica (WW)",
            #     color = 'green')
            
            plot_pure_dvcs_minus_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = convert_to_nb_over_GeV4(pure_dvcs_minus_beam_lp_target_ww),
                radial_size = 4.,
                label = "JD's BKM 10 Python (WW)",
                color = 'purple',
                marker = 'd',)
            
            plot_pure_dvcs_minus_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_dvcs_minus_beam_lp_target_ww,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (WW)",
                color = 'orange')
            
            plt.savefig(
                fname = f'compared_pure_dvcs_minus_beam_lp_target_kinematic_bin_{kinematic_bin_number}.png',
                dpi = 500)
            
            plt.close()
            
        def analyze_interference_unpolarized_beam_unpolarized_target():

            # (1): Generate the pure Interference cross-section with: (unpolarized beam, unpolarized target, no WW)
            pure_interference_unpolarized_beam_unpolarized_target = (cross_section_prefactor * (0.5 *
                (calculate_interference_contribution(1.0, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False) +
                calculate_interference_contribution(-1.0, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False))))
            
            # (3): Ji' s Fig. (5.a) (kin. set. #1) and (5.b) (kin. set #2) in [2109.10373] has BKM10 *without* the WW relations applied (red curve):
            lcd_desmos_bkm_interference_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'lcd_interference_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                delimiter = ',')
            
            # (2): Read the data generated from the BKM10 code *in Mathematica* with: (unpolarized beam, unpolarized target, no WW)
            jd_mathematica_pure_interference_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'jd_interference_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma'])
            
            # (3): Ji' s Fig. (7.a) (kin. set. #1) and (7.b) (kin. set #2) in [2109.10373] has BKM10 *without* the WW relations applied (red curve):
            ji_paper_bkm_pure_interference_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'ji_plot_bkm_interference_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                delimiter = ',')
            
            # (4): Ji's Fig. (14.a) (kin. set. #1) and (14.b) (kin. set #2) in [2109.10373] is his own formalism *with* the WW applied (orange curve): 
            ji_paper_cov_pure_interference_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'ji_plot_cov_interference_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                delimiter = ',')
            
            # (5): Generate the pure DVCS cross-section with: (unpolarized beam, unpolarized target, WW)
            pure_interference_unpolarized_beam_unpolarized_target_ww = (cross_section_prefactor * (0.5 *
                (calculate_interference_contribution(1.0, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True) +
                calculate_interference_contribution(-1.0, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True))))
            
            # (6): Ji's formalism coded up in Mathematica with: (unpolarized beam, unpolarized target, WW):
            ji_mathematica_pure_interference_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'ji_interference_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['ji_sigma'])
            
            # (7): Read the data generated from the BKM10 code *in Mathematica* with: (unpolarized beam, unpolarized target, WW)
            jd_mathematica_pure_interference_unpolarized_beam_unpolarized_target_ww = pd.read_csv(
                f'jd_interference_unpolarized_beam_unpolarized_target_ww_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma_ww'])
            
            # (8): Ji' s Fig. (14.a) (kin. set. #1) and (14.b) (kin. set #2) in [2109.10373] has BKM10 *with* the WW relations applied (blue curve):
            ji_paper_bkm_ww_pure_interference_unpolarized_beam_unpolarized_target = pd.read_csv(
                f'ji_plot_bkm_ww_interference_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
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
                radial_size = 4.,
                label = "JD's BKM 10 Python (no WW)",
                color = 'blue',
                marker = 'x')
            
            plot_pure_interference_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_interference_unpolarized_beam_unpolarized_target,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (no WW)",
                color = 'red')
            
            plot_pure_interference_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = lcd_desmos_bkm_interference_unpolarized_beam_unpolarized_target['azimuthal_phi'],
                y_data = lcd_desmos_bkm_interference_unpolarized_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Liliet's Desmos BKM 10 (WW)",
                color = 'dodgerblue',
                marker = '8')

            plot_pure_interference_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = ji_paper_bkm_pure_interference_unpolarized_beam_unpolarized_target['azimuthal_phi'],
                y_data = ji_paper_bkm_pure_interference_unpolarized_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Ji's Paper with BKM 10 (no WW)",
                color = 'gold',
                marker = '*')

            plot_pure_interference_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = ji_mathematica_pure_interference_unpolarized_beam_unpolarized_target,
                radial_size = 1.3,
                label = "Ji's  Formalism with JD's Mathematica (WW)",
                color = 'green')
            
            plot_pure_interference_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = ji_paper_cov_pure_interference_unpolarized_beam_unpolarized_target['azimuthal_phi'],
                y_data = ji_paper_cov_pure_interference_unpolarized_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Ji's Formalism Plot (WW)",
                color = 'cyan',
                marker = "x")

            plot_pure_interference_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = convert_to_nb_over_GeV4(pure_interference_unpolarized_beam_unpolarized_target_ww),
                radial_size = 4.,
                label = "JD's BKM 10 Python (WW)",
                color = 'purple',
                marker = 'd',)

            plot_pure_interference_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_interference_unpolarized_beam_unpolarized_target_ww,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (WW)",
                color = 'orange')
            
            plot_pure_interference_unpolarized_beam_unpolarized_target.add_scatter_plot(
                x_data = ji_paper_bkm_ww_pure_interference_unpolarized_beam_unpolarized_target['azimuthal_phi'],
                y_data = ji_paper_bkm_ww_pure_interference_unpolarized_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Ji's Paper with BKM 10 (WW)",
                color = 'maroon',
                marker = '+')

            plt.savefig(
                fname = f'compared_pure_interference_unpolarized_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.png',
                dpi = 500)
            
            plt.close()
        
        def analyze_interference_plus_beam_unpolarized_target():
            
            pure_interference_plus_beam_unpolarized_target = (cross_section_prefactor * calculate_interference_contribution(1.0, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
            epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k, lepton_propagator_p1, lepton_propagator_p2,
            Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False))
        
            # (3): Ji' s Fig. (5.a) (kin. set. #1) and (5.b) (kin. set #2) in [2109.10373] has BKM10 *without* the WW relations applied (red curve):
            lcd_desmos_bkm_interference_plus_beam_unpolarized_target = pd.read_csv(
                f'lcd_interference_plus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                delimiter = ',')
            
            jd_mathematica_pure_interference_plus_beam_unpolarized_target = pd.read_csv(
                    f'jd_interference_plus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                    names = ['jd_sigma'])
            
            pure_interference_plus_beam_unpolarized_target_ww = (cross_section_prefactor * calculate_interference_contribution(1.0, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k, lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True))
                
            jd_mathematica_pure_interference_plus_beam_unpolarized_target_ww = pd.read_csv(
                f'jd_interference_plus_beam_unpolarized_target_ww_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma_ww']) 
            
            ji_mathematica_pure_interference_plus_beam_unpolarized_target = pd.read_csv(
                f'ji_interference_plus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['ji_sigma'])
            
            ji_paper_bkm_ww_pure_interference_plus_beam_unpolarized_target = pd.read_csv(
                f'ji_plot_bkm_ww_interference_plus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
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
            
            # plot_pure_interference_plus_beam_unpolarized_target.add_scatter_plot(
            #     x_data = azimuthal_phi,
            #     y_data = convert_to_nb_over_GeV4(pure_interference_plus_beam_unpolarized_target),
            #     radial_size = 4.,
            #     label = "Dima's BKM 10 Python (no WW)",
            #     color = 'blue',
            #     marker = 'x')
            
            # plot_pure_interference_plus_beam_unpolarized_target.add_scatter_plot(
            #     x_data = azimuthal_phi,
            #     y_data = jd_mathematica_pure_interference_plus_beam_unpolarized_target,
            #     radial_size = 1.3,
            #     label = "Dima's BKM10 Mathematica (no WW)",
            #     color = 'red')

            plot_pure_interference_plus_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = ji_mathematica_pure_interference_plus_beam_unpolarized_target,
                radial_size = 1.3,
                label = "Ji's  Formalism with Dima's Mathematica (WW)",
                color = 'green')

            plot_pure_interference_plus_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = convert_to_nb_over_GeV4(pure_interference_plus_beam_unpolarized_target_ww),
                radial_size = 4.,
                label = "Dima's BKM 10 Python (WW)",
                color = 'purple',
                marker = 'd',)

            plot_pure_interference_plus_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_interference_plus_beam_unpolarized_target_ww,
                radial_size = 1.3,
                label = "Dima's BKM10 Mathematica (WW)",
                color = 'orange')
            
            plot_pure_interference_plus_beam_unpolarized_target.add_scatter_plot(
                x_data = lcd_desmos_bkm_interference_plus_beam_unpolarized_target['azimuthal_phi'],
                y_data = lcd_desmos_bkm_interference_plus_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Liliet's Desmos BKM 10 (WW)",
                color = 'dodgerblue',
                marker = '8')
            
            plot_pure_interference_plus_beam_unpolarized_target.add_scatter_plot(
                x_data = ji_paper_bkm_ww_pure_interference_plus_beam_unpolarized_target['azimuthal_phi'],
                y_data = ji_paper_bkm_ww_pure_interference_plus_beam_unpolarized_target['cross_section'],
                radial_size = 16.5,
                label = "Ji's Paper with BKM 10 (WW)",
                color = 'maroon',
                marker = '+')
            
            plt.legend(markerscale = 5, fontsize = 15)
            
            plt.savefig(
                fname = f'compared_pure_interference_plus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.png',
                dpi = 500)
            
            plt.close()
                
        def analyze_interference_minus_beam_unpolarized_target():

            pure_interference_minus_beam_unpolarized_target = (cross_section_prefactor * calculate_interference_contribution(-1.0, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False))
            
            lcd_desmos_bkm_interference_minus_beam_unpolarized_target = pd.read_csv(
                f'lcd_interference_minus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                delimiter = ',')
            
            pure_interference_minus_beam_unpolarized_target_ww = (cross_section_prefactor * calculate_interference_contribution(-1.0, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True))
            
            jd_mathematica_pure_interference_minus_beam_unpolarized_target = pd.read_csv(
                f'jd_interference_minus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma'])
            
            jd_mathematica_pure_interference_minus_beam_unpolarized_target_ww = pd.read_csv(
                f'jd_interference_minus_beam_unpolarized_target_ww_kinematic_bin_{kinematic_bin_number}.csv', 
                names = ['jd_sigma_ww'])
            
            ji_mathematica_pure_interference_minus_beam_unpolarized_target = pd.read_csv(
                f'ji_interference_minus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['ji_sigma'])
            
            figure_pure_interference_minus_beam_unpolarized_target = plt.figure(figsize = (13.5, 10))
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
                radial_size = 4.,
                label = "JD's BKM 10 Python (no WW)",
                color = 'blue',
                marker = 'x')
            
            plot_pure_interference_minus_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_interference_minus_beam_unpolarized_target,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (no WW)",
                color = 'red')
            
            plot_pure_interference_minus_beam_unpolarized_target.add_scatter_plot(
                x_data = lcd_desmos_bkm_interference_minus_beam_unpolarized_target['azimuthal_phi'],
                y_data = lcd_desmos_bkm_interference_minus_beam_unpolarized_target['cross_section'],
                radial_size = 11.5,
                label = "Liliet's Desmos BKM 10 (WW)",
                color = 'dodgerblue',
                marker = '8')
            
            plot_pure_interference_minus_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = ji_mathematica_pure_interference_minus_beam_unpolarized_target,
                radial_size = 1.3,
                label = "Ji's  Formalism with JD's Mathematica (WW)",
                color = 'green')
            
            plot_pure_interference_minus_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = convert_to_nb_over_GeV4(pure_interference_minus_beam_unpolarized_target_ww),
                radial_size = 4.,
                label = "JD's BKM 10 Python (WW)",
                color = 'purple',
                marker = 'd',)
            
            plot_pure_interference_minus_beam_unpolarized_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_interference_minus_beam_unpolarized_target_ww,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (WW)",
                color = 'orange')
            
            plt.savefig(
                fname = f'compared_pure_interference_minus_beam_unpolarized_target_kinematic_bin_{kinematic_bin_number}.png',
                dpi = 500)
            
            plt.close()

        def analyze_interference_unpolarized_beam_polarized_target():

            pure_interference_unpolarized_beam_lp_target_ww = (cross_section_prefactor * (0.5 * 
                (calculate_interference_contribution(1.0, 0.5, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True) +
                calculate_interference_contribution(-1.0, 0.5, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True))))

            pure_interference_unpolarized_beam_lp_target = (cross_section_prefactor * (0.5 * 
                (calculate_interference_contribution(1.0, 0.5, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False) +
                calculate_interference_contribution(-1.0, 0.5, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False))))
            
            # (3): Ji' s Fig. (5.a) (kin. set. #1) and (5.b) (kin. set #2) in [2109.10373] has BKM10 *without* the WW relations applied (red curve):
            lcd_desmos_bkm_interference_unpolarized_beam_lp_target = pd.read_csv(
                f'lcd_interference_unpolarized_beam_lp_target_kinematic_bin_{kinematic_bin_number}.csv',
                delimiter = ',')
            
            jd_mathematica_pure_interference_unpolarized_beam_lp_target = pd.read_csv(
                f'jd_interference_unpolarized_beam_lp_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma'])
            
            jd_mathematica_pure_interference_unpolarized_beam_lp_target_ww = pd.read_csv(
                f'jd_interference_unpolarized_beam_lp_target_ww_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma_ww'])
            
            ji_mathematica_pure_interference_unpolarized_beam_lp_target = pd.read_csv(
                f'ji_interference_unpolarized_beam_lp_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['ji_sigma'])
            
            # ji_paper_bkm_pure_interference_unpolarized_beam_lp_target = pd.read_csv(
            #     f'ji_plot_bkm_interference_unpolarized_beam_lp_target_kinematic_bin_{kinematic_bin_number}.csv',
            #     delimiter = ',')
            
            # ji_paper_cov_pure_interference_unpolarized_beam_lp_target = pd.read_csv(
            #     f'ji_plot_cov_interference_unpolarized_beam_lp_target_kinematic_bin_{kinematic_bin_number}.csv',
            #     delimiter = ',')
            
            # ji_paper_bkm_ww_pure_interference_unpolarized_beam_lp_target = pd.read_csv(
            #     f'ji_plot_bkm_ww_interference_unpolarized_beam_lp_target_kinematic_bin_{kinematic_bin_number}.csv',
            #     delimiter = ',')

            figure_pure_interference_unpolarized_beam_lp_target = plt.figure(figsize = (13.5, 10))
            
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
                radial_size = 4.,
                label = "JD's BKM 10 Python (no WW)",
                color = 'blue',
                marker = 'x')
            
            plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_interference_unpolarized_beam_lp_target,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (no WW)",
                color = 'red')
            
            plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
                x_data = lcd_desmos_bkm_interference_unpolarized_beam_lp_target['azimuthal_phi'],
                y_data = lcd_desmos_bkm_interference_unpolarized_beam_lp_target['cross_section'],
                radial_size = 11.5,
                label = "Liliet's Desmos BKM 10 (WW)",
                color = 'dodgerblue',
                marker = '8')
            
            plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = ji_mathematica_pure_interference_unpolarized_beam_lp_target,
                radial_size = 1.3,
                label = "Ji's  Formalism with JD's Mathematica (WW)",
                color = 'green')
            
            plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = convert_to_nb_over_GeV4(pure_interference_unpolarized_beam_lp_target_ww),
                radial_size = 4.,
                label = "JD's BKM 10 Python (WW)",
                color = 'purple',
                marker = 'd',)
            
            plot_pure_interference_unpolarized_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_interference_unpolarized_beam_lp_target_ww,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (WW)",
                color = 'orange')
            
            plt.savefig(
                fname = f'compared_pure_interference_unpolarized_beam_lp_target_kinematic_bin_{kinematic_bin_number}.png',
                dpi = 500)
            
            plt.close()
            
        def analyze_interference_plus_beam_polarized_target():

            pure_interference_plus_beam_lp_target_ww = (cross_section_prefactor * calculate_interference_contribution(1.0, 0.5, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True))
            
            pure_interference_plus_beam_lp_target = (cross_section_prefactor * calculate_interference_contribution(1.0, 0.5, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False))
            
            # (3): Ji' s Fig. (5.a) (kin. set. #1) and (5.b) (kin. set #2) in [2109.10373] has BKM10 *without* the WW relations applied (red curve):
            lcd_desmos_bkm_interference_plus_beam_lp_target = pd.read_csv(
                f'lcd_interference_plus_beam_lp_target_kinematic_bin_{kinematic_bin_number}.csv',
                delimiter = ',')
            
            jd_mathematica_pure_interference_plus_beam_lp_target = pd.read_csv(
                f'jd_interference_plus_beam_lp_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma'])

            jd_mathematica_pure_interference_plus_beam_lp_target_ww = pd.read_csv(
                f'jd_interference_plus_beam_lp_target_ww_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma_ww'])

            ji_mathematica_pure_interference_plus_beam_lp_target = pd.read_csv(
                f'ji_interference_plus_beam_lp_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['ji_sigma'])

            figure_pure_interference_plus_beam_lp_target = plt.figure(figsize = (13.5, 10))
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
                radial_size = 4.,
                label = "JD's BKM 10 Python (no WW)",
                color = 'blue',
                marker = 'x')
            
            plot_pure_interference_plus_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_interference_plus_beam_lp_target,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (no WW)",
                color = 'red')
            
            plot_pure_interference_plus_beam_lp_target.add_scatter_plot(
                x_data = lcd_desmos_bkm_interference_plus_beam_lp_target['azimuthal_phi'],
                y_data = lcd_desmos_bkm_interference_plus_beam_lp_target['cross_section'],
                radial_size = 11.5,
                label = "Liliet's Desmos BKM 10 (WW)",
                color = 'dodgerblue',
                marker = '8')
            
            plot_pure_interference_plus_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = ji_mathematica_pure_interference_plus_beam_lp_target,
                radial_size = 1.3,
                label = "Ji's  Formalism with JD's Mathematica (WW)",
                color = 'green')
            
            plot_pure_interference_plus_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = convert_to_nb_over_GeV4(pure_interference_plus_beam_lp_target_ww),
                radial_size = 4.,
                label = "JD's BKM 10 Python (WW)",
                color = 'purple',
                marker = 'd',)
            
            plot_pure_interference_plus_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_interference_plus_beam_lp_target_ww,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (WW)",
                color = 'orange')
            
            plt.savefig(
                fname = f'compared_pure_interference_plus_beam_lp_target_kinematic_bin_{kinematic_bin_number}.png',
                dpi = 500)
            
            plt.close()
            
        def analyze_interference_minus_beam_polarized_target():

            pure_interference_minus_beam_lp_target = cross_section_prefactor * calculate_interference_contribution(-1.0, 0.5, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, False)
            
            pure_interference_minus_beam_lp_target_ww = cross_section_prefactor * calculate_interference_contribution(-1.0, 0.5, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi,
                epsilon, lepton_energy_fraction_y, skewness_parameter, t_prime, k_tilde, shorthand_k,lepton_propagator_p1, lepton_propagator_p2,
                Dirac_form_factor_F1, Pauli_form_factor_F2, compton_form_factor_h, compton_form_factor_h_tilde, compton_form_factor_e, compton_form_factor_e_tilde, True)
            
            jd_mathematica_pure_interference_minus_beam_lp_target = pd.read_csv(
                f'jd_interference_minus_beam_lp_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma'])

            jd_mathematica_pure_interference_minus_beam_lp_target_ww = pd.read_csv(
                f'jd_interference_minus_beam_lp_target_ww_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['jd_sigma_ww'])

            ji_mathematica_pure_interference_minus_beam_lp_target = pd.read_csv(
                f'ji_interference_minus_beam_lp_target_kinematic_bin_{kinematic_bin_number}.csv',
                names = ['ji_sigma'])

            figure_pure_interference_minus_beam_lp_target = plt.figure(figsize = (13.5, 10))
            
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
                radial_size = 4.,
                label = "JD's BKM 10 Python (no WW)",
                color = 'blue',
                marker = 'x')
            
            plot_pure_interference_minus_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_interference_minus_beam_lp_target,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (no WW)",
                color = 'red')
            
            plot_pure_interference_minus_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = ji_mathematica_pure_interference_minus_beam_lp_target,
                radial_size = 1.3,
                label = "Ji's  Formalism with JD's Mathematica (WW)",
                color = 'green')
            
            plot_pure_interference_minus_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = convert_to_nb_over_GeV4(pure_interference_minus_beam_lp_target_ww),
                radial_size = 4.,
                label = "JD's BKM 10 Python (WW)",
                color = 'purple',
                marker = 'd',)
            
            plot_pure_interference_minus_beam_lp_target.add_scatter_plot(
                x_data = azimuthal_phi,
                y_data = jd_mathematica_pure_interference_minus_beam_lp_target_ww,
                radial_size = 1.3,
                label = "JD's BKM10 Mathematica (WW)",
                color = 'orange')
            
            plt.savefig(
                fname = f'compared_pure_interference_minus_beam_lp_target_kinematic_bin_{kinematic_bin_number}.png',
                dpi = 500)
            
            plt.close()

        # print("> Beginning analysis of DVCS, unpolarized beam, unpolarized target...")
        # analyze_dvcs_unpolarized_beam_unpolarized_target()

        # print("> Beginning analysis of DVCS, (+) polarized beam, unpolarized target...")
        # analyze_dvcs_plus_beam_unpolarized_target()

        # print("> Beginning analysis of DVCS, (-) polarized beam, unpolarized target...")
        # analyze_dvcs_minus_beam_unpolarized_target()

        # print("> Beginning analysis of DVCS, unpolarized beam, longitudinally-polarized target...")
        # analyze_dvcs_unpolarized_beam_polarized_target()

        # print("> Beginning analysis of DVCS, (+) polarized beam, longitudinally-polarized target...")
        # analyze_dvcs_plus_beam_polarized_target()

        # print("> Beginning analysis of DVCS, (-) polarized beam, longitudinally-polarized target...")
        # analyze_dvcs_minus_beam_polarized_target()
        
        # print("> Beginning analysis of Interference, unpolarized beam, unpolarized target...")
        # analyze_interference_unpolarized_beam_unpolarized_target()

        # print("> Beginning analysis of Interference, (+) beam, unpolarized target...")
        # analyze_interference_plus_beam_unpolarized_target()

        # print("> Beginning analysis of Interference, (-) beam, unpolarized target...")
        # analyze_interference_minus_beam_unpolarized_target()

        # print("> Beginning analysis of Interference, unpolarized beam, longitudinally-polarized target...")
        # analyze_interference_unpolarized_beam_polarized_target()

        print("> Beginning analysis of Interference, (+) beam, longitudinally-polarized target...")
        analyze_interference_plus_beam_polarized_target()

        # print("> Beginning analysis of Interference, (-) beam, longitudinally-polarized target...")
        # analyze_interference_minus_beam_polarized_target()

if __name__ == "__main__":
    

    try:
        analysis()

    except Exception as ERROR:
        print(f"> Error running the analysis script: {ERROR}")
        sys.exit(0)

# pure_bh_unpolarized_beam_unpolarized_target = (0.5 * (
# calculate_bh_amplitude_squared(0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
#     lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose) + 
# calculate_bh_amplitude_squared(
#     0.5, 0.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
#     lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose)))

# # jd_mathematica_pure_bh_unpolarized_beam_unpolarized_target = pd.read_csv('jd_interference_bh_beam_unpolarized_target_kinematic_bin_1.csv', names = ['jd_sigma'])
# # ji_mathematica_pure_bh_unpolarized_beam_unpolarized_target = pd.read_csv('ji_interference_bh_beam_unpolarized_target_kinematic_bin_1.csv', names = ['ji_sigma'])

# pure_bh_plus_beam_unpolarized_target = calculate_bh_amplitude_squared(
#     0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
#     lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose)

# # jd_mathematica_pure_bh_plus_beam_unpolarized_target = pd.read_csv('jd_bh_plus_beam_unpolarized_target_kinematic_bin_1.csv', names = ['jd_sigma'])
# # ji_mathematica_pure_bh_plus_beam_unpolarized_target = pd.read_csv('ji_bh_plus_beam_unpolarized_target_kinematic_bin_1.csv', names = ['ji_sigma'])

# pure_bh_minus_beam_unpolarized_target = calculate_bh_amplitude_squared(
#     0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
#     lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose)

# # jd_mathematica_pure_bh_minus_beam_unpolarized_target = pd.read_csv('jd_bh_minus_beam_unpolarized_target_kinematic_bin_1.csv', names = ['jd_sigma'])
# # ji_mathematica_pure_bh_minus_beam_unpolarized_target = pd.read_csv('ji_bh_minus_beam_unpolarized_target_kinematic_bin_1.csv', names = ['ji_sigma'])

# pure_bh_unpolarized_beam_lp_target = (0.5 * (
# calculate_bh_amplitude_squared(0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
#     lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose) + 
# calculate_bh_amplitude_squared(
#     0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
#     lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose)))

# # jd_mathematica_pure_bh_unpolarized_beam_lp_target = pd.read_csv('jd_bh_unpolarized_beam_lp_target_kinematic_bin_1.csv', names = ['jd_sigma'])
# # ji_mathematica_pure_bh_unpolarized_beam_lp_target = pd.read_csv('ji_bh_unpolarized_beam_lp_target_kinematic_bin_1.csv', names = ['ji_sigma'])

# pure_bh_plus_beam_unpolarized_target = calculate_bh_amplitude_squared(0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
#     lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose)

# # jd_mathematica_pure_bh_plus_beam_lp_target = pd.read_csv('jd_bh_plus_beam_lp_target_kinematic_bin_1.csv', names = ['jd_sigma'])
# # ji_mathematica_pure_bh_plus_beam_lp_target = pd.read_csv('ji_bh_plus_beam_lp_target_kinematic_bin_1.csv', names = ['ji_sigma'])

# pure_bh_minus_beam_lp_target = calculate_bh_amplitude_squared(
#     0.5, 1.0, squared_Q_momentum_transfer, x_Bjorken, squared_hadronic_momentum_transfer_t, azimuthal_phi, epsilon,
#     lepton_energy_fraction_y, shorthand_k, lepton_propagator_p1, lepton_propagator_p2, Dirac_form_factor_F1, Pauli_form_factor_F2, verbose)

# # jd_mathematica_pure_bh_minus_beam_lp_target = pd.read_csv('jd_bh_plus_minus_lp_target_kinematic_bin_1.csv', names = ['jd_sigma'])
# # ji_mathematica_pure_bh_minus_beam_lp_target = pd.read_csv('ji_bh_plus_minus_lp_target_kinematic_bin_1.csv', names = ['ji_sigma'])

# # We now calculate the pure DVCS squared term for the UNPOLARIZED target/UNPOLARIZED beam: