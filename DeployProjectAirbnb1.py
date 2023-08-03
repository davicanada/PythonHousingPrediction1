#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import streamlit as st
import joblib

x_numerics = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0,
               'minimum_nights': 0, 'year': 0, 'month': 0, 'n_amenities': 0, 'host_listings_count': 0, 'number_of_reviews': 0}

x_tf = {'host_is_superhost': 0, 'instant_bookable': 0}

x_lists = {'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Others', 'Serviced apartment'],
            'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
            'cancellation_policy': ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period']
            }

dictionary = {}
for item in x_lists:
    for values in x_lists[item]:
        dictionary[f'{item}_{values}'] = 0


for item in x_numerics:
    if item == 'latitude' or item == 'longitude':
        values = st.number_input(f'{item}', step=0.00001, value=0.0, format="%.5f")
    elif item == 'extra_people':
        values = st.number_input(f'{item}', step=0.01, value=0.0)
    else:
        values = st.number_input(f'{item}', step=1, value=0)
    x_numerics[item] = values

for item in x_tf:
    values = st.selectbox(f'{item}', ('Yes', 'No'))
    if values == "Yes":
        x_tf[item] = 1
    else:
        x_tf[item] = 0
    
    
for item in x_lists:
    values = st.selectbox(f'{item}', x_lists[item])
    dictionary[f'{item}_{values}'] = 1
    
buttons = st.button('Predict it')

if buttons:
    dictionary.update(x_numerics)
    dictionary.update(x_tf)
    values_x = pd.DataFrame(dictionary, index=[0])
    model = joblib.load('model.joblib')
    price = model.predict(values_x)
    st.write(preco[0])


# In[ ]:




