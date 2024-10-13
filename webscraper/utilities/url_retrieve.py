import os
import urllib.request
from beartype import beartype

@beartype
def url_retrieve(
    stationid:int, 
    scraped_data_dir:str, 
    data_level:str="dly"
    ):
    """Retrieves met data for a given station id 

    Parameters
    ----------
    stationid : int
        The station id to retrieve data for
    scraped_data_dir : str
        The file directory to write the scraped met data to
    data_level : str
        The time level of the met data to scrape, default is "dly"

    Returns
    -------
    urllib.request.urlretrieve, Exception
        A retrieval response
    """
    data_fname = f"{data_level}{stationid}.csv"
    data_url = f"http://cli.fusio.net/cli/climate_data/webdata/{data_fname}"
    download_data_fpath = os.path.join(scraped_data_dir, data_fname)
    try:
        resp = urllib.request.urlretrieve(data_url, download_data_fpath)
    except Exception as e:
        resp = e
    return resp