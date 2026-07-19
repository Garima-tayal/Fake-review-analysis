import streamlit as st
import joblib
import pandas as pd
import base64
from database import create_tables, save_user, save_review, get_all_reviews

def get_base64_image(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()
    
# Initialize DB
create_tables()

# Load model
model = joblib.load("text_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Session
if "page" not in st.session_state:
    st.session_state.page = "login"

# UI
st.set_page_config(page_title="Fake Review Detector")

img = get_base64_image("photo.jpg")

st.markdown(f"""
<style>
.stApp {{
    background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
                      url("data:image/jpg;base64,{img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

/* Titles */
.title {{
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: white;
}}

/* Normal text (like Welcome sid) */
.stMarkdown, .stText {{
    color: white !important;
}}

/* Labels */
label {{
    color: white !important;
    font-weight: 500;
}}

/* Input text */
input, textarea {{
    color: black !important;
}}

/* Table text */
[data-testid="stDataFrame"] {{
    background-color: white;
    border-radius: 10px;
}}

/* Buttons */
div.stButton > button {{
    background-color: #6a4c93;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}}
</style>
""", unsafe_allow_html=True)

if st.session_state.page == "login":

    st.markdown('<div class="title"> User Details</div>', unsafe_allow_html=True)

    username = st.text_input("Enter Name")
    email = st.text_input("Enter Email")
    age = st.number_input("Enter Age", min_value=10, max_value=100)

    if st.button("Continue"):
        if username and email:
            save_user(username, email, age)

            st.session_state.username = username
            st.session_state.email = email
            st.session_state.age = age

            st.session_state.page = "analysis"
            st.rerun()
            
        else:
            st.warning("Please fill all details")


elif st.session_state.page == "analysis":

    st.markdown('<div class="title"> Fake Review Detector</div>', unsafe_allow_html=True)
    st.write(f"Welcome, {st.session_state.username} ")

    review = st.text_area("Enter your review here:", height=150)

    if st.button("Analyze Review"):
        if review.strip() == "":
            st.warning("Enter review!")
        else:
            review_tfidf = vectorizer.transform([review])
            prediction = model.predict(review_tfidf)[0]
            prob = model.predict_proba(review_tfidf)[0][1]

            if prediction == 1:
                result_text = "Fake Review"
                st.markdown(
                    f'<div class="result-box" style="background:#ffe6f0;color:#c2185b;text-align:center;">⚠️ Fake Review<br>Prob: {prob:.2f}</div>',
                    unsafe_allow_html=True
                )
            else:
                result_text = "Real Review"
                st.markdown(
                    f'<div class="result-box" style="background:#e6fff2;color:#2e7d32;text-align:center;">✅ Real Review<br>Prob: {prob:.2f}</div>',
                    unsafe_allow_html=True
                )

            # Save review with user details
            save_review(
                st.session_state.username,
                st.session_state.email,
                st.session_state.age,
                review,
                result_text,
                prob
            )

    col1, col2 = st.columns(2)

    with col1:
        if st.button(" View History"):
            st.session_state.page = "history"
        

    with col2:
        if st.button("Logout"):
            st.session_state.clear()
            st.session_state.page = "login"
            st.rerun()


elif st.session_state.page == "history":

    st.markdown("## All Users Review History")

    history = get_all_reviews()

    if history:
        df = pd.DataFrame(history, columns=[
            "Username", "Email", "Age",
            "Review", "Prediction", "Fake Probability"
        ])

        df["Fake Probability"] = df["Fake Probability"].apply(lambda x: round(x, 2))

        st.dataframe(df, use_container_width=True)
    else:
        st.info("No data found")

    if st.button("⬅ Back"):
        st.session_state.page = "analysis"
        st.rerun()
        