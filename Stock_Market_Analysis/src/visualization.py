import os
import matplotlib.pyplot as plt
import seaborn as sns

def generate_stock_visualizations(var, corr_matrix):
    print("...[Visualization]...")
    
    sns.set_theme(style="whitegrid", palette="muted")
    plt.rcParams['font.family'] = 'sans-serif'
    
    output_dir = "reports/figures"
    os.makedirs(output_dir, exist_ok=True)
    
    # Price & SMA Trend Crossover
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=var, x='Date', y='Close', label='Close Price', color='navy', linewidth=1.5)
    sns.lineplot(data=var, x='Date', y='SMA_20', label='20-Day SMA (Fast)', color='orange', linestyle='--', linewidth=1.5)
    sns.lineplot(data=var, x='Date', y='SMA_50', label='50-Day SMA (Slow)', color='crimson', linestyle=':', linewidth=1.5)
    plt.title('Technical Trend Analysis: Close Price vs SMA Crossovers (ADANIPORTS)', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Date')
    plt.ylabel('Price (₹)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "chart1_price_moving_averages.png"), dpi=300)
    plt.close()
    
    # Daily Return Density Distribution
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=var.dropna(subset=['Daily_Return']), x='Daily_Return', fill=True, color='teal', alpha=0.4, linewidth=2)
    plt.title('Risk Profile: Daily Return Distribution Density (ADANIPORTS)', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Daily Percentage Return')
    plt.ylabel('Density')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "chart2_returns_kde_distribution.png"), dpi=300)
    plt.close()
    
    # Rolling Volatility Timeline
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=var, x='Date', y='Volatility_20D', color='darkred', linewidth=1.5)
    plt.title('Volatility Profile: 20-Day Annualized Rolling Volatility Timeline', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Date')
    plt.ylabel('Annualized Volatility')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "chart3_rolling_volatility_boxplot.png"), dpi=300)
    plt.close()
    
    # Feature Correlation Heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, square=True, cbar=False)
    plt.title('Equity Metric Covariance Space Map (ADANIPORTS)', fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "chart4_asset_correlation_heatmap.png"), dpi=300)
    plt.close()
    
    fig, axes = plt.subplots(2, 2, figsize=(22, 16))
    
    sns.lineplot(data=var, x='Date', y='Close', label='Close Price', ax=axes[0, 0], color='navy', linewidth=1.5)
    sns.lineplot(data=var, x='Date', y='SMA_20', label='20-Day SMA', ax=axes[0, 0], color='orange', linestyle='--', linewidth=1.5)
    sns.lineplot(data=var, x='Date', y='SMA_50', label='50-Day SMA', ax=axes[0, 0], color='crimson', linestyle=':', linewidth=1.5)
    axes[0, 0].set_title('Technical Trend & Moving Average Signals', fontsize=13, fontweight='bold', pad=15)
    axes[0, 0].set_ylabel('Price (₹)')
    
    sns.kdeplot(data=var.dropna(subset=['Daily_Return']), x='Daily_Return', fill=True, color='teal', alpha=0.4, linewidth=2, ax=axes[0, 1])
    axes[0, 1].set_title('Daily Return Probability Density Profile', fontsize=13, fontweight='bold', pad=15)
    axes[0, 1].set_xlabel('Daily Return')
    
    sns.lineplot(data=var, x='Date', y='Volatility_20D', color='darkred', linewidth=1.5, ax=axes[1, 0])
    axes[1, 0].set_title('20-Day Annualized Volatility Timeline', fontsize=13, fontweight='bold', pad=15)
    axes[1, 0].set_ylabel('Annualized Volatility')
    
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, square=True, ax=axes[1, 1], cbar=False)
    axes[1, 1].set_title('Parameter Interaction & Covariance Space Map', fontsize=13, fontweight='bold', pad=15)
    
    plt.tight_layout()
    dashboard_path = os.path.join(output_dir, "stock_market_executive_master_dashboard.png")
    plt.savefig(dashboard_path, dpi=300, bbox_inches='tight')
    plt.close()