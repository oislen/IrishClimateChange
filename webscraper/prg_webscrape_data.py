import logging
import cons
import time
from beartype import beartype
from utilities.commandline_interface import commandline_interface
from utilities.load_stations_data import load_stations_data
from utilities.retrieve_station_data import retrieve_station_data
from utilities.gen_master_data import gen_master_data
from utilities.gen_preaggregate_data import gen_preaggregate_data
from utilities.gen_counties_data import gen_counties_data
from utilities.gen_stations_data import gen_stations_data

@beartype
def webscrape_data(
    retrieve_data:bool, 
    generate_master_data:bool, 
    generate_preaggregated_data:bool,
    generate_counties_data:bool,
    generate_stations_data:bool
    ):
    """Webscrape and process met data into dashboard files

    Parameters
    ----------
    retrieve_data : bool
        Retrieves / web scrapes the historical met data
    generate_master_data : bool
        Generates the master data file from the retrieved / web scraped met data files
    generate_preaggregated_data : bool
        Preaggreates the master data file into various date levels for the bokeh dashboard app
    generate_counties_data : bool
        Generates the counties gis file for the bokeh dashboard app
    generate_stations_data : bool
        Generates the stations gis file for the bokeh dashboard app

    Returns
    -------
    """
    # start timer
    t0 = time.time()
    if retrieve_data:
        logging.info('~~~~~ Retrieving data for met stations ...')
        # load stations data
        stations = load_stations_data(stations_fpath=cons.stations_fpath, filter_open=True)
        # run webscraper
        resp_log = retrieve_station_data(stations=stations, scraped_data_dir=cons.scraped_data_dir, data_level="dly")
    if generate_master_data:
        logging.info('~~~~~ Generating master data file ...')
        # generate master data file
        gen_master_data(master_data_fpath = cons.master_data_fpath, return_data = False)
    if generate_preaggregated_data:
        logging.info('~~~~~ Generating preaggregated data file ...')
        # generate the preaggregate data
        gen_preaggregate_data(preaggregate_data_fpath = cons.preaggregate_data_fpath, return_data = False)
    if generate_counties_data:
        logging.info('~~~~~ Generating geospatial counties data file ...')
        # generate counties data
        gen_counties_data(map_data_fpath = cons.map_data_fpath, return_data = False)
    if generate_stations_data:
        logging.info('~~~~~ Generating geospatial stations data file ...')
        # generate wheather station points data
        gen_stations_data(points_data_fpath = cons.points_data_fpath, return_data = False)
    # end timer and log result
    t1 = time.time()
    tres = t1 - t0
    eres = round(tres, 2)
    logging.info(f'Total Execution Time: {eres} seconds')

# if running as main programme
if __name__ == '__main__':
    # set up logging
    lgr = logging.getLogger()
    lgr.setLevel(logging.INFO)
    # handle input parameters
    input_params_dict = commandline_interface()
    # call webscrape data
    webscrape_data(
        retrieve_data=input_params_dict['retrieve_data'], 
        generate_master_data=input_params_dict['generate_master_data'], 
        generate_preaggregated_data=input_params_dict['generate_preaggregated_data'],
        generate_counties_data=input_params_dict['generate_counties_data'],
        generate_stations_data=input_params_dict['generate_stations_data']
    )