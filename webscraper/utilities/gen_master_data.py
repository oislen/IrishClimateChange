import os
import polars as pl
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
    data_list = [pl.read_parquet(fpath) for fpath in met_eireann_fpaths]
    data = pl.concat(items=data_list, how='vertical')
    # order results by county, id and date alphabetically
    data = data.sort(by=["county", "id", "date"])
    # if the output
    if os.path.exists(master_data_fpath):
        logging.info("Writing master file to disk as .parquet file ...")
        # save concatenated data to disk
        data.write_parquet(file=master_data_fpath)
    else:
        raise ValueError(f"{master_data_fpath} does not exist")