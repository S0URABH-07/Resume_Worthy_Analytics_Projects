import pandas as pd
import numpy as np

def clean_and_engineer_stock_data(var):
    print("[Cleaning] Executing quantitative feature engineering for NSE equity data...")
    
    var = var.copy()
    var.columns = var.columns.str.strip()
    
    var['Date'] = pd.to_datetime(var['Date'], errors='coerce')
    var = var.dropna(subset=['Date']).sort_values('Date').reset_index(drop=True)
    
    numeric_cols = ['Prev Close', 'Open', 'High', 'Low', 'Last', 'Close', 'VWAP', 'Volume', 'Turnover', 'Trades', 'Deliverable Volume', '%Deliverble']
    for col in numeric_cols:
        if col in var.columns:
            var[col] = pd.to_numeric(var[col], errors='coerce')
            
    var['Close'] = var['Close'].ffill()
    var['VWAP'] = var['VWAP'].ffill()
    
    var['Daily_Return'] = var['Close'].pct_change()
    
    var['SMA_20'] = var['Close'].rolling(20).mean()
    var['SMA_50'] = var['Close'].rolling(50).mean()
    
    var['Volatility_20D'] = var['Daily_Return'].rolling(20).std() * np.sqrt(252)
    
    var['VWAP_Divergence_%'] = ((var['Close'] - var['VWAP']) / var['VWAP']) * 100
    
    return var