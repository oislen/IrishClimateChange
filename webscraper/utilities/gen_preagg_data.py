import cons
import os
import logging
import pickle
import pandas as pd
import numpy as np
import polars as pl
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
    master_data = pl.read_parquet(master_data_fpath)
    logging.info("Performing initial data aggregation to year-month level ...")
    # preaggregate the data to year-month level for each available stat
    pre_agg_data_dict = {}
    strftime = cons.date_strftime_dict["year-month"]
    agg_data = master_data.clone()
    agg_data = agg_data.with_columns(date_str = pl.col("date").dt.to_string(strftime))
    agg_data = agg_data.with_columns(date = pl.col("date_str").str.to_datetime(format=strftime))
    group_cols = ["county", "date", "date_str"]
    logging.info("Performing final data aggregation to desired statistics ...")
    for stat in cons.stat_options:
        logging.info(f"{stat} ...")
        agg_dict = [getattr(pl.col(col), stat)().replace({None:np.nan}).alias(col) for col in cons.col_options]
        tmp_agg_data = agg_data.group_by(group_cols).agg(agg_dict)
        pre_agg_data_dict[stat] = tmp_agg_data.sort(by=group_cols).to_pandas()
    if os.path.exists(preaggregate_data_fpath):
        logging.info("Writing pre-aggregated data to disk as .pickle file ...")
        # pickle the pre-aggregated data dictionary to disk
        with open(cons.preaggregate_data_fpath, "wb") as f:
            pickle.dump(pre_agg_data_dict, f, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        raise ValueError(f"{preaggregate_data_fpath} does not exist")
