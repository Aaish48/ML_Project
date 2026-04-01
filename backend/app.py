import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

stop_words = set(stopwords.words('english'))
negation_words = {'not', 'no', 'don', "don't"}
stop_words = stop_words - negation_words

def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    review = data.get("review", "")

    clean = preprocess_text(review)
    vector = vectorizer.transform([clean])

    prediction = model.predict(vector)[0]

    result = "Positive 😊" if prediction == 1 else "Negative 😡"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
# 