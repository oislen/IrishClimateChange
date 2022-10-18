import cons
import os
import pickle
import pandas as pd
import geopandas as gpd

def gen_counties_data(map_data_fpath = None, return_data = True):
    """"""
    # load in county shape files
    rep_counties = gpd.read_file(cons.rep_counties_fpath)[['ENGLISH', 'geometry']].rename(columns = {'ENGLISH':'county'}).to_crs(epsg = 2157)
    ni_counties = gpd.read_file(cons.ni_counties_fpath)[['county', 'geometry']].to_crs(epsg = 2157)
    # load preaggregated data
    with open(cons.preaggregate_data_fpath, "rb") as f:
        pre_agg_data_dict = pickle.load(f)
    # concatenate county shape files
    counties = gpd.GeoDataFrame(pd.concat([rep_counties, ni_counties], ignore_index=True), crs="EPSG:2157")
    # simplify the granularity of the geometry column
    counties['geometry'] = counties['geometry'].simplify(tolerance = 1000)
    # clean up county column
    counties['county'] = counties['county'].str.lower().str.replace(pat = 'county ', repl = '', regex = False)
    # sort data by county
    counties = counties.sort_values(by = 'county')
    # create a dictionary to contain map data
    map_data_dict = {}
    # iterate over statistic and pre aggregated data
    for stat, pre_agg_data in pre_agg_data_dict.items():
        # aggregate data to county level
        group_cols = ['county']
        agg_dict = {col:stat for col in cons.col_options}
        # filter data to be between 2010 and 2019
        pre_agg_data = pre_agg_data.loc[(pre_agg_data['date'].dt.year >= 2010) & (pre_agg_data['date'].dt.year >= 2010), :]
        county_data = pre_agg_data.groupby(group_cols, as_index = False).agg(agg_dict)
        # join county level data to map data
        map_data_dict[stat] = gpd.GeoDataFrame(pd.merge(left = counties, right = county_data, on = 'county', how = 'left'), crs="EPSG:2157")
    # if the output
    if map_data_fpath != None:
        if os.path.exists(map_data_fpath):
            # pickle the preaggregated data dictionary to disk
            with open(map_data_fpath, 'wb') as f:
                pickle.dump(map_data_dict, f, protocol = pickle.HIGHEST_PROTOCOL)
        else:
            raise ValueError(f'{map_data_fpath} does not exist')
    # if returning data
    if return_data:
        res = map_data_dict
    else:
        res = 0
    return res