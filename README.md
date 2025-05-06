#  Data Cleaning Master - Python Application   

## Project Overview  

![pic](https://orderofficefurniture.co.uk/cdn/shop/articles/Crowded_office_desk.jpg?v=1732617135&width=1600)     


The Data Cleaning Master is a Python-based tool crafted to streamline the cleaning process of datasets by managing duplicate entries, handling missing values, and delivering a polished dataset in just seconds. Designed for ease of use and strong performance, the application has been successfully tested across multiple datasets to ensure reliability and precision.

Capable of processing datasets containing thousands of rows, this tool performs rapid, error-free cleaning. It automatically saves a copy of duplicate rows, imputes missing numeric data using column averages, and removes rows with missing non-numeric values. This makes it an ideal solution for preparing data before analysis.    

## Objectives   

The key objectives of this project are:

1. Load and clean datasets in various formats (CSV and Excel).
2. Identify and remove duplicate records, while keeping a backup of these duplicates.
3. Handle missing values:
* For numeric columns: replace missing values with the column's mean.
* For non-numeric columns: remove rows containing missing values.
4. Save the cleaned dataset and provide access to both the cleaned data and duplicate records.

## Project Requirements  

* Python 3.x
* Pandas
* Numpy
* Openpyxl
* Xlrd
* OS library
* Jupyter Notebook (for testing)

## Step by Step Process  

1. Input and File Verification
The application begins by asking the user for the dataset path and dataset name.
It verifies if the path is valid and checks whether the file is in a supported format (CSV or Excel).
2. Duplicate Detection and Removal
The application checks for duplicate records in the dataset.
Duplicate records are saved as a separate file named {dataset_name}_duplicates.csv.
Duplicate rows are then removed from the main dataset.
3. Handling Missing Values
The application checks for missing values in the dataset.
For numeric columns (integer or float), missing values are replaced by the column’s mean.
For non-numeric columns, rows containing missing values are dropped.
4. Exporting Clean Data
Once cleaned, the dataset is saved as {dataset_name}_Clean_data.csv, and a message confirming successful cleaning is displayed.
5. Multiple Testing & Performance Tuning
The application has been tested with  different datasets. It consistently cleaned datasets in a matter of seconds, without errors.

## Key Features  
* Fast & Efficient: Cleans large datasets (10k+ rows) in seconds.
* Duplicate Backup: Keeps a backup of all duplicate records before removing them.
* Missing Values Handling: Automatically fills missing numeric values and drops rows with missing non-numeric values.
* User-friendly Prompts: Guides the user step by step with appropriate messages and delay prompts.
* Multiple Formats Supported: Handles CSV and Excel files seamlessly.

## Usage  

1. Run the application using a Python environment.
2. Input the dataset path and name when prompted.
3. The application will automatically clean the dataset and save the results.

``` python
python data_cleaning_master.py
```

## Final Thoughts  

The Data Cleaning Master is an efficient tool for data pre-processing. Its ability to handle large datasets, clean data accurately, and save duplicates for further inspection makes it ideal for any data science or data analysis project.







