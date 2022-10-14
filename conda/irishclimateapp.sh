# create and activate new environment
conda env remove --name ica
conda create --name ica python --yes
conda activate ica

# update conda version
conda update -n base conda --yes

# install required data processing packages
conda install -c conda-forge numpy --yes
conda install -c conda-forge pandas --yes
conda install -c conda-forge geopandas --yes

# install required visualisation packages
conda install -c conda-forge matplotlib --yes
conda install -c conda-forge seaborn --yes
conda install -c conda-forge bokeh --yes

# install jupyterlab
conda install -c conda-forge jupyterlab --yes

# deactivate new environment
conda deactivate