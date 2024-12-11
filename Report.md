# ClimaTrade

Sample run YouTube video here:
[Demo video](https://youtu.be/-JLXc4ZJAxY)

*Contributor: Duoduo Xu*

## Project Description:

ClimaTrade is a weather information analysis website that visualizes weather information using dashboards and provides modern machine-learning techniques to predict weather events. It uses open-source weather data to predict the next day's highest temperature in specific cities, such as New York City. This helps investors make informed wagers on Kalshi, an American financial exchange and prediction market.

For more information, please visit the following link:
[Highest temperature in NYC today?](https://kalshi.com/markets/highny/highest-temperature-in-nyc?1ClickUuid=fd7a903c-4aff-48b5-a69b-bbb536ad86d4)

## Project Deliverables:

* A user-friendly website with temperature predictions powered by accurate machine-learning models.
* Visualizations of weather information and model performance, such as temperature trends over time, weather condition overlays, and true and predicted value comparison.

## Data Collection and Preprocessing:

After carefully researching five open-source weather data sources—Visual Crossing, NOAA climate data online, World Weather Online, Weatherbit, and Open Weather Map—we found that Visual Crossing provided the most detailed information for free trials. Therefore, we chose Visual Crossing as our data source, with data being downloaded via CSV files or retrieved by API calls.
The raw data contained various features, such as temperature, humidity, wind speed, cloud cover, and precipitation. We carried out preprocessing with the following steps:
* **Handling Missing Values:** We addressed missing values using simple imputation methods. Numerical features were imputed with the mean, while categorical features like weather conditions were imputed with the most frequent value.
* **Feature Engineering:** We engineered additional features to capture temporal patterns, including:
    * **Moving averages** over 3-day and 7-day periods.
    * **Trigonometric encoding** of day of the year to capture seasonality.
    * **Temperature change features** to add context about day-to-day changes.
* **Dropping Unnecessary and "Shortcut" Features:** We dropped features that were either uninformative or redundant, such as unique identifiers and non-numeric fields that did not correlate with temperature. This helped reduce dimensionality and improve model efficiency. In addition, some features that are highly correlated with the target feature (temp max) are dropped to prevent the models from overfitting by not learning anything from the data.
* **Nowcasting Technique:** We explored nowcasting to predict the highest temperature for the next day based on the most recent weather data available. This approach leverages features like current temperature, humidity, and wind speed to improve the model's responsiveness to rapid changes in weather conditions.

## Data Visualization:
To better understand the data, we created several interactive visualizations of the dataset and models, including:
* **Temperature Trend Charts:** Users can hover over data points to view exact temperatures and dates and zoom into specific time frames. This allows for an in-depth analysis of temperature patterns and model predictions.
* **Weather Condition Overlays:** This weather information chart overlays weather variables such as precipitation, humidity, wind speed, and dew point, providing a comprehensive view of factors influencing temperature changes.
* **Comparative Model Performance Graphs:**
   * *Performance Metrics Bar Chart:* A bar chart showing all models' performance on Mean Squared Error (MSE), Mean Absolute Error (MAE), and R-squared (R²) allows users to assess which model is more suitable based on their needs for accuracy and reliability.
   * *True vs. Predicted Line Plot:* A comparative line plot showing the actual observed values against predicted values from different models (Linear Regression, Random Forest, Gradient Boosting). To dynamically update the graph, users can select the time range of the last 7, 30, 180, or 360 days, which supports an intuitive way to evaluate how closely each model aligns with real-world data.
* **Real-time Weather Information:** A card object that displays the real-time weather information retrieved from Visual Crossing API.
* **Model Predictions:** The predicted next day's highest temperature of each model will be displayed to the user. 

## **Data Modeling Methods**

We evaluated several models to predict the next day's highest temperature, starting with simpler models and progressing to more advanced ones:

### **Linear Regression**
- Established as a baseline model to provide a benchmark for comparison.  
- Showed promising results with very low Mean Squared Error (MSE) but likely overfitted the data.

### **Random Forest Regressor**
- Captured non-linear dependencies and complex feature interactions.  
- Demonstrated strong generalization to unseen data and performed well on test datasets.

### **Gradient Boosting Regressor**
- Outperformed other models by iteratively reducing residual errors and bias.  
- Achieved the best predictive accuracy among all tested models.

### **Long Short-Term Memory (LSTM)**
LSTM is a recurrent neural network (RNN) designed to learn long-term dependencies in sequential data, such as text, speech, and time series. It is well-suited for tasks involving sequences because it can prevent the vanishing or exploding gradient problem that often plagues traditional RNN architectures.

However, after testing, the LSTM model was not included in the website for the following reasons:

1. **Performance Limitations**:  
   - Despite the sequential nature of weather data, the LSTM model did not outperform simpler models such as Random Forest or Gradient Boosting in terms of predictive accuracy.  
   - The addition of LSTM did not provide significant improvements over existing models, even with hyperparameter tuning.

2. **Complexity and Compilation Time**:  
   - LSTMs require significantly more computational resources and training time than simpler models.  
   - The additional compile-time and resources needed to deploy an LSTM model for a real-time application outweighed its potential benefits.

Given these considerations, we prioritized simpler and more interpretable models that performed well on sequential trends and were computationally efficient. Focusing on Random Forests and Gradient Boosting, we balanced accuracy and efficiency with user experience.

PS: the fine-tuned LSTM can be found in Google Colab notebook, **ClimaTrade.ipynb**.

## Results:
* **Linear Regression:** The model achieved an R-squared value of 0.99 on the training data, suggesting overfitting. The MSE and MAE are low, indicating that it may have memorized the data rather than generalized it well.
    * Mean Squared Error: 0.3465134335911787
    * Mean Absolute Error: 0.43834924792325175
    * R-squared: 0.9962379236743456
* **Random Forest Regressor:** The Random Forest model performed well on unseen data, demonstrating good generalizability.
    * Mean Squared Error: 1.7645513576309821
    * Mean Absolute Error: 0.980683371298406
    * R-squared: 0.9808423678725917
* **Gradient Boosting Regressor:** The Gradient Boosting model slightly outperformed the Random Forest regarding the balanced MSE, MAE, and R-squared value.
    * Mean Squared Error: 1.0547909680611989
    * Mean Absolute Error: 0.7836856355807986
    * R-squared: 0.9885481954095352
  * **Long Short-Term Memory (LSTM):** Although the LSTM achieved the lowest MAE, it does not outperform the other models' prediction of the next day's highest temperature.
     * Mean Absolute Error: 0.015393544919788837
* **Data Table:**
  
| Date       | True Value | LR Prediction | RF Prediction | GB Prediction | LSTM Prediction |
|------------|------------|---------------|---------------|---------------|-----------------|
| 12/4/2024  | 41         | 40.4          | 39.6          | 39            | 40.3            |
| 12/5/2024  | 39.5       | 39.7          | 38.5          | 39.3          | 41.4            |
| 12/6/2024  | 34.1       | 33.6          | 35.8          | 34.2          | 32.6            |
| 12/7/2024  | 39.9       | 40            | 40.5          | 38.2          | 38.9            |
| 12/8/2024  | 54.1       | 53.5          | 49.5          | 50.1          | 51.7            |
| 12/9/2024  | 50.7       | 49.8          | 48.2          | 48.6          | 49.3            |
| 12/10/2024 | 48         | 49.3          | 50.6          | 51            | 51.6            |

* **Evaluation Table:**
  
| Model | MSE       | MAE       |
|-------|-----------|-----------|
| LR    | 0.502857  | 0.600000  |
| RF    | 5.788929  | 2.064286  |
| GB    | 5.192857  | 1.871429  |
| LSTM  | 4.004286  | 1.785714  |

Surprisingly, linear regression performed the best for real-world weather forecasting even though it seems to overfit the data. This might be because models like Random Forest (RF), Gradient Boosting (GB), and LSTM are more complex and prone to overfitting on smaller datasets or data with noise. In contrast, Linear Regression (LR) is less flexible and thus less likely to overfit, which might explain its superior performance in this dataset. In this case, the Linear Regression model achieved my goal of an average ± 0.5 max temperature error.
