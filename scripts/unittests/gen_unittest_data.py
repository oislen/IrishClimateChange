import sys
import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

sys.path.append(os.path.join(os.getcwd(), "scripts"))

import cons

def gen_unittest_data(
    unittest_country_station_map=cons.unittest_country_station_map, 
    start_date=cons.unittest_start_date, 
    n_dates=cons.unittest_n_dates, 
    normal_dists=cons.unittest_normal_dists
    ):
    """
    """
    unittest_data_list = []
    # iterate over each county and station pairs
    for county, stations in unittest_country_station_map.items():
        for station in stations:
            # generate the id variables
            unittest_list_dict = {}
            unittest_list_dict['county'] = [county] * n_dates
            unittest_list_dict['station'] = [station] * n_dates
            unittest_list_dict['id'] = [532] * n_dates
            start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = start_datetime + timedelta(days=n_dates)
            unittest_list_dict['date'] = np.arange(start_datetime, end_date, timedelta(days=1)).astype(datetime)
            unittest_list_dict['ind'] = [0] * n_dates
            # iterate over the normal distributions mean and std for each numeric variable
            for col, normal_dist in normal_dists.items():
                # create the numeric variable
                unittest_list_dict[col] = np.random.normal(loc=normal_dist['loc'], scale=normal_dist['scale'], size=n_dates)
            # append random generated data to list
            unittest_data_list.append(pd.DataFrame(unittest_list_dict))
    # concatenate all random generated data together
    unittest_data = pd.concat(objs=unittest_data_list, axis=0, ignore_index=True)
    return unittest_data