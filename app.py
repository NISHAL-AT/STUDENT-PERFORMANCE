# import streamlit as st
# import pandas as pd
# import joblib

# # ---------- Load model and encoders ----------
# lr = joblib.load('linear_model.pkl')
# encoders = joblib.load('encoders.pkl')  # dict of LabelEncoders
# categorical_cols = list(encoders.keys())

# st.title("Math Score Predictor")
# st.subheader("Enter student details:")

# # ---------- Get User Input ----------
# def get_user_input():
#     gender = st.selectbox("Gender", ["male", "female"])
#     race_ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
#     parental_education = st.selectbox("Parental Level of Education", [
#         "some high school", "high school", "some college", 
#         "associate's degree", "bachelor's degree", "master's degree"
#     ])
#     lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
#     test_prep = st.selectbox("Test Preparation Course", ["none", "completed"])
#     reading_score = st.number_input("Reading Score", 0, 100)
#     writing_score = st.number_input("Writing Score", 0, 100)
    
#     data = {
#         'gender': gender,
#         'race/ethnicity': race_ethnicity,
#         'parental level of education': parental_education,
#         'lunch': lunch,
#         'test preparation course': test_prep,
#         'reading score': reading_score,
#         'writing score': writing_score
#     }
#     return pd.DataFrame([data])

# input_df = get_user_input()

# # ---------- Encode categorical columns using saved encoders ----------
# for col in categorical_cols:
#     le = encoders[col]
#     input_df[col] = le.fit_transform(input_df[col])

# # ---------- Predict ----------
# try:
#     prediction = lr.predict(input_df)[0]
#     st.success(f"Predicted Math Score: {prediction:.2f}")
# except Exception as e:
#     st.error(f"Error: {e}")


import streamlit as st
import pandas as pd
import joblib

# ---------- Load model and encoders ----------
lr = joblib.load('linear_model.pkl')
encoders = joblib.load('encoders.pkl')  # dict of LabelEncoders
categorical_cols = list(encoders.keys())

st.title("Math Score Predictor")
st.subheader("Enter student details:")

# ---------- Get User Input ----------
def get_user_input():
    gender = st.selectbox("Gender", ["male", "female"])
    race_ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
    parental_education = st.selectbox("Parental Level of Education", [
        "some high school", "high school", "some college", 
        "associate's degree", "bachelor's degree", "master's degree"
    ])
    lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
    test_prep = st.selectbox("Test Preparation Course", ["none", "completed"])
    reading_score = st.number_input("Reading Score", 0, 100)
    writing_score = st.number_input("Writing Score", 0, 100)
    
    data = {
        'gender': gender,
        'race/ethnicity': race_ethnicity,
        'parental level of education': parental_education,
        'lunch': lunch,
        'test preparation course': test_prep,
        'reading score': reading_score,
        'writing score': writing_score
    }
    return pd.DataFrame([data])

input_df = get_user_input()

# ---------- Encode categorical columns ----------
try:
    for col in categorical_cols:
        le = encoders[col]
        # Transform and convert to numeric
        input_df[col] = le.transform(input_df[col])
except ValueError as e:
    st.error(f"Input contains unknown category: {e}")
    st.stop()

# ---------- Ensure feature order ----------
feature_order = ['gender', 'race/ethnicity', 'parental level of education',
                 'lunch', 'test preparation course', 'reading score', 'writing score']
input_df = input_df[feature_order]

# ---------- Predict ----------
try:
    prediction = lr.predict(input_df)[0]
    st.success(f"Predicted Math Score: {prediction:.2f}")
except Exception as e:
    st.error(f"Prediction error: {e}")
