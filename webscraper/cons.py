import platform
import os

free_images_url = 'https://www.met.ie/climate/available-data/historical-data'

root_dir = 'E:\\GitHub\\IrishClimateDashboard' if platform.system() == 'Windows' else '/home/ubuntu/IrishClimateDashboard'
# set directories
data_dir = os.path.join(root_dir, 'data')
met_eireann_dir = os.path.join(data_dir, 'Met_Eireann')
scraped_data_dir = os.path.join(met_eireann_dir, 'scraped_data')
stations_fpath = os.path.join(met_eireann_dir, 'ref', 'StationDetails.csv')