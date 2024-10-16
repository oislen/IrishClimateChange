import platform
import os
import sys
import json

met_eir_historical_data_url = 'https://www.met.ie/climate/available-data/historical-data'
stations_data_url = 'https://cli.fusio.net/cli/climate_data/webdata/StationDetails.csv'

root_dir = 'E:\\GitHub\\IrishClimateDashboard' if platform.system() == 'Windows' else '/home/ubuntu/IrishClimateDashboard'
sys.path.append(root_dir)
# set directories
data_dir = os.path.join(root_dir, 'data')
creds_data = os.path.join(root_dir, '.creds')
gis_dir = os.path.join(data_dir, "gis")
met_eireann_dir = os.path.join(data_dir, 'Met_Eireann')
bokeh_ref_data_dir = os.path.join(data_dir, "bokeh", "ref")
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
cleaned_data_dir = os.path.join(met_eireann_dir, 'cleaned_data')
stations_fpath = os.path.join(met_eireann_dir, 'ref', 'StationDetails.csv')
unittest_normal_dists_fpath = os.path.join(bokeh_ref_data_dir, "unittest_normal_dists.json")
col_options_fpath = os.path.join(bokeh_ref_data_dir, "col_options.json")
stat_options_fpath = os.path.join(bokeh_ref_data_dir, "stat_options.json")
agg_level_strftime_fpath = os.path.join(bokeh_ref_data_dir, "agg_level_strftime.json")
session_token_fpath = os.path.join(creds_data, "sessionToken.json")

# load bokeh reference data
with open(col_options_fpath) as json_file: 
    col_options = json.load(json_file)
with open(stat_options_fpath) as json_file: 
    stat_options = json.load(json_file)
with open(agg_level_strftime_fpath) as json_file: 
    date_strftime_dict = json.load(json_file)

# aws s3 constants
s3_bucket = "irishclimatedashboard"
s3_scraped_directory = "data/Met_Eireann/scraped_data"
s3_clean_directory = "data/Met_Eireann/cleaned_data"
s3_fname = "dly{station_id}.csv"