import io
import os
import cons
from aws_rootkey import aws_rootkey_fpath
import pandas as pd
import boto3

def gen_boto3_excel(bucket = 'irishclimateapp', prefix = 'data/Met_Eireann'):
    """"""
    # load aws root key
    rootkey = pd.read_csv(aws_rootkey_fpath, sep='=', header = None, index_col = 0)[1]
    # generate boto3 s3 connection
    client = boto3.client('s3', aws_access_key_id=rootkey['AWSAccessKeyId'], aws_secret_access_key= rootkey['AWSSecretKey'])
    # create a paginator to list all objects
    paginator = client.get_paginator('list_objects_v2')
    # apply the paginator to list all files in the irishclimateapp bucket with key data/Met_Eireann
    operation_parameters = {'Bucket': bucket, 'Prefix': prefix}
    page_iterator = paginator.paginate(**operation_parameters)
    # filter down contents keys with .xlsx
    filtered_iterator = page_iterator.search("Contents[?contains(Key,'.xlsx')].Key")
    # extract out the file keys
    file_keys = [content_key for content_key in filtered_iterator]
    # load s3 objects into list
    objs_list = [client.get_object(Bucket = bucket, Key = file_key) for file_key in file_keys]
    # decode xlsx files in body
    data_list = [io.BytesIO(obj['Body'].read()) for obj in objs_list]
    return data_list

def gen_master_data(met_eireann_fpaths = None, master_data_fpath = None, return_data = True, aws_s3 = False):
    """"""
    # set data type constraints
    dtypes = {'date':'str'}
    # if load data locally
    if not aws_s3:
        if met_eireann_fpaths == None:
            # load data files from file directory
            met_eireann_fpaths = [os.path.join(cons.met_eireann_dir, fpath) for fpath in os.listdir(cons.met_eireann_dir) if '.xlsx' in fpath]
    # otherwise if loading data from aws s3
    else:
        met_eireann_fpaths = gen_boto3_excel(bucket = 'irishclimateapp', prefix = 'data/Met_Eireann')
    # load and concatenate data files together
    data_list = [pd.read_excel(fpath, dtype = dtypes, na_values = [' ']) for fpath in met_eireann_fpaths]
    data = pd.concat(objs = data_list, ignore_index = True, axis = 0)
    data = data[data.columns[~data.columns.str.contains('ind')]]
    data['date'] = pd.to_datetime(data['date'])
    # order results by county and station alphabetically
    data = data.sort_values(by = ['county', 'station']).reset_index(drop = True)
    # if the output
    if master_data_fpath != None:
        if os.path.exists(master_data_fpath):
            # save concatenated data to disk
            data.to_feather(master_data_fpath)
        else:
            raise ValueError(f'{master_data_fpath} does not exist')
    # if returning data
    if return_data:
        res = data
    else:
        res = 0
    return res