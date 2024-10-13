import pickle
from bokeh.models import Select, Div, CheckboxButtonGroup
from bokeh.layouts import column, row
from beartype import beartype

import cons
from utilities.bokeh_map_data import bokeh_map_data
from utilities.bokeh_map_plot import bokeh_map_plot

@beartype
def bokeh_map_dash():
    """Generates the bokeh map dashboard

    Parameters
    ----------

    Returns
    -------
    bokeh.layouts.row
        The interactive bokeh map dashboard
    """
    with open(cons.map_data_fpath, "rb") as handle:
        map_data_dict = pickle.load(handle)
    with open(cons.points_data_fpath, "rb") as handle:
        station_data = pickle.load(handle)
    # generate bokeh data for map plot
    bokeh_map_data_dict, pointgeosource = bokeh_map_data(map_data_dict, station_data)
    # create bokeh map plot
    map_plot = bokeh_map_plot(
        bokeh_map_data_dict=bokeh_map_data_dict,
        pointgeosource=pointgeosource,
        col=cons.col_default,
        stat=cons.stat_default,
        show_stations=cons.show_stations_default,
    )

    # create call back function for bokeh dashboard interaction
    def callback_map_plot(attr, old, new):
        # extract new selector value
        col = map_col_selector.value
        stat = map_stat_selector.value
        show_stations = toggle_stations.active
        # update bokeh plot
        map_plot = bokeh_map_plot(
            bokeh_map_data_dict=bokeh_map_data_dict,
            pointgeosource=pointgeosource,
            col=col,
            stat=stat,
            show_stations=show_stations,
        )
        # reassign bokeh plot to bokeh dashboard
        dashboard_map.children[1] = map_plot

    # set up selectors for bokeh map plot
    map_col_selector = Select(
        title="Climate Measure:",
        value=cons.col_default,
        options=cons.col_options,
        width=120,
        height=60,
        aspect_ratio=10,
    )
    map_stat_selector = Select(
        title="Aggregate:",
        value=cons.stat_default,
        options=cons.stat_options,
        width=120,
        height=60,
        aspect_ratio=10,
    )
    toggle_stations = CheckboxButtonGroup(
        labels=["Toggle Stations"], 
        active=[], 
        width=120,
        height=40
    )
    map_col_selector.on_change("value", callback_map_plot)
    map_stat_selector.on_change("value", callback_map_plot)
    toggle_stations.on_change("active", callback_map_plot)

    # structure dashboard map plot
    widgets_map = column(
        toggle_stations, map_col_selector, map_stat_selector
    )
    dashboard_map = row(widgets_map, map_plot)

    return dashboard_map
