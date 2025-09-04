# 1. Create a model that can predict the disease of cancer based on features given in the dataset. Use appropriate evaluation metrics. Dataset : cancer.csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.impute import SimpleImputer

cancer = pd.read_csv("D:/Development/Wipro_TalentNext_Python/datasets/cancer.csv")

# Drop column with all NaN values
if 'Unnamed: 32' in cancer.columns:
    cancer.drop(columns=['Unnamed: 32'], inplace=True)

num_cols = cancer.select_dtypes(include=['int64','float64']).columns
cat_cols = cancer.select_dtypes(include=['object']).columns

imputer_num = SimpleImputer(strategy='mean')
cancer[num_cols] = imputer_num.fit_transform(cancer[num_cols])

imputer_cat = SimpleImputer(strategy='most_frequent')
cancer[cat_cols] = imputer_cat.fit_transform(cancer[cat_cols])

for col in cat_cols:
    cancer[col] = cancer[col].astype('category').cat.codes

X_cancer = cancer.drop(columns=['diagnosis'])
y_cancer = cancer['diagnosis']

X_train, X_test, y_train, y_test = train_test_split(X_cancer, y_cancer, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# 2. Create a model that can predict that the customer has purchased item or not based on features given in the dataset. Use appropriate evaluation metrics. Dataset : Social_Ntetwork_Ads.csv
social = pd.read_csv("D:/Development/Wipro_TalentNext_Python/datasets/Social_Network_Ads.csv")

num_cols_social = social.select_dtypes(include=['int64','float64']).columns
for col in num_cols_social:
    social[col].fillna(social[col].mean(), inplace=True)
cat_cols_social = social.select_dtypes(include=['object']).columns
for col in cat_cols_social:
    social[col].fillna(social[col].mode()[0], inplace=True)
    social[col] = social[col].astype('category').cat.codes
X_social = social.drop(columns=['Purchased'])
y_social = social['Purchased']
X_train_social, X_test_social, y_train_social, y_test_social = train_test_split(X_social, y_social, test_size=0.2, random_state=42)
model_social = LogisticRegression(max_iter=1000)
model_social.fit(X_train_social, y_train_social)
y_pred_social = model_social.predict(X_test_social)
print("\nSocial Network Ads Dataset - Logistic Regression")
print("Accuracy:", accuracy_score(y_test_social, y_pred_social))
print("Confusion Matrix:\n", confusion_matrix(y_test_social, y_pred_social))
print("Classification Report:\n", classification_report(y_test_social, y_pred_social))
