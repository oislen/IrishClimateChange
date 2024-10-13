import os
import pandas as pd
import logging
import cons
from beartype import beartype
from typing import Union
from webscraper.utilities.load_data import load_data

@beartype
def gen_master_data(
    met_eireann_fpaths:Union[list,None]=None,
    master_data_fpath:Union[str,None]=None,
    ):
    """Generates the master data from the individual raw Met Eireann .xlsx files

    Parameters
    ----------
    met_eireann_fpaths : None or list
        The raw Met Eireann .xlsx file paths, default is None
    master_data_fpath : None or str
        The file location to write the master data to disk, default is None

    Returns
    -------
    """
    # if load data locally
    if met_eireann_fpaths == None:
        logging.info("Retrieving raw met eireann .xlsx file paths from disk ...")
        # load data files from file directory
        met_eireann_fpaths = [os.path.join(cons.scraped_data_dir, fname) for fname in os.listdir(cons.scraped_data_dir)]
    logging.info("Reading, concatenating and cleaning .xlsx files ...")
    # load and concatenate data files together
    data_list = [load_data(fpath) for fpath in met_eireann_fpaths]
    data = pd.concat(objs=data_list, ignore_index=True, axis=0)
    # order results by county, id and date alphabetically
    data = data.sort_values(by=["county", "id", "date"]).reset_index(drop=True)
    # if the output
    if master_data_fpath != None:
        if os.path.exists(master_data_fpath):
            logging.info("Writing master file to disk as .feather file ...")
            # save concatenated data to disk
            data.to_feather(master_data_fpath)
        else:
            raise ValueError(f"{master_data_fpath} does not exist")