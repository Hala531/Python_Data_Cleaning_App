#!/usr/bin/env python
# coding: utf-8

# ## Data cleaning app 

# Requirements : Please create a Python application  that can take datasets and clean the data 

# * It should ask for datasets path and name
# * It should check number of Duplicates and remove all the duplicates
# * it should keep a copy of all the duplicates
# * it should check for missing values
# * if any column that is numeric, it should replace nulls with mean else it should drop those rows
# * t end it should save the data as clean_data
# * it should return duplicate records, clean_data

# In[1]:


pip list


# In[3]:


get_ipython().system('pip install openpyxl')


# In[5]:


get_ipython().system('pip install xlrd')


# **importing dependencies** 

# In[8]:


import pandas as pd 
import numpy as np 
import time 
import openpyxl 
import xlrd 
import os 
import random 


# **checking if the path exists**

# In[138]:


def data_cleaning_master(data_path, data_name):
    print("thank you for giving the details") 
    sec = random.randint(1,4)  #generating random number 
    #print delay message 
    print(f"please wait for {sec} seconds ! checking file path ")
    time.sleep(sec)
    #first we wanna check f the path is correct or not 
    if not  os.path.exists(data_path) : #if the path doesn't exist 
        print("please enter correct path!") 
        return
    else: 
    #checking the file type 
        if data_path.endswith('.csv') :
            Print("dataset is csv")  
            data = pd.read_csv(data_path, encoding = 'utf-8', errors = 'ignore')
        elif data_path.endswith('.xlsx') :
            print('dataset is xlsx')
            data = pd.read_excel(data_path)
        else: 
            print("unkown file type") 
            return 

    #print delay message 
    print(f"please wait for {sec} seconds! checking total columns and rows")
    time.sleep(sec)
    #showing number of records 
    print(f"Dataset contains total rows: {data.shape[0]} \n Total colums : {data.shape[1]}")  
    
    #start cleaning 
    #print delay message 
    print(f"please wait for {sec} seconds! checking duplicates")
    time.sleep(sec)
    ## checking duplicates 
    duplicates = data.duplicated() 
    total_duplicate = data.duplicated().sum()
    print(f"Datasets has total duplicated records: {total_duplicate}")
    #print delay message 
    print(f"please wait for {sec} seconds! saving total duplicates")
    time.sleep(sec)
    
    #saving the duplicates 
    if total_duplicate > 0 : 
        duplicate_rows = data[duplicates] 
        duplicate_rows.to_csv(f'{data_name}_duplicates.csv', index= None)
    #deleting duplicates 
    df = data.drop_duplicates()  
    #print delay message 
    print(f"please wait for {sec} seconds ! checking for missing values !")
    time.sleep(sec)
    
    #finding missing values 
    total_missing_values = df.isnull().sum().sum()
    missing_values_columns = df.isnull().sum() 
    print (f"Dataset has total missing value : {total_missing_values}") 
    print(f"Dataset contains missing values by columns \n{missing_values_columns}")
    #dealing with missing values 
    #if the column data type is int or float i want to replace NA with the mean 
    columns = df.columns 
    #first i want to check all the columns and their data types  
    #fillna 'int and float'
    #dropna 'any object type' 

    #print delay message 
    print(f"please wait for {sec} seconds ! cleaning dataset")
    time.sleep(sec)
    columns = df.columns
    for col in columns:
        if df[col].dtype in (float, int) : #if all the columns are float or int
           df.loc[:, col] = df[col].fillna(df[col].mean()) #then fill with the mean 
        else:
        #dropping all rows with missing values 
            df = df.dropna(subset = [col])
    
    #data is cleaned 

    #print delay message 
    print (f"please wait for {sec} seconds ! Exporting Dataset ")
    time.sleep(sec)
    print(f"congrats, data set is cleaned!  \nNumber of rows : {df.shape[0]} Number of columns: {df.shape[1]}")
    #saving the clean dataset  
    df.to_csv(f'{data_name}clean_data.csv', index= False)
    print("Dataset is saved!") 
if __name__ == "__main__": 
    print("welcome to data cleaning master !")
    #ask path and file name 
    
    data_path = input("please enter dataset path")
    data_name = input("please enter dataset name")
    #calling the function 
    data_cleaning_master(data_path, data_name)


# In[138]:


def data_cleaning_master(data_path, data_name):
    print("thank you for giving the details") 
    sec = random.randint(1,4)  #generating random number 
    #print delay message 
    print(f"please wait for {sec} seconds ! checking file path ")
    time.sleep(sec)
    #first we wanna check f the path is correct or not 
    if not  os.path.exists(data_path) : #if the path doesn't exist 
        print("please enter correct path!") 
        return
    else: 
    #checking the file type 
        if data_path.endswith('.csv') :
            Print("dataset is csv")  
            data = pd.read_csv(data_path, encoding = 'utf-8', errors = 'ignore')
        elif data_path.endswith('.xlsx') :
            print('dataset is xlsx')
            data = pd.read_excel(data_path)
        else: 
            print("unkown file type") 
            return 

    #print delay message 
    print(f"please wait for {sec} seconds! checking total columns and rows")
    time.sleep(sec)
    #showing number of records 
    print(f"Dataset contains total rows: {data.shape[0]} \n Total colums : {data.shape[1]}")  
    
    #start cleaning 
    #print delay message 
    print(f"please wait for {sec} seconds! checking duplicates")
    time.sleep(sec)
    ## checking duplicates 
    duplicates = data.duplicated() 
    total_duplicate = data.duplicated().sum()
    print(f"Datasets has total duplicated records: {total_duplicate}")
    #print delay message 
    print(f"please wait for {sec} seconds! saving total duplicates")
    time.sleep(sec)
    
    #saving the duplicates 
    if total_duplicate > 0 : 
        duplicate_rows = data[duplicates] 
        duplicate_rows.to_csv(f'{data_name}_duplicates.csv', index= None)
    #deleting duplicates 
    df = data.drop_duplicates()  
    #print delay message 
    print(f"please wait for {sec} seconds ! checking for missing values !")
    time.sleep(sec)
    
    #finding missing values 
    total_missing_values = df.isnull().sum().sum()
    missing_values_columns = df.isnull().sum() 
    print (f"Dataset has total missing value : {total_missing_values}") 
    print(f"Dataset contains missing values by columns \n{missing_values_columns}")
    #dealing with missing values 
    #if the column data type is int or float i want to replace NA with the mean 
    columns = df.columns 
    #first i want to check all the columns and their data types  
    #fillna 'int and float'
    #dropna 'any object type' 

    #print delay message 
    print(f"please wait for {sec} seconds ! cleaning dataset")
    time.sleep(sec)
    columns = df.columns
    for col in columns:
        if df[col].dtype in (float, int) : #if all the columns are float or int
           df.loc[:, col] = df[col].fillna(df[col].mean()) #then fill with the mean 
        else:
        #dropping all rows with missing values 
            df = df.dropna(subset = [col])
    
    #data is cleaned 

    #print delay message 
    print (f"please wait for {sec} seconds ! Exporting Dataset ")
    time.sleep(sec)
    print(f"congrats, data set is cleaned!  \nNumber of rows : {df.shape[0]} Number of columns: {df.shape[1]}")
    #saving the clean dataset  
    df.to_csv(f'{data_name}clean_data.csv', index= False)
    print("Dataset is saved!") 
if __name__ == "__main__": 
    print("welcome to data cleaning master !")
    #ask path and file name 
    
    data_path = input("please enter dataset path")
    data_name = input("please enter dataset name")
    #calling the function 
    data_cleaning_master(data_path, data_name)


# In[ ]:





# In[ ]:





# In[62]:





# In[70]:




