import io
import boto3
import pandas as pd
from aws_rootkey import aws_rootkey_fpath

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