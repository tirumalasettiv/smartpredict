'''
This is the main Streamlit application file.
'''
import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from data.data_fetcher import fetch_stock_data
from utils.helpers import format_stock_data

# List of SPY tickers (example subset)
SPY_TICKERS = ["NVDA", "MSFT", "GOOGL", "AMZN", "TSLA", "META"]

# Streamlit app
st.title("Stock Performance Viewer")

# Sidebar for ticker selection
st.sidebar.header("Select Stock Ticker")
selected_ticker = st.sidebar.selectbox("Choose a ticker:", SPY_TICKERS)

# Sidebar for time range selection
st.sidebar.header("Select Time Range")
time_range = st.sidebar.selectbox(
    "Choose a time range:",
    ["1 Day", "1 Month", "1 Quarter", "1 Year", "3 Years", "5 Years", "10 Years"]
)

# Map time range to yfinance period
time_range_map = {
    "1 Day": "1D",
    "1 Month": "1M",
    "1 Quarter": "3M",
    "1 Year": "12M",
    "3 Years": "36M",
    "5 Years": "60M",
    "10 Years": "120M",
}
period = time_range_map[time_range]

# Fetch stock data
st.write(f"Fetching data for {selected_ticker} over {time_range}...")
data = fetch_stock_data(selected_ticker, period=period)

# Format and display data
if data is not None:
    df = format_stock_data(data)
    st.write(f"Displaying data for {selected_ticker}:")
    st.dataframe(df)

    # Plot stock performance
    fig = px.line(
        df,
        x=df.index,
        y="close",
        title=f"{selected_ticker} Stock Performance",
        labels={"Close": "Closing Price", "Date": "Date"}
    )
    st.plotly_chart(fig)
else:
    st.error("No data available for the selected ticker and time range.")