# load relevant libraries
from bokeh.io import curdoc
from bokeh.models import TabPanel, Tabs

# load custom modules
from BokehApp.bokeh_line_dash import bokeh_line_dash
from BokehApp.bokeh_map_dash import bokeh_map_dash

# initialise and structure bokeh line dashboard
dashboard_line = bokeh_line_dash()
panel_line_tab = TabPanel(child = dashboard_line, title = 'Time Series')

# initialise and structure bokeh map dashboard
dashboard_map = bokeh_map_dash()
panel_map_tab = TabPanel(child = dashboard_map, title = 'GIS Map')

# create combined dashboard
layout = Tabs(tabs=[panel_line_tab, panel_map_tab])

# deploy bokeh server and add dashboard layout
curdoc().add_root(layout)