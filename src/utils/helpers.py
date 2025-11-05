'''
This file will contain utility functions, such as formatting or data transformation.

'''

import pandas as pd

def format_stock_data(data):
    data = pd.DataFrame(data["bars"][list(data["bars"].keys())[0]])

    # Rename columns for clarity
    data.rename(columns={
        "t": "timestamp",
        "o": "open",
        "h": "high",
        "l": "low",
        "c": "close",
        "v": "volume",
        "vw": "vwap",
        "n": "transactions"
    }, inplace=True)

    data["timestamp"] = pd.to_datetime(data["timestamp"])
    data.set_index("timestamp", inplace=True)
    data.sort_index(inplace=True, ascending=False)
    
    return data