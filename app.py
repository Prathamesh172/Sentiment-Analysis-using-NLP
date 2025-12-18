from flask import Flask, render_template, request
import joblib
import re
import os  
app = Flask(__name__)

model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Text preprocessing 
def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    text = re.sub(r'\@w+|\#','', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.strip().lower()
    return text

def final_cleaner(review, summary):
    review = clean_text(review if review else "")
    summary = re.sub(r'[^A-Za-z0-9\s]', '', str(summary))
    summary = re.sub(r'\s+', ' ', summary).strip().lower()
    return review + " " + summary

@app.route('/')
def home():
    return render_template('index.html')  # The intro/landing page

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        summary = request.form['summary']
        combined = final_cleaner(review, summary)
        transformed = vectorizer.transform([combined])
        prediction = model.predict(transformed)[0]
        
        label_map = {0: "Negative", 1: "Neutral", 2: "Positive"}
        emoji_map = {0: "😠", 1: "😐", 2: "😊"}

        prediction_label = label_map.get(int(prediction), "Unknown")
        emoji = emoji_map.get(int(prediction), "🤔")

        return render_template('predict.html', prediction=prediction_label, emoji=emoji)
    
    return render_template('predict.html')  
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 7860))
    app.run(host='0.0.0.0', port=port)

