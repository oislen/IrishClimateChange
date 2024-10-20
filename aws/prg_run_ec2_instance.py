import logging
import cons
from utilities.EC2Client import EC2Client
from utilities.commandline_interface import commandline_interface
from beartype import beartype

@beartype
def run_ec2_instance(launch:bool=False, terminate:bool=False):
    """

    Parameters
    ----------

    Returns
    -------
    """
    logging.info("Creating EC2 client.")
    # create EC2 client
    ec2_client = EC2Client(sessionToken=cons.session_token_fpath)
    # if launch ec2 instance
    if launch:
        logging.info("Launching EC2 instance.")
        # delete any existing launch template
        ec2_client.delete_launch_template(cons.launch_template_config)
        # create a new launch template
        ec2_client.create_launch_template(cons.launch_template_config)
        # start ec2 instance
        ec2_client.run_instances(cons.run_instances_config)
        # list any instances
        Filters=[{"Name":"instance-state-name","Values":["running","pending"]}]
        response = ec2_client.describe_instances(Filters=Filters)
        logging.info(response)
    # if terminating ec2 instance
    if terminate:
        logging.info("Terminating EC2 instances.")
        # list any running instances
        Filters=[{"Name":"instance-state-name","Values":["running"]}]
        response = ec2_client.describe_instances(Filters=Filters)
        # set instance ids to shut down
        InstanceIds=[instance["InstanceId"] for reservation in response["Reservations"] for instance in reservation["Instances"]]
        if InstanceIds != []:
            # stop instance
            ec2_client.stop_instances(InstanceIds=InstanceIds)
            # terminate instance
            ec2_client.terminate_instances(InstanceIds=InstanceIds)
        # list any instances
        response = ec2_client.describe_instances(Filters=Filters)
        logging.info(response)

if __name__ == "__main__":

    # set up logging
    lgr = logging.getLogger()
    lgr.setLevel(logging.INFO)
    # handle input parameters
    input_params_dict = commandline_interface()
    # run main programme
    run_ec2_instance(
        launch=input_params_dict["launch"],
        terminate=input_params_dict["terminate"]
        )