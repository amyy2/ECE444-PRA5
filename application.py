from flask import Flask, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

def load_model():
    loaded_model = None
    with open('basic_classifier.pkl', 'rb') as fid:
        loaded_model = pickle.load(fid)

    vectorizer = None
    with open('count_vectorizer.pkl', 'rb') as vd:
        vectorizer = pickle.load(vd)

    prediction = loaded_model.predict(vectorizer.transform(['This is fake news']))[0]

    return prediction

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form.get('text')
        prediction = load_model()
        return f"Prediction for '{text}': {prediction}"
    return "flask works"