import pandas as pd

def load_retail_data(filepath):
    print(f"Ingesting enterprise sales transaction ledger from: {filepath}")
    try:
        var = pd.read_csv(filepath)
        return var
    except FileNotFoundError:
        print(f"Core dataset file not discovered at path: {filepath}")
        raise