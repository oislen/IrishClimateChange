import cons
import matplotlib.pyplot as plt
import matplotlib.colors
import geopandas as gpd
from beartype import beartype

@beartype
def map_plot(
    map_data:gpd.GeoDataFrame, 
    station_data:gpd.GeoDataFrame,
    year:str,
    stat:str, 
    col:str
    ) -> int:
    """Creates a gis heatmap plot for the aggregated Met Eireann dataset given a specific statistic to visualise

    Parameters
    ----------
    map_data : geopandas.DataFrame
        The gis map data for each given statistic to plot
    station_data : geopandas.DataFrame
        The Met Eireann station data to plot as an overlay of red points over the gis map
    year : str
        The year to plot the gis heatmap for
    stat : str
        The specific statistic to plot the gis map for
    col : str
        The climate / whether category to plot the gis map for

    Returns
    -------
    0
        Successful execution
    """
    # create map of ireland
    sub_cols = ["county", "geometry", "year", col, "stat"]
    data_filter = (map_data["year"] == year) & (map_data["stat"] == stat)
    missing_filter = (map_data["year"].isnull())
    map_plot_data = map_data.loc[missing_filter | data_filter, sub_cols]
    # extract out any rows missing year
    fig, ax = plt.subplots(figsize=cons.sns_fig_settings["figure.figsize"])
    plt.axis("off")
    plt.title("Irish Climate App", size=20)
    # create custom colour map
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["lightblue", "steelblue"])
    norm = plt.Normalize(map_plot_data[col].min(), map_plot_data[col].max())
    # plot heatmap of county climate
    legend_kwds = {"label": col, "orientation": "horizontal", "fraction": 0.046, "pad": 0.04}
    missing_kwds = {"color": "slategrey"}
    # fill in counties of ireland
    map_plot_data.plot(column=col, ax=ax, cmap=cmap, legend=True, legend_kwds=legend_kwds, norm=norm, missing_kwds=missing_kwds)
    # overlay met eireann weather station locations
    station_data.plot(ax=ax, color="red", alpha=0.6)
    plt.show()
    plt.close()
    return 0
