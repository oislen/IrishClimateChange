# reset premission for the /opt /dev /run and /sys directories
ls -larth /.
sudo chmod -R 777 /opt /dev /run /sys/fs/cgroup
sudo chmod 775 /var/run/screen
ls -larth /.
# update overcommit memory setting
cat /proc/sys/vm/overcommit_memory
echo 1 | sudo tee /proc/sys/vm/overcommit_memory

# update os
sudo yum update -y
# install required base software
sudo yum install -y htop vim tmux dos2unix docker git
# remove unneed dependencies
sudo yum autoremove

# pull git repo
sudo mkdir /home/ubuntu
sudo git clone https://github.com/oislen/IrishClimateDashboard.git --branch v0.0.0 /home/ubuntu/IrishClimateDashboard
cd /home/ubuntu/IrishClimateDashboard
# create python environment
sudo yum install -y python3 python3-pip
python3 -m pip install -v -r /home/ubuntu/IrishClimateDashboard/requirements.txt
# run bokeh app
bokeh serve /home/ubuntu/IrishClimateDashboard/dashboard/bokeh_dash_app.py --allow-websocket-origin=*.*.*.*:5006
# http://34.243.42.137:5006/bokeh_dash_app
