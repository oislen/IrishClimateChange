# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 11:45:02 2022

@author: OisinLeonard
"""

# bokeh serve --show bokeh_app.py

# load relevant libraries
from bokeh.io import curdoc
from bokeh.models import Select, Panel, Tabs
from bokeh.layouts import column, row
import pandas as pd
import geopandas as gpd

# import custom modules
import cons
from utilities.bokeh_map_data import bokeh_map_data
from utilities.bokeh_map_plot import bokeh_map_plot
from utilities.bokeh_line_data import bokeh_line_data
from utilities.bokeh_line_plot import bokeh_line_plot

# load input datasets
data = pd.read_feather(cons.master_data_fpath)
counties = gpd.read_file(cons.counties_data_fpath)

# generate bokeh data for map plot
bokeh_map_data_dict = bokeh_map_data(data, counties)
# create bokeh map plot
map_plot = bokeh_map_plot(bokeh_map_data_dict)

# generate bokeh data for line plot
bokeh_line_data_dict = bokeh_line_data(data = data, agg_level = cons.line_agg_level_default, stat = cons.line_stat_default)
# create bokeh plot
line_plot = bokeh_line_plot(bokeh_line_data_dict, col = cons.line_col_default, stat = cons.line_stat_default)

# create call back function for bokeh dashboard interaction
def callback_line_plot(attr, old, new):
    # extract new selector value
    agg_level = line_agg_level_selector.value
    col = line_col_selector.value
    stat = line_stat_selector.value
    # update bokeh data
    bokeh_line_data_dict = bokeh_line_data(data = data, agg_level = agg_level, stat = stat)
    # update bokeh plot
    line_plot = bokeh_line_plot(bokeh_line_data_dict, col = col, stat = stat)
    # reassign bokeh plot to bokeh dashboard
    dashboard_line.children[0] = line_plot

# set up selectors for bokeh dashboard
line_agg_level_selector = Select(title='Aggregate Level:', value=cons.line_agg_level_default, options=cons.line_agg_level_options, width=120, height=60, aspect_ratio=10)
line_col_selector = Select(title='Column:', value=cons.line_col_default, options=cons.line_col_options, width=120, height=60, aspect_ratio=10)
line_stat_selector = Select(title='Statistic:', value=cons.line_stat_default, options=cons.line_stat_options, width=120, height=60, aspect_ratio=10)
line_agg_level_selector.on_change('value', callback_line_plot)  
line_col_selector.on_change('value', callback_line_plot)  
line_stat_selector.on_change('value', callback_line_plot)  

# structure dashboard map plot
dashboard_map = column(map_plot)
panel_map = Panel(child = dashboard_map, title = 'GIS Map')
tab_map = Tabs(tabs=[panel_map])
# structure dashboard line plot
dashboard_line = column(line_plot, row(line_agg_level_selector, line_col_selector, line_stat_selector))
panel_line = Panel(child = dashboard_line, title = 'Time Series')
tab_line = Tabs(tabs=[panel_line])
# combine map and line dashboards
layout = column(row(tab_map, tab_line))
curdoc().add_root(layout)