
# 1. Perform Exploratory Data Analysis for the dataset Mall_Customers. The dataset can be downloaded from https://www.kaggle.com/datasets

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mall = pd.read_csv("D:/Development/Wipro_TalentNext_Python/datasets/Mall_Customers.csv")
num_cols_mall = mall.select_dtypes(include=['int64','float64']).columns
cat_cols_mall = mall.select_dtypes(include=['object']).columns
for col in cat_cols_mall:
    mall[col] = mall[col].astype('category').cat.codes

for col in num_cols_mall:
    plt.figure()
    sns.histplot(mall[col], kde=True)
    plt.title(f'Mall_Customers Uni-variate Analysis: {col}')
    plt.show()

for col1 in num_cols_mall:
    for col2 in num_cols_mall:
        if col1 != col2:
            plt.figure()
            sns.scatterplot(x=mall[col1], y=mall[col2])
            plt.title(f'Mall_Customers Bi-variate Analysis: {col1} vs {col2}')
            plt.show()

# 2. Perform Exploratory Data Analysis for the dataset salary_data. The dataset can be downloaded from https://www.kaggle.com/datasets
salary = pd.read_csv("D:/Development/Wipro_TalentNext_Python/datasets/Salary_Data.csv")
num_cols_salary = salary.select_dtypes(include=['int64','float64']).columns
cat_cols_salary = salary.select_dtypes(include=['object']).columns
for col in cat_cols_salary:
    salary[col] = salary[col].astype('category').cat.codes

for col in num_cols_salary:
    plt.figure()
    sns.histplot(salary[col], kde=True)
    plt.title(f'salary_data Uni-variate Analysis: {col}')
    plt.show()

for col1 in num_cols_salary:
    for col2 in num_cols_salary:
        if col1 != col2:
            plt.figure()
            sns.scatterplot(x=salary[col1], y=salary[col2])
            plt.title(f'salary_data Bi-variate Analysis: {col1} vs {col2}')
            plt.show()

# 3. Perform Exploratory Data Analysis for the dataset Social Network Ads. The dataset can be downloaded from https://www.kaggle.com/datasets
social = pd.read_csv("D:/Development/Wipro_TalentNext_Python/datasets/Social_Network_Ads.csv")
num_cols_social = social.select_dtypes(include=['int64','float64']).columns
cat_cols_social = social.select_dtypes(include=['object']).columns
for col in cat_cols_social:
    social[col] = social[col].astype('category').cat.codes

for col in num_cols_social:
    plt.figure()
    sns.histplot(social[col], kde=True)
    plt.title(f'Social_Network_Ads Uni-variate Analysis: {col}')
    plt.show()

for col1 in num_cols_social:
    for col2 in num_cols_social:
        if col1 != col2:
            plt.figure()
            sns.scatterplot(x=social[col1], y=social[col2])
            plt.title(f'Social_Network_Ads Bi-variate Analysis: {col1} vs {col2}')
            plt.show()
