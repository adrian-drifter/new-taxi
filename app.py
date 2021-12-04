import streamlit as st

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')
'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
'''


## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''
date = st.text_input('input date and time')
lon1 = st.text_input('input pickup longitud')
lat1 = st.text_input('input pickup latitude')
lon2 = st.text_input('input dropoff longitude')
lat2 = st.text_input('input dropoff latitude')
num_pass = st.text_input('input number of passengers')
url = 'https://taxifare.lewagon.ai/predict?pickup_datetime=2012-10-06%2012:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown(
        'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'
    )
'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''


import requests


param = {
    'pickup_datetime': date,
    'pickup_longitude': lon1,
    'pickup_latitude': lat1,
    'dropoff_longitude': lon2,
    'dropoff_latitude': lat2,
    'passenger_count': num_pass
}

response = requests.get('https://taxifare.lewagon.ai/predict', params=param).json()

st.text(f'the fare will be: {response["prediction"]}')
