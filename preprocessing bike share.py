import numpy as np
import glob
import os
import pandas as pd
from pandas import Series, DataFrame

# specify the folder conatining the 2023 csv files
bike2023_folder_path = r'C:\Users\Elliot\Downloads\bikeshare-ridership-2023\bikeshare-ridership-2023'

# this will use glob to find all csv files in the bike2023 folder
csv_files2023 = glob.glob(os.path.join(bike2023_folder_path, '*.csv'))

dataframes2023 = []                 # this will hold the data from each csv file

for file in csv_files2023:
    print(f'Reading file: {file}')  # Print the current file being read (for debugging)
    df = pd.read_csv(file, encoding='cp1252')     # reads the file and stores it in a pandas dataframe, encoding = "latin1" since the csv contained characters not compatible with utf-8
    dataframes2023.append(df)       # append the DataFrame to the list

combined2023data = pd.concat(dataframes2023)    #pd.concat() combines all DataFrames in a list into a single DataFrame

# we will now do the same thing for 2024 data

bike2024_folder_path = r'C:\Users\Elliot\Downloads\bikeshare-ridership-2024'

csv_files2024 = glob.glob(os.path.join(bike2024_folder_path, '*.csv'))

dataframes2024 = []

for file in csv_files2024:
    print(f'Reading file: {file}')
    df = pd.read_csv(file, encoding='cp1252')
    dataframes2024.append(df)

combined2024data = pd.concat(dataframes2024)

combined2023data.head()