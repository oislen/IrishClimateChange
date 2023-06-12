import os
import pickle 
import pandas as pd
import geopandas as gpd
import cons

def gen_stations_data(points_data_fpath = None, return_data = True):
    """
    """
    # load master and station data
    master_data = pd.read_feather(cons.master_data_fpath)
    stations_data = pd.read_csv(cons.stations_fpath)
    # extract out station ids from mater file
    master_station_ids = master_data['id'].unique()
    # filter master data with station ids
    master_stations = stations_data.loc[stations_data['station_id'].isin(master_station_ids), :]
    # create gis data
    geo_master_stations = gpd.GeoDataFrame(master_stations, geometry=gpd.points_from_xy(master_stations.longitude, master_stations.latitude), crs="EPSG:2157")
    # if the output
    if points_data_fpath != None:
        if os.path.exists(points_data_fpath):
            # pickle the gis stations data
            with open(points_data_fpath, 'wb') as f:
                pickle.dump(geo_master_stations, f, protocol = pickle.HIGHEST_PROTOCOL)
        else:
            raise ValueError(f'{points_data_fpath} does not exist')
    # if returning data
    if return_data:
        res = geo_master_stations
    else:
        res = 0
    return res
    