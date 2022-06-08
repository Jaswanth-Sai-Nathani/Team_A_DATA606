# DATA 606 PROJECT PROPOSAL

# STOCK PRICE PREDICTION ANALYSIS



## Introduction
A stock market is a public market where you can buy and sell shares for publicly listed companies. The stocks, also known as equities, represent ownership in the company. The stock exchange is the mediator that allows the buying and selling of shares. The stock market broadly refers to a number of exchanges and other venues in which shares of publicly held companies are bought and sold. Such financial activities are conducted through institutionalized formal exchanges (physical or electronic) and via over-the-counter (OTC) marketplaces that operate under a defined set of regulations. While both the terms “stock market” and “stock exchange” are often used interchangeably, the latter term is really a subset of the former. Traders in the stock market buy or sell shares on one or more of the stock exchanges that are part of the overall stock market. This essentially means that a company divides itself into a number of shares (for example, 20 million shares) and sells some of those shares (say, 5 million shares) to the public at a price (for instance, 10$ per share).

## Stock Price Prediction

Stock price analysis has been a critical area of research and is one of the top applications of machine learning.
Stock Price Prediction using machine learning helps you discover the future value of company stock and other financial assets traded on an exchange. The entire idea of predicting stock prices is to gain significant profits. Predicting how the stock market will perform is a hard task to do. There are other factors involved in the prediction, such as physical and psychological factors, rational and irrational behavior, and so on. All these factors combine to make share prices dynamic and volatile. This makes it very difficult to predict stock prices with high accuracy. 
Many people nowadays are investing a small part of their income regularly in stocks hence understanding the trends of their investments has become very important to gain return on their investments. Hence machine learning algorithm can b|e used effectively to understand and predict the future trends of these stock market for better investments.

## HYPOTHESIS

Predicting the future stock value of a user selected stock based on the historical stock data over an year period and understand if it is good to invest in that particular stock or not.



## DATASET 

Dataset will vary based on the stock selected because we will directly webscrape the data from google and use it.
But for all the datasets the columns in the dataset we are going to analyze would be same.

Dataset Attributes
1. Date
2. Open 
3. High
4. Low 
5. Close 
6. Adj Close
7. Volume

We will use webscrapping on this website: https://finance.yahoo.com

## PRIMARY UNIT OF ANALYSIS

The primary unit of analysis the I would be using currently would be Open,Close,Adj Close and new column that I would create based on the difference value between Open and Adj Close to determine loss or profit for that particular day.

## Machine Learning Techniques Planning to use

My plan is to use machine learning techniques such as ARIMA(Autoregressive Integrated Moving Average) and try and understand the stock behaviour. The ARIMA model has been widely utilized in banking and economics since it is recognized to be reliable, efficient, and capable of predicting short-term share market movements. 

## OUTCOMES

1. Try and understand the behaviour of stock prices
2. Learn time series techniques used for predictive modelling
3. Extend this idea in future to implement smart web based application.
