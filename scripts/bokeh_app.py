# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 11:45:02 2022

@author: OisinLeonard
"""

# load relevant libraries
from bokeh.io import curdoc
from bokeh.models import Panel, Tabs
from bokeh.layouts import column, row

# load custom modules
from BokehApp.bokeh_map_dash import bokeh_map_dash
from BokehApp.bokeh_line_dash import bokeh_line_dash

# initialise and structure bokeh map dashboard
dashboard_map = bokeh_map_dash()
panel_map = Panel(child = dashboard_map, title = 'GIS Map')
tab_map = Tabs(tabs=[panel_map])

# initialise and structure bokeh line dashboard
dashboard_line = bokeh_line_dash()
panel_line = Panel(child = dashboard_line, title = 'Time Series')
tab_line = Tabs(tabs=[panel_line])

# combine map and line dashboards
layout = column(row(tab_map, tab_line))

# deploy bokeh server and add dashboard layout
curdoc().add_root(layout)