# Stock Data Outlier Detection

This project processes stock data from CSV files, selects random samples, and detects outliers using statistical methods.

### How to Use:
1. Open the LSE_Final.py file
2. Upload in Google Colab
3. Make sure you have the Stock Files and Directories in local
4. On running the first function "process_uploaded_files" it will ask you to upload the file from local
5. Upload any file
6. On running the second function "detect_outliers" it will generate a final output file and download the final output file
7. Apart from that we have certain plots to understand the distribution

### Files:
- `your_script_name.py`: Main script to detect outliers.
- `sample_input.csv`: Example CSV data.

### Outlier Detection:
- Outliers are defined as data points that are more than 2 standard deviations from the mean of 30 randomly sampled data points.
"""
