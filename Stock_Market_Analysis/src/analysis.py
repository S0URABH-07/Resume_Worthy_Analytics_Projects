import pandas as pd

def compute_stock_analytics(var):
    
    total_trading_days = var.shape[0]
    latest_close = var['Close'].iloc[-1]
    min_price = var['Close'].min()
    max_price = var['Close'].max()
    mean_volatility = var['Volatility_20D'].mean() * 100
    
    print(f"Total Recorded Business Days: {total_trading_days} Days")
    print(f"Latest Trading Price: ₹{latest_close:.2f}")
    print(f"Historical Price Bounds: ₹{min_price:.2f} (Min) - ₹{max_price:.2f} (Max)")
    print(f"Average Annualized Volatility: {mean_volatility:.2f}%")
    
    numeric_features = ['Close', 'VWAP', 'Volume', 'Trades', 'Daily_Return', 'Volatility_20D', '%Deliverble', 'VWAP_Divergence_%']
    available_cols = [c for c in numeric_features if c in var.columns]
    
    corr_matrix = var[available_cols].corr()
    print("\nMetric Correlation Space Map:")
    print(corr_matrix[['Close', 'Daily_Return', 'Volatility_20D', 'Volume']])
    
    return corr_matrix