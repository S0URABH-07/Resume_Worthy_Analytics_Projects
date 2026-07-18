import matplotlib.pyplot as plt
import seaborn as sns

def build_reporting_graphics(var, corr_matrix):
    print("[Visualization] Drawing standalone plots and boardroom dashboard grid...")
    sns.set_theme(style="whitegrid", palette="muted")
    plt.rcParams['font.family'] = 'sans-serif'
    
    # Box Plot (Fulfillment duration variants across traffic constraints)
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=var, x='Road_traffic_density', y='Time_taken(min)', palette='Set2', hue='Road_traffic_density', legend=False)
    plt.title('Logistics Efficiency: Total Delivery Time Spreads by Traffic Density', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Road Traffic Density Class')
    plt.ylabel('Time Taken (Minutes)')
    plt.tight_layout()
    plt.savefig("reports/figures/chart1_traffic_delivery_time.png", dpi=300)
    plt.close()
    
    # Demand Density Curves
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=var, x='Order_Hour', fill=True, color='darkorange', alpha=0.4, linewidth=2.5)
    plt.title('Market Demand Windows: Hourly Traffic Distribution Density', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Hour of the Day (24h Clock)')
    plt.ylabel('Order Probability Mass')
    plt.tight_layout()
    plt.savefig("reports/figures/chart2_peak_hours_kde.png", dpi=300)
    plt.close()
    
    # Heatmap Matrix Covariance Space
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, square=True, cbar=False)
    plt.title('Logistics Parameter Covariance & Correlation Space Matrix Map', fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig("reports/figures/chart3_correlation_matrix.png", dpi=300)
    plt.close()

    # Bar Plot (Weather Impact Rankings)
    plt.figure(figsize=(10, 6))
    weather_order = var.groupby('Weatherconditions')['Time_taken(min)'].mean().sort_values(ascending=False).index
    sns.barplot(data=var, x='Time_taken(min)', y='Weatherconditions', order=weather_order, palette='viridis', hue='Weatherconditions', errorbar=None, legend=False)
    plt.title('Environmental Constraints: Mean Order Fulfillment Speed by Weather', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Average Delivery Time (Minutes)')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig("reports/figures/chart4_weather_efficiency.png", dpi=300)
    plt.close()

    fig, axes = plt.subplots(2, 2, figsize=(22, 16))
    
    sns.boxplot(data=var, x='Road_traffic_density', y='Time_taken(min)', palette='Set2', hue='Road_traffic_density', legend=False, ax=axes[0, 0])
    axes[0, 0].set_title('Logistics Efficiency Variances Across Traffic Density Classes', fontsize=13, fontweight='bold')
    axes[0, 0].set_ylabel('Time Taken (Min)')
    axes[0, 0].set_xlabel('')
    
    sns.kdeplot(data=var, x='Order_Hour', fill=True, color='darkorange', alpha=0.4, linewidth=2, ax=axes[0, 1])
    axes[0, 1].set_title('Hourly Order Volume Pattern Distributions', fontsize=13, fontweight='bold')
    axes[0, 1].set_xlabel('Hour of Day')
    
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, square=True, ax=axes[1, 0], cbar=False)
    axes[1, 0].set_title('Operational Supply Chain Parameter Correlation Map', fontsize=13, fontweight='bold')
    
    sns.barplot(data=var, x='Time_taken(min)', y='Weatherconditions', order=weather_order, palette='viridis', hue='Weatherconditions', errorbar=None, legend=False, ax=axes[1, 1])
    axes[1, 1].set_title('Environmental Service SLA Rankings (Fulfillment Impact)', fontsize=13, fontweight='bold')
    axes[1, 1].set_xlabel('Mean Minutes')
    axes[1, 1].set_ylabel('')
    
    plt.tight_layout()
    plt.savefig("reports/figures/food_delivery_executive_master_dashboard.png", dpi=300)
    plt.close()