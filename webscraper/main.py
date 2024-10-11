import os
import logging
import cons
import pandas as pd
import urllib.request

def load_stations_data(filter_open=True):
    """
    """
    # load stations data
    stations = pd.read_csv(cons.stations_fpath)
    if filter_open:
        # only consider open stations for now
        open_stations_filter = stations['close_year'].isnull()
        stations = stations.loc[open_stations_filter, :]
    return stations

# define main webscraping programme
def retrieve_station_data(stationid, scraped_data_dir, data_level="dly"):
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


def main():
    """
    """
    logging.info("Loading stations data ...")
    stations = load_stations_data(filter_open=True)
    # iterate over each station and pull daily level data using using stationid
    resp_log =[]
    for idx, row in stations.iterrows():
        logging.info(f"{idx} {row['county']} {row['station_id']} {row['name']}")
        resp = retrieve_station_data(stationid=row['station_id'], scraped_data_dir = cons.scraped_data_dir, data_level="dly")
        logging.info(resp)
        resp_log.append(resp_log)

# if running as main programme
if __name__ == '__main__':

    # set up logging
    lgr = logging.getLogger()
    lgr.setLevel(logging.INFO)
    # run webscraper
    main()