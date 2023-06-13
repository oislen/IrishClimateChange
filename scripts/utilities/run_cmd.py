from subprocess import Popen


def run_cmd(cmd, cwd, shell=True):
    """Executes a given os command in the commandline

    Parameters
    ----------
    cmd : str
        The os command to be executed
    cwd : str
        The working directory to run the os command from
    shell : bool
        Whether to  run the os command through shell, default is True

    Returns
    -------

    """
    # run os command
    p = Popen(cmd, cwd=cwd, shell=shell)
    stdout, stderr = p.communicate()
