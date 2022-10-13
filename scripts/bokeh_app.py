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

# import custom modules
import cons
from utilities.bokeh_data import bokeh_data
from utilities.bokeh_plot import bokeh_plot

# load input datasets
data = pd.read_feather(cons.master_data_fpath)

# generate bokeh data for plot
bokeh_data_dict = bokeh_data(data = data, option = cons.agg_level_default)

# create bokeh plot
plot = bokeh_plot(bokeh_data_dict)

# create call back function for bokeh dashboard interaction
def callback(attr, old, new):
    # extract new selector value
    target_value = agg_level_selector.value
    # update bokeh data
    bokeh_data_dict = bokeh_data(data, option = target_value)
    # update bokeh plot
    update_plot = bokeh_plot(bokeh_data_dict)
    # reassign bokeh plot to bokeh dashboard
    dashboard.children[0] = update_plot

# set up selectors for bokeh dashboard
agg_level_selector = Select(title='Aggregate Level', value='year', options=cons.agg_level_options, width=300, height=60, aspect_ratio=10)
agg_level_selector.on_change('value', callback)  

# structure dashboard layout
dashboard = column(plot)
panel = Panel(child = dashboard, title = 'Irish Climate Change')
tab = Tabs(tabs=[panel])
layout = column(row(tab), agg_level_selector)
curdoc().add_root(layout)