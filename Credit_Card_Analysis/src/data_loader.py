import pandas as pd

def load_transaction_data(filepath):
    print(f"Ingesting Kaggle transaction ledger from: {filepath}")
    try:
        var = pd.read_csv(filepath)
        if 'Unnamed: 0' in var.columns:
            var = var.drop(columns=['Unnamed: 0'])
        return var
    except FileNotFoundError:
        print(f"Core file not discovered at path: {filepath}")
        raise