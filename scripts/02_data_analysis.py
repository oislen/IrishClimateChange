import cons
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from utilities.gen_master_data import gen_master_data
from utilities.time_data import time_data
from utilities.time_plot import time_plot

gen_master_data(cons.met_eireann_fpaths, cons.master_data_fpath)

### Proto-type Bokeh App Plot Design using Seaborn

# load master data
data = pd.read_feather(cons.master_data_fpath)

# aggregate by year month
date_strftime_dict = {'year':'%Y', 'year-month':'%Y-%m', 'month':'%m'}
date_strftime = date_strftime_dict['year']
time_span = ['2010', '2020']
counties = ['dublin', 'wexford']
agg_dict = {'maxtp':'mean', 'mintp':'mean', 'wdsp':'mean', 'sun':'mean', 'evap':'mean', 'rain':'mean'}
# generate time data
agg_data = time_data(data = data, agg_dict = agg_dict, time_span = time_span, counties = counties, strftime = date_strftime)

# generate time plots
time_plot(agg_data, x = 'date', y = 'maxtp', hue = 'county', strftime = date_strftime)
time_plot(agg_data, x = 'date', y = 'mintp', hue = 'county', strftime = date_strftime)
time_plot(agg_data, x = 'date', y = 'wdsp', hue = 'county', strftime = date_strftime)
time_plot(agg_data, x = 'date', y = 'sun', hue = 'county', strftime = date_strftime)
time_plot(agg_data, x = 'date', y = 'evap', hue = 'county', strftime = date_strftime)
time_plot(agg_data, x = 'date', y = 'rain', hue = 'county', strftime = date_strftime)