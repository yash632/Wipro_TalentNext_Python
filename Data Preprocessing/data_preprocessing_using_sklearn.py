# Perform Data Preprocessing on melb_data.csv dataset with statistical perspective.
# The dataset can be downloaded from:
# https://www.kaggle.com/datasets/gunjanpathak/melb-data?resource=download

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

data = pd.read_csv("D:/Development/Wipro_TalentNext_Python/datasets/melb_data.csv")

num_cols = data.select_dtypes(include=['int64','float64']).columns
imputer_num = SimpleImputer(strategy='mean')
data[num_cols] = imputer_num.fit_transform(data[num_cols])

cat_cols = data.select_dtypes(include=['object']).columns
imputer_cat = SimpleImputer(strategy='most_frequent')
data[cat_cols] = imputer_cat.fit_transform(data[cat_cols])

le = LabelEncoder()
for col in cat_cols:
    data[col] = le.fit_transform(data[col])

scaler = StandardScaler()
data[num_cols] = scaler.fit_transform(data[num_cols])

print(data.describe())
