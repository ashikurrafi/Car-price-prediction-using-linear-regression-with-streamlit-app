import pandas as pd
import numpy as np
import pickle as pkl
import streamlit as st

model = pkl.load(open('./models/lass_reg_model.pkl', 'rb'))

st.title("Used Car Price Prediction")

car_data = pd.read_csv('./dataset/car_data.csv')

def get_brand_name(car_name):
    car_name = car_name.split(' ')[0]
    return car_name.strip()

car_data['Car_Name'] = car_data['Car_Name'].apply(get_brand_name)
Car_Name = st.selectbox('Select Car Name', car_data['Car_Name'].unique())
Year = st.slider('Car Manufactured Year', car_data['Year'].min(), car_data['Year'].max())
Kms_Driven = st.slider('Number of Kms Driven', car_data['Kms_Driven'].min(), car_data['Kms_Driven'].max())
Present_Price = st.slider('Present Price', car_data['Present_Price'].min(), car_data['Present_Price'].max())
Fuel_Type = st.selectbox('Fuel Type', car_data['Fuel_Type'].unique())
Seller_Type = st.selectbox('Seller Type', car_data['Seller_Type'].unique())
Transmission = st.selectbox('Transmission Type', car_data['Transmission'].unique())
Owner = st.selectbox('Owner Type', car_data['Owner'].unique())

if st.button("Predict"):
    input_data = pd.DataFrame([[Car_Name, Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner]],
                              columns=['Car_Name', 'Year', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner'])
    input_data['Fuel_Type'] = input_data['Fuel_Type'].replace({'Petrol': 0, 'Diesel': 1, 'CNG': 2})
    input_data['Seller_Type'] = input_data['Seller_Type'].replace({'Dealer': 0, 'Individual': 1})
    input_data['Transmission'] = input_data['Transmission'].replace({'Manual': 0, 'Automatic': 1})
    input_data['Owner'] = input_data['Owner'].replace({'First Owner': 0, 'Second Owner': 1, 'Third Owner': 2})
    input_data = input_data.drop(columns=['Car_Name'])
    car_price = model.predict(input_data)
    st.markdown(f'Predicted Car Price is: ₹{car_price[0]:.2f}')
