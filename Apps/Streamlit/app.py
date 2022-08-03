import streamlit as st
import pickle
import numpy as np
import pandas as pd
from PIL import Image

# import the model
pipe = pickle.load(open('/Users/jaswanthsai/Documents/DATA 606/EDA/Final Gradient Boost Model.pkl','rb'))
df = pickle.load(open('/Users/jaswanthsai/Documents/DATA 606/EDA/df.pkl','rb'))

html_temp = """
<div style="background-color:tomato;padding:10px">
<h1 style="color:white;text-align:center;">Know price of your car </h1>
</div>
"""
image = Image.open('/Users/jaswanthsai/Documents/DATA 606/EDA/background.jpeg')
st.image(image, use_column_width=True)
st.title("Car Price Predictor")

# Brand
brand = st.selectbox('Select Brand',df['brand'].unique())

# Model
model_list = df.loc[df['brand'] == brand, 'model'].unique()
model = st.selectbox('Select Model',sorted(model_list))

# Mileage
mileage = st.number_input('Enter Mileage')

# Drive Type
drive_type = st.selectbox('Select Drive Type',df['drive_type'].unique())

# Fuel Type
fuel_type = st.selectbox('Select Fuel Type',df['fuel_type'].unique())

# Accidents
accidents_list = df['accidents'].unique()
accidents = st.selectbox('Number of accidents occured',sorted(accidents_list))#df['accidents'].unique())

# Owners
owners_list = df['owners'].unique()
owners = st.selectbox('Number of owners',sorted(owners_list))

# Age of Car
car_age = st.number_input('Enter Age of Car')

# Miles per Gallon
MPG = st.number_input('Enter Fuel Efficiency')

user_report_data = {
        'brand': brand,
        'model': model,
        'mileage': mileage,
        'drive_type': drive_type,
        'fuel_type': fuel_type,
        'accidents': accidents,
        'owners': owners,
        'car_age': car_age,
        'MPG': MPG
    }
report_data = pd.DataFrame(user_report_data, index=[0])

if st.button('Predict Price'):

    price = pipe.predict(report_data)
    st.subheader('Predicted Car Price')
    st.subheader('$ ' + str(int(np.exp(np.round(price[0], 2)))))

