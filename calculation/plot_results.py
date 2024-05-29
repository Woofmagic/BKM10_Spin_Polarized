import matplotlib.pyplot as plt

from utilities.plotting.plot_customizer import PlotCustomizer

def plot_cross_section(lab_azimuthal_phi, calculated_cross_section):
    
    # (1): Figure instance:
    figure = plt.figure(figsize = (18, 6))

    # (2): Add an Axes Object:
    axes_object = figure.add_subplot(131)

    # (3): Obtain the data:
    values_of_x_B = jlab_pandas_df['x_b']
    values_of_Q_squared = jlab_pandas_df['QQ']
    values_of_t = jlab_pandas_df['t']
    
    customized_plot = PlotCustomizer(
        axes_object,
        title = r"Kinematic Phase Space for JLab Data",
        xlabel = r"$\phi [\text{deg}]$",
        ylabel = r"$d^{4} \sigma [\text{nb}/\text{GeV}^{{4}}]$",
        grid = True)
    
    customized_plot.add_scatter_plot(
        x_data = lab_azimuthal_phi,
        y_data = calculated_cross_section,
        color = 'blue')