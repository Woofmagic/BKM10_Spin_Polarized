import matplotlib.pyplot as plt

def plot_cross_section():
    
    # (1): Figure instance:
    figure = plt.figure(figsize = (18, 6))

    # (2): Add an Axes Object:
    axes_1 = figure.add_subplot(131)
    axes_2 = figure.add_subplot(132)
    axes_3 = figure.add_subplot(133, projection = '3d')

    # (3): Obtain the data:
    values_of_x_B = jlab_pandas_df['x_b']
    values_of_Q_squared = jlab_pandas_df['QQ']
    values_of_t = jlab_pandas_df['t']
    
    customized_plot = PlotCustomizer(
        axes_3,
        title = r"Kinematic Phase Space for JLab Data",
        xlabel = r"$x_{B}$",
        ylabel = r"$Q^{2}$",
        zlabel = r"$t$",
        grid = True)