# Use-Case : House Price Prediction

# Dataset : melb_data.csv

# The dataset can be downloaded melb_data.csv | Kaggle

# Perform the following tasks:

# 1. Load the data in dataframe (Pandas)
# 2. Handle inappropriate data
# 3. Handle the missing data
# 4. Handle the categorical data


import pandas as pd

data = pd.read_csv("D:/Development/Wipro_TalentNext_Python/datasets/melb_data.csv")


print(data.head())
print(data.info())

data = data.drop(columns=['Address']) if 'Address' in data.columns else data

num_cols = data.select_dtypes(include=['int64','float64']).columns
for col in num_cols:
    data[col].fillna(data[col].mean(), inplace=True)

cat_cols = data.select_dtypes(include=['object']).columns
for col in cat_cols:
    data[col].fillna(data[col].mode()[0], inplace=True)
    data[col] = data[col].astype('category').cat.codes

print(data.head())
print(data.info())
