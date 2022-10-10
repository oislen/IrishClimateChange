import seaborn as sns
import matplotlib.pyplot as plt

def time_plot(data, y, x, hue = None, strftime = None):
    """"""
    tmp_data = data.copy()
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    fig, ax = plt.subplots()
    chart = sns.lineplot(x = x, y = y, hue = hue, data = tmp_data, ax = ax)
    # set x axis ticks and labels
    chart.set_xticks(tmp_data[x])
    if strftime != None:
        tmp_data[x] = tmp_data[x].dt.strftime(strftime)
    chart.set_xticklabels(tmp_data[x], rotation = 45)
    plt.show()
    plt.close()
    return 0