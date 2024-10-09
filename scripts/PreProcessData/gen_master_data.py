import os
import pandas as pd
import cons
from utilities.gen_boto3_excel import gen_boto3_excel
from beartype import beartype
from typing import Union

@beartype
def gen_master_data(
    met_eireann_fpaths:Union[list,None]=None,
    master_data_fpath:Union[str,None]=None, 
    return_data:bool=True, 
    aws_s3:bool=False
) -> Union[int, pd.DataFrame]:
    """Generates the master data from the individual raw Met Eireann .xlsx files

    Parameters
    ----------
    met_eireann_fpaths : None or list
        The raw Met Eireann .xlsx file paths, default is None
    master_data_fpath : None or str
        The file location to write the master data to disk, default is None
    return_data : bool
        Whether to return the master data, default is True
    aws_s3 : bool
        Whether to load the taw Met Eireann .xlex files from s3, default is False

    Returns
    -------

    0, pandas.DataFrame
        Depending on return_data parameter, either return zero or master data
    """
    # set data type constraints
    dtypes = {"date": "str"}
    # if load data locally
    if not aws_s3:
        if met_eireann_fpaths == None:
            print("Retrieving raw met eireann .xlsx file paths from disk ...")
            # load data files from file directory
            met_eireann_fpaths = [
                os.path.join(cons.met_eireann_dir, fpath)
                for fpath in os.listdir(cons.met_eireann_dir)
                if ".xlsx" in fpath
            ]
    # otherwise if loading data from aws s3
    else:
        print("Retrieving raw met eireann .xlsx file paths from aws s3 ...")
        met_eireann_fpaths = gen_boto3_excel(
            bucket="irishclimateapp", prefix="data/Met_Eireann"
        )
    print("Reading, concatenating and cleaning .xlsx files ...")
    # load and concatenate data files together
    data_list = [
        pd.read_excel(fpath, dtype=dtypes, na_values=[" "])
        for fpath in met_eireann_fpaths
    ]
    data = pd.concat(objs=data_list, ignore_index=True, axis=0)
    data = data[data.columns[~data.columns.str.contains("ind")]]
    data["date"] = pd.to_datetime(data["date"])
    data["county"] = data["county"].str.title()
    print("Sorting master file by county and station names ...")
    # order results by county and station alphabetically
    data = data.sort_values(by=["county", "station"]).reset_index(drop=True)
    # if the output
    if master_data_fpath != None:
        if os.path.exists(master_data_fpath):
            print("Writing master file to disk as .feather file ...")
            # save concatenated data to disk
            data.to_feather(master_data_fpath)
        else:
            raise ValueError(f"{master_data_fpath} does not exist")
    # if returning data
    if return_data:
        res = data
    else:
        res = 0
    return res
