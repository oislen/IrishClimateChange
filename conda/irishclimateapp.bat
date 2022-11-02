:: create and activate new environment
call conda env remove --name ica
call conda create --name ica python --yes
call conda activate ica

:: update conda version
call conda update -n base conda --yes

:: install required data processing packages
call conda install -c conda-forge numpy --yes
call conda install -c conda-forge pyarrow --yes
call conda install -c conda-forge pyexcel --yes
call conda install -c conda-forge openpyxl --yes
call conda install -c conda-forge pandas --yes
call conda install -c conda-forge geopandas --yes

:: install required visualisation packages
call conda install -c conda-forge colour --yes
call conda install -c conda-forge matplotlib --yes
call conda install -c conda-forge seaborn --yes
call conda install -c conda-forge bokeh --yes

:: install boto3 for aws connection
call conda install -c conda-forge boto3

:: install jupyterlab
call conda install -c conda-forge ipywidgets --yes
call conda install -c conda-forge jupyterlab --yes

:: export environment to .yml file
call conda env export > environment.yml

:: deactivate new environment
call conda deactivate