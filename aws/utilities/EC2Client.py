import io
import boto3
import json
import logging
import pandas as pd
from typing import Union
from beartype import beartype
import cons

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
        """
        # create ec2 launch template
        response = self.client.create_launch_template(**launch_template_config)
        return response
    
    def delete_launch_template(self, launch_template_config):
        """
        """
        # delete ec2 launch template
        response = self.client.delete_launch_template(DryRun=launch_template_config["DryRun"], LaunchTemplateName=launch_template_config["LaunchTemplateName"])
        return response
    
    def create_fleet(self, create_fleet_config):
        """
        """
        response = self.client.create_fleet(**create_fleet_config)
        return response
    
    def describe_fleets(self):
        """
        """
        response = self.client.describe_fleets()
        return response
    
    def delete_fleets(self, FleetIds=[], TerminateInstances=False):
        """
        """
        response = self.client.delete_fleets(FleetIds=FleetIds, TerminateInstances=TerminateInstances)
        return response
    
    def run_instances(self, run_instances_config):
        """
        """
        response = self.client.run_instances(**run_instances_config)
        return response
    
    def stop_instances(self, InstanceIds=[]):
        """
        """
        response = self.client.stop_instances(InstanceIds=InstanceIds)
        return response
    
    def terminate_instances(self, InstanceIds=[]):
        """
        """
        response = self.client.terminate_instances(InstanceIds=InstanceIds)
        return response
    
    def describe_instances(self, InstanceIds=[], Filters=[], MaxResults=20):
        """
        """
        response = self.client.describe_instances(InstanceIds=InstanceIds, Filters=Filters, MaxResults=MaxResults)
        return response


ec2_client = EC2Client(sessionToken=cons.session_token_fpath)
ec2_client.delete_launch_template(cons.launch_template_config)
ec2_client.create_launch_template(cons.launch_template_config)
#ec2_client.create_fleet(cons.create_fleet_config)
ec2_client.run_instances(cons.run_instances_config)
InstanceIds=["i-0dfe7150a875c4d45"]
ec2_client.stop_instances(InstanceIds=InstanceIds)
ec2_client.terminate_instances(InstanceIds=InstanceIds)
ec2_client.describe_instances()

# Issues with Fleets
#ec2_client.client.describe_capacity_reservation_fleets()
#ec2_client.client.cancel_capacity_reservation_fleets(CapacityReservationFleetIds=['9f3e14aa-26f2-4e36-b635-938d752a2bc5'])
ec2_client.client.describe_fleets()
#ec2_client.client.describe_fleet_instances()
#ec2_client.client.delete_fleets(FleetIds=["fleet-4605729e-1523-4f9e-add0-7d6229915c25"], TerminateInstances=True)
#ec2_client.client.delete_fleets(FleetIds=["fleet-b9d79eb1-dce2-4649-b321-f2158039454a"], TerminateInstances=True)
#ec2_client.client.delete_fleets(FleetIds=["fleet-24040711-8eb0-42dd-b80f-5e6b54b200b0"], TerminateInstances=True)