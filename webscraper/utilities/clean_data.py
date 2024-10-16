import logging
import os
from beartype import beartype
from typing import Union
import cons
from webscraper.utilities.load_data import load_data
from utilities.S3Client import S3Client

@beartype
def clean_data(
    scraped_data_dir:str=cons.scraped_data_dir,
    cleaned_data_dir:str=cons.cleaned_data_dir,
    store_on_s3:bool=False
    ):
    """Generates the master data from the individual raw Met Eireann .xlsx files

    Parameters
    ----------
    scraped_data_dir : str
        The local directory to load the raw Met Eireann .csv files from
    cleaned_data_dir : str
        The local directory to write the cleaned Met Eireann .csv files to

    Returns
    -------
    """
     # load data files from file directory
    scraped_data_fpaths = [os.path.join(scraped_data_dir, fname) for fname in os.listdir(scraped_data_dir)]
    logging.info("Reading, cleaning and storing files ...")
    s3client = S3Client(sessionToken=cons.session_token_fpath)
    for fpath in scraped_data_fpaths:
        # extract basename
        fname = os.path.basename(fpath)
        # load data
        clean_data = load_data(fpath)
        # write data to clean data directory
        cleaned_data_fpath = os.path.join(cleaned_data_dir, fname)
        clean_data.to_csv(cleaned_data_fpath, header=True, index=False)
        if store_on_s3:
            # store data on s3 back up repository
            s3client.store(data=clean_data, bucket=cons.s3_bucket, key=f"{cons.s3_clean_directory}/{fname}")