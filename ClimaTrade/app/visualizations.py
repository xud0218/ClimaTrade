from utils.preprocessing import preprocess_and_split_data
from utils.evaluation import model_performance_eval
from utils.nowcasting import *
import plotly.graph_objects as go
import pandas as pd
import joblib

# Load data
weather_data = pd.read_csv('./data/Central_Park_Weather.csv')

X_train, X_test, y_train, y_test = preprocess_and_split_data(weather_data)

# Load pre-trained models
lr_model = joblib.load('models/linear_regression_model.pkl')
rf_model = joblib.load('models/random_forest_model.pkl')
gb_model = joblib.load('models/gradient_boosting_model.pkl')

def get_weather_and_predictions():
    features_df, tempmax, tempmin = run()
    
    predicted_tempmax_rf = rf_model.predict(features_df)[0] * 9 / 5 + 32
    predicted_tempmax_lr = lr_model.predict(features_df)[0] * 9 / 5 + 32
    predicted_tempmax_gb = gb_model.predict(features_df)[0] * 9 / 5 + 32
    
    # Current weather information
    current_weather = {
        "tempmax": tempmax,
        "tempmin": tempmin,
        "precip": features_df['precip'].iloc[0],
        "windspeed": f"{features_df['windspeed'].iloc[0]} kph",
        "humidity": features_df['humidity'].iloc[0],
        "dew": features_df['dew'].iloc[0]
    }
    
    # Predictions
    model_predictions = {
        "RandomForest": predicted_tempmax_rf,
        "LinearRegression": predicted_tempmax_lr,
        "GradientBoosting": predicted_tempmax_gb
    }
    
    return current_weather, model_predictions

# Temperature Trend Chart
def create_temperature_trend_chart():
    weather_data['datetime'] = pd.to_datetime(weather_data['datetime'])
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=weather_data['datetime'], y=weather_data['tempmax'],
                             mode='lines+markers', name='Max Temperature'))
    fig.update_layout(
        title="Temperature Trends Over Time in NYC",
        xaxis_title="Date",
        yaxis_title="Temperature (°C)",
        hovermode="x unified"
    )
    return fig

# Weather Condition Overlays
def create_weather_condition_overlay():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=weather_data['datetime'], y=weather_data['feelslike'], mode='lines', name='Temperature'))
    fig.add_trace(go.Scatter(x=weather_data['datetime'], y=weather_data['humidity'], mode='lines', name='Humidity'))
    fig.add_trace(go.Scatter(x=weather_data['datetime'], y=weather_data['windspeed'], mode='lines', name='Wind Speed'))
    fig.add_trace(go.Scatter(x=weather_data['datetime'], y=weather_data['precip'], mode='lines', name='Precipitation'))
    fig.add_trace(go.Scatter(x=weather_data['datetime'], y=weather_data['dew'], mode='lines', name='Dew Point'))
    fig.update_layout(
        title="Weather Condition Overlays",
        xaxis=dict(title="Date"),
        yaxis=dict(title="Weather Conditions")
    )
    return fig

def create_model_performance_dashboard():
    df = model_performance_eval(lr_model, rf_model, gb_model, X_test, y_test)

    fig = go.Figure()

    # Add MAE, MSE, and R2 as separate bars
    fig.add_trace(go.Bar(x=df['Model'], y=df['Mean Absolute Error'], name='MAE'))
    fig.add_trace(go.Bar(x=df['Model'], y=df['Mean Squared Error'], name='MSE'))
    fig.add_trace(go.Bar(x=df['Model'], y=df['R2 Score'], name='R2'))

    # Update layout
    fig.update_layout(
        title="Model Performance Metrics",
        xaxis_title="Model",
        yaxis_title="Metric Value",
        barmode="group"
    )

    return fig

def plot_true_vs_predicted(selected_days):
    n_days = min(selected_days, len(y_test))

    # Make predictions
    y_pred_lr = lr_model.predict(X_test)
    y_pred_rf = rf_model.predict(X_test)
    y_pred_gb = gb_model.predict(X_test)

    fig = go.Figure()

    # Add True Values
    fig.add_trace(go.Scatter(
        x=list(range(n_days)), 
        y=y_test.reset_index(drop=True)[:n_days],
        mode='lines',
        name='True Values'
    ))

    # Add Linear Regression Predictions
    fig.add_trace(go.Scatter(
        x=list(range(n_days)), 
        y=y_pred_lr[:n_days],
        mode='lines',
        name='Linear Regression Prediction',
        line=dict(dash='dash', color='orange')
    ))

    # Add Random Forest Predictions
    fig.add_trace(go.Scatter(
        x=list(range(n_days)), 
        y=y_pred_rf[:n_days],
        mode='lines',
        name='Random Forest Prediction',
        line=dict(dash='dash', color='green')
    ))

    # Add Gradient Boosting Predictions
    fig.add_trace(go.Scatter(
        x=list(range(n_days)), 
        y=y_pred_gb[:n_days],
        mode='lines',
        name='Gradient Boosting Prediction',
        line=dict(dash='dash', color='red')
    ))

    # Update layout
    fig.update_layout(
        title="True Values vs Predicted Values",
        xaxis_title="Days",
        yaxis_title="Temperature (°C)",
        legend_title="Legend"
    )

    return fig
