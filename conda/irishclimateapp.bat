:: create and activate new environment
call conda deactivate
call conda env remove --name irishclimateapp
call conda create --name irishclimateapp python --yes
call conda activate irishclimateapp

:: update conda version
call conda update -n base conda --yes

:: install relevant libraries
call pip install -r ..\requirements.txt

:: export environment to .yml file
call conda env export > irishclimateapp.yml
