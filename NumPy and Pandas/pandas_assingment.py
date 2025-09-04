# Exercise 3: Pandas-DataFrame
# Download the data set and rename to cars.csv
# Link : Dataset: https://www.kaggle.com/uciml/autompg-dataset/data?select=auto-mpg.csv
# or https://archive.ics.uci.edu/ml/datasets/Auto+MPG

# a. Import Pandas
import pandas as pd

# b. Import the Cars Dataset and store the Pandas DataFrame in the variable cars
cars = pd.read_csv("D:\Development\Wipro_TalentNext_Python\datasets\cars.csv")

# c. Inspect the first 10 Rows of the DataFrame cars
print(cars.head(10))

# d. Inspect the DataFrame cars by "printing" cars
print(cars)

# e. Inspect the last 5 Rows
print(cars.tail(5))

# f. Get some meta information on our DataFrame!
print(cars.info())



# Exercise 4 : Download 50_startups dataset
# Link : https://www.kaggle.com/datasets/farhanmd29/50-startups

# a. Create DataFrame using Pandas
# b. Read the data from 50_startups.csv file and load the data into dataframe.
startups = pd.read_csv("D:\Development\Wipro_TalentNext_Python\datasets\startups.csv")

# c. Check the statistical summary.
print(startups.describe())

# d. Check for corelation coefficient between dependent and independent variables.

print(startups.select_dtypes(include='number').corr())