import io
import boto3
import json
import logging
import pandas as pd
from typing import Union
from beartype import beartype


class EC2Client():
    
    @beartype
    def __init__(self, sessionToken:str):
        # load aws config
        with open(sessionToken, "r") as j:
            aws_config = json.loads(j.read())
        # connect to aws boto3
        self.session = boto3.Session(
            aws_access_key_id=aws_config["Credentials"]["AccessKeyId"],
            aws_secret_access_key=aws_config["Credentials"]["SecretAccessKey"],
            aws_session_token=aws_config["Credentials"]["SessionToken"],
            region_name="eu-west-1"
        )
        # generate boto3 s3 connection
        self.client = self.session.client("ec2")
    
    def create_launch_template(self, launch_template_config):
        """
        
        Parameters
        ----------

        Returns
        -------
        """
        # create ec2 launch template
        response = self.client.create_launch_template(**launch_template_config)
        return response
    
    def delete_launch_template(self, launch_template_config):
        """
        
        Parameters
        ----------

        Returns
        -------
        """
        # delete ec2 launch template
        response = self.client.delete_launch_template(DryRun=launch_template_config["DryRun"], LaunchTemplateName=launch_template_config["LaunchTemplateName"])
        return response
    
    def create_fleet(self, create_fleet_config):
        """
        
        Parameters
        ----------

        Returns
        -------
        """
        response = self.client.create_fleet(**create_fleet_config)
        return response
    
    def describe_fleets(self):
        """
        
        Parameters
        ----------

        Returns
        -------
        """
        response = self.client.describe_fleets()
        return response
    
    def delete_fleets(self, FleetIds=[], TerminateInstances=False):
        """
        
        Parameters
        ----------

        Returns
        -------
        """
        response = self.client.delete_fleets(FleetIds=FleetIds, TerminateInstances=TerminateInstances)
        return response
    
    def run_instances(self, run_instances_config):
        """
        
        Parameters
        ----------

        Returns
        -------
        """
        response = self.client.run_instances(**run_instances_config)
        return response
    
    def stop_instances(self, InstanceIds=[]):
        """
        
        Parameters
        ----------

        Returns
        -------
        """
        response = self.client.stop_instances(InstanceIds=InstanceIds)
        return response
    
    def terminate_instances(self, InstanceIds=[]):
        """
        
        Parameters
        ----------

        Returns
        -------
        """
        response = self.client.terminate_instances(InstanceIds=InstanceIds)
        return response
    
    def describe_instances(self, InstanceIds=[], Filters=[], MaxResults=20):
        """
        
        Parameters
        ----------

        Returns
        -------
        """
        response = self.client.describe_instances(InstanceIds=InstanceIds, Filters=Filters, MaxResults=MaxResults)
        return response
