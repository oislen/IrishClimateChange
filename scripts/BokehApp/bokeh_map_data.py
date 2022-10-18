import cons
import pickle
import pandas as pd
import geopandas as gpd
from bokeh.models import GeoJSONDataSource
from PreProcessData.gen_preaggregate_data import gen_preaggregate_data
from PreProcessData.gen_counties_data import gen_counties_data

def bokeh_map_data():
    """"""
    print('~~~ Generating bokeh map data ...')
    # load map data
    #with open(cons.map_data_fpath, "rb") as f:
    #    map_data_dict = pickle.load(f)
    pre_agg_data_dict = gen_preaggregate_data(return_data = True)
    map_data_dict = gen_counties_data(pre_agg_data_dict = pre_agg_data_dict, return_data = True)
    bokeh_map_data_dict = {}
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
        bokeh_map_data_dict[stat] = tmp_data_dict
    # pickle the bokeh map data dictionary to disk
    #with open(cons.bokeh_map_data_fpath, 'wb') as f:
    #    pickle.dump(bokeh_map_data_dict, f, protocol = pickle.HIGHEST_PROTOCOL)
    return bokeh_map_data_dict
