import seaborn as sns
import matplotlib.pyplot as plt

def time_plot(data, y, x = 'index'):
    # plot line chart of average max temperature
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    chart = sns.lineplot(x = x, y = y, data = data)
    #chart.set(title = 'Mean Max Temperature', xlabel = 'Year', ylabel = 'Mean Max Temperature')
    # set x axis ticks and labels
    chart.set_xticks(data[x])
    chart.set_xticklabels(data['year'], rotation = 45, size = 5)
    plt.show()
    plt.close()
    return 0