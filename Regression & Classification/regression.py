# Problem 1: Predict the price of the car based on its features using Multiple Linear Regression
# Dataset: cars.csv

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
cars = pd.read_csv("D:/Development/Wipro_TalentNext_Python/datasets/cars.csv")
cars.replace('?', pd.NA, inplace=True)
num_cols_c = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin']
for col in num_cols_c:
    cars[col] = pd.to_numeric(cars[col])
cars.dropna(inplace=True)
X_cars = cars.drop(columns=['mpg','car name'])
y_cars = cars['mpg']
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_cars, y_cars, test_size=0.2, random_state=42)
model_cars = LinearRegression()
model_cars.fit(X_train_c, y_train_c)
y_pred_c = model_cars.predict(X_test_c)
print("Cars Dataset Predictions (Test Set):")
print(y_pred_c)

# Problem 2: Predict the profit based on features using Multiple Linear Regression
# Dataset: 50_startups.csv
startups = pd.read_csv("D:/Development/Wipro_TalentNext_Python/datasets/startups.csv")
startups['State'] = startups['State'].astype('category').cat.codes
X_start = startups.drop(columns=['Profit'])
y_start = startups['Profit']
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X_start, y_start, test_size=0.2, random_state=42)
model_start = LinearRegression()
model_start.fit(X_train_s, y_train_s)
y_pred_s = model_start.predict(X_test_s)
print("\n50_Startups Dataset Predictions (Test Set):")
print(y_pred_s)


# Problem 3: Predict Salary based on YearsExperience using Simple Linear Regression
# Dataset: Salary_Data.csvsalary = pd.read_csv("D:/Development/Wipro_TalentNext_Python/datasets/Salary_Data.csv")

salary = pd.read_csv("D:/Development/Wipro_TalentNext_Python/datasets/Salary_Data.csv")
X_sal = salary[['YearsExperience']]
y_sal = salary['Salary']
X_train_sal, X_test_sal, y_train_sal, y_test_sal = train_test_split(X_sal, y_sal, test_size=0.2, random_state=42)
model_sal = LinearRegression()
model_sal.fit(X_train_sal, y_train_sal)
y_pred_sal = model_sal.predict(X_test_sal)
print("\nSalary Dataset Predictions (Test Set):")
print(y_pred_sal)