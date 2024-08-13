import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import pandas as pd
import pickle

# Load the dataset
data = pd.read_csv('data/reliance_stock_data_processed.csv', parse_dates=['Date'])

# Load the Prophet model from the pickle file
with open('prophet_model.pkl', 'rb') as f:
    prophet_model = pickle.load(f)

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Reliance Stock Analysis Dashboard"), className="text-center mb-4")
    ]),
    
    # Date Picker for showing actual and predicted values
    dbc.Row([
        dbc.Col([
            html.Div([
                html.Label("Select a Date:"),
                dcc.DatePickerSingle(
                    id='date-picker-single',
                    min_date_allowed=data['Date'].min(),
                    max_date_allowed=data['Date'].max(),
                    initial_visible_month=data['Date'].min(),
                    date=data['Date'].min(),
                    display_format='YYYY-MM-DD'
                ),
                html.Div(id='date-value-output', className="mt-2")
            ], className="d-flex flex-column align-items-start"),
        ], width=12)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dcc.DatePickerRange(
                id='date-picker',
                min_date_allowed=data['Date'].min(),
                max_date_allowed=data['Date'].max(),
                start_date=data['Date'].min(),
                end_date=data['Date'].max(),
                display_format='YYYY-MM-DD'
            )
        ], width=6),
        dbc.Col([
            dcc.Dropdown(
                id='sma-ema-dropdown',
                options=[
                    {'label': 'SMA 10', 'value': 'SMA_10'},
                    {'label': 'SMA 30', 'value': 'SMA_30'},
                    {'label': 'EMA 10', 'value': 'EMA_10'},
                    {'label': 'EMA 30', 'value': 'EMA_30'}
                ],
                value=['SMA_10', 'SMA_30'],
                multi=True
            )
        ], width=6)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='price-chart', config={'displayModeBar': True})
        ], width=12)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='volume-chart', config={'displayModeBar': True})
        ], width=12)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='volatility-chart', config={'displayModeBar': True})
        ], width=6),
        dbc.Col([
            dcc.Graph(id='daily-return-histogram', config={'displayModeBar': True})
        ], width=6)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='correlation-heatmap', config={'displayModeBar': True})
        ], width=12)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='forecast-chart', config={'displayModeBar': True})
        ], width=12)
    ], className="mb-4")
])

# Define callbacks to update charts based on user input
@app.callback(
    [Output('price-chart', 'figure'),
     Output('volume-chart', 'figure'),
     Output('volatility-chart', 'figure'),
     Output('daily-return-histogram', 'figure'),
     Output('correlation-heatmap', 'figure'),
     Output('forecast-chart', 'figure')],
    [Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date'),
     Input('sma-ema-dropdown', 'value')]
)
def update_charts(start_date, end_date, selected_indicators):
    filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

    # Price chart with SMA/EMA
    price_chart = go.Figure()
    price_chart.add_trace(go.Scatter(x=filtered_data['Date'], y=filtered_data['Close'], mode='lines', name='Close Price'))
    for indicator in selected_indicators:
        price_chart.add_trace(go.Scatter(x=filtered_data['Date'], y=filtered_data[indicator], mode='lines', name=indicator))
    price_chart.update_layout(title="Price Chart with SMA/EMA", xaxis_title="Date", yaxis_title="Price")

    # Volume chart
    volume_chart = go.Figure(go.Bar(x=filtered_data['Date'], y=filtered_data['Volume'], name='Volume'))
    volume_chart.update_layout(title="Volume Chart", xaxis_title="Date", yaxis_title="Volume")

    # Volatility chart
    volatility_chart = go.Figure(go.Scatter(x=filtered_data['Date'], y=filtered_data['Volatility'], mode='lines', name='Volatility'))
    volatility_chart.update_layout(title="Volatility Chart", xaxis_title="Date", yaxis_title="Volatility")

    # Daily return histogram
    daily_return_histogram = go.Figure(go.Histogram(x=filtered_data['Daily_Return'], nbinsx=50, name='Daily Return'))
    daily_return_histogram.update_layout(title="Daily Return Histogram", xaxis_title="Daily Return", yaxis_title="Frequency")

    # Correlation heatmap
    corr_matrix = filtered_data[['Close', 'Volume', 'SMA_10', 'SMA_30', 'EMA_10', 'EMA_30', 'Daily_Return', 'Volatility']].corr()
    correlation_heatmap = go.Figure(go.Heatmap(z=corr_matrix.values, x=corr_matrix.columns, y=corr_matrix.columns, colorscale='Viridis'))
    correlation_heatmap.update_layout(title="Correlation Heatmap")

    # Forecast vs Actual (using Prophet's prediction)
    future = filtered_data[['Date', 'Volume', 'SMA_10', 'SMA_30', 'EMA_10', 'EMA_30', 'Daily_Return', 'Volatility']].rename(columns={'Date': 'ds'})
    forecast = prophet_model.predict(future)
    
    forecast_chart = go.Figure()
    forecast_chart.add_trace(go.Scatter(x=filtered_data['Date'], y=filtered_data['Close'], mode='lines', name='Actual'))
    forecast_chart.add_trace(go.Scatter(x=filtered_data['Date'], y=forecast['yhat'], mode='lines', name='Prophet Forecast'))
    forecast_chart.update_layout(title="Actual vs Prophet Forecast", xaxis_title="Date", yaxis_title="Price")

    return price_chart, volume_chart, volatility_chart, daily_return_histogram, correlation_heatmap, forecast_chart

# Callback for showing the value on the selected date
@app.callback(
    Output('date-value-output', 'children'),
    [Input('date-picker-single', 'date')]
)
def show_value_on_date(selected_date):
    if selected_date is None:
        return "Please select a date."
    
    selected_date = pd.to_datetime(selected_date)
    if selected_date not in data['Date'].values:
        return "No data available for this date."

    actual_value = data.loc[data['Date'] == selected_date, 'Close'].values[0]
    future = pd.DataFrame({
        'ds': [selected_date],
        'Volume': data.loc[data['Date'] == selected_date, 'Volume'].values,
        'SMA_10': data.loc[data['Date'] == selected_date, 'SMA_10'].values,
        'SMA_30': data.loc[data['Date'] == selected_date, 'SMA_30'].values,
        'EMA_10': data.loc[data['Date'] == selected_date, 'EMA_10'].values,
        'EMA_30': data.loc[data['Date'] == selected_date, 'EMA_30'].values,
        'Daily_Return': data.loc[data['Date'] == selected_date, 'Daily_Return'].values,
        'Volatility': data.loc[data['Date'] == selected_date, 'Volatility'].values
    })
    predicted_value = prophet_model.predict(future)['yhat'].values[0]

    return f"On {selected_date.strftime('%Y-%m-%d')}: Actual Close Price = {actual_value}, Predicted Close Price = {predicted_value}"

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
