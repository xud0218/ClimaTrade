# ClimaTrade

Sample run YouTube video here:
[Demo video]()

*Contributor: Duoduo Xu*

## Project Description:

ClimaTrade aims to provide modern machine learning techniques for weather predictions to help investors wager on future weather events; it will be built as a website that uses open-source weather data from online to predict the next day's highest temperature of specific cities, such as New York City and Chicago, and use the prediction to bet on Kalshi. Kalshi is an American financial exchange and prediction market based in Lower Manhattan that offers event contracts. 

Please visit this link for clarity:
[Highest temperature in NYC today?](https://kalshi.com/markets/highny/highest-temperature-in-nyc?1ClickUuid=fd7a903c-4aff-48b5-a69b-bbb536ad86d4)

## Project Deliverables:

* A user-friendly website that provides modern machine learning models to predict the next day's highest temperature and supports different plots to visualize the temperature trend.
* Use Kalshi API to make a bet efficiently based on the provided predictions.

## Data Collection and Preprocessing:

After carefully researching and comparing five different open-source weather data sources: Visual Crossing, NOAA climate data online, World Weather Online, Weatherbit, and Open Weather Map, we found that Visual Crossing provides the most detailed weather information. Therefore, Data will be downloaded and scraped from either Visual Crossing's CSV file or API. The raw data contained various features such as temperature, humidity, wind speed, cloud cover, and precipitation types. Our preprocessing steps included the following:
* Handling Missing Values: We addressed missing values using simple imputation methods. We used mean imputation for numerical features, and we used the most frequent value for categorical features like conditions.
* Feature Engineering: To capture temporal patterns, we engineered additional features, including:
    * Lagged values of temperature.
    * Moving averages over 3-day and 7-day periods.
    * Trigonometric encoding of day of the year to capture seasonality.
    * Temperature change features to add context about day-to-day changes.
* Dropping Unnecessary Features: During data preprocessing, we dropped features that needed to be more informative for our models, such as unique identifiers, non-numeric fields that did not correlate well with temperature, and redundant features that were highly collinear with other predictors. This helped reduce dimensionality, minimize overfitting risk, and improve model efficiency.
* Nowcasting Technique: We explored a form of nowcasting to predict the highest temperature for the next day based on the most recent weather data available. This technique involved using features from the current day (e.g., temperature, humidity, wind speed) to make near-term predictions. By leveraging recent data, nowcasting provided a valuable perspective for predicting rapid temperature changes, improving the model's responsiveness to changing weather conditions.

## Data Visualization:
In this project, we aim to predict the highest temperature for the next day in New York City using historical weather data. We began by analyzing the dataset, which consists of daily weather observations over a period of 6 years. To get a better understanding of the data, we created preliminary visualizations, including:
* Line plots of temperature trends over time.
* Histograms of key features such as temperature, humidity, and wind speed.
* Boxplots for features such as cloud cover, humidity, and precipitation, which indicated consistent changes across seasons.

## Models Selection:

We used various models to predict the next day's highest temperature, starting with a simple Linear Regression model to establish a baseline and moving on to more complex models. The methods we used include:
* Linear Regression: We trained a linear regression model as a baseline without delving into detailed results. The model showed promising results with a very low Mean Squared Error (MSE), but it likely overfitted the data.
* Random Forest Regressor: A Random Forest model was used to capture the non-linear dependencies in the dataset. Random Forests are effective in handling complex feature interactions, and the model performed well in generalizing to unseen data.
* Gradient Boosting Regressor: We also trained a Gradient Boosting Regressor with 100 estimators. The Gradient Boosting model demonstrated strong predictive performance, likely due to its ability to iteratively learn from residuals and reduce bias.

## Preliminary Results:
* Linear Regression: The Linear Regression model achieved an R-squared value of 1.0 on the training data, suggesting overfitting. The mean squared error was very low, indicating that it may have memorized the data rather than generalized it well.
    * Mean Squared Error: 6.841476583654742e-27
    * R-squared: 1.0
* Random Forest Regressor: The Random Forest model performed well on unseen data, demonstrating good generalizability.
    * Mean Squared Error: 0.25645066894977153
    * R-squared: 0.997311882930939
* Gradient Boosting Regressor: The Gradient Boosting model slightly outperformed the Random Forest regarding Mean Squared Error and R-squared value.
    * Mean Squared Error: 0.1856274044111826
    * R-squared: 0.9980542527093936

We also visually compared the predicted values versus the actual values for each model over 30 days. The line plot with four lines (True Values, Linear Regression, Random Forest, and Gradient Boosting) illustrated that the Gradient Boosting and Random Forest predictions were closest to the actual values, while Linear Regression had more variance in some instances.

## Next Steps:
* Hyperparameter Tuning: To further improve accuracy, we plan to perform hyperparameter tuning on Random Forest and Gradient Boost models.
* Feature Importance Analysis: Analyze which features contribute the most to the predictive accuracy of the models.
* Implement and Fine-Tune LSTM: As LSTM is a famous weather data forecasting model, it might potentially achieve better performance than current models.
* Website Design: Integrate the machine learning models and historical temperature trends into a website that advises investors.
* Finish Kalshi API Functionality: The Kalshi API call is implemented but not tested because of the trouble in creating accounts.
