import pandas as pd
import numpy as np

def clean_transaction_matrix(var):
    print("[Cleaning] Executing data hygiene functions for financial logs...")
    
    var['amt'] = pd.to_numeric(var['amt'], errors='coerce')
    var['amt'] = var['amt'].fillna(var['amt'].median())
    
    var['is_fraud'] = pd.to_numeric(var['is_fraud'], errors='coerce').fillna(0).astype(int)
    
    for col in ['merchant', 'category', 'gender', 'state', 'job']:
        if col in var.columns:
            var[col] = var[col].astype(str).str.strip().fillna('Unknown')
            
    var['trans_date_trans_time'] = pd.to_datetime(var['trans_date_trans_time'], errors='coerce')
    
    var['TransactionHour'] = var['trans_date_trans_time'].dt.hour
    var['DayOfWeek'] = var['trans_date_trans_time'].dt.day_name()
    
    if 'dob' in var.columns:
        var['dob'] = pd.to_datetime(var['dob'], errors='coerce')
        var['Customer_Age'] = 2026 - var['dob'].dt.year
        var['Customer_Age'] = var['Customer_Age'].fillna(var['Customer_Age'].median()).astype(int)

    var['Fraud_Label'] = var['is_fraud'].map({1: 'Fraudulent', 0: 'Legitimate'})
    
    return var