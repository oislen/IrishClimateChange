import cons
import os
import pickle
import pandas as pd

def gen_preaggregate_data(master_data = None, preaggregate_data_fpath = None, return_data = True):
    """"""
    if type(master_data) == type(None):
        # load master data
        master_data = pd.read_feather(cons.master_data_fpath)
    # preaggregate the data to year-month level for each available stat
    pre_agg_data_dict = {}
    strftime = cons.date_strftime_dict['year-month']
    agg_data = master_data.copy()
    agg_data['date_str'] = agg_data['date'].dt.strftime(strftime)
    agg_data['date'] = pd.to_datetime(agg_data['date_str'], format = strftime)
    group_cols = ['county', 'date', 'date_str']
    for stat in cons.stat_options:
        agg_dict = {col:stat for col in cons.col_options}
        agg_data = agg_data.groupby(group_cols, as_index = False).agg(agg_dict)
        pre_agg_data_dict[stat] = agg_data
    # if the output
    if preaggregate_data_fpath != None:
        if os.path.exists(preaggregate_data_fpath):
            # pickle the preaggregated data dictionary to disk
            with open(cons.preaggregate_data_fpath, 'wb') as f:
                pickle.dump(pre_agg_data_dict, f, protocol = pickle.HIGHEST_PROTOCOL)
        else:
            raise ValueError(f'{preaggregate_data_fpath} does not exist')
    # if returning data
    if return_data:
        res = pre_agg_data_dict
    else:
        res = 0
    return res