import pandas as pd

def load_churn_data(filepath):
    print(f"Stream loading customer ledger matrix from: {filepath}")
    try:
        var = pd.read_csv(filepath)
        return var
    except FileNotFoundError:
        print(f"Core file not discovered at path: {filepath}")
        raise   