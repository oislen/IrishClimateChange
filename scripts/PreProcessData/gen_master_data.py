import os
import cons
import pandas as pd

def gen_master_data(met_eireann_fpaths = None, master_data_fpath = None, return_data = True):
    """"""
    if met_eireann_fpaths == None:
        # load data files from file directory
        met_eireann_fpaths = [os.path.join(cons.met_eireann_dir, fpath) for fpath in os.listdir(cons.met_eireann_dir) if '.xlsx' in fpath]
    dtypes = {'date':'str'}
    data_list = [pd.read_excel(fpath, dtype = dtypes, na_values = [' ']) for fpath in met_eireann_fpaths]
    data = pd.concat(objs = data_list, ignore_index = True, axis = 0)
    data = data[data.columns[~data.columns.str.contains('ind')]]
    data['date'] = pd.to_datetime(data['date'])
    # order results by county and station alphabetically
    data = data.sort_values(by = ['county', 'station']).reset_index(drop = True)
    # if the output
    if master_data_fpath != None:
        if os.path.exists(master_data_fpath):
            # save concatenated data to disk
            data.to_feather(master_data_fpath)
        else:
            raise ValueError(f'{master_data_fpath} does not exist')
    # if returning data
    if return_data:
        res = data
    else:
        res = 0
    return res