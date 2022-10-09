import cons
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from utilities.time_plot import time_plot

# load dublin airport weather data
dtypes = {'date':'str'}
data = pd.DataFrame()
for fpath in cons.met_eireann_fpaths:
    print(fpath)
    tmp_data = pd.read_excel(fpath, dtype = dtypes, na_values = [' '])
    data = pd.concat(objs = [data, tmp_data], ignore_index = True, axis = 0)
data['date'] = pd.to_datetime(data['date'])

# aggregate by year month
agg_data = data.assign(year = data['date'].dt.year)
group_cols = ['county', 'year']
agg_dict = {'maxtp':'mean', 'mintp':'mean', 'wdsp':'mean', 'sun':'mean', 'evap':'mean'}
agg_data = agg_data[agg_data['year'] != '2022'].groupby(group_cols, as_index = False).agg(agg_dict).reset_index()
#agg_data.pivot(index = ['county', 'year'], columns = ['maxtp', 'mintp', 'wdsp', 'sun', 'evap'])

# generate time plots
time_plot(agg_data, x = 'year', y = 'maxtp', hue = 'county', time_span = [2010, 2021], counties = ['dublin', 'wexford'])
time_plot(agg_data, x = 'year', y = 'mintp', hue = 'county', time_span = [2010, 2021], counties = ['dublin', 'wexford'])
time_plot(agg_data, x = 'year', y = 'wdsp', hue = 'county', time_span = [2010, 2021], counties = ['dublin', 'wexford'])
time_plot(agg_data, x = 'year', y = 'sun', hue = 'county', time_span = [2010, 2021], counties = ['dublin', 'wexford'])
time_plot(agg_data, x = 'year', y = 'evap', hue = 'county', time_span = [2010, 2021], counties = ['dublin', 'wexford'])