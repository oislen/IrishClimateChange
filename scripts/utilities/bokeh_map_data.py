import cons
import pandas as pd
import geopandas as gpd
from bokeh.models import GeoJSONDataSource

def bokeh_map_data(map_data_dict):
    """"""
    bokeh_data_dict = {}
    for stat, map_data in map_data_dict.items():
        tmp_data_dict = {}
        # split data into missing and nonmissing
        nonmiss_map_data = map_data[map_data[cons.col_options].notnull().any(axis = 1)]
        miss_map_data = map_data[~map_data[cons.col_options].notnull().any(axis = 1)]
        # Input GeoJSON source that contains features for plotting
        missgeosource = GeoJSONDataSource(geojson=miss_map_data.to_json())
        nonmissgeosource = GeoJSONDataSource(geojson=nonmiss_map_data.to_json())
        # assign data to temp dict
        tmp_data_dict['map_data'] = map_data
        tmp_data_dict['nonmiss_map_data'] = nonmiss_map_data
        tmp_data_dict['miss_map_data'] = miss_map_data
        tmp_data_dict['missgeosource'] = missgeosource
        tmp_data_dict['nonmissgeosource'] = nonmissgeosource
        # assign temp data dict to bokeh data dict
        bokeh_data_dict[stat] = tmp_data_dict
    return bokeh_data_dict
