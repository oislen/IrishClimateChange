from subprocess import Popen

def run_bokeh_server_apps(cmd, cwd, shell=True):
    """"""
    # run bokeh application in background via execution command
    p = Popen(cmd, cwd=cwd, shell=shell)
    stdout, stderr = p.communicate()