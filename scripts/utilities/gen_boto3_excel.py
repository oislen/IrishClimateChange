import io
import boto3
import json
from beartype import beartype

@beartype
def gen_boto3_excel(
    sessionToken:str,
    bucket:str="irishclimateapp", 
    prefix:str="data/Met_Eireann"
    ) -> list:
    """Retrieves the raw Met Eireann data from AWS s3

    Parameters
    ----------
    sessionToken : str
        The file path to an active aws session token
    bucket : str
        The s3 bucket containing the Met Eireann data files
    prefix : str
        The s3 directory containing the Met Eireann data files

    Returns
    -------
    list
        The raw Met Eireann data
    """
    # load aws config
    with open(sessionToken, "r") as j:
        aws_config = json.loads(j.read())
    # connect to aws boto3
    session = boto3.Session(
        aws_access_key_id=aws_config['Credentials']["AccessKeyId"],
        aws_secret_access_key=aws_config['Credentials']["SecretAccessKey"],
        aws_session_token=aws_config['Credentials']["SessionToken"],
        region_name="eu-west-1"
    )
    # generate boto3 s3 connection
    client = session.client("s3")
    # create a paginator to list all objects
    paginator = client.get_paginator("list_objects_v2")
    # apply the paginator to list all files in the irishclimateapp bucket with key data/Met_Eireann
    operation_parameters = {"Bucket": bucket, "Prefix": prefix}
    page_iterator = paginator.paginate(**operation_parameters)
    # filter down contents keys with .xlsx
    filtered_iterator = page_iterator.search("Contents[?contains(Key,'.xlsx')].Key")
    # extract out the file keys
    file_keys = [content_key for content_key in filtered_iterator]
    # load s3 objects into list
    objs_list = [
        client.get_object(Bucket=bucket, Key=file_key) for file_key in file_keys
    ]
    # decode xlsx files in body
    data_list = [io.BytesIO(obj["Body"].read()) for obj in objs_list]
    return data_list
