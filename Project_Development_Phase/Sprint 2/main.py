import streamlit as st
import pandas as pd
import pickle

formData = st.container()
model = pickle.load(open('demandest.pkl', 'rb'))
data = pd.read_csv('transformedData.csv')

with formData:
    st.image('wallpaperflare.com_wallpaper.jpg')
    text = 'Food Demand Forecaster'
    st.markdown(f'<p style="font-family:Trebuchet MS; font-size: 53px; text-align: center"><b>{text.upper()}</b></p>', unsafe_allow_html=True)    
    
    homepage = st.selectbox('Homepage Featured', data['homepage_featured'].unique())
    emailer = st.selectbox('emailer for Promotion', data['emailer_for_promotion'].unique())
    opArea = st.slider("Operational Area", 2.0, 7.0)
    cuisine = st.selectbox('Cuisine', data['cuisine'].unique())
    city_code = st.text_input('Enter the City code')
    region_code = st.text_input('Enter the Region code')
    category = st.selectbox('category', data['category'].unique())
    # button = st.button('Forecast the Number of Orders')
    # st.markdown('<p style="text-align: center"></p>', unsafe_allow_html=True)
    # # if button:
    if homepage == 'Yes': 
        homepage = 1
    else:
        homepage = 0
        
    if emailer == 'Yes': 
        emailer = 1
    else:
        emailer = 0
        
    if cuisine == 'Thai': 
        cuisine = 3.0
    elif cuisine == 'Indian':
        cuisine = 1.0
    elif cuisine == 'Italian':
        cuisine = 2.0
    elif cuisine == 'Continental':
        cuisine = 0.0
        
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
    out = pd.DataFrame(model.predict([[homepage, emailer, opArea, cuisine, city_code, region_code, category]])).to_csv(sep='\t', index=False)
    st.markdown(f'<p style="font-family:Verdana; font-size: 30px;background-color:red; color:white; text-align: center"><b>{out.split()[1]}</b></p>', unsafe_allow_html=True)