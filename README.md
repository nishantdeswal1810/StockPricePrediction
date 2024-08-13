# Reliance Stock Price Prediction Dashboard

This project involves building a dashboard to predict and analyze Reliance stock prices. The dashboard is created using Dash and Plotly, and it is deployed on Render.

## Table of Contents

- [Project Overview](#project-overview)
- [Data Collection](#data-collection)
- [Feature Engineering](#feature-engineering)
- [Model Training](#model-training)
- [Model Evaluation](#model-evaluation)
- [Dashboard Development](#dashboard-development)
- [Deployment](#deployment)
- [Installation](#installation)
- [Results](#results)


## Project Overview

This project aims to predict Reliance stock prices using time series models and display the results on an interactive dashboard. Two models were trained: SARIMA and Prophet, with Prophet being selected for deployment due to its superior performance.

## Data Collection

- The data was scraped using the `yfinance` library.
- We collected the last one year of data for Reliance Industries stock.

## Feature Engineering

We introduced the following columns through feature engineering:

- **SMA_10:** 10-day Simple Moving Average
- **SMA_30:** 30-day Simple Moving Average
- **EMA_10:** 10-day Exponential Moving Average
- **EMA_30:** 30-day Exponential Moving Average
- **Daily_Return:** The daily percentage change in the stock price
- **Volatility:** A measure of the stock's price fluctuations over a certain period

## Model Training

We trained two models to forecast stock prices:

1. **SARIMA (Seasonal AutoRegressive Integrated Moving Average):**
   - A statistical model commonly used for time series forecasting.
   
2. **Prophet:**
   - Developed by Facebook, this model handles time series data with strong seasonal effects and can accommodate missing data points.

## Model Evaluation

The models were evaluated using the following metrics:

- **RMSE (Root Mean Squared Error)**
- **MAE (Mean Absolute Error)**
- **R² (Coefficient of Determination)**

### Evaluation Results

**SARIMA Model:**
- RMSE: 40.31
- MAE: 29.33
- R²: 0.837

**Prophet Model:**
- RMSE: 14.62
- MAE: 11.03
- R²: 0.997

Due to its better performance, the Prophet model was selected for the final deployment.

## Dashboard Development

The interactive dashboard was built using Dash and Plotly. The dashboard allows users to:

- View various financial indicators such as SMA, EMA, daily returns, and volatility.
- Forecast future stock prices using the Prophet model.

## Deployment

The dashboard was deployed on Render. You can access it via the following link:

[Stock Price Prediction Dashboard](https://stockpriceprediction-av0t.onrender.com/about)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/nishantdeswal1810/StockPricePrediction.git
   cd StockPricePrediction
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
3. Run the application:
   ```bash
   python app.py

## Results

The final deployed dashboard allows users to interactively explore the stock data and view forecasts based on the Prophet model. The results demonstrate the effectiveness of Prophet in accurately predicting future stock prices.

