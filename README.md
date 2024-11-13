# Stock Data Outlier Detection

This project processes stock data from CSV files, selects random samples, and detects outliers using statistical methods.
Python libraries like Numpy, Pandas, Matplotlib, Seaborn has been used here

### How to Use:
1. Open the outlier_detection.py file
2. Upload in Google Colab
3. Make sure the Stock Files and Directories are saved in local
4. On running the first function "process_uploaded_files" it will ask the user to upload the file from local
5. Upload any file
6. On running the second function "detect_outliers" it will generate a final output file and download the final output file
7. Apart from that we have certain plots to understand the distribution

### Files:
- ``: - Pdf File with distribution document
- `Connect_to_github_from_Colab`: If the user hasnt connected to github from colab, this is a reference file

### Outlier Detection:
- Outliers are defined as data points that are more than 2 standard deviations from the mean of 30 randomly sampled data points.
"""
