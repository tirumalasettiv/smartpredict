
def fetch_stock_data(ticker='NVDA', period="12M"):
    import requests
    api_key = 'PKR3524QYQ5NYWMYIT6WPSVXBX'
    api_secret = 'EMuQVETSkD4iTKzP3MXArTz62T8aEQVQLBkw8ffdGozu'
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


