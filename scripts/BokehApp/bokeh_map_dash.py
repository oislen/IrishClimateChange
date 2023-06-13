import pickle
from bokeh.models import Select, Div, CheckboxButtonGroup
from bokeh.layouts import column, row

import cons
from PreProcessData.gen_preaggregate_data import gen_preaggregate_data
from PreProcessData.gen_counties_data import gen_counties_data
from PreProcessData.gen_stations_data import gen_stations_data
from BokehApp.bokeh_map_data import bokeh_map_data
from BokehApp.bokeh_map_plot import bokeh_map_plot

def bokeh_map_dash(load_data_dict = True):
    """"""
    if load_data_dict:
        with open(cons.map_data_fpath, 'rb') as handle:
            map_data_dict = pickle.load(handle)
        with open(cons.points_data_fpath, 'rb') as handle:
            station_data = pickle.load(handle)
    else:
        pre_agg_data_dict = gen_preaggregate_data(return_data = True)
        map_data_dict = gen_counties_data(pre_agg_data_dict = pre_agg_data_dict, return_data = True)
        station_data = gen_stations_data(points_data_fpath = cons.points_data_fpath, return_data = True)
    # generate bokeh data for map plot
    bokeh_map_data_dict, pointgeosource = bokeh_map_data(map_data_dict, station_data)
    # create bokeh map plot
    map_plot = bokeh_map_plot(bokeh_map_data_dict = bokeh_map_data_dict, pointgeosource = pointgeosource, col = cons.col_default, stat = cons.stat_default, show_stations = cons.show_stations_default)

    # create call back function for bokeh dashboard interaction
    def callback_map_plot(attr, old, new):
        # extract new selector value
        col = map_col_selector.value
        stat = map_stat_selector.value
        show_stations = toggle_stations.active
        # update bokeh plot
        map_plot = bokeh_map_plot(bokeh_map_data_dict = bokeh_map_data_dict, pointgeosource = pointgeosource, col = col, stat = stat, show_stations = show_stations)
        # reassign bokeh plot to bokeh dashboard
        dashboard_map.children[1] = map_plot

    # set up selectors for bokeh map plot
    map_col_selector = Select(title='Column:', value=cons.col_default, options=cons.col_options, width=120, height=60, aspect_ratio=10)
    map_stat_selector = Select(title='Statistic:', value=cons.stat_default, options=cons.stat_options, width=120, height=60, aspect_ratio=10)
    toggle_stations = CheckboxButtonGroup(labels=['Toggle Stations'], active=[], width=30)
    map_col_selector.on_change('value', callback_map_plot)  
    map_stat_selector.on_change('value', callback_map_plot)
    toggle_stations.on_change('active', callback_map_plot)

    # structure dashboard map plot
    space_div = Div(width = 30, height = 30)
    widgets_map = column(map_col_selector, space_div, map_stat_selector, space_div, toggle_stations)
    dashboard_map = row(widgets_map, map_plot)

    return dashboard_map
