# 1.
# Cat Hands-on Assignment
# Perform Data Preprocessing on melb_data.csv dataset with statistical perspective.
# The dataset can be downloaded from:
# https://www.kaggle.com/datasets/gunjanpathak/melb-data?resource=download
# Topics Covered: Data Preprocessing

import pandas as pd

data = pd.read_csv("D:/Development/Wipro_TalentNext_Python/datasets/melb_data.csv")

num_cols = data.select_dtypes(include=['int64','float64']).columns
for col in num_cols:
    data[col].fillna(data[col].mean(), inplace=True)

cat_cols = data.select_dtypes(include=['object']).columns
for col in cat_cols:
    data[col].fillna(data[col].mode()[0], inplace=True)

for col in cat_cols:
    data[col] = data[col].astype('category').cat.codes

print(data.describe())
