# 📈 Quantitative Stock Forecasting System

## 🧠 Objective

Build a predictive system to forecast 5-day stock returns and generate actionable trade signals (BUY, SELL, HOLD) using a combination of:

* Historical price data
* Technical indicators
* Market sentiment
* Fundamental factors
* Macro-economic indicators

## 🌟 Primary Goals

### 🎯 1. Expected Return Forecasting (Regression)

* Predict short-term % returns (e.g., next 5-10 days)
* Use Case: Alpha generation, portfolio optimization
* Model Type: Regression (XGBoost, LSTM, Transformer)

### 🎯 2. Signal Generation (Multi-class Classification)

* Translate return predictions into discrete trading signals
* Use Case: Strategy automation and backtesting
* Model Type: Classification

### 🎯 3. Volatility Forecasting (Risk Modeling)

* Predict risk levels over the next N days
* Use Case: Risk-adjusted allocations, position sizing, trade filtering
* Model Type: GARCH, LSTM, Transformer-based models

## 🔍 Scope

* Tickers: AAPL, TSLA, MSFT, AMZN, NVDA
* Time Horizon: Full history since IPO
* Environment: Local-only, macOS, PyCharm, PostgreSQL

## 🤩 Data Sources

| Type                 | Source/API                 |
| -------------------- | -------------------------- |
| Price Data           | Alpha Vantage, Yahoo       |
| Technical Indicators | TA-Lib, pandas-ta          |
| Sentiment            | GNews API, Reddit, Finnhub |
| Fundamentals         | Financial Modeling Prep    |
| Macroeconomics       | FRED API                   |

## 🧠 Architecture Overview

1. Data Collection & Ingestion
2. Preprocessing & Feature Engineering
3. Label Generation
4. Model Training (XGBoost / LSTM / Transformer)
5. Signal Classification
6. Volatility Forecasting
7. Backtesting (Backtrader)
8. Evaluation & Risk Adjustment
9. Tableau Dashboard (via PostgreSQL)
10. Automated ETL + Retrain Schedulers

## 📦 Dependencies

* Python 3.11+
* pandas, numpy, scikit-learn, xgboost
* SQLAlchemy, psycopg2
* TA-Lib, vaderSentiment
* Backtrader
* Tableau Desktop

## 🗓️ Milestones

### Milestone 1: Setup + Data Ingestion

* ✅ Finalize scope
* ✅ Initialize Git repo
* ✅ Setup venv
* ✅ Setup PostgreSQL DB & tables
* ✅ Load price + sentiment data

### Milestone 2: Feature Engineering

* ✅ Technical feature scripts (TA-Lib)
* ✅ Sentiment scoring + aggregation
* ✅ Macro & fundamentals ingestion
* ✅ Merge and normalize all features

### Milestone 3: Label Creation

* ⏳ Compute forward returns
* ⏳ Encode signals

### Milestone 4: Model Training

* ⏳ Baseline regressors + classifiers
* ⏳ Time series split validation

### Milestone 5: Backtesting & Evaluation

* ⏳ Strategy simulation with Backtrader
* ⏳ Metrics (Sharpe, drawdown, etc.)

### Milestone 6: Volatility Modeling

* ⏳ GARCH / LSTM based volatility prediction

### Milestone 7: Tableau Dashboard

* ⏳ Export predictions to DB
* ⏳ Live dashboard

### Milestone 8: Automation

* ⏳ Daily ETL job
* ⏳ Weekly model retrain

## 📂 Folder Structure

```
quant-forecast/
│
├── data_ingestion/
│   ├── fetch_prices.py
│   ├── fetch_sentiment.py
│   ├── fetch_fundamentals.py
│   └── fetch_macro.py
│
├── features/
│   ├── compute_technical.py
│   ├── merge_features.py
│
├── models/
│   ├── train_model.py
│   ├── predict_signals.py
│   └── volatility_model.py
│
├── backtesting/
│   └── simulate_strategy.py
│
├── dashboard/
│   └── tableau_exports/
│
├── database/
│   ├── sql_connector.py
│   ├── technical.py
│   ├── sentiment.py
│   ├── fundamentals.py
│   └── macro.py
│
├── notebooks/
│   └── exploratory_analysis.ipynb
├── .env
├── requirements.txt
└── README.md
```

## 🔑 API Keys

* Alpha Vantage: `OAMTD9BGJ01HYGUX`
* GNews API: `023bc968f5addc9809524cee9cca7b54`
* Finnhub API: `MWqwfOzycCDt9jWD4r1zFscVaLuAUr28`

## 🔄 Next Steps

* ⏳ Finalize label creation
* ⏳ Begin training baseline models
* ⏳ Set up model evaluation pipeline
