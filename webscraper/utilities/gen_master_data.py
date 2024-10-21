import os
import pandas as pd
import logging
import cons
from beartype import beartype
from typing import Union

@beartype
def gen_master_data(
    cleaned_data_dir:str=cons.cleaned_data_dir,
    master_data_fpath:str=cons.master_data_fpath,
    ):
    """Generates the master data from the individual raw Met Eireann .xlsx files

    Parameters
    ----------
    cleaned_data_dir : str
        The raw Met Eireann .xlsx file paths, default is cons.cleaned_data_dir
    master_data_fpath : str
        The file location to write the master data to disk, default is cons.master_data_fpath

    Returns
    -------
    """
    logging.info("Retrieving cleaned file paths from disk ...")
    # load data files from file directory
    met_eireann_fpaths = [os.path.join(cleaned_data_dir, fname) for fname in os.listdir(cleaned_data_dir)]
    logging.info("Reading and concatenating files ...")
    # load and concatenate data files together
    data_list = [pd.read_parquet(fpath) for fpath in met_eireann_fpaths]
    data = pd.concat(objs=data_list, ignore_index=True, axis=0)
    # convert date to datetime
    data["date"] = pd.to_datetime(data["date"], format="%Y-%m-%d")
    # order results by county, id and date alphabetically
    data = data.sort_values(by=["county", "id", "date"]).reset_index(drop=True)
    # if the output
    if os.path.exists(master_data_fpath):
        logging.info("Writing master file to disk as .feather file ...")
        # save concatenated data to disk
        data.to_feather(master_data_fpath)
    else:
        raise ValueError(f"{master_data_fpath} does not exist")