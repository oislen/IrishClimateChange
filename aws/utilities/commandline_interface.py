import argparse


def commandline_interface() -> dict:
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
    parser.add_argument("--launch", action=argparse.BooleanOptionalAction, dest="launch", type=bool, default=False, help="Boolean, whether to launch a new ec2 instance",)
    parser.add_argument("--terminate", action=argparse.BooleanOptionalAction, dest="terminate", type=bool, default=False, help="Boolean, whether to terminate all running ec2 instances",)
    # create an output dictionary to hold the results
    input_params_dict = {}
    # extract input arguments
    args = parser.parse_args()
    # map input arguments into output dictionary
    input_params_dict["launch"] = args.launch
    input_params_dict["terminate"] = args.terminate
    return input_params_dict
