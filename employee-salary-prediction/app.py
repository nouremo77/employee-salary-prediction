import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Employee Salary Prediction",
    page_icon="💼",
    layout="centered"
)

model = joblib.load("models/salary_model.pkl")

df = pd.read_csv("data/processed/cleaned_salary.csv")

st.title("💼 Employee Salary Prediction")

st.write(
    "Predict employee salary using Machine Learning."
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=70,
    value=25
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

education = st.selectbox(
    "Education Level",
    sorted(df["Education Level"].dropna().unique())
)

job_title = st.selectbox(
    "Job Title",
    sorted(df["Job Title"].dropna().unique())
)

experience = st.number_input(
    "Years of Experience",
    min_value=0,
    max_value=40,
    value=1
)

if st.button("Predict Salary"):

    input_data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Education Level": [education],
        "Job Title": [job_title],
        "Years of Experience": [experience]
    })

    prediction = model.predict(input_data)

    st.success(f"Estimated Salary: ${prediction[0]:,.2f}")