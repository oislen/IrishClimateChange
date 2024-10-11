import logging
import cons
from utilities.load_stations_data import load_stations_data
from utilities.retrieve_station_data import retrieve_station_data

# if running as main programme
if __name__ == '__main__':
    
    # set up logging
    lgr = logging.getLogger()
    lgr.setLevel(logging.INFO)
    # load stations data
    logging.info("Loading stations data ...")
    stations = load_stations_data(stations_fpath=cons.stations_fpath, filter_open=True, topn=5)
    # run webscraper
    resp_log = retrieve_station_data(stations=stations, scraped_data_dir=cons.scraped_data_dir, data_level="dly")