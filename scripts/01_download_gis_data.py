# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 18:24:29 2020

@author: oislen
"""

# import relevent libraries
# tmqd
import cons
from utilities.url_data_download import url_data_download

# TODO: could use google map api https://docs.bokeh.org/en/latest/docs/user_guide/geo.html
# TODO: https://developers.google.com/maps/documentation/javascript/get-api-key

# https://www.cso.ie/en/census/census2011boundaryfiles/
# https://www.cso.ie/en/census/census2016reports/census2016smallareapopulationstatistics/
# https://www.met.ie/climate/available-data/historical-data

#-- Download Census Data --#

# run download function
#url_data_download(links_dict = cons.census_2011, data_dir = cons.census_2011_dir)
#url_data_download(links_dict = cons.census_2016, data_dir = cons.census_2016_dir)
url_data_download(links_dict = cons.met_eireann, data_dir = cons.met_eireann_dir)