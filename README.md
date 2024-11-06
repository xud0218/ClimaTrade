# ClimaTrade

Sample run YouTube video here:
[Demo video](https://youtu.be/-JLXc4ZJAxY)

*Contributor: Duoduo Xu*

## Project Description:

ClimaTrade aims to leverage modern machine-learning techniques for weather predictions to help investors make informed wagers on future weather events. Built as a website, ClimaTrade will use open-source weather data to predict the next day's highest temperature in specific cities, such as New York City. Based on these predictions, the website will facilitate placing event-based contracts on Kalshi, an American financial exchange and prediction market. ClimaTrade will help investors make better financial decisions by providing accurate weather forecasts. 

For more information, please visit the following link:
[Highest temperature in NYC today?](https://kalshi.com/markets/highny/highest-temperature-in-nyc?1ClickUuid=fd7a903c-4aff-48b5-a69b-bbb536ad86d4)

## Project Deliverables:

* A user-friendly website that provides temperature predictions using modern machine learning models and supports different visualizations of temperature trends.
* Efficient use of Kalshi API calls to make bets based on the provided predictions.

## Data Collection and Preprocessing:

After carefully researching five open-source weather data sources—Visual Crossing, NOAA climate data online, World Weather Online, Weatherbit, and Open Weather Map—we found that Visual Crossing provided the most detailed information for free trials. Therefore, we chose Visual Crossing as our data source, with data being downloaded via CSV files or API.
The raw data contained various features, such as temperature, humidity, wind speed, cloud cover, and precipitation. We carried out preprocessing with the following steps:
* **Handling Missing Values:** We addressed missing values using simple imputation methods. Numerical features were imputed with the mean, while categorical features like weather conditions were imputed with the most frequent value.
* **Feature Engineering:** We engineered additional features to capture temporal patterns, including:
    * **Lagged values** of temperature.
    * **Moving averages** over 3-day and 7-day periods.
    * **Trigonometric encoding** of day of the year to capture seasonality.
    * **Temperature change features** to add context about day-to-day changes.
* **Dropping Unnecessary Features:** We dropped features that were either uninformative or redundant, such as unique identifiers and non-numeric fields that did not correlate with temperature. This helped reduce dimensionality, minimize overfitting risk, and improve model efficiency.
* **Nowcasting Technique:** We explored nowcasting to predict the highest temperature for the next day based on the most recent weather data available. This approach leverages features like current temperature, humidity, and wind speed to improve the model's responsiveness to rapid changes in weather conditions.

## Data Visualization:
To better understand the data, we created preliminary visualizations of daily weather observations spanning six years, including:
* **Line Plots:** Visualizing temperature trends over time helped identify seasonal patterns and trends.
* **Histograms:** We analyzed key features such as temperature, humidity, and wind speed to observe data distribution.
* **Boxplots:** Examining features like cloud cover, humidity, and precipitation revealed consistent seasonal changes, aiding in feature engineering.

## Data Modeling Methods:

We evaluated several models to predict the next day's highest temperature, starting with simpler models and progressing to more advanced ones:
* **Linear Regression:** We trained a linear regression model as a baseline without delving into detailed results. The model showed promising results with a very low Mean Squared Error (MSE), but it likely overfitted the data.
* **Random Forest Regressor:** A Random Forest model was used to capture the non-linear dependencies in the dataset. Random Forests effectively handle complex feature interactions, and the model performed well in generalizing to unseen data.
* **Gradient Boosting Regressor:** We also trained a Gradient Boosting Regressor with 100 estimators. The Gradient Boosting model demonstrated strong predictive performance, likely due to its ability to iteratively learn from residuals and reduce bias.

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
