# Streamlit app for predicting stroke risk using Logistic Regression

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model
with open('Notebooks/finalmodel.pickle', 'rb') as model_file:
    model = pickle.load(model_file)

# Define Streamlit app layout and functionality
def main():
    st.title("Stroke Prediction App")
    
    # User input fields
    age = st.slider("Age", 0, 100)
    hypertension = st.selectbox("Hypertension", [0, 1])
    heart_disease = st.selectbox("Heart Disease", [0, 1])
    avg_glucose_level = st.slider("Average Glucose Level", 50, 250)
    bmi = st.slider("BMI", 10, 40)
    
    gender = st.selectbox("Gender", ['Male', 'Female'])
    ever_married = st.selectbox("Ever Married", ['Yes', 'No'])
    work_type = st.selectbox("Work Type", ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
    residence_type = st.selectbox("Residence Type", ['Urban', 'Rural'])
    smoking_status = st.selectbox("Smoking Status", ['formerly smoked', 'never smoked', 'smokes', 'Unknown'])

    # Predict button
    if st.button("Predict"):
        input_data = pd.DataFrame({
            'age': [age],
            'hypertension': [hypertension],
            'heart_disease': [heart_disease],
            'avg_glucose_level': [avg_glucose_level],
            'bmi': [bmi],
            'gender': [gender],
            'ever_married': [ever_married],
            'work_type': [work_type],
            'Residence_type': [residence_type],
            'smoking_status': [smoking_status]
        })
        
        prediction = model.predict(input_data)
        
        if prediction[0] == 1:
            st.warning("The individual is at risk of stroke!")
        else:
            st.success("The individual is not at risk of stroke.")

# Run Streamlit app
if __name__ == "__main__":
    main()
