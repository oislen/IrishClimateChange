import cons
import seaborn as sns
import matplotlib.pyplot as plt

def time_plot(data, y, x = 'index', hue = None, strftime = None, refline = None, title = None, xlabel = None, ylabel = None):
    """"""
    # take deep copy of data
    tmp_data = data.copy()
    # set plot size and style
    sns.set(rc=cons.sns_fig_settings)
    sns.set_style("white")
    # initiate subplots
    fig, ax = plt.subplots()
    # create point plot
    line_chart = sns.pointplot(data = tmp_data, x = x, y = y, hue = hue, ax = ax,  palette = cons.county_line_colors)
    #point_chart.legend_.remove()
    # create line plot
    #line_chart = sns.lineplot(data = tmp_data, x = x, y = y, hue = hue, palette = cons.county_line_colors)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    # add horizontal reference line
    if refline != None:
        plt.axhline(y = refline, color = 'red', linestyle = '--')
    # set x axis ticks and labels
    axis_data_dict = tmp_data[['index', 'date_str']].drop_duplicates().sort_values(by = 'index').set_index('index').to_dict()['date_str']
    line_chart.set_xticks(list(axis_data_dict.keys()))
    line_chart.set_xticklabels(list(axis_data_dict.values()), rotation = 45)
    # add title and axis labels to plot
    if title != None:
        line_chart.set(title = title)
    if xlabel != None:
        line_chart.set(xlabel = xlabel)
    if ylabel != None:
        line_chart.set(ylabel = ylabel)
    # show and close plot
    plt.show()
    plt.close()
    return 0