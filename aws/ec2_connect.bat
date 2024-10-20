:: set EC2 login info
SET EC2_USER=ec2-user
SET EC2_PEM_FPATH="C:\Users\oisin\.aws\kaggle.pem"
SET EC2_CREDS_FDIR=E:\GitHub\IrishClimateDashboard\.creds
SET EC2_SETUP_FPATH=E:\GitHub\IrishClimateDashboard\aws\linux_docker_setup.sh
SET EC2_DNS_FPATH=%EC2_CREDS_FDIR%\ec2_dns

:: enable delyaed expansion to allow parsing of the %EC2_DNS_FPATH% file
SETLOCAL ENABLEDELAYEDEXPANSION
:: loop over %EC2_DNS_FPATH% lines and assign to variable
FOR /F "tokens=* USEBACKQ" %%F IN (`type %EC2_DNS_FPATH%`) DO (
    SET EC2_DNS!=%%F
)
:: scp docker file and linuc setup shell script to EC2 home
:: call scp -i %EC2_PEM_FPATH% %EC2_SETUP_FPATH% %EC2_USER%@%EC2_DNS%:~/linux_docker_setup.sh
:: ssh to EC2
call ssh -i %EC2_PEM_FPATH% %EC2_USER%@%EC2_DNS%
ENDLOCAL