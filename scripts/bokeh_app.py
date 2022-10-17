# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 11:45:02 2022

@author: OisinLeonard
"""

# load relevant libraries
from bokeh.io import curdoc
from bokeh.models import Select, CheckboxGroup, Panel, Tabs, Div
from bokeh.layouts import column, row

# import custom modules
import cons
from utilities.bokeh_map_data import bokeh_map_data
from utilities.bokeh_map_plot import bokeh_map_plot
from utilities.bokeh_line_data import bokeh_line_data
from utilities.bokeh_line_plot import bokeh_line_plot

#################
##-- Map Plot --#
#################

# generate bokeh data for map plot
bokeh_map_data_dict = bokeh_map_data()
# create bokeh map plot
map_plot = bokeh_map_plot(bokeh_map_data_dict, col = cons.col_default, stat = cons.stat_default)

# create call back function for bokeh dashboard interaction
def callback_map_plot(attr, old, new):
    # extract new selector value
    col = map_col_selector.value
    stat = map_stat_selector.value
    # update bokeh plot
    map_plot = bokeh_map_plot(bokeh_map_data_dict = bokeh_map_data_dict, col = col, stat = stat)
    # reassign bokeh plot to bokeh dashboard
    dashboard_map.children[0] = map_plot

# set up selectors for bokeh map plot
map_col_selector = Select(title='Column:', value=cons.col_default, options=cons.col_options, width=120, height=60, aspect_ratio=10)
map_stat_selector = Select(title='Statistic:', value=cons.stat_default, options=cons.stat_options, width=120, height=60, aspect_ratio=10)
map_col_selector.on_change('value', callback_map_plot)  
map_stat_selector.on_change('value', callback_map_plot) 

###################
##-- Line Plot --##
###################

# generate bokeh data for line plot
bokeh_line_data_dict = bokeh_line_data()
# create bokeh plot
line_plot = bokeh_line_plot(bokeh_line_data_dict, col = cons.col_default, stat = cons.stat_default, agg_level = cons.line_agg_level_default, selection = cons.counties)

# create call back function for bokeh dashboard interaction
def callback_line_plot(attr, old, new):
    # extract new selector value
    agg_level = line_agg_level_selector.value
    col = line_col_selector.value
    stat = line_stat_selector.value

    selection = list()
    for i in line_county_checkboxgroup.active:
        selection.append(cons.counties[i])
    
    # update bokeh plot
    line_plot = bokeh_line_plot(bokeh_line_data_dict, col = col, stat = stat, agg_level = agg_level, selection = selection)
    # reassign bokeh plot to bokeh dashboard
    dashboard_line.children[0] = line_plot

# set up selectors for bokeh line plot
line_agg_level_selector = Select(title='Aggregate Level:', value=cons.line_agg_level_default, options=cons.line_agg_level_options, width=120, height=60, aspect_ratio=10)
line_col_selector = Select(title='Column:', value=cons.col_default, options=cons.col_options, width=120, height=60, aspect_ratio=10)
line_stat_selector = Select(title='Statistic:', value=cons.stat_default, options=cons.stat_options, width=120, height=60, aspect_ratio=10)
line_county_checkboxgroup = CheckboxGroup(labels=cons.counties, active = list(range(len(cons.counties))))
line_agg_level_selector.on_change('value', callback_line_plot)  
line_col_selector.on_change('value', callback_line_plot)  
line_stat_selector.on_change('value', callback_line_plot)
line_county_checkboxgroup.on_change('active', callback_line_plot)

############################
##-- Dashboard Structure --#
############################

# structure dashboard map plot
space_div = Div(width = 30, height = 30)
widgets_map = column(map_col_selector, space_div, map_stat_selector)
dashboard_map = row(map_plot, widgets_map)
panel_map = Panel(child = dashboard_map, title = 'GIS Map')
tab_map = Tabs(tabs=[panel_map])
# structure dashboard line plot
widgets_line = column(line_agg_level_selector, space_div, line_col_selector, space_div, line_stat_selector, space_div, line_county_checkboxgroup)
dashboard_line = row(line_plot, widgets_line)
panel_line = Panel(child = dashboard_line, title = 'Time Series')
tab_line = Tabs(tabs=[panel_line])
# combine map and line dashboards
layout = column(row(tab_map, tab_line))
curdoc().add_root(layout)