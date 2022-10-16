import cons
import pandas as pd
import geopandas as gpd
from bokeh.models import GeoJSONDataSource

def bokeh_map_data(map_data_dict, stat):
    """"""
    map_data = map_data_dict[stat]
    bokeh_data_dict = {}
    # split data into missing and nonmissing
    nonmiss_map_data = map_data[map_data[cons.col_options].notnull().any(axis = 1)]
    miss_map_data = map_data[~map_data[cons.col_options].notnull().any(axis = 1)]
    # Input GeoJSON source that contains features for plotting
    missgeosource = GeoJSONDataSource(geojson=miss_map_data.to_json())
    nonmissgeosource = GeoJSONDataSource(geojson=nonmiss_map_data.to_json())
    # assign data to bokeh data dict
    bokeh_data_dict['map_data'] = map_data
    bokeh_data_dict['nonmiss_map_data'] = nonmiss_map_data
    bokeh_data_dict['miss_map_data'] = miss_map_data
    bokeh_data_dict['missgeosource'] = missgeosource
    bokeh_data_dict['nonmissgeosource'] = nonmissgeosource
    return bokeh_data_dict
