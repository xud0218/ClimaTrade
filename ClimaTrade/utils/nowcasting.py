import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configuration
API_KEY = "JGT7BGCB9PG84US59NMH2H8X8"
BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
LOCATION = "Central Park, New York"

def fetch_weather_data(api_key, location, start_date, end_date):
    """
    Fetch weather data from Visual Crossing API.
    """
    api_url = f"{BASE_URL}{location}/{start_date}/{end_date}?unitGroup=metric&include=days&key={api_key}&contentType=json"
    response = requests.get(api_url)

    if response.status_code == 200:
        weather_data = response.json()
        return pd.DataFrame(weather_data['days'])
    elif response.status_code == 429:
        raise Exception("API Limit Exceeded: You have exceeded the maximum number of daily result records for your account. Please add a credit card to continue retrieving results.")
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


def add_engineered_features(data):
    """
    Add engineered features to the weather data.
    """
    # Ensure datetime is in datetime format
    data['datetime'] = pd.to_datetime(data['datetime'])
    
    # Calculate engineered features
    data['temp_range'] = data['tempmax'] - data['tempmin']
    data['tempmax_change'] = data['tempmax'].diff()
    data['tempmin_change'] = data['tempmin'].diff()
    data['tempmax_3d_avg'] = data['tempmax'].rolling(window=3).mean()
    data['humidity_3d_avg'] = data['humidity'].rolling(window=3).mean()
    data['windspeed_3d_avg'] = data['windspeed'].rolling(window=3).mean()
    return data

def extract_features_for_prediction(current_day):
    """
    Extract features from the most recent day's weather data.
    """
    current_day_datetime = pd.to_datetime(current_day['datetime'])
    features = {
        'dew': current_day['dew'],
        'humidity': current_day['humidity'],
        'precip': current_day['precip'],
        'precipprob': current_day['precipprob'],
        'precipcover': current_day['precipcover'],
        'snow': current_day['snow'],
        'snowdepth': current_day['snowdepth'],
        'windgust': current_day['windgust'],
        'windspeed': current_day['windspeed'],
        'winddir': current_day['winddir'],
        'sealevelpressure': current_day['pressure'],
        'cloudcover': current_day['cloudcover'],
        'visibility': current_day['visibility'],
        'solarradiation': current_day['solarradiation'],
        'solarenergy': current_day['solarenergy'],
        'uvindex': current_day['uvindex'],
        'temp_range': current_day['temp_range'],
        'tempmax_change': current_day['tempmax_change'],
        'tempmin_change': current_day['tempmin_change'],
        'tempmax_3d_avg': current_day['tempmax_3d_avg'],
        'humidity_3d_avg': current_day['humidity_3d_avg'],
        'windspeed_3d_avg': current_day['windspeed_3d_avg'],
        'day_of_year': current_day_datetime.dayofyear,
        'sin_day': np.sin(2 * np.pi * current_day_datetime.dayofyear / 365.25),
        'cos_day': np.cos(2 * np.pi * current_day_datetime.dayofyear / 365.25),
    }
    return features

def run():
    # Define date range
    current_date = (datetime.now() - timedelta(days=0)).strftime('%Y-%m-%d')  # Yesterday as end date
    start_date = (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')  # 5 days ago as start date
    
    # Fetch data
    historical_data = fetch_weather_data(API_KEY, LOCATION, start_date, current_date)
    
    # Add engineered features
    historical_data = add_engineered_features(historical_data)

    # Extract `tempmax` and `tempmin` for the most recent day
    tempmax = historical_data['tempmax'].iloc[-1]
    tempmin = historical_data['tempmin'].iloc[-1]
    
    # Extract features for the most recent day
    current_day = historical_data.iloc[-1]
    features = extract_features_for_prediction(current_day)
    
    # Convert features to DataFrame
    features_df = pd.DataFrame([features])

    return features_df, tempmax, tempmin