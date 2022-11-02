# question 1 What is the result of the following code?

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
df.apply(lambda x: x.max() - x.min())
print(df.columns)

#question 2 - Download a csv file from 
# https://stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2022-quarter/Download-data/business-employment-data-june-2022-quarter-csv.zip 
# and load it into a pandas dataframe. How many rows and columns are there?
import requests
import os

# Load CSV
def download_csv(url):
    r = requests.get(url)
    with open('business.csv', 'wb') as f:
        f.write(r.content)

if not os.path.exists('business.csv'):
    download_csv('https://stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2022-quarter/Download-data/business-employment-data-june-2022-quarter-csv.zip')

df = pd.read_csv('business.csv')

print(df)
row_count = len(df)
print("Number of rows:", row_count)
col_count = len(df.columns)
print("Number of columns:", col_count)

#question 3
# What method can be used to get the number of non-NA values in a pandas dataframe?
#Options to choose from
# A. df.count()

# B. df.na_count()

# C. df.na_values()

# D. df.na_count()

print("The method is (df.count()) on option  A")


#question 4 Create a dataframe with 10 rows and 3 columns, 
# where the values are random numbers between 1 and 10 (inclusive). 
#Then, replace all values greater than 5 with the value 10.

import random 

df = pd.DataFrame(np.random.randint(0,11, size=(10, 3)), columns=['col1', 'col2', 'col3'])
df = df.replace(['6', '7', '8', '9'], '10')
print(df)


#question 5 - create a dataframe from this link 
#https://jsonplaceholder.typicode.com/albums

album = requests.get("https://jsonplaceholder.typicode.com/albums").json()

df = pd.DataFrame(album)

print(df.head())


