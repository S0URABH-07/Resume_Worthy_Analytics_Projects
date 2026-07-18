import matplotlib.pyplot as plt
import seaborn as sns

def generate_analytical_plots(var, corr_matrix):
    print("...[Visualization]...")
    sns.set_theme(style="whitegrid", palette="muted")
    plt.rcParams['font.family'] = 'sans-serif'
    
    # Plot 1: Box Plot (Financial value spread across standard merchant categories)
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=var, x='category', y='amt', hue='Fraud_Label', palette='Set2')
    plt.xticks(rotation=30, ha='right')
    plt.yscale('log')  # Log scale handles extreme fraudulent dollar amounts gracefully
    plt.title('Spending Profiles: Transaction Value Spread across Retail Categories', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Merchant Spending Category')
    plt.ylabel('Amount Spent ($ - Log Scale)')
    plt.tight_layout()
    plt.savefig("reports/figures/chart1_category_amounts.png", dpi=300)
    plt.close()
    
    # Plot 2: Temporal KDE Distribution Plot (Hourly velocity curves)
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=var, x='TransactionHour', hue='Fraud_Label', fill=True, common_norm=False, palette='coolwarm', alpha=0.5, linewidth=2)
    plt.title('Temporal Risk Profile: Time of Day Distribution Curves by Fraud Status', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Hour of Day (24h Clock)')
    plt.ylabel('Density Weight')
    plt.tight_layout()
    plt.savefig("reports/figures/chart2_temporal_fraud.png", dpi=300)
    plt.close()
    
    # Plot 3: Heatmap Matrix (Core Feature Association Spaces Map)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, square=True, cbar=False)
    plt.title('Risk Vector Covariances: Structural Feature Correlation Space', fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig("reports/figures/chart3_correlation_matrix.png", dpi=300)
    plt.close()

    # Plot 4: Bar Count Plot (Demographic Exposure across Gender Codes)
    plt.figure(figsize=(10, 6))
    sns.countplot(data=var, x='gender', hue='Fraud_Label', palette='viridis', edgecolor='black')
    plt.title('Portfolio Exposure: Transaction Volume Distribution Spreads by Gender', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Gender Code')
    plt.ylabel('Recorded Actions Count')
    plt.tight_layout()
    plt.savefig("reports/figures/chart4_gender_volumes.png", dpi=300)
    plt.close()

    fig, axes = plt.subplots(2, 2, figsize=(24, 18))
    
    # Panel [0, 0]: Categories Box Plot
    sns.boxplot(data=var, x='category', y='amt', hue='Fraud_Label', palette='Set2', ax=axes[0, 0])
    axes[0, 0].set_yscale('log')
    axes[0, 0].tick_params(axis='x', rotation=30)
    axes[0, 0].set_title('Transaction Value Ranges Across Retail Categories (Log Scale)', fontsize=13, fontweight='bold')
    axes[0, 0].set_xlabel('Category')
    axes[0, 0].set_ylabel('Amount ($)')
    
    # Panel [0, 1]: Hourly Density Line
    sns.kdeplot(data=var, x='TransactionHour', hue='Fraud_Label', fill=True, common_norm=False, palette='coolwarm', alpha=0.5, linewidth=2, ax=axes[0, 1])
    axes[0, 1].set_title('Hourly Transaction Velocity Curve Density Comparison', fontsize=13, fontweight='bold')
    axes[0, 1].set_xlabel('Hour of the Day')
    
    # Panel [1, 0]: Pearson Correlation Grid Map
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, square=True, ax=axes[1, 0], cbar=False)
    axes[1, 0].set_title('Metric Interaction & Covariance Space Grid Map', fontsize=13, fontweight='bold')
    
    # Panel [1, 1]: Demographics Gender Split
    sns.countplot(data=var, x='gender', hue='Fraud_Label', palette='viridis', edgecolor='black', ax=axes[1, 1])
    axes[1, 1].set_title('Account Volume Distributions Across Gender Slices', fontsize=13, fontweight='bold')
    axes[1, 1].set_xlabel('Gender')
    axes[1, 1].set_ylabel('Transaction Count')
    
    plt.tight_layout()
    plt.savefig("reports/figures/credit_card_executive_master_dashboard.png", dpi=300, bbox_inches='tight')
    plt.close()
