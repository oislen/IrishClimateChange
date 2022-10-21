# load relevant libraries
import os
import platform

root_dir = 'E:\\GitHub\\IrishClimateApp' if platform.system() == 'Windows' else '~'
# set directories
data_dir = os.path.join(root_dir, 'data')
census_2011_dir = os.path.join(data_dir, 'Census_2011')
census_2016_dir = os.path.join(data_dir, 'Census_2016')
met_eireann_dir = os.path.join(data_dir, 'Met_Eireann')
gis_dir = os.path.join(data_dir, "gis")
# set data files
master_data_fpath = os.path.join(data_dir, 'master.feather')
preaggregate_data_fpath = os.path.join(data_dir, "preaggregate_data.pickle")
bokeh_line_data_fpath = os.path.join(data_dir, "bokeh_line_data.pickle")
bokeh_map_data_fpath = os.path.join(data_dir, "bokeh_map_data.pickle")
rep_counties_fpath = os.path.join(data_dir, 'gis', 'arch', 'Counties_-_OSi_National_Statutory_Boundaries_-_2019', 'Counties___OSi_National_Statutory_Boundaries_.shp')
ni_counties_fpath = os.path.join(data_dir, 'gis', 'arch', 'northern_ireland_counties', 'northern_ireland_counties.shp')
counties_data_fpath = os.path.join(gis_dir, "counties.shp")
map_data_fpath = os.path.join(gis_dir, "map_data.pickle")

# met eireann weather data
met_eireann = {'dublin_airport':'https://cli.fusio.net/cli/climate_data/webdata/dly532.zip'}

# seaborn plot settings
sns_fig_settings = {'figure.figsize':(7, 7), "lines.linewidth": 0.7}

# set whether to load in pickle data for bokeh app or generate from master file
load_data_dict = True

# bokeh figure settings
FIG_SETTING = {'plot_height':640, 
               'plot_width':640, 
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
county_line_colors = {'donegal':'greenyellow', 'dublin':'blue', 
                      'clare':'yellow', 'cork':'red', 
                      'galway':'maroon', 
                      'kerry':'gold', 'kilkenny':'black', 
                      'limerick':'olivedrab', 
                      'mayo':'green', 
                      'sligo':'indianred', 
                      'tipperary':'royalblue',
                      'waterford':'whitesmoke', 'wexford':'purple'}

counties = list(county_line_colors.keys())
line_colors = list(county_line_colors.values())
date_strftime_dict = {'year':'%Y', 'year-month':'%Y-%m', 'month':'%m'}
line_agg_level_options = list(date_strftime_dict.keys())
line_agg_level_default = line_agg_level_options[0]
col_options = ['maxtp', 'mintp', 'gmin', 'soil', 'wdsp', 'sun', 'evap', 'rain']
col_default = col_options[0]
stat_options = ['mean', 'median', 'max', 'min', 'var', 'std', 'sum']
stat_default = stat_options[0]

# bokeh server execution commands
bat_execBokehApp = "START /MIN CMD.EXE /C exeBokehApp.bat"
sh_execBokehApp = "bash exeBokehApp.sh &"