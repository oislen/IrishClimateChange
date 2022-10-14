import pandas as pd
import geopandas as gpd
from bokeh.models import GeoJSONDataSource

def bokeh_map_data(data, counties):
    """"""
    bokeh_data_dict = {}
    # filter data to be between 2010 and 2019
    data_filt = data.loc[(data['date'].dt.year >= 2010) & (data['date'].dt.year >= 2010), :]
    # aggregate to county level
    groupby_cols = ['county']
    agg_dict = {'maxtp':'mean', 'mintp':'mean', 'wdsp':'mean', 'sun':'mean', 'evap':'mean', 'rain':'mean'}
    agg_data = data_filt.groupby(groupby_cols, as_index = False).agg(agg_dict)
    # join aggregated county level data to counties gis data
    map_data = gpd.GeoDataFrame(pd.merge(left = counties, right = agg_data, on = 'county', how = 'left'), crs="EPSG:2157")
    # split data into missing and nonmissing
    nonmiss_map_data = map_data[map_data[list(agg_dict.keys())].notnull().any(axis = 1)]
    miss_map_data = map_data[~map_data[list(agg_dict.keys())].notnull().any(axis = 1)]
    # Input GeoJSON source that contains features for plotting
    missgeosource = GeoJSONDataSource(geojson=miss_map_data.to_json())
    nonmissgeosource = GeoJSONDataSource(geojson=nonmiss_map_data.to_json())
    # assign data to bokeh data dict
    bokeh_data_dict['data_filt'] = data_filt
    bokeh_data_dict['agg_data'] = agg_data
    bokeh_data_dict['map_data'] = map_data
    bokeh_data_dict['nonmiss_map_data'] = nonmiss_map_data
    bokeh_data_dict['miss_map_data'] = miss_map_data
    bokeh_data_dict['missgeosource'] = missgeosource
    bokeh_data_dict['nonmissgeosource'] = nonmissgeosource
    return bokeh_data_dict
