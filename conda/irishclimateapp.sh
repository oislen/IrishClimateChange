# create and activate new environment
conda deactivate
conda env remove --name irishclimateapp
conda create --name irishclimateapp python --yes
conda activate irishclimateapp

# update conda version
conda update -n base conda --yes

# install relevant libraries
pip install -r ../requirements.txt

# export environment to .yml file
conda env export > irishclimateapp.yml
