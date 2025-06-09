# 📈 Quantitative Stock Forecasting System

## 🧠 Objective

Build a predictive system to forecast 5-day stock returns and generate actionable trade signals (`BUY`, `SELL`, `HOLD`) using a combination of:

- Historical price data
- Technical indicators
- Market sentiment
- Fundamental factors
- Macro-economic indicators

## 🌟 Primary Goals

### 🎯 1. Expected Return Forecasting (Regression)
- **Objective**: Predict short-term % returns (e.g., next 5-10 days)
- **Use Case**: Alpha generation, portfolio optimization
- **Model Type**: Regression (XGBoost, LSTM, Transformer)

### 🎯 2. Signal Generation (Multi-class Classification)
- **Objective**: Translate return predictions into discrete trading signals
- **Use Case**: Strategy automation and backtesting
- **Model Type**: Classification

### 🎯 3. Volatility Forecasting (Risk Modeling)
- **Objective**: Predict risk levels over the next N days
- **Use Case**: Risk-adjusted allocations, position sizing, trade filtering
- **Model Type**: GARCH, LSTM, Transformer-based models

## 🔍 Scope

- Initial tickers: AAPL, TSLA, MSFT, AMZN, NVDA
- Time horizon: All available historical data (from listing date)
- Environment: Local-only, macOS (Apple Silicon), PyCharm, MSSQL

## 🤩 Data Sources

| Type               | Source/API              |
|--------------------|-------------------------|
| Price Data         | Alpha Vantage, Yahoo Finance |
| Technical Indicators | TA-Lib, pandas-ta        |
| Sentiment          | GNews API, Reddit        |
| Fundamentals       | Financial Modeling Prep  |
| Macroeconomics     | FRED API                 |

## 🧠 Architecture Overview

1. Data Collection & Ingestion
2. Preprocessing & Feature Engineering
3. Label Generation
4. Model Training (XGBoost / LSTM / Transformer)
5. Signal Classification
6. Volatility Forecasting
7. Backtesting (Backtrader)
8. Evaluation & Risk Adjustment
9. Tableau Dashboard (via MSSQL)
10. Automated ETL + Retrain Schedulers

## 📦 Dependencies (to be installed later)

- Python 3.11+
- pandas, numpy, scikit-learn, xgboost
- SQLAlchemy, pyodbc
- TA-Lib, vaderSentiment
- Backtrader
- Tableau Desktop (local)

## 🗓️ Milestone 1: Setup + Data Ingestion

- [x] Finalize project scope (this doc)
- [ ] Initialize Git repo
- [ ] Create conda/venv environment
- [ ] Setup MSSQL DB and tables
- [ ] Build API wrappers for Alpha Vantage and GNews
- [ ] Load raw price + sentiment data into MSSQL

## 🧭 Project Roadmap

### Milestone 2: Feature Engineering
- [ ] Merge technical, sentiment, and macro features
- [ ] Normalize and handle missing values
- [ ] Add lag-based and rolling-window indicators

### Milestone 3: Label Creation
- [ ] Compute 5-day forward return
- [ ] Encode `BUY/SELL/HOLD` signals

### Milestone 4: Model Training
- [ ] Train XGBoost and baseline regressors
- [ ] Validate using time-series split
- [ ] Optimize hyperparameters

### Milestone 5: Backtesting & Evaluation
- [ ] Build Backtrader-based simulation
- [ ] Evaluate strategy metrics (Sharpe, drawdown, win ratio)

### Milestone 6: Volatility Modeling
- [ ] Build risk models using GARCH / LSTM
- [ ] Integrate volatility into position sizing

### Milestone 7: Tableau Dashboard
- [ ] Export predictions to MSSQL
- [ ] Build dashboard for signal monitoring

### Milestone 8: Automation
- [ ] Daily ETL + prediction job
- [ ] Weekly model retrain scheduler

---

## 📂 Folder Structure (Planned)

```
quant-forecast/
│
├── data_ingestion/
│   └── fetch_prices.py
│   └── fetch_sentiment.py
├── features/
│   └── compute_technical.py
│   └── merge_features.py
├── models/
│   └── train_model.py
│   └── predict_signals.py
│   └── volatility_model.py
├── backtesting/
│   └── simulate_strategy.py
├── dashboard/
│   └── tableau_exports/
├── utils/
│   └── sql_connector.py
├── notebooks/
│   └── exploratory_analysis.ipynb
├── requirements.txt
└── README.md
```

---

## 🔄 Next Steps

1. ✅ Finalize project scope (this doc)
2. 🔧 Create MSSQL schemas
3. 💪 Begin coding data ingestion scripts
