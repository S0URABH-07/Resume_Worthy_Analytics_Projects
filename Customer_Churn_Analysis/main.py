import os
from src.data_loader import load_churn_data
from src.cleaning import clean_churn_matrix
from src.analysis import compute_retention_kpis
from src.visualization import generate_analytical_plots

def run_pipeline():
    print("[Pipeline] Initializing workspace directories framework...")
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True) 
    os.makedirs("reports/figures", exist_ok=True) 

    # 1. Ingest your single customer dataset directly from data/raw/
    raw_file_path = "data/raw/customer_churn.csv"
    raw_var = load_churn_data(raw_file_path)
    
    # 2. Pipeline Execution Data Hygiene Cleanse & Imputation
    cleaned_var = clean_churn_matrix(raw_var)
    
    # 3. Compute Business Key Metrics & Continuous Variable Covariances
    correlation_space = compute_retention_kpis(cleaned_var)
    
    # 4. Generate Reporting Visualization Portfolio Suite
    generate_analytical_plots(cleaned_var, correlation_space)
    
    # 5. Export cleaned dataset file back out into the processed folder directory
    processed_file_path = "data/processed/cleaned_transactions.csv"
    cleaned_var.to_csv(processed_file_path, index=False)
    
    print("\n===========================================================")
    print("===   PIPELINE SUCCESSFUL: PORTFOLIO ASSETS GENERATED   ===")
    print("===========================================================")

if __name__ == "__main__":
    run_pipeline()