import pandas as pd
import numpy as np

def clean_churn_matrix(var):
    print("[Cleaning] Executing data hygiene and datatype enforcement functions...")
    
    var.columns = var.columns.str.strip()
    
    # 2. Datatype Enforcement & Missing Value Resolution
    for col in ['Age', 'Tenure', 'Usage Frequency', 'Support Calls', 'Payment Delay', 'Total Spend', 'Last Interaction']:
        if col in var.columns:
            var[col] = pd.to_numeric(var[col], errors='coerce')
            var[col] = var[col].fillna(var[col].median())
            
    # Impute categorical variables safely
    for col in ['Gender', 'Subscription Type', 'Contract Length']:
        if col in var.columns:
            var[col] = var[col].astype(str).str.strip().fillna('Unknown')
            
    if 'Churn' in var.columns:
        var['Churn'] = pd.to_numeric(var['Churn'], errors='coerce').fillna(0).astype(int)
        var['Churn_Label'] = var['Churn'].map({1: 'Churned', 0: 'Retained'})
        
    # 3. ADVANCED BUSINESS FEATURE ENGINEERING
    var['Spend_Velocity'] = np.where(var['Tenure'] > 0, var['Total Spend'] / var['Tenure'], var['Total Spend'])
    
    var['Customer_Friction_Score'] = var['Support Calls'] * (var['Payment Delay'] + 1)
    
    return var