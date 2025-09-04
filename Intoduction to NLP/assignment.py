# 1. Perform Text Preprocessing on SMSSpamCollection Dataset. The dataset can be downloaded from https://www.kaggle.com/datasets

import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

sms = pd.read_csv("D:/Development/Wipro_TalentNext_Python/datasets/spam.csv",
                  sep='\t', header=None, names=['Label', 'Message'])

sms['Label'] = sms['Label'].map({'ham': 0, 'spam': 1})

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

sms['Message'] = sms['Message'].apply(preprocess_text)

X_train, X_test, y_train, y_test = train_test_split(
    sms['Message'], sms['Label'], test_size=0.2, random_state=42
)

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

print("Sample preprocessed messages:")
print(X_train_vec[:5])
