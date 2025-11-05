
def fetch_stock_data(ticker='NVDA', period="12M"):
    import streamlit as st
    import requests

    
    api_key = st.secrets["api_key"]
    api_secret = st.secrets["api_secret"]


    if not api_key or not api_secret:
        
        # Access the environment variables
        from dotenv import load_dotenv
        import os
        # Load environment variables from .env file
        load_dotenv()
        api_key = os.getenv('api_key')
        api_secret = os.getenv('api_secret')
        
    base_url = 'https://data.alpaca.markets/v2/stocks/bars'
    
    # Define the API endpoint and parameters
    url = (           
        base_url + 
        "?symbols=" + ticker +
        "&timeframe=3M"
        "&start=2000-01-03T00%3A00%3A00Z"
        "&end=2026-01-04T00%3A00%3A00Z"
        "&limit=10000"
        "&adjustment=split"
        "&feed=iex"
        "&sort=desc"
    )

    # Set the request headers with API credentials
    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": api_key,
        "APCA-API-SECRET-KEY": api_secret
    }

    # Make the GET request and parse the JSON response
    response = requests.get(url, headers=headers).json()
    return response


