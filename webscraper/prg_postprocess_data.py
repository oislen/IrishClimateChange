import time
import cons
import logging
from utilities.gen_master_data import gen_master_data
from utilities.gen_preaggregate_data import gen_preaggregate_data
from utilities.gen_counties_data import gen_counties_data
from utilities.gen_stations_data import gen_stations_data

if __name__ == '__main__':

    # set up logging
    lgr = logging.getLogger()
    lgr.setLevel(logging.INFO)

    # start timer
    t0 = time.time()

    logging.info('~~~~~ Generating master data file ...')
    # generate master data file
    gen_master_data(master_data_fpath = cons.master_data_fpath, return_data = False)

    logging.info('~~~~~ Generating preaggregated data file ...')
    # generate the preaggregate data
    gen_preaggregate_data(preaggregate_data_fpath = cons.preaggregate_data_fpath, return_data = False)

    logging.info('~~~~~ Generating geospatial counties data file ...')
    # generate counties data
    gen_counties_data(map_data_fpath = cons.map_data_fpath, return_data = False)

    logging.info('~~~~~ Generating geospatial stations data file ...')
    # generate wheather station points data
    gen_stations_data(points_data_fpath = cons.points_data_fpath, return_data = False)

    # end timer and log result
    t1 = time.time()
    tres = t1 - t0
    eres = round(tres, 2)
    logging.info(f'Total Execution Time: {eres} seconds')