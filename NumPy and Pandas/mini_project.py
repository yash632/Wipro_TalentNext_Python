# Use Case: Perform the Outlier detection for the given dataset i.e.
# datasetExample

# Dataset : datasetExample.csv

# Perform the following task

# . Load the data in the DataFrame.
# . Detection of Outliers

import pandas as pd

df = pd.read_csv("D:\Development\Wipro_TalentNext_Python\datasets\startups.csv")  

print("First 5 rows of dataset:")
print(df.head())

def detect_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers, lower_bound, upper_bound

outliers, lower, upper = detect_outliers_iqr(df, "Profit")

print(f"\nOutliers in Profit column (using IQR):")
print(outliers)

print(f"\nLower Bound: {lower}, Upper Bound: {upper}")
