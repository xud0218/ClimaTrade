import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback
from app.visualizations import (
    create_temperature_trend_chart,
    create_weather_condition_overlay,
    create_model_performance_dashboard,
    plot_true_vs_predicted,
    get_weather_and_predictions
)
@callback(
    Output('true-vs-predicted-graph', 'figure'),
    Input('day-range-dropdown', 'value')
)
def update_true_vs_predicted_graph(selected_days):
    return plot_true_vs_predicted(selected_days)

current_weather, model_predictions = get_weather_and_predictions()

def create_weather_card(current_weather):
    return dbc.Card(
        dbc.CardBody([
            html.H2("Current Weather Information", className="card-title", style={'textAlign': 'center'}),
            html.Div([
                html.P(f"Highest Temperature: {current_weather['tempmax']}°C", style={'fontSize': '16px'}),
                html.P(f"Lowest Temperature: {current_weather['tempmin']}°C", style={'fontSize': '16px'}),
                html.P(f"Precipitation: {current_weather['precip']}mm", style={'fontSize': '16px'}),
                html.P(f"Wind Speed: {current_weather['windspeed']}", style={'fontSize': '16px'}),
                html.P(f"Humidity: {current_weather['humidity']}%", style={'fontSize': '16px'}),
                html.P(f"Dew Point: {current_weather['dew']}°C", style={'fontSize': '16px'}),
            ])
        ]),
        className="shadow-sm bg-light",
        style={'marginBottom': '20px', 'padding': '20px'}
    )

def create_prediction_card(model_predictions):
    return dbc.Card(
        dbc.CardBody([
            html.H2("Model Predictions: NYC Next Day Highest Temperature", className="card-title", style={'textAlign': 'center'}),
            html.Div([
                html.P(f"RandomForest: {model_predictions['RandomForest']:.2f}°F", style={'fontSize': '16px'}),
                html.P(f"LinearRegression: {model_predictions['LinearRegression']:.2f}°F", style={'fontSize': '16px'}),
                html.P(f"GradientBoosting: {model_predictions['GradientBoosting']:.2f}°F", style={'fontSize': '16px'}),
            ])
        ]),
        className="shadow-sm bg-light",
        style={'marginBottom': '20px', 'padding': '20px'}
    )

def create_layout():
    return html.Div([
        html.Div([
            html.Img(
                src="/assets/icon/weather-app.png",
                style={'height': '50px', 'marginRight': '20px'}
            ),
            html.H1("ClimaTrade Dashboard", style={'display': 'inline', 'verticalAlign': 'middle'})
        ], style={'textAlign': 'center', 'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center', 'marginBottom': '20px'}),
        
        # Current Weather Card Section
        html.Div([
            create_weather_card(current_weather)
        ], style={'marginBottom': '20px'}),

        # Model Predictions Card Section
        html.Div([
            create_prediction_card(model_predictions)
        ], style={'marginBottom': '40px'}),

        # Temperature Trend Chart Section
        html.Div([
            html.H2("Dataset", className="card-title", style={'textAlign': 'center'}),
            dcc.Graph(figure=create_temperature_trend_chart())
        ], style={'marginBottom': '40px'}),
        
        # Weather Condition Overlays Section
        html.Div([
            dcc.Graph(figure=create_weather_condition_overlay())
        ], style={'marginBottom': '40px'}),
        
        # Model Performance Metrics Section
        html.Div([
            html.H2("Models", className="card-title", style={'textAlign': 'center'}),
            dcc.Graph(figure=create_model_performance_dashboard())
        ], style={'marginBottom': '40px'}),
        
        # True vs Predicted Visualization Section
        html.Div([
            dcc.Dropdown(
                id='day-range-dropdown',
                options=[
                    {'label': 'Last 7 Days', 'value': 7},
                    {'label': 'Last 30 Days', 'value': 30},
                    {'label': 'Last 180 Days', 'value': 180},
                    {'label': 'Last 360 Days', 'value': 360}
                ],
                value=30,  # Default to 30 days
                clearable=False,
                style={'width': '50%', 'marginBottom': '20px', 'marginLeft': 'auto', 'marginRight': 'auto'}
            ),
            dcc.Graph(id='true-vs-predicted-graph')  # Placeholder for dynamic graph
        ])
    ])

