import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Importing page layouts
from pages import about, forecasting

# Define the app layout
app.layout = html.Div([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("About", href="/about")),
            dbc.NavItem(dbc.NavLink("Forecasting", href="/forecasting")),
        ],
        brand="Reliance Stock Analysis",
        brand_href="/",
        color="primary",
        dark=True,
    ),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Update the page content based on URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname == '/about':
        return about.layout
    elif pathname == '/forecasting':
        return forecasting.layout
    else:
        return about.layout  # Default to about page if the path doesn't match

# Register the callbacks for forecasting page
forecasting.register_callbacks(app)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
