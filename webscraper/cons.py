import platform
import os

free_images_url = 'https://www.met.ie/climate/available-data/historical-data'

root_dir = 'E:\\GitHub\\IrishClimateDashboard' if platform.system() == 'Windows' else '/home/ubuntu/IrishClimateDashboard'
# set directories
data_dir = os.path.join(root_dir, 'data')
gis_dir = os.path.join(data_dir, "gis")
met_eireann_dir = os.path.join(data_dir, 'Met_Eireann')
master_data_fpath = os.path.join(data_dir, 'master.feather')
preaggregate_data_fpath = os.path.join(data_dir, "preaggregate_data.pickle")
bokeh_line_data_fpath = os.path.join(data_dir, "bokeh_line_data.pickle")
bokeh_map_data_fpath = os.path.join(data_dir, "bokeh_map_data.pickle")
rep_counties_fpath = os.path.join(data_dir, 'gis', 'arch', 'Counties_-_OSi_National_Statutory_Boundaries_-_2019', 'Counties___OSi_National_Statutory_Boundaries_.shp')
ni_counties_fpath = os.path.join(data_dir, 'gis', 'arch', 'northern_ireland_counties', 'northern_ireland_counties.shp')
counties_data_fpath = os.path.join(gis_dir, "counties.shp")
map_data_fpath = os.path.join(gis_dir, "map_data.pickle")
points_data_fpath = os.path.join(gis_dir, "points_data.pickle")
scraped_data_dir = os.path.join(met_eireann_dir, 'scraped_data')
stations_fpath = os.path.join(met_eireann_dir, 'ref', 'StationDetails.csv')

date_strftime_dict = {'year':'%Y', 'year-month':'%Y-%m', 'month':'%m'}
col_options = ['maxtp', 'mintp', 'gmin', 'soil', 'wdsp', 'sun', 'evap', 'rain']
stat_options = ['mean', 'median', 'max', 'min', 'var', 'std', 'sum']