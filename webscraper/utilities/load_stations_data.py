import pandas as pd
from beartype import beartype

@beartype
def load_stations_data(
    stations_fpath:str, 
    filter_open:bool=True, 
    topn:int=None
    ) -> pd.DataFrame:
    """Loads the station reference data file

    Parameters
    ----------
    stations_fpath : str
        The file path to load the reference station data from disk
    filter_open : bool
        Whether to only consider open stations and not closed stations
    topn : int
        The number of rows to filter from the head of the loaded stations data


    Returns
    -------
    pd.DataFrame
        The loaded stations reference data
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