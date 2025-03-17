import pickle
import re
from flask import Flask, request, jsonify

# Load the saved model and vectorizer
filename = 'svm_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))
file_name = "vectorizer.pkl"
loaded_vectorizer = pickle.load(open(file_name, 'rb'))

try:
    def clean_text(text):
        text = re.sub('http\S+\s*', ' ', text)  # remove URLs
        text = re.sub('RT|cc', ' ', text)  # remove RT and cc
        text = re.sub('#\S+', '', text)  # remove hashtags
        text = re.sub('@\S+', '  ', text)  # remove mentions
        text = re.sub('[%s]' % re.escape("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"), ' ', text)  # remove punctuations
        text = re.sub(r'[^\x00-\x7f]', r' ', text)
        text = re.sub('\s+', ' ', text)  # remove extra whitespace
        return text
except:
    print("NN.....")

def predict_spam(text):
    cleaned_text = clean_text(text)
    vectorized_text = loaded_vectorizer.transform([cleaned_text.lower()])
    prediction = loaded_model.predict(vectorized_text)
    return "Spam" if prediction[0] == 1 else "Ham"

# Flask API
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    result = predict_spam(text)
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(port=5000, debug=True)