from flask import Flask, request, render_template, redirect, url_for, session
import joblib
import nltk
import string

nltk.download('stopwords')
from nltk.corpus import stopwords

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to something secret for production

# Load your pre-trained model and vectorizer
model = joblib.load('model/model.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')

stop_words = stopwords.words('english')

def clean_text(text):
    # Remove punctuation and stopwords, convert to lowercase
    text = ''.join([char.lower() for char in text if char not in string.punctuation])
    return ' '.join([word for word in text.split() if word not in stop_words])

# Dummy user credentials for login
USER_CREDENTIALS = {
    "admin": "password123"  # Change as needed
}

@app.route('/')
def home():
    # Redirect to login if not logged in
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return redirect(url_for('predict_page'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if USER_CREDENTIALS.get(username) == password:
            session['logged_in'] = True
            return redirect(url_for('predict_page'))
        else:
            error = "Invalid username or password"
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))

@app.route('/predict', methods=['GET', 'POST'])
def predict_page():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    prediction = None
    news = ''
    if request.method == 'POST':
        news = request.form.get('news', '')
        cleaned_news = clean_text(news)
        vect_news = vectorizer.transform([cleaned_news])
        prediction = model.predict(vect_news)[0]

    return render_template('index.html', prediction=prediction, news=news)

if __name__ == '__main__':
    app.run(debug=True)

