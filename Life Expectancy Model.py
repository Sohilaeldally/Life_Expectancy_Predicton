import streamlit as st
import joblib
import pandas as pd

# Load the saved model pipeline
loaded_pipeline = joblib.load('life_expectancy_pipeline.pkl')
# Load the imputer and transformer separately
y_imputer = joblib.load('y_imputer.pkl')
y_transformer = joblib.load('y_transformer.pkl')


# Define user inputs in Streamlit
data = pd.read_csv('LifeExpectancy.csv')  # Load your original dataset
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
    # Predict life expectancy
    life_expectancy_pred_r = loaded_pipeline.predict(user_df)

    # Prepare the prediction for inverse transformation
    life_expectancy_pred_r_reshaped = life_expectancy_pred_r.reshape(-1, 1)

    # First, handle missing values using the imputer
    y_imputed = y_imputer.transform(life_expectancy_pred_r_reshaped)

    # Now apply the inverse transform
    life_expectancy_pred = y_transformer.inverse_transform(y_imputed)

    # Display the prediction
    st.write('Predicted Life Expectancy:', life_expectancy_pred[0][0])
