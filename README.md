# 📈 Quantitative Stock Forecasting System

## 🧠 Objective

Build a predictive system to forecast 5-day stock returns and generate actionable trade signals (`BUY`, `SELL`, `HOLD`) using:

- Historical price data
- Technical indicators
- Market sentiment
- Fundamental factors
- Macro-economic indicators

---

## 🌟 Primary Goals

### 🎯 1. Expected Return Forecasting (Regression)
- Predict 5-10 day % returns
- Model: XGBoost, LSTM, Transformer

### 🎯 2. Signal Generation (Classification)
- Convert returns into `BUY`, `SELL`, `HOLD`
- Model: Classifier

### 🎯 3. Volatility Forecasting (Risk Modeling)
- Predict N-day risk
- Model: GARCH, LSTM, Transformer

---

## 🔍 Scope

- Tickers: AAPL, TSLA, MSFT, AMZN, NVDA
- Time Horizon: All available historical data
- Environment: Local-only, macOS (Apple Silicon), PyCharm
- Database: ✅ **PostgreSQL**

---

## 🤩 Data Sources

| Type                | Source/API                      |
|---------------------|----------------------------------|
| Price Data          | Alpha Vantage, Yahoo Finance     |
| Technical Indicators| TA-Lib, pandas-ta                |
| Sentiment           | GNews API, Reddit                |
| Fundamentals        | Financial Modeling Prep          |
| Macroeconomics      | FRED API                         |

---

## 🧠 Architecture Overview

1. ✅ Data Collection & Ingestion  
2. ✅ Preprocessing & Feature Engineering (`technical_features`)  
3. 🔜 Label Generation (`target`, 5-day return)  
4. 🔜 Model Training  
5. 🔜 Signal Classification  
6. 🔜 Volatility Modeling  
7. 🔜 Backtesting  
8. 🔜 Evaluation & Risk Adjustment  
9. 🔜 Tableau Dashboard  
10. 🔜 Automated Retraining + ETL

---

## 📦 Dependencies (setup later)

- Python 3.11+
- `pandas`, `numpy`, `scikit-learn`, `xgboost`
- `sqlalchemy`, `psycopg2`, `dotenv`
- `vaderSentiment`, `TA-Lib`
- `backtrader`
- `yfinance` (for historical data)
- Tableau Desktop (local)

---

## 🗓️ Milestone 1: Setup + Ingestion ✅

- ✅ Finalized scope
- ✅ Initialized Git repo
- ✅ Created `.env` with PostgreSQL + API keys
- ✅ Built and tested `fetch_prices.py`
- ✅ Created and populated `price_data` table
- ✅ Created and tested `compute_technical.py`
- ✅ Generated `technical_features` in PostgreSQL

---

## 🧭 Project Roadmap

### Milestone 2: Feature Engineering
- 🔜 Merge technical, sentiment, macro
- 🔜 Normalize and handle nulls
- 🔜 Lag + rolling features

### Milestone 3: Label Creation
- 🔜 Compute 5-day return
- 🔜 Encode labels for classification

### Milestone 4: Model Training
- 🔜 Train XGBoost, baseline classifiers
- 🔜 Time-series split + eval
- 🔜 Save trained model

### Milestone 5: Backtesting
- 🔜 Simulate strategy with `Backtrader`

### Milestone 6: Volatility Modeling
- 🔜 Build GARCH / LSTM models
- 🔜 Add volatility-adjusted signals

### Milestone 7: Dashboard
- 🔜 Export results to PostgreSQL
- 🔜 Build Tableau dashboard

### Milestone 8: Automation
- 🔜 Daily ingestion, retrain scripts

---

## 📂 Folder Structure

```bash
quant-forecast/
│
├── data_ingestion/
│   ├── fetch_prices.py            # ✅ Done
│   ├── fetch_sentiment.py         # In progress
│   ├── fetch_fundamentals.py      # 🔜 To be added
│   └── fetch_macro.py             # 🔜 To be added
│
├── features/
│   ├── compute_technical.py       # ✅ Done
│   └── merge_features.py          # 🔜 Next
│
├── models/
│   ├── train_model.py             # 🔜
│   ├── predict_signals.py         # 🔜
│   └── volatility_model.py        # 🔜
│
├── backtesting/
│   └── simulate_strategy.py       # 🔜
│
├── dashboard/
│   └── tableau_exports/           # 🔜
│
├── utils/
│   └── sql_connector.py           # ✅ optional
│
├── notebooks/
│   └── exploratory_analysis.ipynb # Optional
│
├── requirements.txt               # ✅ to update
├── .env.template                  # ✅ PostgreSQL + API
└── README.md
