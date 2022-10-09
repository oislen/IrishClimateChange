import seaborn as sns
import matplotlib.pyplot as plt

def time_plot(data, y, x, hue = None, time_span = None, counties = None):
    # if filtering date with respect to timespan
    if time_span != None:
        data = data.loc[(data[x] >= min(time_span)) & (data[x] <= max(time_span)), :]
    # if filtering data with respect to countues
    if counties != None:
        data = data.loc[data[hue].isin(counties)]
    # plot line chart of average max temperature
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    chart = sns.lineplot(x = x, y = y, hue = hue, data = data)
    #chart.set(title = 'Mean Max Temperature', xlabel = 'Year', ylabel = 'Mean Max Temperature')
    # set x axis ticks and labels
    chart.set_xticks(data[x])
    chart.set_xticklabels(data['year'], rotation = 45, size = 5)
    plt.show()
    plt.close()
    return 0