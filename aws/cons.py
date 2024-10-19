import platform
import os
import sys
import json

root_dir = 'E:\\GitHub\\IrishClimateDashboard' if platform.system() == 'Windows' else '/home/ubuntu/IrishClimateDashboard'
sys.path.append(root_dir)
# set directories
data_dir = os.path.join(root_dir, 'data')
creds_data = os.path.join(root_dir, '.creds')
session_token_fpath = os.path.join(creds_data, "sessionToken.json")

# aws ec2 constants
