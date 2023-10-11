# Stroke Risk Prediction App

## Overview

The Stroke Risk Prediction App is designed to evaluate the risk of a patient having a stroke based on certain indicators of life and health status. Developed with Streamlit, it provides instant feedback to medical professionals, aiding in timely intervention and consultation.

## Features

- **Data Input Form**: Simple and intuitive form to input patient details.
- **Rapid Predictions**: Uses a pre-trained model to quickly predict stroke risk.
- **Detailed Statistics**: View comprehensive statistics on model performance.

## Justification for Model Choice

We prioritize reducing false negatives, as it's critical to not miss any patients who might be at risk of having a stroke. Speed and simplicity are also factors, as the application is designed for fast feedback before a medical consultation.

## Frontend Overview

The frontend is developed using Streamlit and consists of a basic form. It provides rapid predictions using the saved pickle file. This application is designed so that before the consultation, the patient's data and prediction are registered, giving the doctor preliminary feedback.


## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required packages.
4. Run the Streamlit app.

## Usage

1. Open the app in your browser.
2. Fill in the patient details in the provided form.
3. Submit the form to get an instant prediction on stroke risk.

## Files and Folders

- README.md: Project usage guide.

- requirements.txt: Install this file to ensure your environment has all the necessary libraries. You can install it by running "pip install -r requirements.txt" in the terminal.

- .gitignore: Prevents selected files and folders from being uploaded to the repository.

- strokeapp.py: Interface for predicting whether a patient is at risk of having a stroke. Note: to make this script work, you need the .pickle file, which is not uploaded to the repository and is generated automatically when running Modelling.ipynb.

- Notebooks:
    · EDA: Exploratory data analysis.
    · Hyperparameter_tuning: Search for the best hyperparameters for the final model.
    · Modelling: Training the final chosen model and creating the pickle.
    · Model_comparison: Model comparison to determine which one provides the best metrics.


## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

1. Fork the Project
2. Create your Feature Branch 
3. Commit your Changes 
4. Push to the Branch 
5. Open a Pull Request