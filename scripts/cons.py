# load relevant libraries
import os

# set directories
root_dir = 'E:\\GitHub\\IrishClimateChange'
data_dir = os.path.join(root_dir, 'data')
census_2011_dir = os.path.join(data_dir, 'Census_2011')
census_2016_dir = os.path.join(data_dir, 'Census_2016')
met_eireann_dir = os.path.join(data_dir, 'Met_Eireann')

# set data files
master_data_fpath = os.path.join(data_dir, 'master.feather')

# set dictionary of hyperlinks to download data files
census_2011 = {'Census2011_Province_generalised20m':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_Province_generalised20m.zip',
              'Census2011_NUTS2_generalised20m':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_NUTS2_generalised20m.zip',
              'Census2011_NUTS3_generalised20m':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_NUTS3_generalised20m.zip',
              'Census2011_Admin_Counties_generalised20m':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_Admin_Counties_generalised20m.zip',
              'Census2011_Electoral_Divisions_generalised20m':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_Electoral_Divisions_generalised20m.zip',
              'Census2011_Small_Areas_generalised20m':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_Small_Areas_generalised20m.zip',
              'Census2011_Constituencies_2007':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_Constituencies_2007.zip',
              'Census2011_Constituencies_2013':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_Constituencies_2013.zip',
              'Census2011_Gaeltacht':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_Gaeltacht.zip',
              'Census2011_Local_Electoral_Areas_2008':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_Local_Electoral_Areas_2008.zip',
              'Census2011_Cities_Legal_Towns':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_Cities_Legal_Towns.zip',
              'Census2011_Settlements':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_Settlements.zip',
              'Census2011_Dioceses_generalised':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_Dioceses_generalised.zip',
              'Census2011_Dublin_Parishes_generalised':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_Dublin_Parishes_generalised.zip',
              'Census2011_Garda_Regions_Nov2013':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_Garda_Regions_Nov2013.zip',
              'Census2011_Garda_Divisions_Nov2013':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_Garda_Divisions_Nov2013.zip',
              'Census2011_Garda_Districts_Nov2013':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_Garda_Districts_Nov2013.zip',
              'Census2011_Garda_SubDistricts_Nov2013':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_Garda_SubDistricts_Nov2013.zip',
              'Census2011_Baronies':'http://census.cso.ie/censusasp/saps/boundaries/Census2011_Baronies.zip'
              }

# set dictionary of hyperlinks to download data files
census_2016 = {'Census2016_Constituencies_2017':'https://opendata.arcgis.com/datasets/862a628b73d14a86b2f46ef9506dda8b_0.zip?outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D',
               'Census2016_Electoral_Divisions_2015':'https://opendata.arcgis.com/datasets/9dcb2f00f16140bcac1610f678af6577_0.zip?outSR=%7B%22latestWkid%22%3A2157%2C%22wkid%22%3A2157%7D',
               'Census2016_Gaeltacht_2015':'https://opendata.arcgis.com/datasets/aa3980fab81f466bb67f86f045ad14f0_3.zip?outSR=%7B%22latestWkid%22%3A2157%2C%22wkid%22%3A2157%7D',
               'Census2016_Gaeltacht_Language_2015':'https://opendata.arcgis.com/datasets/2a2072b38dd64da69702b0249fc9284b_3.zip?outSR=%7B%22latestWkid%22%3A2157%2C%22wkid%22%3A2157%7D',
               'Census2016_Local_Electoral_Areas_2019':'https://opendata.arcgis.com/datasets/c85b428153724f8385257d3c9826cf43_0.zip?outSR=%7B%22latestWkid%22%3A2157%2C%22wkid%22%3A2157%7D',
               'Census2016_Province_2015':'https://opendata.arcgis.com/datasets/b1b11bee5cbe4989812fd517f5ac3039_3.zip?outSR=%7B%22latestWkid%22%3A2157%2C%22wkid%22%3A2157%7D',
               'Census2016_NUTS3_2015':'https://opendata.arcgis.com/datasets/6ecb0a452ce545a6944ae7a26a891d2b_3.zip?outSR=%7B%22latestWkid%22%3A2157%2C%22wkid%22%3A2157%7D',
               'Census2016_Settlements_2015':'https://opendata.arcgis.com/datasets/059f9de9770147a2a18c5e5d710839ad_3.zip?outSR=%7B%22latestWkid%22%3A2157%2C%22wkid%22%3A2157%7D',
               'Census2016_Small_Areas_2015':'https://opendata.arcgis.com/datasets/c85e610da1464178a2cd84a88020c8e2_3.zip?outSR=%7B%22latestWkid%22%3A2157%2C%22wkid%22%3A2157%7D'
               }

# met eireann weather data
met_eireann = {'dublin_airport':'https://cli.fusio.net/cli/climate_data/webdata/dly532.zip'}

# bokeh figure settings
FIG_SETTING = {'plot_height':800, 
               'plot_width':1400, 
               'min_border_left':50, 
               'min_border_right':50,
               'min_border_top':50, 
               'min_border_bottom': 20, 
               'tools':'pan,wheel_zoom, box_zoom,reset,save'
               }

# bokeh selctor settings
agg_level_options = ['year', 'year-month', 'month']
agg_level_default = agg_level_options[0]