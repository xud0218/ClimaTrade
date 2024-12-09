import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def model_performance_eval(lr_model, rf_model, gb_model, X_test, y_test):
    """
    Create a DataFrame summarizing the performance of multiple models
    and return the DataFrame for visualization.

    Parameters:
        lr_model: Trained Linear Regression model.
        rf_model: Trained Random Forest model.
        gb_model: Trained Gradient Boosting model.
        X_test (pd.DataFrame): Test features.
        y_test (pd.Series): True target values for the test set.

    Returns:
        pd.DataFrame: Model performance metrics.
    """
    # Make predictions
    y_pred_lr = lr_model.predict(X_test)
    y_pred_rf = rf_model.predict(X_test)
    y_pred_gb = gb_model.predict(X_test)

    # Compute metrics
    mae_lr = mean_absolute_error(y_test, y_pred_lr)
    mse_lr = mean_squared_error(y_test, y_pred_lr)
    r2_lr = r2_score(y_test, y_pred_lr)

    mae_rf = mean_absolute_error(y_test, y_pred_rf)
    mse_rf = mean_squared_error(y_test, y_pred_rf)
    r2_rf = r2_score(y_test, y_pred_rf)

    mae_gb = mean_absolute_error(y_test, y_pred_gb)
    mse_gb = mean_squared_error(y_test, y_pred_gb)
    r2_gb = r2_score(y_test, y_pred_gb)

    # Create DataFrame for performance metrics
    model_data = {
        "Model": ["Linear Regression", "Random Forest", "Gradient Boosting"],
        "Mean Absolute Error": [mae_lr, mae_rf, mae_gb],
        "Mean Squared Error": [mse_lr, mse_rf, mse_gb],
        "R2 Score": [r2_lr, r2_rf, r2_gb]
    }
    df = pd.DataFrame(model_data)

    return df
