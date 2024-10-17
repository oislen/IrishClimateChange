import cons
import os
import logging
import pickle
import pandas as pd
from beartype import beartype
from typing import Union

@beartype
def gen_preagg_data(
    master_data_fpath:str=cons.master_data_fpath, 
    preaggregate_data_fpath:str=cons.preaggregate_data_fpath
    ):
    """Generates preaggregate data for bokeh dashboard app

    Parameters
    ----------
    master_data_fpath : None or pd.DataFrame
        The file location to write the master data to disk, default is cons.master_data_fpath
    preaggregate_data_fpath : str
        The file location to write the preaggregated data to disk, default is cons.preaggregate_data_fpath

    Returns
    -------
    """
    logging.info("Loading master data from disk ...")
    # load master data
    master_data = pd.read_feather(master_data_fpath)
    logging.info("Performing initial data aggregation to year-month level ...")
    # preaggregate the data to year-month level for each available stat
    pre_agg_data_dict = {}
    strftime = cons.date_strftime_dict["year-month"]
    agg_data = master_data.copy()
    agg_data["date_str"] = agg_data["date"].dt.strftime(strftime)
    agg_data["date"] = pd.to_datetime(agg_data["date_str"], format=strftime)
    group_cols = ["county", "date", "date_str"]
    logging.info("Performing final data aggregation to desired statistics ...")
    for stat in cons.stat_options:
        logging.info(f"{stat} ...")
        agg_dict = {col: stat for col in cons.col_options}
        tmp_agg_data = agg_data.groupby(group_cols, as_index=False).agg(agg_dict)
        pre_agg_data_dict[stat] = tmp_agg_data
    if os.path.exists(preaggregate_data_fpath):
        logging.info("Writing preaggregated data to disk as .pickle file ...")
        # pickle the preaggregated data dictionary to disk
        with open(cons.preaggregate_data_fpath, "wb") as f:
            pickle.dump(pre_agg_data_dict, f, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        raise ValueError(f"{preaggregate_data_fpath} does not exist")
