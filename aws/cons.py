import platform
import os
import sys
import json

root_dir = 'E:\\GitHub\\IrishClimateDashboard' if platform.system() == 'Windows' else '/home/ubuntu/IrishClimateDashboard'
sys.path.append(root_dir)
# set directories
data_dir = os.path.join(root_dir, 'data')
creds_dir = os.path.join(root_dir, '.creds')
aws_dir = os.path.join(root_dir, 'aws')
ec2_ref_data_dir = os.path.join(aws_dir, "ref")
session_token_fpath = os.path.join(creds_dir, "sessionToken.json")
launch_template_config_fpath = os.path.join(ec2_ref_data_dir, "launch_template_config.json")
create_fleet_config_fpath = os.path.join(ec2_ref_data_dir, "create_fleet_config.json")
run_instances_config_fpath = os.path.join(ec2_ref_data_dir, "run_instances_config.json")

# load aws ec2 references
with open(launch_template_config_fpath) as json_file: 
    launch_template_config = json.load(json_file)
with open(create_fleet_config_fpath) as json_file: 
    create_fleet_config = json.load(json_file)
with open(run_instances_config_fpath) as json_file: 
    run_instances_config = json.load(json_file)
