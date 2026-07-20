# Enterprise Retail Business Intelligence & Executive Performance Report

An industry-style analytical case study evaluating enterprise retail sales, net profit drivers, promotional discount impacts, fulfillment lead times, and category profit margins using Seaborn.

## Core Engineered Architecture
* **Executive Metric Calculations:** Computes core enterprise KPIs including Gross Sales, Net Sales ($\text{SalesAmount} - \text{DiscountAmount}$), Net Profit, Profit Margin Percentage, and Fulfillment Days ($\text{Shipdate} - \text{Orderdate}$).
* **Data Hygiene & Date Parsing:** Robust chronological parsing across `Orderdate`, `Duedate`, and `Shipdate` to prevent pipeline breaks and calculate fulfillment efficiency.
* **Modular Multi-Asset Suite:** Automatically exports 4 standalone boardroom graphics, 1 combined executive dashboard grid, and processed analytical datasets.

## Key Executive Findings & Business Insights
1. **Promotional Discount Impact:** Evaluating `DiscountAmount` against top-line volume highlights whether discounting strategies genuinely drive net margin growth or simply erode bottom-line profitability.
2. **Logistics & Fulfillment SLAs:** Tracking `Fulfillment_Days` across `SalesRegion` pinpoints supply chain bottlenecks between order placement and shipping execution.

## Execution Guide
1. Save your raw dataset at: `data/raw/retail_sales_dataset.csv`.
2. Install dependencies: `pip install -r requirements.txt`
3. Execute master pipeline script: `python main.py`