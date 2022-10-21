# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 11:45:02 2022

@author: OisinLeonard
"""

# load relevant libraries
from bokeh.io import curdoc
from bokeh.models import Panel, Tabs

# load custom modules
from BokehApp.bokeh_line_dash import bokeh_line_dash

# initialise and structure bokeh line dashboard
dashboard_line = bokeh_line_dash(load_data_dict = True)
panel_line = Panel(child = dashboard_line, title = 'Time Series')
layout = Tabs(tabs=[panel_line])

# deploy bokeh server and add dashboard layout
curdoc().add_root(layout)