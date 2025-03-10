import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the saved model pipeline
loaded_pipeline_x = joblib.load('life_expectancy_pipeline.pkl')
#loaded_pipeline_y = joblib.load('y_pipeline.pkl')  # Adjust the path if needed

# Load your original dataset
data = pd.read_csv('LifeExpectancy.csv')
unique_countries = data['Country'].unique()  # Get unique countries from the dataset

# Define user inputs in Streamlit
user_data = {
    'Population': st.number_input('Population'),
    'Total expenditure': st.number_input('Total expenditure'),
    'HIV/AIDS': st.number_input('HIV/AIDS'),
    'Income composition of resources': st.number_input('Income composition of resources'),
    'percentage expenditure': st.number_input('percentage expenditure'),
    'under-five deaths': st.number_input('under-five deaths'),
    'thinness 5-9 years': st.number_input('thinness 5-9 years'),
    'Diphtheria': st.number_input('Diphtheria'),
    'Polio': st.number_input('Polio'),
    'Measles': st.number_input('Measles'),
    'Hepatitis B': st.number_input('Hepatitis B'),
    'Alcohol': st.number_input('Alcohol'),
    'Adult Mortality': st.number_input('Adult Mortality'),
    'BMI': st.number_input('BMI'),
    'Year': st.number_input('Year'),
    'Country': st.selectbox('Country', unique_countries),
    'Status': st.selectbox('Status', ['Developed', 'Developing'])
}

# Convert user input to DataFrame
user_df = pd.DataFrame([user_data])

if st.button('Predict Life Expectancy'):
   input_array = np.array(user_df).reshape(1, -1)  # Reshape for model input
   prediction = loaded_pipeline_x.predict(user_df)
   st.write(f"Predicted Life Expectancy: {prediction[0]:.2f}")
