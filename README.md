**📈 Stock Data Outlier Detection**

Analyze stock price data, detect outliers, and visualize distributions with ease! This project allows you to process stock data from CSV files, sample data points randomly, and identify outliers using robust statistical methods. The project uses powerful Python libraries like **NumPy, Pandas, Matplotlib, and Seaborn** to simplify data analysis.

**🚀 Features**

- **Random Sampling**: Efficiently select random stock data points from CSV files.  
- **Outlier Detection**: Identify outliers based on 2-standard deviation thresholds.  
- **Distribution Visualization**: Generate visual plots to understand data distribution.

**🛠️ How to Use**  

- Open `outlier_detection.py` in Google Colab.  
- Ensure your stock data files are saved locally and are in CSV format.  
- Run the first function, `process_uploaded_files`, which will prompt you to upload your file.  
- Upload any CSV file containing stock data.  
- Run the second function, `detect_outliers`, to generate the final output file, highlighting any detected outliers.  
- View and download output files and data distribution plots.

**📁 Project Files**  

- `outlier_detection.py` – Core Python script for detecting outliers in stock data.  
- `Outlier_Code_PDFFormat` – PDF version of the code, ideal for reference and documentation.  
- `Connect_to_github_from_Colab` – Reference file for connecting Colab to GitHub.  
- `kde_distribution_for_30_sample.png` – KDE plot for 30 sampled data points, visualizing distribution.  
- `kde_distribution_for_population_data_all_stock_files.png` – KDE plot showing distribution across all stock data files.  
- `Sample_Output_Outlier_Detection.csv` – Example output file with outlier-detected data.  


**📊 Outlier Detection Process** 

Outliers are identified as any data points exceeding **2 standard deviations** from the sample mean, based on a random selection of 30 stock prices. This method allows you to detect unusual price changes effectively, enabling data-driven decision-making.


**📘 Requirements**  

To run this project, you’ll need:  

- `Google Colab` (or a similar Jupyter Notebook environment)  
- Python libraries: `NumPy`, `Pandas`, `Matplotlib`, `Seaborn`


**🔍 Visual Insights**

Use included plots to visualize data distributions:  

- **KDE Plot for Sample Data:** Understand how the selected sample data is distributed.
- **KDE Plot for Population Data:** View the overall distribution for a comprehensive data overview.  
