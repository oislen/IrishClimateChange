import os
import urllib.request

# define main webscraping programme
def url_retrieve(stationid, scraped_data_dir, data_level="dly"):
    """
    """
    data_fname = f"{data_level}{stationid}.csv"
    data_url = f"http://cli.fusio.net/cli/climate_data/webdata/{data_fname}"
    download_data_fpath = os.path.join(scraped_data_dir, data_fname)
    try:
        resp = urllib.request.urlretrieve(data_url, download_data_fpath)
    except Exception as e:
        resp = e
    return resp