# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 11:45:02 2022

@author: OisinLeonard
"""

# load relevant libraries
import cons
from bokeh.io import curdoc
from bokeh.models import Panel, Tabs
from bokeh.layouts import column, row

# load custom modules
from BokehApp.bokeh_map_dash import bokeh_map_dash

# initialise and structure bokeh map dashboard
dashboard_map = bokeh_map_dash(load_data_dict = cons.load_data_dict)
panel_map = Panel(child = dashboard_map, title = 'GIS Map')
tab_map = Tabs(tabs=[panel_map])

# deploy bokeh server and add dashboard layout
curdoc().add_root(tab_map)