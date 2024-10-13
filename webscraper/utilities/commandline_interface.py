import argparse


def commandline_interface():
    """A commandline interface for parsing input parameters with

    Windows
    python IrishClimateDashboard\\webscraper\\prg_webscraper_data.py --retrieve_data --generate_master_data --generate_preaggregated_data --generate_counties_data --generate_stations_data

    Linux
    python3 IrishClimateDashboard/webscraper/prg_webscraper_data.py --retrieve_data --generate_master_data --generate_preaggregated_data --generate_counties_data --generate_stations_data

    Parameters
    ----------

    Returns
    -------
    dict
        A dictionary of key, value pairs where the values are parsed input parameters
    """
    # define argument parser object
    parser = argparse.ArgumentParser(description="Execute Random TeleCom Data Programme.")
    # add input arguments
    parser.add_argument("--retrieve_data", action=argparse.BooleanOptionalAction, dest="retrieve_data", type=bool, default=False, help="Boolean, retrieves / web scrapes the historical met data",)
    parser.add_argument("--generate_master_data", action=argparse.BooleanOptionalAction, dest="generate_master_data", type=bool, default=False, help="Boolean, generates the master data file from the retrieved / web scraped met data files",)
    parser.add_argument("--generate_preaggregated_data", action=argparse.BooleanOptionalAction, dest="generate_preaggregated_data", type=bool, default=False, help="Boolean, preaggreates the master data file into various date levels for the bokeh dashboard app",)
    parser.add_argument("--generate_counties_data", action=argparse.BooleanOptionalAction, dest="generate_counties_data", type=bool, default=False, help="Boolean, generates the counties gis file for the bokeh dashboard app",)
    parser.add_argument("--generate_stations_data", action=argparse.BooleanOptionalAction, dest="generate_stations_data", type=bool, default=False, help="Boolean, generates the stations gis file for the bokeh dashboard app",)
    # create an output dictionary to hold the results
    input_params_dict = {}
    # extract input arguments
    args = parser.parse_args()
    # map input arguments into output dictionary
    input_params_dict["retrieve_data"] = args.retrieve_data
    input_params_dict["generate_master_data"] = args.generate_master_data
    input_params_dict["generate_preaggregated_data"] = args.generate_preaggregated_data
    input_params_dict["generate_counties_data"] = args.generate_counties_data
    input_params_dict["generate_stations_data"] = args.generate_stations_data
    return input_params_dict
