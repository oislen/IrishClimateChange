import os
import pandas as pd

def gen_master_data(met_eireann_fdir, master_data_fpath):
    """"""
    # load data files from file directory
    met_eireann_fpaths = [os.path.join(met_eireann_fdir, fpath) for fpath in os.listdir(met_eireann_fdir) if '.xlsx' in fpath]
    dtypes = {'date':'str'}
    data = pd.DataFrame()
    for fpath in met_eireann_fpaths:
        print(fpath)
        tmp_data = pd.read_excel(fpath, dtype = dtypes, na_values = [' '])
        data = pd.concat(objs = [data, tmp_data], ignore_index = True, axis = 0)
    data['date'] = pd.to_datetime(data['date'])
    # save concatenated data to disk and reread
    data.to_feather(master_data_fpath)
    return 0