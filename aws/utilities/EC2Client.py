import io
import boto3
import json
import logging
import pandas as pd
from typing import Union
from beartype import beartype
import cons

launch_template={
    "DryRun":False,
    "LaunchTemplateName":"irishclimatedashboard",
    "VersionDescription":"Initial version",
    "LaunchTemplateData":{
        "ImageId": "ami-00385a401487aefa4",
        "InstanceType": "t2.micro",
        "Placement": {"AvailabilityZone": "eu-west-1"},
        "SecurityGroupIds": ["sg-03864b806cd78ded3"]
        }    
    }

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
    
    def create_launch_template(self, launch_template):
        """
        """
        # create ec2 launch template
        response = self.client.create_launch_template(**launch_template)
        return response
    
    def delete_launch_template(self, launch_template):
        """
        """
        # delete ec2 launch template
        response = self.client.delete_launch_template(
            DryRun=launch_template["DryRun"], 
            LaunchTemplateName=launch_template["LaunchTemplateName"]
            )
        return response

    
    def create_fleet(self):
        """
        """
        self.client.create_fleet(
            DryRun=False,
            TargetCapacitySpecification={
                "TotalTargetCapacity": target_capacity,
                "OnDemandTargetCapacity": 0,
                "SpotTargetCapacity": target_capacity,
                "DefaultTargetCapacityType": "spot"
                },
            LaunchTemplateConfigs=launch_template_configs,
            SpotOptions={
                "AllocationStrategy": "diversified",
                },
            )

    

ec2_client = EC2Client(sessionToken=cons.session_token_fpath)
ec2_client.delete_launch_template(launch_template)
ec2_client.create_launch_template(launch_template)

LaunchTemplateConfigs=[{"LaunchTemplateSpecification":{"LaunchTemplateName":launch_template["LaunchTemplateName"]}}]