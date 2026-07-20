import os
from src.data_loader import load_stock_data
from src.cleaning import clean_and_engineer_stock_data
from src.analysis import compute_stock_analytics
from src.visualization import generate_stock_visualizations

def run_pipeline():
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("reports/figures", exist_ok=True)
    
    raw_file_path = "data/raw/ADANIPORTS.csv"
    raw_var = load_stock_data(raw_file_path)
    
    cleaned_var = clean_and_engineer_stock_data(raw_var)
    
    correlation_space = compute_stock_analytics(cleaned_var)
    
    generate_stock_visualizations(cleaned_var, correlation_space)
    
    processed_file_path = "data/processed/cleaned_stock_data.csv"
    cleaned_var.to_csv(processed_file_path, index=False)


if __name__ == "__main__":
    run_pipeline()