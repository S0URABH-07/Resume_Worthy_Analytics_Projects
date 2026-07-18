import pandas as pd

def load_delivery_ledger(filepath):
    print(f"Stream loading food delivery transactions from: {filepath}")
    try:
        var = pd.read_csv(filepath)
        return var
    except FileNotFoundError:
        print(f"Target dataset path unreached: {filepath}")
        raise