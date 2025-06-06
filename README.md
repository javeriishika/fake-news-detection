# Fake News Detection Using NLP and Machine Learning

This project aims to detect fake news articles using Natural Language Processing (NLP) and Machine Learning techniques. It includes data preprocessing, model training, and a Flask-based web app for real-time fake news detection.

---

## Features

- **Data Merging:** Combines fake and true news datasets into a single cleaned file.
- **Model Training:** Trains a Logistic Regression classifier on the news data.
- **Web Application:** Flask app with a login page and an intuitive UI to classify news articles.
- **User-friendly Interface:** Includes user authentication and centered layout with colors to enhance UX.
- **Deployable:** Easy to run locally and deploy on any platform supporting Flask.

---

## Project Structure

fake-news-detection/
├── app.py # Flask application
├── train_model.py # Script to train ML model
├── merge_csv.py # Script to merge CSV datasets
├── data/ # Data folder (excluded from Git repo)
│ ├── Fake.csv # Fake news dataset
│ └── True.csv # True news dataset
├── templates/ # HTML templates
│ ├── index.html
│ └── login.html
├── requirements.txt # Python dependencies
└── README.md # This file


---

## Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/javeriishika/fake-news-detection.git
cd fake-news-detection
Create and activate a Python virtual environment:
python3 -m venv venv
source venv/bin/activate
Install required packages:
pip install -r requirements.txt
Download datasets:
Download Fake.csv and True.csv from the original source and place them inside the data/ folder.

Merge datasets and train the model:
python3 merge_csv.py
python3 train_model.py
Run the Flask app:
python3 app.py
Open your browser:
Navigate to http://127.0.0.1:5000 to use the app.

Notes

The data/ folder is excluded from Git to avoid pushing large files.
Ensure datasets are downloaded manually and placed correctly.
The login page improves app security and user experience.
Feel free to customize HTML/CSS in templates/ for a personalized look.

License

This project is open-source and available under the MIT License.






