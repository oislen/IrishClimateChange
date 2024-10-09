import cons
from colour import Color
from bokeh.models import LinearColorMapper, ColorBar, HoverTool
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource
from beartype import beartype

@beartype
def bokeh_map_plot(
    bokeh_map_data_dict:dict, 
    pointgeosource:GeoJSONDataSource, 
    col:str, 
    stat:str, 
    show_stations:list
    ) -> figure:
    """Generates the data used in the bokeh map plot.

    Parameters
    ----------
    bokeh_map_data_dict : dict
        A dictionary of bokeh aggregated data objects to construct the interactive bokeh heatmap with
    pointgeosource : geopandas.DataFrame
        The geospatial Met Eireann station data to overlay was red dots in the interactive bokeh heatmap
    col : str
        The climate measure category to plot in the interactive bokeh heatmap
    stat : str
        The aggregated statistic to plot in the interactive bokeh heatmap
    show_stations : list
        Whether to toggle the Met Eireann station data overlay in the interactive bokeh heatmap

    Returns
    -------
    bokeh.plotting.figure
        The interactive bokeh heat map
    """
    # define a blue color palette
    lightblue = Color("lightblue")
    steelblue = Color("steelblue")
    palette = tuple([col.get_hex() for col in lightblue.range_to(steelblue, 100)])
    # palette = ("lightblue", "steelblue")
    # instantiate LinearColorMapper that linearly maps numbers in a range, into a sequence of colors.
    nonmiss_map_data = bokeh_map_data_dict[stat]["nonmiss_map_data"]
    color_mapper = LinearColorMapper(
        palette=palette,
        low=nonmiss_map_data[col].min(),
        high=nonmiss_map_data[col].max(),
    )
    # create color bar.
    color_bar = ColorBar(
        color_mapper=color_mapper,
        label_standoff=8,
        width=500,
        height=25,
        border_line_color=None,
        location=(0, 0),
        orientation="horizontal",
        major_label_text_font_size="18px",
    )
    # create underlying figure object
    map_plot = figure(
        toolbar_location="below", output_backend="webgl", **cons.FIG_SETTING
    )
    map_plot.axis.visible = False
    map_plot.xgrid.grid_line_color = None
    map_plot.ygrid.grid_line_color = None
    #map_plot.x_range.min_interval = 1
    #map_plot.y_range.min_interval = 1
    #map_plot.x_range.max_interval = 70
    #map_plot.y_range.max_interval = 70
    map_plot.title.text_font_style = "bold"
    map_plot.title.text_font_size = "22px"
    # add patches to render states with no aggregate data
    missgeosource = bokeh_map_data_dict[stat]["missgeosource"]
    misscounties = map_plot.patches(
        "xs", "ys", source=missgeosource, fill_color="white", **cons.MAP_SETTINGS
    )
    map_plot.add_tools(
        HoverTool(
            renderers=[misscounties],
            tooltips=[("County Name", "@county"), ("County Value", "NA")],
            attachment="left",
            mode="mouse",
        )
    )
    # add patches to render states with aggregate data
    nonmissgeosource = bokeh_map_data_dict[stat]["nonmissgeosource"]
    nonmisscounties = map_plot.patches(
        "xs",
        "ys",
        source=nonmissgeosource,
        fill_color={"field": col, "transform": color_mapper},
        **cons.MAP_SETTINGS,
    )
    map_plot.add_tools(
        HoverTool(
            renderers=[nonmisscounties],
            tooltips=[("County Name", "@county"), ("County Value", f"@{col}")],
            attachment="left",
            mode="mouse",
        )
    )
    # add points to render stations
    if show_stations == [0]:
        stationpoints = map_plot.scatter(
            "x", "y", source=pointgeosource, color="red", size=8, alpha=0.3
        )
        map_plot.add_tools(
            HoverTool(
                renderers=[stationpoints],
                tooltips=[
                    ("Station Name", "@name"),
                    ("Latitude", "@latitude"),
                    ("Longitude", "@longitude"),
                    ("Open Year", "@open_year"),
                ],
                attachment="right",
                mode="mouse",
            )
        )
    # set layout of color bar
    map_plot.add_layout(color_bar, "below")
    return map_plot
