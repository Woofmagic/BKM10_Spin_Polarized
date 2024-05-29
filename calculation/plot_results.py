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
    axes_object = figure.add_subplot(131)

    customized_plot = PlotCustomizer(
        axes_object,
        title = r"$d^{{4}}\sigma \quad \text{{at}} \quad E = {} \text{{GeV}}, Q^{{2}} = {} \text{{GeV}}^{{2}}, t = {} \text{{GeV}}^{{2}}, x_{{B}}= {}$".format(value_of_beam_energy, value_of_Q_squared, value_of_hadron_recoil, value_of_x_Bjorken),
        xlabel = r"$\phi \left[ \text{deg} \right]$",
        ylabel = r"$d^{{4}} \sigma \left[ \text{nb} / \text{GeV}^{4} \right]$",
        grid = True)
    
    customized_plot.add_scatter_plot(
        x_data = lab_azimuthal_phi,
        y_data = calculated_cross_section,
        color = 'blue')
    
    plt.show()

    return customized_plot