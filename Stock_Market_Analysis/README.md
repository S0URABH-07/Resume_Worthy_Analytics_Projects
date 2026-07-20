# Quantitative Equity Analytics & Technical Indicator Pipeline (ADANIPORTS)

An industry-grade financial data science pipeline evaluating historical price trends, moving average momentum signals (SMA_20 & SMA_50 Crossovers), VWAP divergences, delivery volume distributions, and 20-day annualized rolling volatility using Seaborn.

## Core Engineered Features
* **Quantitative Technical Indicators:** Computes daily percentage returns, fast & slow Simple Moving Averages (SMA), 20-day annualized rolling volatility, and VWAP percentage divergence.
* **Chronological Cleaning & Imputation:** Handles date parsing and forward-fills missing price ticks without lookahead bias.
* **Multi-Asset Delivery Suite:** Automatically exports 4 standalone high-resolution charts, 1 combined boardroom executive dashboard grid layout, and processed financial data files.

## Strategic Quantitative Insights
1. **Moving Average Trend Signals:** The interaction between the 20-Day Fast SMA and 50-Day Slow SMA highlights structural momentum shifts. Golden Crosses confirm sustained upward trends, while Death Crosses mark downside risk regimes.
2. **Volume & Deliverable Dynamics:** Comparing raw traded volume with `%Deliverble` volume helps distinguish speculative day-trading spikes from genuine institutional accumulation.

## Execution Guide
1. Save your raw dataset at: `data/raw/ADANIPORTS.csv`.
2. Install dependencies: `pip install -r requirements.txt`
3. Execute master pipeline script: `python main.py`