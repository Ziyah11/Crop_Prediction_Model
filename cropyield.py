import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import warnings
warnings.filterwarnings ('ignore')
import streamlit as st 
import joblib
from sklearn.linear_model import LinearRegression


data = pd.read_excel('crop yield data sheet.xlsx')
st.markdown("<h1 style = 'color: #416D19; text-align: center; font-family: helvetica '>CROP PREDICTION MODEL</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #F11A7B; text-align: center; font-family: cursive '>Built By Oluyemi Isaiah(Ziyah)</h4>", unsafe_allow_html = True)

st.image('pngwing.com (2).png', width = 350, use_column_width = True )

st.markdown("<p>This machine learning project centers on predicting crop yields, a pivotal aspect of agriculture with direct implications for food production and resource planning. The project aims to harness historical crop yield data and relevant features to build a machine learning model capable of accurately forecasting future crop yields. Factors such as weather conditions, soil quality, and farming practices play a crucial role in influencing crop yields, making it imperative to develop a robust predictive model.</p>", unsafe_allow_html=True) 

st.markdown("<br>", unsafe_allow_html = True)
data.rename(columns = {'Yeild (Q/acre)': 'Yield', 'Rain Fall (mm)': 'RainFall', 'Nitrogen (N)' : 'Nitrogen', 'Phosphorus (P)' : 'Phosphorus', 'Potassium (K)' : 'Potassium', 'Temperatue' :'Temperature'}, inplace = True)
st.dataframe(data, use_container_width = True )

data['Temperature'] = pd.to_numeric(data['Temperature'], errors = 'coerce')
st.sidebar.image('pngwing.com (3).png', caption= 'Welcome User')

st.sidebar.write('Feature Input')
rainfall = st.sidebar.number_input('Rainfall', data['RainFall'].min(), data['RainFall'].max()+ 10000)
Fertilizer = st.sidebar.number_input('Fertilizer', data['Fertilizer'].min(), data['Fertilizer'].max()+ 10000)
Temperature = st.sidebar.number_input('Temperature', int(data['Temperature'].min()), int(data['Temperature'].max()) + 10000)
Nitrogen= st.sidebar.number_input('Nitrogen', data['Nitrogen'].min(), data['Nitrogen'].max()+10000)
Phosphorus = st.sidebar.number_input('Phosphorus', data['Phosphorus'].min(), data['Phosphorus'].max()+ 10000)
Potassium = st.sidebar.number_input('Potassium', data['Potassium'].min(), data['Potassium'].max()+ 10000)

st.markdown("<br>", unsafe_allow_html= True)
st.write('Input Variables')

input_var = pd.DataFrame({'RainFall': [rainfall], 'Fertilizer': [Fertilizer], 'Temperature': [Temperature],'Nitrogen' :[Nitrogen],'Phosphorus' : [Phosphorus],'Potassium' : [Potassium]})
st.dataframe(input_var)

model = joblib.load('CropPrediction.pkl')


predicter =st.button('Predicted Crop Yield')
if predicter:
    prediction = model.predict(input_var)
    st.success(f"The Predicted yield for your crop is {prediction} tonnes")
    st.balloons()