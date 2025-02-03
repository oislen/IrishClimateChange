import argparse


def commandline_interface():
    """A commandline interface for parsing input parameters with

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
    parser.add_argument("--run_met_data", action=argparse.BooleanOptionalAction, dest="run_met_data", type=bool, default=False, help="Boolean, retrieves / web scrapes the historical met data",)
    parser.add_argument("--run_clean_data", action=argparse.BooleanOptionalAction, dest="run_clean_data", type=bool, default=False, help="Boolean, cleans and processes the scraped met data",)
    parser.add_argument("--run_master_data", action=argparse.BooleanOptionalAction, dest="run_master_data", type=bool, default=False, help="Boolean, generates the master data file from the retrieved / web scraped met data files",)
    parser.add_argument("--run_map_data", action=argparse.BooleanOptionalAction, dest="run_map_data", type=bool, default=False, help="Boolean, generates the map gis file for the bokeh dashboard app",)
    parser.add_argument("--run_points_data", action=argparse.BooleanOptionalAction, dest="run_points_data", type=bool, default=False, help="Boolean, generates the stations gis file for the bokeh dashboard app",)
    # create an output dictionary to hold the results
    input_params_dict = {}
    # extract input arguments
    args = parser.parse_args()
    # map input arguments into output dictionary
    input_params_dict["run_met_data"] = args.run_met_data
    input_params_dict["run_clean_data"] = args.run_clean_data
    input_params_dict["run_master_data"] = args.run_master_data
    input_params_dict["run_map_data"] = args.run_map_data
    input_params_dict["run_points_data"] = args.run_points_data
    return input_params_dict
