import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

# Load dataset, but keep only first two columns
df = pd.read_csv(
    "D:/Development/Wipro_TalentNext_Python/datasets/spam.csv", 
    encoding='latin-1',
    usecols=[0, 1],         # take only the first 2 columns
    names=['label', 'message'], 
    skiprows=1              # skip the first row (header mess)
)

# Ensure all messages are strings
df['message'] = df['message'].astype(str)

# Lowercase
df['message'] = df['message'].str.lower()

# Remove punctuation
df['message'] = df['message'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))

# Remove stopwords
stop_words = set(stopwords.words('english'))
df['message'] = df['message'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))

# Stemming
ps = PorterStemmer()
df['message'] = df['message'].apply(lambda x: ' '.join([ps.stem(word) for word in x.split()]))

# Show clean data
print(df.sample(5))
print(df.head(10))
