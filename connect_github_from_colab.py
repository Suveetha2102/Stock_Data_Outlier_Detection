#Followed below steps to connect to github from colab notebook

!apt-get install git
!git config --global user.name "Suveetha2102"
!git config --global user.email "suveethamaheshkumar@gmail.com"
!git init
!git remote add origin https://github.com/Suveetha2102/stock_data_outlier_detection.git
%cd /content/stock_data_outlier_detection
!mkdir stock_outlier_detection
!mv /content/lse_final.py /content/stock_data_outlier_detection
!mv /content/connect_github_from_colab.py /content/stock_data_outlier_detection
!git add .
!git commit -m "Initial commit with code for outlier detection"
!git push https://<PAT Token>@github.com/Suveetha2102/Stock_Data_Outlier_Detection.git
