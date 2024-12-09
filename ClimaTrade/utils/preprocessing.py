import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def preprocess_and_split_data(data, target_column='tempmax', test_size=0.2, random_state=42):
    """
    Preprocesses the input weather data and splits it into training and testing sets.
    
    Parameters:
        data (pd.DataFrame): Input dataset containing weather data.
        target_column (str): The target column for prediction. Default is 'tempmax'.
        test_size (float): Proportion of the dataset to include in the test split. Default is 0.2.
        random_state (int): Random seed for reproducibility. Default is 42.
    
    Returns:
        X_train (pd.DataFrame): Training features.
        X_test (pd.DataFrame): Testing features.
        y_train (pd.Series): Training target.
        y_test (pd.Series): Testing target.
    """
    # Convert datetime to datetime format
    data['datetime'] = pd.to_datetime(data['datetime'])

    # Drop unnecessary columns
    columns_to_drop = ['name', 'stations', 'moonphase', 'description', 'icon', 'severerisk', 
                       'sunrise', 'sunset', 'conditions', 'preciptype']
    data = data.drop(columns=columns_to_drop, errors='ignore')

    # Handle missing values
    data = data.ffill()

    # Feature Engineering
    # Daily temperature range
    data['temp_range'] = data['tempmax'] - data['tempmin']

    # Temperature Change from previous day
    data['tempmax_change'] = data['tempmax'] - data['tempmax'].shift(1)
    data['tempmin_change'] = data['tempmin'] - data['tempmin'].shift(1)

    # Rolling averages
    data['tempmax_3d_avg'] = data['tempmax'].rolling(window=3).mean()
    data['humidity_3d_avg'] = data['humidity'].rolling(window=3).mean()
    data['windspeed_3d_avg'] = data['windspeed'].rolling(window=3).mean()

    # Date-based features
    data['day_of_year'] = data['datetime'].dt.dayofyear
    data['sin_day'] = np.sin(2 * np.pi * data['day_of_year'] / 365.25)
    data['cos_day'] = np.cos(2 * np.pi * data['day_of_year'] / 365.25)

    # Drop rows with NaN values introduced by lagging or rolling
    data = data.dropna().reset_index(drop=True)

    # Drop "shortcut" columns
    additional_columns_to_drop = ['feelslikemax', 'feelslikemin', 'feelslike', 'temp', 'tempmin']
    data = data.drop(columns=additional_columns_to_drop, errors='ignore')

    # Define features (X) and target (y)
    X = data.drop(columns=['datetime', target_column])
    y = data[target_column]

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    return X_train, X_test, y_train, y_test
