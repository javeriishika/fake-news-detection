# Fake News Detection Using NLP and Machine Learning

This project detects fake news articles using natural language processing (NLP) and machine learning techniques. It includes:

- Data preprocessing and merging CSV files containing fake and true news.
- Training a machine learning model (Logistic Regression) to classify news articles.
- A Flask web app to interact with the model and predict whether a news article is fake or true.
- A simple login page with user authentication.
- Instructions for running the app locally.

## Project Structure

fake-news-detection/
│
├── app.py # Flask web app
├── train_model.py # Model training script
├── merge_csv.py # Script to merge CSV data files
├── data/ # Folder for CSV data files (NOT tracked in Git)
├── templates/ # HTML templates for the Flask app
│ ├── index.html
│ └── login.html
├── requirements.txt # Python dependencies
└── README.md # This file


## Setup Instructions

1. Clone the repo:

```bash
git clone https://github.com/yourusername/fake-news-detection.git
cd fake-news-detection
Create a Python virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate
Install dependencies:
pip install -r requirements.txt
Download the data files (Fake.csv and True.csv) from [Google Drive link or wherever you uploaded] and place them inside the data/ folder.
Merge CSV files and train the model:
python3 merge_csv.py
python3 train_model.py
Run the Flask app:
python3 app.py
Open your browser and go to:
http://127.0.0.1:5000

