import logging
import os
import re
import pandas as pd
from beartype import beartype
import cons
from utilities.S3Client import S3Client

@beartype
def load_data(
    fpath:str,
    stations_fpath:str=cons.stations_fpath
    ) -> pd.DataFrame:
    """Loads webscraped met data from disk

    Parameters
    ----------
    fpath : str
        The file path to load the webscraped met data from disk
    stations_fpath : str
        The file path to load the reference station data from disk, default is cons.stations_fpath

    Returns
    -------
    pd.DataFrame
        The loaded webscraped met data
    """
    # extract stationid
    station_id = int(re.findall(pattern="dly([0-9]+).csv", string=os.path.basename(fpath))[0])
    # load file lines
    with open(fpath) as file:
        lines = [line.rstrip().lower() for line in file]
    # split into rows
    split_lines = [row.split(',') for row in lines]
    # generate dataframe
    n_cols = len(split_lines[-1])
    data_lines = [line for line in split_lines if len(line) == n_cols]
    dataframe = pd.DataFrame(data_lines[1:], columns = data_lines[0])
    # rename columns to standard names
    rename_cols = {'maxt':'maxtp', 'mint':'mintp', 'g_rad':'glorad'}
    dataframe = dataframe.rename(columns=rename_cols)
    # subset required rows and columns
    sub_cols = dataframe.columns[dataframe.columns.isin(['date'] + cons.col_options)]
    row_filter = dataframe['date'].str.contains('20[1-2]+')
    dataframe = dataframe.loc[row_filter, sub_cols]
    # convert numeric columns
    for col in cons.col_options:
        if col in dataframe.columns:
            dataframe[col] = dataframe[col].apply(lambda x: x.strip()).replace('', None).astype(float)
    # subset return columns
    cols = dataframe.columns[~dataframe.columns.isin(['ind'])]
    dataframe = dataframe[cols]
    dataframe['station_id'] = station_id
    stations_data = pd.read_csv(stations_fpath).rename(columns={'name':'station'})
    dataframe = pd.merge(left=dataframe, right=stations_data, on='station_id', how='inner').rename(columns={'station_id':'id'})
    dataframe["county"] = dataframe["county"].str.title()
    dataframe["date"] = pd.to_datetime(dataframe["date"], format='%d-%b-%Y')
    return dataframe


@beartype
def gen_clean_data(
    scraped_data_dir:str=cons.scraped_data_dir,
    cleaned_data_dir:str=cons.cleaned_data_dir,
    store_on_s3:bool=False
    ):
    """Generates the master data from the individual raw Met Eireann .xlsx files

    Parameters
    ----------
    scraped_data_dir : str
        The local directory to load the raw Met Eireann .csv files from, default is cons.scraped_data_dir
    cleaned_data_dir : str
        The local directory to write the cleaned Met Eireann .csv files to, default is cons.cleaned_data_dir
    store_on_s3 : bool
        Whether to back up the clean data files on s3, default is False

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
        logging.info(f"Writing cleaned data file {cleaned_data_fpath} to disk")
        clean_data.to_csv(cleaned_data_fpath, header=True, index=False)
        if store_on_s3:
            # store data on s3 back up repository
            s3client.store(data=clean_data, bucket=cons.s3_bucket, key=f"{cons.s3_clean_directory}/{fname}")