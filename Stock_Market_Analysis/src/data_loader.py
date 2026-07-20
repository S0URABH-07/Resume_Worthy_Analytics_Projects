import pandas as pd

def load_stock_data(filepath):
    print(f"Ingesting ADANIPORTS equity ledger from: {filepath}")
    try:
        var = pd.read_csv(filepath)
        return var
    except FileNotFoundError:
        print(f"Core file not discovered at path: {filepath}")
        raise