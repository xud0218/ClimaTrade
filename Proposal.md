# ClimaTrade

*Contributor: Duoduo Xu*

## Project Description:

ClimaTrade aims to demonstrate the relationship between weather predictions and stock market movements, it will build as a website that use open-source weather data from online to predict the next day highest temperature of specific cities, such as New York City and Chicago, and use the prediction to buy stock from Kalshi.

## Clear Goal:

The goal is to achieve accurate next day high-temperature predictions for NYC and Chicago with an error margin below 0.5 degrees, leading to stock purchases on Kalshi based on prediction confidence.

## Data Collection:

Data will be scraped from Visual Crossing's API and NOAA's public datasets. The data will be preprocessed to handle missing values, normalize temperature, and align with stock market timing data.

## Desired Models:

This project will mainly use Recurrent Neural Network to predict the next day high-temperature because RNN is designed to handle time series data by maintaining memory of past information. We will explore different architectures, such as LSTMs and GRUs, to optimize predictive performance, comparing these against a simple linear regression model as a baseline.

## Visualization:

As the weather data are time-series data, I will use simple line plot to visualize the historical highest temperature and model predicted next day high-temperature.

## Test Plan:

The data will separate as 80% training and 20% testing. For example, if we want to predict the highest temperature for Fall 2024, the training data will be September 1th to November 1th 2023 and the testing data will be November 2nd to 30th 2023\. We will evaluate the model's accuracy using Root Mean Squared Error.   
