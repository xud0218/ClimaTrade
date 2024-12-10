# ClimaTrade

Sample run YouTube video here:
[Demo video](https://youtu.be/-JLXc4ZJAxY)

*Contributor: Duoduo Xu*

## Project Description:

ClimaTrade aims to leverage modern machine-learning techniques for weather predictions to help investors make informed wagers on future weather events. Built as a website, ClimaTrade will use open-source weather data to predict the next day's highest temperature in specific cities, such as New York City. Based on these predictions, the website will facilitate placing event-based contracts on Kalshi, an American financial exchange and prediction market. ClimaTrade will help investors make better financial decisions by providing accurate weather forecasts. 

For more information, please visit the following link:
[Highest temperature in NYC today?](https://kalshi.com/markets/highny/highest-temperature-in-nyc?1ClickUuid=fd7a903c-4aff-48b5-a69b-bbb536ad86d4)

## Project Deliverables:

* A user-friendly website with temperature predictions powered by advanced machine learning models.
* Visualizations of weather information and model performance, such as temperature trends over time, weather condition overlays, and true and predicted value comparison.

## Data Collection and Preprocessing:

After carefully researching five open-source weather data sources—Visual Crossing, NOAA climate data online, World Weather Online, Weatherbit, and Open Weather Map—we found that Visual Crossing provided the most detailed information for free trials. Therefore, we chose Visual Crossing as our data source, with data being downloaded via CSV files or API.
The raw data contained various features, such as temperature, humidity, wind speed, cloud cover, and precipitation. We carried out preprocessing with the following steps:
* **Handling Missing Values:** We addressed missing values using simple imputation methods. Numerical features were imputed with the mean, while categorical features like weather conditions were imputed with the most frequent value.
* **Feature Engineering:** We engineered additional features to capture temporal patterns, including:
    * **Moving averages** over 3-day and 7-day periods.
    * **Trigonometric encoding** of day of the year to capture seasonality.
    * **Temperature change features** to add context about day-to-day changes.
* **Dropping Unnecessary and "Shortcut" Features:** We dropped features that were either uninformative or redundant, such as unique identifiers and non-numeric fields that did not correlate with temperature. This helped reduce dimensionality and improve model efficiency. In addition, some features that have high correlation values with the target feature (temp max) are dropped to prevent the models from overfitting by not learning anything from the data.
* **Nowcasting Technique:** We explored nowcasting to predict the highest temperature for the next day based on the most recent weather data available. This approach leverages features like current temperature, humidity, and wind speed to improve the model's responsiveness to rapid changes in weather conditions.

## Data Visualization:
To better understand the data, we created various interactive visualizations of the dataset and models, including:
* **Temperature Trend Charts:** Users can hover over data points to view exact temperatures and dates and zoom into specific time frames. This allows for an in-depth analysis of temperature patterns and model predictions.
* **Weather Condition Overlays:** This weather information chart overlays weather variables such as precipitation, humidity, wind speed, and dew point, providing a comprehensive view of factors influencing temperature changes.
* **Comparative Model Performance Graphs:**
   * *Performance Metrics Bar Chart:* A bar chart showing all models' performance on Mean Squared Error (MSE), Mean Absolute Error (MAE), and R-squared (R²) allows users to assess which model is more suitable based on their needs for accuracy and reliability.
   * *True vs. Predicted Line Plot:* A comparative line plot showing the actual observed values against predicted values from different models (Linear Regression, Random Forest, Gradient Boosting).
To dynamically update the graph, users can select the time range of the last 7, 30, 180, or 360 days, which supports an intuitive way to evaluate how closely each model aligns with real-world data.

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

Given these considerations, we prioritized simpler and more interpretable models that performed well on sequential trends and were computationally efficient. By focusing on Random Forests and Gradient Boosting, we ensured a balance between accuracy, efficiency, and user experience.


## Preliminary Results:
* **Linear Regression:** The model achieved an R-squared value of 1.0 on the training data, suggesting overfitting. The mean squared error was very low, indicating that it may have memorized the data rather than generalized it well.
    * Mean Squared Error: 6.841476583654742e-27
    * R-squared: 1.0
* **Random Forest Regressor:** The Random Forest model performed well on unseen data, demonstrating good generalizability.
    * Mean Squared Error: 0.25645066894977153
    * R-squared: 0.997311882930939
* **Gradient Boosting Regressor:** The Gradient Boosting model slightly outperformed the Random Forest regarding Mean Squared Error and R-squared value.
    * Mean Squared Error: 0.1856274044111826
    * R-squared: 0.9980542527093936

We also visually compared the predicted values versus the actual values for each model over 30 days. The line plot with four lines (True Values, Linear Regression, Random Forest, and Gradient Boosting) illustrated that the Gradient Boosting and Random Forest predictions were closest to the actual values, while Linear Regression had more variance in some instances.

## Next Steps:
* **Hyperparameter Tuning:** To further improve accuracy, we plan to perform hyperparameter tuning on Random Forest and Gradient Boost models.
* **Feature Importance Analysis:** Analyze which features contribute the most to the predictive accuracy of the models.
* **Implement and Fine-Tune LSTM:** Given the temporal nature of weather data, we aim to experiment with Long-Short-Term Memory (LSTM) networks to achieve better performance.
* **Website Integration:** We will integrate the machine learning models and historical temperature trends into a user-friendly website that provides actionable advice for investors.
* **Finish Kalshi API Functionality:** The Kalshi API call is implemented but not tested because of the trouble in creating accounts.
