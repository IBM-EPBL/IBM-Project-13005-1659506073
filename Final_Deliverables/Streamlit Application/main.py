import streamlit as st
import pandas as pd
import xgboost

formData = st.container()
model = xgboost.XGBRegressor()
model.load_model("model_xgb.txt")
data = pd.read_csv('transformedData.csv')
desc = open('desc.txt', 'r')

with formData:
    st.image('wallpaperflare.com_wallpaper.jpg')
    text = 'Food Demand Forecaster'
    st.markdown('<hr style="height:3px;color:#000000;background-color:#FFFFFF;"/> ', unsafe_allow_html=True)
    st.markdown(f'<p style="font-family:Trebuchet MS; font-size: 50px; background-color:orange; text-align: center"><b>{text.upper()}</b></p>', unsafe_allow_html=True)    
    st.markdown(f'<p style="font-family: Verdana; font-size: 20px;"><i>{desc.read()}</i></p>', unsafe_allow_html=True)
    
    st.markdown('<hr style="height:3px;color:#000000;background-color:#FFFFFF;"/> ', unsafe_allow_html=True)
    st.markdown(f'<p style="font-family: Verdana; font-size: 30px; text-align:center">FORECASTER</p>', unsafe_allow_html=True)
    category = st.selectbox('category', data['category'].unique())
    checkout_price = st.number_input('Enter Checkout Price')
    base_price = st.number_input('Enter Base Price')
    if category == 'Beverages': 
        category = 0.0
    elif category == 'Rice Bowl':
        category = 8.0
    elif category == 'Starters':
        category = 13.0
    elif category == 'Pasta':
        category = 6.0
    elif category == 'Sandwich':
        category = 10.0
    elif category == 'Biryani':
        category = 1.0
    elif category == 'Extras':
        category = 3.0
    elif category == 'Pizza':
        category = 7.0
    elif category == 'Seafood':
        category = 11.0
    elif category == 'Other Snacks':
        category = 5.0
    elif category == 'Desert':
        category = 2.0
    elif category == 'Salad':
        category = 9.0
    elif category == 'Fish':
        category = 4.0
    elif category == 'Soup':
        category = 12.0

    text = 'The Forecast of number of orders is '    
    st.markdown(f'<p style="font-family:Trebuchet MS; font-size: 35px; text-align: center"><b>{text}</b></p>', unsafe_allow_html=True)    
    out = pd.DataFrame(model.predict([[category, checkout_price, base_price]])).to_csv(sep='\t', index=False)
    out = int(float(out.split()[1]))
    st.markdown(f'<p style="font-family:Verdana; font-size: 30px;background-color:green; color:white; text-align: center"><b>{round(out)}</b></p>', unsafe_allow_html=True)