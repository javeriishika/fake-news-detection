import pandas as pd
import string
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import joblib

nltk.download('stopwords')
from nltk.corpus import stopwords

# Load dataset
df = pd.read_csv('data/news.csv')

# Combine title and text columns
df['content'] = df['title'] + ' ' + df['text']

# Drop rows with missing content or label
df.dropna(subset=['content', 'label'], inplace=True)

# Define stopwords and cleaning function
stop_words = stopwords.words('english')
def clean_text(text):
    text = ''.join([char.lower() for char in text if char not in string.punctuation])
    return ' '.join([word for word in text.split() if word not in stop_words])

df['content'] = df['content'].apply(clean_text)

# Prepare features and labels
X = df['content']
y = df['label']

# Vectorize text
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Train classifier
model = PassiveAggressiveClassifier()
model.fit(X_train, y_train)

# Save model and vectorizer
joblib.dump(model, 'model/model.pkl')
joblib.dump(vectorizer, 'model/vectorizer.pkl')

print("Training complete. Model and vectorizer saved in 'model/' folder.")

