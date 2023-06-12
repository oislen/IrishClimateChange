import cons
import matplotlib.pyplot as plt
import matplotlib.colors

def map_plot(map_data_dict, station_data, stat, col):
    """"""
    # create map of ireland
    map_data = map_data_dict[stat]
    fig, ax = plt.subplots(figsize=cons.sns_fig_settings['figure.figsize'])
    plt.axis('off')
    plt.title('Irish Climate App', size = 20)
    # plot counties of the island of Ireland
    map_data['geometry'].boundary.plot(ax = ax, color = 'grey', linewidth = 0.9, alpha=0.6)
    # create custom colour map
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["lightblue", "steelblue"])
    norm = plt.Normalize(map_data[col].min(),map_data[col].max())
    # plot heatmap of county climate 
    legend_kwds = {'label':col, 'orientation': "horizontal", 'fraction':0.046, 'pad':0.04}
    map_data.plot(column = col, ax = ax, cmap = cmap, legend = True, legend_kwds = legend_kwds, norm = norm)
    # overlay met eireann weather station locations
    station_data.plot(ax = ax, color = 'red', alpha=0.6)
    plt.show()
    return 0