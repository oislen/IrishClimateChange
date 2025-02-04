import os
import re
import sys
import json
import pyarrow as pa

met_eir_historical_data_url = 'https://www.met.ie/climate/available-data/historical-data'
stations_data_url = 'https://cli.fusio.net/cli/climate_data/webdata/StationDetails.csv'

root_dir_re_match = re.findall(string=os.getcwd(), pattern="^.+IrishClimateDashboard")
root_dir = root_dir_re_match[0] if len(root_dir_re_match) > 0 else os.path.join(".", "IrishClimateDashboard")
sys.path.append(root_dir)
# set directories
data_dir = os.path.join(root_dir, 'data')
creds_dir = os.path.join(root_dir, '.creds')
webscraper_dir = os.path.join(root_dir, 'webscraper')
dashboard_dir = os.path.join(root_dir, 'dashboard')
gis_dir = os.path.join(data_dir, "gis")
met_eireann_dir = os.path.join(data_dir, 'Met_Eireann')
bokeh_ref_data_dir = os.path.join(dashboard_dir, "ref")
webscraper_ref_data_dir = os.path.join(webscraper_dir, "ref")
master_data_fpath = os.path.join(data_dir, 'master.parquet')
preaggregate_data_fpath = os.path.join(data_dir, "preaggregate_data.parquet")
bokeh_line_data_fpath = os.path.join(data_dir, "bokeh_line_data.pickle")
bokeh_map_data_fpath = os.path.join(data_dir, "bokeh_map_data.pickle")
rep_counties_fpath = os.path.join(data_dir, 'gis', 'arch', 'Counties_-_OSi_National_Statutory_Boundaries_-_2019', 'Counties___OSi_National_Statutory_Boundaries_.shp')
ni_counties_fpath = os.path.join(data_dir, 'gis', 'arch', 'northern_ireland_counties', 'northern_ireland_counties.shp')
counties_data_fpath = os.path.join(gis_dir, "counties.shp")
map_data_fpath = os.path.join(gis_dir, "map_data.parquet")
points_data_fpath = os.path.join(gis_dir, "points_data.parquet")
scraped_data_dir = os.path.join(met_eireann_dir, 'scraped_data')
cleaned_data_dir = os.path.join(met_eireann_dir, 'cleaned_data')
stations_fpath = os.path.join(met_eireann_dir, 'StationDetails.csv')
unittest_normal_dists_fpath = os.path.join(bokeh_ref_data_dir, "unittest_normal_dists.json")
col_options_fpath = os.path.join(bokeh_ref_data_dir, "col_options.json")
stat_options_fpath = os.path.join(bokeh_ref_data_dir, "stat_options.json")
agg_level_strftime_fpath = os.path.join(bokeh_ref_data_dir, "agg_level_strftime.json")
cleaned_data_cols_fpath = os.path.join(webscraper_ref_data_dir, "cleaned_data_cols.json")
session_token_fpath = os.path.join(creds_dir, "sessionToken.json")

# load bokeh reference data
with open(col_options_fpath) as json_file: 
    col_options = json.load(json_file)
with open(stat_options_fpath) as json_file: 
    stat_options = json.load(json_file)
with open(agg_level_strftime_fpath) as json_file: 
    date_strftime_dict = json.load(json_file)
with open(cleaned_data_cols_fpath) as json_file: 
    cleaned_data_cols = json.load(json_file)

# aws s3 constants
s3_bucket = "irishclimatedashboard"
s3_scraped_directory = "data/Met_Eireann/scraped_data"
s3_clean_directory = "data/Met_Eireann/cleaned_data"
s3_fname = "dly{station_id}.csv"

# create pyarrow schema for cleaned data
cleaned_data_pa_schema = pa.schema([
    pa.field("id", pa.uint64(), nullable=False),
    pa.field("county", pa.string(), nullable=False),
    pa.field("station", pa.string(), nullable=False),
    pa.field("open_year", pa.uint16(), nullable=False),
    pa.field("close_year", pa.uint16(), nullable=True),
    pa.field("height(m)", pa.uint32(), nullable=False),
    pa.field("easting", pa.uint64(), nullable=False),
    pa.field("northing", pa.uint64(), nullable=False),
    pa.field("latitude", pa.float64(), nullable=False),
    pa.field("longitude", pa.float64(), nullable=False),
    pa.field("maxtp", pa.float64(), nullable=True),
    pa.field("mintp", pa.float64(), nullable=True),
    pa.field("gmin", pa.float64(), nullable=True),
    pa.field("rain", pa.float64(), nullable=True),
    pa.field("wdsp", pa.float64(), nullable=True),
    pa.field("soil", pa.float64(), nullable=True),
    pa.field("sun", pa.float64(), nullable=True),
    pa.field("evap", pa.float64(), nullable=True),
    pa.field("glorad", pa.float64(), nullable=True),
    pa.field("date", pa.date64(), nullable=False),
])