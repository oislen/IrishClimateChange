import time
import cons
from PreProcessData.gen_master_data import gen_master_data
from PreProcessData.gen_preaggregate_data import gen_preaggregate_data
from PreProcessData.gen_counties_data import gen_counties_data
from PreProcessData.gen_stations_data import gen_stations_data

if __name__ == '__main__':

    # start timer
    t0 = time.time()

    print('~~~~~ Generating master data file ...')
    # generate master data file
    gen_master_data(master_data_fpath = cons.master_data_fpath, return_data = False)

    print('~~~~~ Generating preaggregated data file ...')
    # generate the preaggregate data
    gen_preaggregate_data(preaggregate_data_fpath = cons.preaggregate_data_fpath, return_data = False)

    print('~~~~~ Generating geospatial counties data file ...')
    # generate counties data
    gen_counties_data(map_data_fpath = cons.map_data_fpath, return_data = False)

    print('~~~~~ Generating geospatial stations data file ...')
    # generate wheather station points data
    gen_stations_data(points_data_fpath = cons.points_data_fpath, return_data = False)

    # end timer and print result
    t1 = time.time()
    tres = t1 - t0
    eres = round(tres, 2)
    print(f'Total Execution Time: {eres} seconds')