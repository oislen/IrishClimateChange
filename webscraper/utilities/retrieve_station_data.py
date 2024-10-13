import logging
import pandas as pd
from utilities.url_retrieve import url_retrieve
from beartype import beartype

@beartype
def retrieve_station_data(
    stations:pd.DataFrame,
    scraped_data_dir:str,
    data_level:str="dly"
    ) -> list:
    """Webscrapes the met data for all station ids in a given stations dataframe

    Parameters
    ----------
    stations : pd.DataFrame
        The loaded reference stations data
    scraped_data_dir : str
        The file directory to write the scraped met data to
    data_level : str
        The time level of the met data to scrape, default is "dly"


    Returns
    -------
    list
        A log of the webscrape responses
    """
    # iterate over each station and pull daily level data using using stationid
    resp_log =[]
    for idx, row in stations.iterrows():
        logging.info(f"{idx} {row['county']} {row['station_id']} {row['name']}")
        resp = url_retrieve(stationid=row['station_id'], scraped_data_dir=scraped_data_dir, data_level=data_level)
        logging.info(resp)
        resp_log.append(resp)
    return resp_log