# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 11:45:02 2022

@author: OisinLeonard
"""

# bokeh serve --show bokeh_app.py

# load relevant libraries
from bokeh.io import curdoc
from bokeh.models import ColorBar, Select, ColumnDataSource, HoverTool, LinearColorMapper, Panel, Tabs, Span
from bokeh.layouts import column, row
from bokeh.palettes import brewer
from bokeh.plotting import figure
import math
import cons
import pandas as pd

from utilities.time_data import time_data

#target_value = cons.default_select

# load input datasets
data = pd.read_feather(cons.master_data_fpath)
# generate time data aggregated by year
date_strftime_dict = {'year':'%Y', 'year-month':'%Y-%m', 'month':'%m'}
counties = ['dublin', 'wexford']
agg_dict = {'maxtp':'mean', 'mintp':'mean', 'wdsp':'mean', 'sun':'mean', 'evap':'mean', 'rain':'mean'}
year_strftime = date_strftime_dict['year']
time_span = ['2010', '2019']
year_data = time_data(data = data, agg_dict = agg_dict, time_span = time_span, counties = counties, strftime = year_strftime)
dublin_data = year_data.loc[year_data['county'] == 'dublin', :]
wexford_data = year_data.loc[year_data['county'] == 'wexford', :]
# create bokeh data source
dublin_datasource = ColumnDataSource(dublin_data)
wexford_datasource = ColumnDataSource(wexford_data)

#################
#-- Bar Chart --#
#################

plot = figure(title="Line Plot", toolbar_location='below', output_backend="webgl", **cons.FIG_SETTING)
dublin_line = plot.line(x='date', y='maxtp', source = dublin_datasource)
wexford_line = plot.line(x='date', y='maxtp', source = wexford_datasource)
#plot2.x_range.min_interval = 1
#plot2.x_range.max_interval = 47.5
#plot2.xgrid.grid_line_color = None
#plot2.title.text_font_style="bold"
#plot2.title.text_font_size="22px"
#plot2.xaxis.major_label_text_font_size = "11pt"
#plot2.yaxis.major_label_text_font_size = "11pt"
#plot2.xaxis.major_label_orientation = math.pi/4

# create hover tools
plot.add_tools(HoverTool(renderers=[dublin_line],
                      tooltips=[('Date', '@date'),
                                ('Max Temperature', '@maxtp')
                                ],
                      attachment='left')
            )

plot.add_tools(HoverTool(renderers=[wexford_line],
                      tooltips=[('Date', '@date'),
                                ('Max Temperature', '@maxtp')
                                ],
                      attachment='left')
            )

#####################
#-- App Structure --#
#####################

# define a blue color palette
#palette = brewer['Blues'][8]
# reverse order of colors so higher values have darker colors
#palette = palette[::-1]  
# instantiate LinearColorMapper that linearly maps numbers in a range, into a sequence of colors.
#color_mapper = LinearColorMapper(palette=palette)
# create color bar.
#color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=500, height=25, border_line_color=None, location=(0, 0), orientation='horizontal', major_label_text_font_size="18px")

#def callback(attr, old, new):
#    target_value = selector.value
#    df1_mod, df2_mod = utils.update_dataframes(legal_level = target_value, df1 = s_22mr22_nonmiss, df2 = ratenorms_latlng_gpd)
#    df2_mod = df2_mod.sort_values(by = ['target_col'], ascending = False).reset_index(drop = True)
#    nonmissgeosource.geojson = df1_mod.to_json()
#    pointsource.geojson = df2_mod.to_json()
#    plot2.x_range.factors = df2_mod['city'].to_list()
#    hline.location = df2_mod['target_col'].mean()
    
#options=list(cons.selector_map.keys())
selector = Select(title='Aggregate Level', value='year', options=['year', 'month'], width=300, height=60, aspect_ratio=10)
#selector.on_change('value', callback)  

# structure app layout
structure2 = column(plot)
panel2 = Panel(child = structure2, title = 'Comparison Bar Chart')

tab2 = Tabs(tabs=[panel2])
layout = column(row(tab2), selector)
curdoc().add_root(layout)