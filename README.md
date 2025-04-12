# 🧠 Sentiment Analysis Web App

A stylish and simple Flask-based web application that predicts the **sentiment** (Positive, Neutral, or Negative) of product reviews, powered by Natural Language Processing and Machine Learning.

<div align="center">
  <img src="https://img.shields.io/badge/Made_with-Flask-blue?style=flat-square" alt="Flask Badge">
  <img src="https://img.shields.io/badge/Deployed_on-Hugging--Face-yellow?style=flat-square" alt="Hugging Face Badge">
  <img src="https://img.shields.io/badge/Language-Python3-brightgreen?style=flat-square" alt="Python Badge">
</div>

---

## 🔍 Features

- 📃 Input: Full product review and optional summary
- 🔎 Cleaned and preprocessed before prediction
- 📊 Output: One of three sentiment classes:
  - 😊 Positive
  - 😐 Neutral
  - 😠 Negative
- 🖍️ Minimalist dark-themed UI with dynamic card and button effects
- 🐳 Dockerized and deployable on Hugging Face Spaces or any container-based platform

---

## 📁 Project Structure

```
sentiment-app/
│
├── app.py                  # Flask application
├── Dockerfile              # Docker setup
├── requirements.txt        # Python dependencies
├── sentiment_model.pkl     # Trained sentiment classifier
├── tfidf_vectorizer.pkl    # TF-IDF vectorizer
├── templates/
│   ├── index.html          # Landing page
│   └── predict.html        # Prediction form + result
│
└── README.md
```

---

## 🧠 Model Overview

The model used here is a **multi-class classifier** trained on labeled product reviews. It combines **TF-IDF vectorization** with **Logistic Regression** for final sentiment classification.

This setup was chosen due to Logistic Regression's efficiency and interpretability, making it a strong baseline for text classification tasks.

Prediction Labels:
- `0` → Negative
- `1` → Neutral
- `2` → Positive

---

## 📦 Setup Instructions

### 🔧 Local Run

1. Clone the repository
   ```bash
   git clone https://github.com/your-username/sentiment-app.git
   cd sentiment-app
   ```

2. Create virtual environment (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app
   ```bash
   python app.py
   ```

### 🐳 Docker (for Hugging Face or local containers)

```bash
docker build -t sentiment-app .
docker run -p 7860:7860 sentiment-app
```

---

## 📊 Dataset

> This dataset contains information about Product name, Product price, Rate, Reviews, Summary and Sentiment in csv format. There are 104 different types of products of flipkart.com such as electronics items, clothing of men, women and kids, Home decor items, Automated systems, so on. It has 205053 rows and 6 columns. Also, if any product doesn't have any review but summary is present then Nan value already added to its blank space.

This dataset has multiclass label as sentiment such as positive, neutral amd negative.The sentiment given was based on column called Summary using NLP and Vader model. Also, after that we manually check the label and put it into the appropriate categories like if summary has text like okay, just ok or one positive and negative we labeled as neutral for better understanding while using this dataset for human languages. On the summary and price column, data cleaning method is already performed using python module called NumPy and Pandas which are famous.You can learn it also through any online resource.

---

## ### 🌍 Live Demo

**Hosted on Hugging Face:** [Click here](https://huggingface.co/spaces/TheGrandmaSlayer/NLPSentimentAnalysis)

---

## ✨ Aesthetic Highlights

- Dark, modern interface
- Smooth hover transitions for buttons and cards
- Responsive layout
- Emoji-based result display for quick emotional grasp

---

Built with ❤️ by Prathamesh
