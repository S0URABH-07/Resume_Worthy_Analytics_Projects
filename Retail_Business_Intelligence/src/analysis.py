import pandas as pd

def compute_executive_kpis(var):
    
    gross_sales = var['SalesAmount'].sum()
    total_discounts = var['DiscountAmount'].sum()
    net_sales = var['Net_Sales'].sum()
    net_profit = var['Net_Profit'].sum()
    overall_margin = (net_profit / net_sales) * 100 if net_sales > 0 else 0
    total_orders = var['OrderNumber'].nunique()
    total_items_sold = var['OrderQuantity'].sum()
    avg_fulfillment = var['Fulfillment_Days'].mean() if 'Fulfillment_Days' in var.columns else 0
    
    print(f"Gross Sales Amount: ${gross_sales:,.2f}")
    print(f"Total Discounts Applied: ${total_discounts:,.2f}")
    print(f"Net Enterprise Sales: ${net_sales:,.2f}")
    print(f"Net Enterprise Profit: ${net_profit:,.2f}")
    print(f"Overall Profit Margin: {overall_margin:.2f}%")
    print(f"Total Unique Orders: {total_orders:,}")
    print(f"Total Units Sold: {total_items_sold:,}")
    print(f"Avg Fulfillment Time: {avg_fulfillment:.1f} Days")
    
    # Regional performance matrix
    regional_summary = var.groupby('SalesRegion').agg({
        'Net_Sales': 'sum',
        'Net_Profit': 'sum',
        'OrderNumber': 'nunique'
    }).rename(columns={'OrderNumber': 'Total_Orders'}).sort_values(by='Net_Sales', ascending=False)
    
    regional_summary['Profit_Margin_%'] = (regional_summary['Net_Profit'] / regional_summary['Net_Sales']) * 100
    
    print("\nRegional Performance Matrix:")
    print(regional_summary)
    
    # Monthly trend aggregator
    monthly_kpis = var.groupby('YearMonth').agg({
        'Net_Sales': 'sum',
        'Net_Profit': 'sum',
        'OrderNumber': 'nunique',
        'OrderQuantity': 'sum'
    }).reset_index()
    
    return monthly_kpis