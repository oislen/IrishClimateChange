import pandas as pd
import cons

def load_stations_data(stations_fpath, filter_open=True, topn=None):
    """
    """
    # load stations data
    stations = pd.read_csv(stations_fpath)
    if filter_open:
        # only consider open stations for now
        open_stations_filter = stations['close_year'].isnull()
        stations = stations.loc[open_stations_filter, :].reset_index(drop=True)
    if topn != None:
        stations = stations.head(topn)
    return stations