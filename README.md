# 🔍 Fake Review Detection System

## 📌 Overview

This project is a Machine Learning-based web application that detects whether a given review is **Fake or Real**.
It is built using **Streamlit** for the frontend and **SQLite** for database storage.

The system analyzes user input reviews using **TF-IDF vectorization** and a trained classification model to provide predictions along with probability scores.

---

## 🚀 Features

* 👤 User Registration (Name, Email, Age)
* 🕵️ Fake vs Real Review Detection
* 📊 Probability Score Display
* 📜 Review History Storage
* 💾 Persistent Data using SQLite
* 🎨 Interactive UI using Streamlit

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Machine Learning (TF-IDF, Classification Model)
* SQLite Database
* Pandas
* Joblib

---

## 📂 Project Structure

```
REVIEW_DETECTION/
│
├── apps.py                 # Main Streamlit App
├── database.py            # Database operations
├── reviews.db             # SQLite Database
├── text_model.pkl         # Trained ML model
├── tfidf_vectorizer.pkl   # TF-IDF Vectorizer
├── processed_reviews.csv  # Dataset
├── project.ipynb          # Model training notebook
└── README.md              # Project documentation
```

---

## ▶️ How to Run the Project

1. Install dependencies:

```
pip install streamlit pandas scikit-learn joblib
```

2. Run the app:

```
streamlit run apps.py
```

3. Open in browser:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. User enters a review
2. Text is converted using **TF-IDF Vectorizer**
3. ML model predicts:

   * Fake Review
   * Real Review
4. Result + probability is displayed
5. Data is stored in SQLite database

---

## 📊 Output

* Shows prediction (Fake / Real)
* Displays probability score
* Stores history for future reference

---

## 🔮 Future Scope

* Improve model accuracy using Deep Learning
* Add sentiment analysis
* Deploy on cloud (Streamlit Cloud / Render)
* Add user authentication system
* Use cloud database (MongoDB / Firebase)

---

## 👩‍💻 Author

Garima Tayal
MCA Student

---

## ⭐ Conclusion

This project helps identify misleading or fake reviews, improving trust in online platforms like e-commerce websites.
