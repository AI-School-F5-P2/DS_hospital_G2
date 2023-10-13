# Streamlit app for predicting stroke risk using Logistic Regression

import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image


# Load the model
with open('Notebooks/finalmodel.pickle', 'rb') as model_file:
    model = pickle.load(model_file)

# Define Streamlit app layout and functionality
def main():
    col1, col2 = st.columns([1,3])
    with Image.open("heart.webp") as img:
            img = img.resize((120, 120))  
    # Exibe a imagem na primeira coluna (col1)
    col1.image(img, width=120)
    col2.title("Stroke Prediction App")
   
    
    # User input fields
    age = st.slider("Age", 0, 100)
    hypertension = st.selectbox("Hypertension", ['Yes', 'No'])
    heart_disease = st.selectbox("Heart Disease", ['Yes', 'No'])
    avg_glucose_level = st.slider("Average Glucose Level", 50, 250)
    bmi = st.slider("BMI", 10, 40)
    
    gender = st.selectbox("Gender", ['Male', 'Female'])
    ever_married = st.selectbox("Ever Married", ['Yes', 'No'])
    work_type = st.selectbox("Work Type", ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
    residence_type = st.selectbox("Residence Type", ['Urban', 'Rural'])
    smoking_status = st.selectbox("Smoking Status", ['formerly smoked', 'never smoked', 'smokes', 'Unknown'])
    
    if hypertension == "Yes":
                hypertension = 1
    else:
                hypertension = 0
    
    if heart_disease == "Yes":
                heart_disease = 1
    else:
                heart_disease = 0
    
            
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
