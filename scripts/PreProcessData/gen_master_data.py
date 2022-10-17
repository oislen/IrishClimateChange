import os
import cons
import pandas as pd

def gen_master_data():
    """"""
    print('~~~ Generating master data ...')
    # load data files from file directory
    met_eireann_fpaths = [os.path.join(cons.met_eireann_dir, fpath) for fpath in os.listdir(cons.met_eireann_dir) if '.xlsx' in fpath]
    dtypes = {'date':'str'}
    data = pd.DataFrame()
    for fpath in met_eireann_fpaths:
        print(f'loading {fpath} ...')
        tmp_data = pd.read_excel(fpath, dtype = dtypes, na_values = [' '])
        data = pd.concat(objs = [data, tmp_data], ignore_index = True, axis = 0)
    data['date'] = pd.to_datetime(data['date'])
    # save concatenated data to disk and reread
    print('outputting feather file ...')
    data.to_feather(cons.master_data_fpath)
    return 0