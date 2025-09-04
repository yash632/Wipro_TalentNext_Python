# Use Case : Diabetes Prediction

# Perform Exploratory Data Analysis for the Diabetes Dataset.

# Dataset : Diabetes.csv

# The dataset can be downloaded from https://www.kaggle.com/datasets

# Perform the following tasks

# 1. Load the data in the DataFrame
# 2. Data Pre-processing
# 3. Handle the Categorical Data
# 4. Perform Uni-variate Analysis
# 5. Perform Bi-variate Analysis


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("D:/Development/Wipro_TalentNext_Python/datasets/diabetes.csv")

num_cols = data.select_dtypes(include=['int64','float64']).columns
for col in num_cols:
    data[col].fillna(data[col].mean(), inplace=True)

cat_cols = data.select_dtypes(include=['object']).columns
for col in cat_cols:
    data[col].fillna(data[col].mode()[0], inplace=True)
    data[col] = data[col].astype('category').cat.codes

print(data.head())
print(data.info())
print(data.describe())

for col in num_cols:
    plt.figure()
    sns.histplot(data[col], kde=True)
    plt.title(f'Uni-variate Analysis: {col}')
    plt.show()

for col1 in num_cols:
    for col2 in num_cols:
        if col1 != col2:
            plt.figure()
            sns.scatterplot(x=data[col1], y=data[col2])
            plt.title(f'Bi-variate Analysis: {col1} vs {col2}')
            plt.show()

