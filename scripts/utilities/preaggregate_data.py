import cons
import pickle
import pandas as pd

def preaggregate_data(master_data_fpath):
    """"""
    # load master data
    data = pd.read_feather(master_data_fpath)
    # preaggregate the data to year-month level for each available stat
    pre_agg_data_dict = {}
    strftime = cons.date_strftime_dict['year-month']
    agg_data = data.copy()
    agg_data['date_str'] = agg_data['date'].dt.strftime(strftime)
    agg_data['date'] = pd.to_datetime(agg_data['date_str'], format = strftime)
    group_cols = ['county', 'date', 'date_str']
    for stat in cons.stat_options:
        agg_dict = {col:stat for col in cons.col_options}
        agg_data = agg_data.groupby(group_cols, as_index = False).agg(agg_dict)
        pre_agg_data_dict[stat] = agg_data
    # pickle the preaggregated data dictionary to disk
    with open(cons.preaggregate_data_fpath, 'wb') as f:
        pickle.dump(pre_agg_data_dict, f, protocol = pickle.HIGHEST_PROTOCOL)
    return 0