import numpy as np
import matplotlib.pyplot as plt

from utilities.plotting.plot_customizer import PlotCustomizer

# Helper Modules | Convert Degrees to Radians
from utilities.mathematics.math_units import convert_degrees_to_radians

def plot_dvcs_contributions(
        lab_azimuthal_phi,
        c0DVCS_amplitude_contribution,
        c1DVCS_amplitude_contribution,
        s1DVCS_amplitude_contribution):

    # (1): Figure instance:
    figure = plt.figure(figsize = (18, 6))

    # (2): Add an Axes Object:
    DVCS_coefficient_contours = figure.add_subplot(121)
    DVCS_coefficient_bar_graph = figure.add_subplot(122)

    DVCS_coefficients_plot = PlotCustomizer(
            DVCS_coefficient_contours,
            title = "DVCS Coefficients",
            xlabel = r"$\phi$",
            ylabel = "nb/GeV4",
            grid = True)
    
    DVCS_coefficients_plot.add_line_plot(
            x_data = lab_azimuthal_phi,
            y_data = c0DVCS_amplitude_contribution,
            label = r"$c_{0}$",
            color = 'red')
        
    DVCS_coefficients_plot.add_line_plot(
        x_data = lab_azimuthal_phi,
        y_data = c1DVCS_amplitude_contribution * np.cos(np.pi - convert_degrees_to_radians(lab_azimuthal_phi)),
        label = r"$c_{1} \cos(\pi - \phi)$",
        color = 'orange')
    
    DVCS_coefficients_plot.add_line_plot(
        x_data = lab_azimuthal_phi,
        y_data = s1DVCS_amplitude_contribution * np.sin(np.pi - convert_degrees_to_radians(lab_azimuthal_phi)),
        label = r"$s_{1} \sin(\pi - \phi)$",
        color = 'yellow')
    
    DVCS_coefficients_contributions = PlotCustomizer(
            DVCS_coefficient_bar_graph,
            title = "DVCS Coefficients",
            xlabel = "Fourier Coefficients",
            ylabel = r"$\mathrm{nb} / \mathrm{GeV}^{4}",
            grid = True)
    
    DVCS_coefficients_contributions.add_bar_plot(
        x_positions = [r'$c_{0}$',r'$c_{1}$',r'$s_{1}$'],
        y_data_heights = np.array([c0DVCS_amplitude_contribution[0], c1DVCS_amplitude_contribution[0], s1DVCS_amplitude_contribution[0]])
    )
    
    plt.savefig('dvcs_coefficient_contributions_v1.png')

def plot_interference_contributions(
        lab_azimuthal_phi,
        c0Interference_amplitude_contribution,
        c1Interference_amplitude_contribution,
        c2Interference_amplitude_contribution,
        c3Interference_amplitude_contribution,
        s1Interference_amplitude_contribution,
        s2Interference_amplitude_contribution,
        s3Interference_amplitude_contribution):
    
    
    # (1): Figure instance:
    figure = plt.figure(figsize = (18, 6))

    # (2): Add an Axes Object:
    interference_coefficient_contours = figure.add_subplot(121)
    interference_coefficient_bar_graph = figure.add_subplot(122)

    interference_coefficients_plot = PlotCustomizer(
            interference_coefficient_contours,
            title = "Interference Coefficients",
            xlabel = r"$\phi$",
            ylabel = "nb/GeV4",
            grid = True)
    
    interference_coefficients_plot.add_line_plot(
            x_data = lab_azimuthal_phi,
            y_data = c0Interference_amplitude_contribution ,
            label = r"$c_{0}$",
            color = 'red')
        
    interference_coefficients_plot.add_line_plot(
        x_data = lab_azimuthal_phi,
        y_data = c1Interference_amplitude_contribution * np.cos(np.pi - convert_degrees_to_radians(lab_azimuthal_phi)),
        label = r"$c_{1} \cos(\pi - \phi)$",
        color = 'orange')
    
    interference_coefficients_plot.add_line_plot(
            x_data = lab_azimuthal_phi,
            y_data = c2Interference_amplitude_contribution * np.cos(2. * (np.pi - convert_degrees_to_radians(lab_azimuthal_phi))),
            label = r"$c_{2} \cos(\pi - \phi)$",
            color = 'yellow')
        
    interference_coefficients_plot.add_line_plot(
        x_data = lab_azimuthal_phi,
        y_data = c3Interference_amplitude_contribution * np.cos(3. * (np.pi - convert_degrees_to_radians(lab_azimuthal_phi))),
        label = r"$c_{3} \cos(\pi - \phi)$",
        color = 'green')
    
    interference_coefficients_plot.add_line_plot(
        x_data = lab_azimuthal_phi,
        y_data = s1Interference_amplitude_contribution * np.sin(np.pi - convert_degrees_to_radians(lab_azimuthal_phi)),
        label = r"$s_{1} \sin(\pi - \phi)$",
        color = 'cyan')
    
    interference_coefficients_plot.add_line_plot(
        x_data = lab_azimuthal_phi,
        y_data = s2Interference_amplitude_contribution * np.sin(2. * (np.pi - convert_degrees_to_radians(lab_azimuthal_phi))),
        label = r"$s_{2} \sin(\pi - \phi)$",
        color = 'blue')
        
    interference_coefficients_plot.add_line_plot(
        x_data = lab_azimuthal_phi,
        y_data = s3Interference_amplitude_contribution * np.sin(3. * (np.pi - convert_degrees_to_radians(lab_azimuthal_phi))),
        label = r"$s_{3} \sin(\pi - \phi)$",
        color = 'purple')
    
    DVCS_coefficients_contributions = PlotCustomizer(
            interference_coefficient_bar_graph,
            title = "Interference Coefficients",
            xlabel = "Fourier Coefficients",
            ylabel = r"$\mathrm{nb} / \mathrm{GeV}^{4}",
            grid = True)
    
    DVCS_coefficients_contributions.add_bar_plot(
        x_positions = [r'$c_{0}$', r'$c_{1}$', r'$c_{2}$', r'$c_{3}$', r'$s_{1}$', r'$s_{2}$', r'$s_{3}$'],
        y_data_heights = np.array([
            c0Interference_amplitude_contribution[0],
            c1Interference_amplitude_contribution[0],
            c2Interference_amplitude_contribution[0],
            c3Interference_amplitude_contribution[0],
            s1Interference_amplitude_contribution[0],
            s2Interference_amplitude_contribution[0],
            s3Interference_amplitude_contribution[0]
            ])
    )
    
    plt.savefig('interference_coefficient_contributions_v1.png')



def plot_cross_section(
        lab_azimuthal_phi,
        value_of_beam_energy,
        value_of_Q_squared,
        value_of_hadron_recoil,
        value_of_x_Bjorken,
        calculated_cross_section):
    """
    # Title: `plot_cross_section`

    ## Description:
    We plot the four-fold cross section using this method. It uses the custom-
    built `PlotCustomizer` class that allows us to easily configure things 
    about the plot. 

    Parameters
    --------------

    Function Flow
    --------------

    Notes
    --------------

    """
    
    # (1): Figure instance:
    figure = plt.figure(figsize = (18, 6))

    # (2): Add an Axes Object:
    axes_object = figure.add_subplot(111)

    customized_plot = PlotCustomizer(
        axes_object,
        title = r"$E = {} \mathrm{GeV}, Q^{{2}} = {} \mathrm{GeV}^{{2}}, t = {} \mathrm{GeV}^{{2}}, x_{\mathrm{B}}= {}$".format(value_of_beam_energy, value_of_Q_squared, value_of_hadron_recoil, value_of_x_Bjorken),
        xlabel = r"$\phi \left[ \mathrm{deg} \right]$",
        ylabel = r"$d^{4} \sigma_{\mathrm{LP}} \left[ \mathrm{nb} / \mathrm{GeV}^{4} \right]$",
        grid = True)
    
    customized_plot.add_scatter_plot(
        x_data = lab_azimuthal_phi,
        y_data = calculated_cross_section,
        color = 'blue')
    
    plt.savefig('cross_section_v1.png')

    return customized_plot

def plot_coefficient_contributions():

    # (1): Figure instance:
    figure = plt.figure(figsize = (18, 6))

    # (2): Add an Axes Object:
    axes_object = figure.add_subplot(111)

    customized_plot = PlotCustomizer(
        axes_object,
        title = r"Coefficient Contributions",
        xlabel = r"Fuck",
        ylabel = r"Coefficient Value",
        grid = True)
    
    customized_plot.add_bar_plot(
        x_data = 0.,
        y_data_heights = 0.,
        color = 'blue')
    
    plt.show()

    # return customized_plot

def plot_beam_spin_asymmetry(
        lab_azimuthal_phi,
        value_of_beam_energy,
        value_of_Q_squared,
        value_of_hadron_recoil,
        value_of_x_Bjorken,
        bsa_data):
    
    # (1): Figure instance:
    figure = plt.figure(figsize = (18, 6))

    # (2): Add an Axes Object:
    axes_object = figure.add_subplot(111)

    customized_plot = PlotCustomizer(
        axes_object,
        title = r"$E = {} \text{{GeV}}, Q^{{2}} = {} \text{{GeV}}^{{2}}, t = {} \text{{GeV}}^{{2}}, x_{{B}}= {}$".format(value_of_beam_energy, value_of_Q_squared, value_of_hadron_recoil, value_of_x_Bjorken),
        xlabel = r"$\phi \left[ \text{deg} \right]$",
        ylabel = r"BSA",
        grid = True)
    
    customized_plot.add_scatter_plot(
        x_data = lab_azimuthal_phi,
        y_data = bsa_data,
        color = 'blue')
    
    plt.show()

    return customized_plot
