import seaborn as sns
import matplotlib.pyplot as plt

def time_plot(data, y, x, hue = None, strftime = None, refline = None, title = None, xlabel = None, ylabel = None):
    """"""
    # take deep copy of data
    tmp_data = data.copy()
    # set plot size and style
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.set_style("white")
    # initiate subplots
    fig, ax = plt.subplots()
    # create line plot
    chart = sns.lineplot(x = x, y = y, hue = hue, data = tmp_data, ax = ax)
    # add horizontal reference line
    if refline != None:
        plt.axhline(y = refline, color = 'red', linestyle = '--')
    # set x axis ticks and labels
    chart.set_xticks(tmp_data[x])
    if strftime != None:
        tmp_data[x] = tmp_data[x].dt.strftime(strftime)
    chart.set_xticklabels(tmp_data[x], rotation = 45)
    # add title and axis labels to plot
    if title != None:
        chart.set(title = title)
    if xlabel != None:
        chart.set(xlabel = xlabel)
    if ylabel != None:
        chart.set(ylabel = ylabel)
    # show and close plot
    plt.show()
    plt.close()
    return 0