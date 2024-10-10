# ClimaTrade

*Contributor: Duoduo Xu*

## Project Description:

ClimaTrade aims to provide modern machine learning techniques for weather predictions to help investors wager on future weather events; it will be built as a website that uses open-source weather data from online to predict the next day's highest temperature of specific cities, such as New York City and Chicago, and use the prediction to bet on Kalshi. Kalshi is an American financial exchange and prediction market-based in Lower Manhattan that offers event contracts. 

Please visit this link for clarity:
[Highest temperature in NYC today?](https://kalshi.com/markets/highny/highest-temperature-in-nyc?1ClickUuid=fd7a903c-4aff-48b5-a69b-bbb536ad86d4)

## Clear Goal:

The goal is to achieve accurate next day's high-temperature predictions for NYC and Chicago with an error margin below 0.5 degrees, which will lead the investor to make confident wagers.

## Data Collection:

Data will be scraped from Visual Crossing's API and NOAA's public datasets. The data will be preprocessed to handle missing values and normalize temperature.

## Desired Models:

This project will mainly use a Recurrent Neural Network (RNN) to predict the next day's high temperature because RNNs are designed to handle time-series data by maintaining the memory of past information. I will explore different architectures, such as LSTMs and GRUs, and compare these RNNs against a simple baseline linear regression model to optimize predictive performance.

## Visualization:

Kalshi provides a historical wager graph for some popular events. Unfortunately, our weather forecasting event does not have that. Therefore, as the weather data are time-series data, I will use a simple line plot to visualize the historical highest temperature of NYC and Chicago and compare it with the model's predicted high temperature the next day.

## Test Plan:

The data will be divided into 80% training and 20% testing. For example, if we want to predict the highest temperature for Fall 2024, the training data will be from September 1st to November 1st, 2023, and the testing data will be from November 2nd to 30th, 2023. I will evaluate the model's accuracy using Root Mean Squared Error.   
