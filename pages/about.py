from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.H2("About This Dashboard", className="mt-4 mb-4"),
    html.P(
        """
        This dashboard is designed to provide an interactive analysis of Reliance stock data. 
        It allows users to explore various financial indicators such as Simple Moving Averages (SMA), 
        Exponential Moving Averages (EMA), daily returns, and volatility. Additionally, 
        it provides a forecasting feature using the SARIMA and Prophet models to predict future stock prices.
        """,
        className="mb-4"
    ),
    
    html.H4("Data Overview"),
    html.P(
        """
        The data used in this dashboard is historical stock price data for Reliance Industries. 
        The dataset includes the following columns:
        """,
        className="mb-3"
    ),
    
    html.Ul([
        html.Li("Date: The date of the trading day."),
        html.Li("Open: The price at which the stock opened on the trading day."),
        html.Li("High: The highest price reached during the trading day."),
        html.Li("Low: The lowest price reached during the trading day."),
        html.Li("Close: The price at which the stock closed on the trading day."),
        html.Li("Volume: The number of shares traded on that day."),
        html.Li("SMA 10: 10-day Simple Moving Average."),
        html.Li("SMA 30: 30-day Simple Moving Average."),
        html.Li("EMA 10: 10-day Exponential Moving Average."),
        html.Li("EMA 30: 30-day Exponential Moving Average."),
        html.Li("Daily Return: The daily percentage change in the stock price."),
        html.Li("Volatility: A measure of the stock's price fluctuations over a certain period."),
    ]),
    
    html.H4("What are SMAs and EMAs?"),
    html.P(
        """
        The Simple Moving Average (SMA) and Exponential Moving Average (EMA) are technical indicators 
        used by traders to smooth out price data and identify trends over time. 
        While SMAs give equal weight to all price data, EMAs give more weight to recent prices, 
        making them more sensitive to recent changes in the stock's price.
        """,
        className="mb-4"
    ),

    html.H4("Forecasting Models: SARIMA and Prophet"),
    html.P(
        """
        The dashboard uses two models for forecasting stock prices: SARIMA and Prophet.
        """,
        className="mb-3"
    ),
    
    html.H5("SARIMA Model"),
    html.P(
        """
        SARIMA (Seasonal AutoRegressive Integrated Moving Average) is a widely used statistical model 
        for time series forecasting. It captures linear patterns in the data and accounts for both 
        trend and seasonality, making it a powerful tool for forecasting stock prices with regular 
        patterns over time.
        """,
        className="mb-4"
    ),
    
    html.H5("Prophet Model"),
    html.P(
        """
        Prophet is a forecasting model developed by Facebook. It is specifically designed to handle 
        time series data with strong seasonal effects and a large number of missing data points. 
        Prophet is flexible and allows the inclusion of additional regressors (like trading volume, 
        moving averages, etc.), making it suitable for more complex forecasting scenarios.
        """,
        className="mb-4"
    ),

    html.H4("Using the Dashboard"),
    html.P(
        """
        - Use the Date Picker to select a date range for analysis.
        - Use the dropdown to toggle between different financial indicators (SMA, EMA).
        - View the forecasted stock prices using the SARIMA and Prophet models on the Forecasting page.
        """,
        className="mb-4"
    ),
    
    html.H4("Disclaimer"),
    html.P(
        """
        This dashboard is for educational purposes only. The stock prices and forecasts displayed 
        should not be considered financial advice.
        """,
        className="mb-4"
    ),
])
