import matplotlib.pyplot as plt

from utilities.plotting.plot_customizer import PlotCustomizer

def plot_cross_section(
        lab_azimuthal_phi,
        value_of_beam_energy,
        value_of_Q_squared,
        value_of_hadron_recoil,
        value_of_x_Bjorken,
        calculated_cross_section):
    
    # (1): Figure instance:
    figure = plt.figure(figsize = (18, 6))

    # (2): Add an Axes Object:
    axes_object = figure.add_subplot(111)

    # customized_plot = PlotCustomizer(
    #     axes_object,
    #     title = r"$E = {} \text{{GeV}}, Q^{{2}} = {} \text{{GeV}}^{{2}}, t = {} \text{{GeV}}^{{2}}, x_{{B}}= {}$".format(value_of_beam_energy, value_of_Q_squared, value_of_hadron_recoil, value_of_x_Bjorken),
    #     xlabel = r"$\phi \left[ \text{deg} \right]$",
    #     ylabel = r"$d^{{4}} \sigma_{\text{LP}} \left[ \text{nb} / \text{GeV}^{4} \right]$",
    #     grid = True)
    
    customized_plot = PlotCustomizer(
        axes_object,
        title = r"fuck",
        xlabel = r"z",
        ylabel = r"d",
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
