# Stock Performance Viewer

This is a Streamlit application that allows users to select stock tickers from the SPY index and view their performance over various time ranges.

## Features
- Select stock tickers from a predefined list of SPY tickers.
- View stock performance over time ranges like 1 day, 1 month, 1 quarter, 1 year, 3 years, 5 years, and 10 years.
- Interactive line chart visualization of stock performance.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/stock-performance-app.git
   cd stock-performance-app
   ```


2. Install dependencies:
   ```   
   pip install -r requirements.txt
   ```
 

3. Run the app:
   ``` 
   streamlit run src/app.py
   ```

### Dependencies
- Streamlit
- yfinance
- pandas
- plotly