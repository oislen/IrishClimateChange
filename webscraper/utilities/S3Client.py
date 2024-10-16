import io
import boto3
import json
import logging
import pandas as pd
from typing import Union
from beartype import beartype

class S3Client():
    
    @beartype
    def __init__(self, sessionToken:str):
        # load aws config
        with open(sessionToken, "r") as j:
            aws_config = json.loads(j.read())
        # connect to aws boto3
        self.session = boto3.Session(
            aws_access_key_id=aws_config['Credentials']["AccessKeyId"],
            aws_secret_access_key=aws_config['Credentials']["SecretAccessKey"],
            aws_session_token=aws_config['Credentials']["SessionToken"],
            region_name="eu-west-1"
        )
        # generate boto3 s3 connection
        self.client = self.session.client("s3")
    
    @beartype
    def store(
        self,
        data:pd.DataFrame,
        key:str,
        bucket:str="irishclimateapp"
        ):
        """Stores a raw Met Eireann data file on s3.
        
        Parameters
        ----------
        directory : str
            The s3 key to store the Met Eireann data files
        bucket : str
            The s3 bucket storing the Met Eireann data files
        
        Returns
        -------
        """
        try:
            logging.info(f"Storing data to S3://{bucket}/{key}")
            csv_buf = io.StringIO()
            data.to_csv(csv_buf, header=True, index=False)
            csv_buf.seek(0)
            self.client.put_object(Bucket=bucket, Body=csv_buf.getvalue(), Key=key)
        except Exception as e:
            logging.info(str(e))
            
    @beartype
    def retrieve(
        self,
        key:str,
        bucket:str="irishclimateapp" 
        ):
        
        """Retrieves a raw Met Eireann data from AWS s3.
        
        Parameters
        ----------
        key : str
            The s3 key containing the Met Eireann data file
        bucket : str
            The s3 bucket containing the Met Eireann data file
        
        Returns
        -------
        
            The raw Met Eireann data
        """
        data = None
        try:
            logging.info(f"Retrieving data from S3://{bucket}/{key}")
            # load s3 objects into list
            obj = self.client.get_object(Bucket=bucket, Key=key)
            # decode xlsx files in body
            data = pd.read_csv(obj["Body"])
        except Exception as e:
            logging.info(str(e))
        return data