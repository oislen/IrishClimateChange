import cons
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from utilities.time_plot import time_plot

# load dublin airport weather data
dtypes = {'date':'str'}
parse_dates = ['date']
data = pd.read_csv(cons.dublin_airport_fpath, skiprows = 25, dtype = dtypes, parse_dates = parse_dates, na_values = [' '])

# aggregate by year month
agg_data = data.assign(year = data['date'].dt.strftime('%Y'))
group_cols = ['year']
agg_dict = {'maxtp':'mean', 'mintp':'mean', 'wdsp':'mean', 'sun':'mean', 'evap':'mean'}
agg_data = agg_data[agg_data['year'] != '2022'].groupby(group_cols, as_index = False).agg(agg_dict).reset_index()

# generate time plots
time_plot(agg_data, y = 'maxtp')
time_plot(agg_data, y = 'mintp')
time_plot(agg_data, y = 'wdsp')
time_plot(agg_data, y = 'sun')
time_plot(agg_data, y = 'evap')