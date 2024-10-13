# load relevant libraries
import os
import sys
import platform
from datetime import datetime

root_dir = 'E:\\GitHub\\IrishClimateDashboard' if platform.system() == 'Windows' else '/home/ubuntu/IrishClimateDashboard'
sys.path.append(root_dir)
# set directories
data_dir = os.path.join(root_dir, 'data')
# set data files
master_data_fpath = os.path.join(data_dir, 'master.feather')
gis_dir = os.path.join(data_dir, "gis")
preaggregate_data_fpath = os.path.join(data_dir, "preaggregate_data.pickle")
bokeh_line_data_fpath = os.path.join(data_dir, "bokeh_line_data.pickle")
bokeh_map_data_fpath = os.path.join(data_dir, "bokeh_map_data.pickle")
map_data_fpath = os.path.join(gis_dir, "map_data.pickle")
points_data_fpath = os.path.join(gis_dir, "points_data.pickle")

# seaborn plot settings
sns_fig_settings = {'figure.figsize':(7, 7), "lines.linewidth": 0.7}

# set whether to load in pickle data for bokeh app or generate from master file
load_data_dict = True

# bokeh figure settings
FIG_SETTING = {'height':640, 
               'width':640, 
               'min_border_left':40, 
               'min_border_right':40,
               'min_border_top':40, 
               'min_border_bottom': 16, 
               'tools':'pan,wheel_zoom, box_zoom,reset,save'
               }

# bokeh map settings
MAP_SETTINGS = {'line_color':'gray', 
                'line_width':0.25, 
                'fill_alpha':1
                }

# bokeh line selector settings
county_line_colors = {'Donegal':'greenyellow', 'Dublin':'lightblue', 
                      'Carlow':'sandybrown', 'Cavan':'dodgerblue', 'Clare':'yellow', 'Cork':'red', 
                      'Galway':'maroon', 
                      'Kerry':'gold', 'Kildare':'lavender', 'Kilkenny':'black', 
                      'Laois':'fuchsia', 'Leitrim':'khaki', 'Limerick':'olivedrab', 'Longford':'blueviolet',
                      'Mayo':'green',  'Meath':'lawngreen', 'Monaghan':'slateblue',
                      'Offaly':'lightgreen',
                      'Roscommon':'cornsilk',
                      'Sligo':'indianred', 
                      'Tipperary':'royalblue',
                      'Waterford':'whitesmoke', 'Westmeath':'darkred', 'Wexford':'purple', 'Wicklow':'darkblue'
                      }

counties = list(county_line_colors.keys())
line_colors = list(county_line_colors.values())
counties_values = [str(i) for i in range(len(counties))]
counties_options = [(str(i), c) for i, c in enumerate(counties)]
date_strftime_dict = {'year':'%Y', 'year-month':'%Y-%m', 'month':'%m'}
line_agg_level_options = list(date_strftime_dict.keys())
line_agg_level_default = line_agg_level_options[0]
col_options = ['maxtp', 'mintp', 'gmin', 'soil', 'wdsp', 'sun', 'evap', 'rain', 'glorad']
col_default = col_options[0]
stat_options = ['mean', 'median', 'max', 'min', 'var', 'std', 'sum']
stat_default = stat_options[0]
show_stations_default = []
linedash_yearend = str(int(datetime.now().strftime('%Y')) - 1)
linedash_year_timespan = ["2010", linedash_yearend]
linedash_yearmonth_timespan = ["2010-01", f"{linedash_yearend}-12"]
linedash_month_timespan = ["01", "12"]

# bokeh server execution commands
bat_execBokehApp = "START /MIN CMD.EXE /C exeBokehApp.bat"
sh_execBokehApp = "bash exeBokehApp.sh &"

# unittest constants
unittest_n_dates = 3
unittest_country_station_map ={'dublin':['dublin airport', 'casement'], 'cork':['ucc']}
unittest_start_date = '2020-01-01'
unittest_normal_dists = {
    "maxtp":{"loc":13, "scale":4.9},
    "mintp":{"loc":6.1, "scale":4.3},
    "igmin":{"loc":0.2, "scale":0.4},
    "gmin":{"loc":.4, "scale":5.2},
    "rain":{"loc":2.0, "scale":4.4},
    "wdsp":{"loc":9.9, "scale":4},
    "hm":{"loc":17, "scale":6},
    "ddhm":{"loc":206, "scale":85},
    "hg":{"loc":25, "scale":8.8},
    "sun":{"loc":4.1, "scale":3.8},
    "dos":{"loc":0.3, "scale":18},
    "glorad":{"loc":1062, "scale":741},
    "soil":{"loc":11.2, "scale":5.3},
    "pe":{"loc":1.6, "scale":1.0},
    "evap":{"loc":2.3, "scale":1.4},
    "smd_wd":{"loc":20.5, "scale":22.5},
    "smd_md":{"loc":19.9, "scale":23.1},
    "smd_pd":{"loc":18.2, "scale":27.3}
}
