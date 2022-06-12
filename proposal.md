# DATA 606 PROJECT PROPOSAL

# USED CARS PRICE PPREDICTION

## TEAM DESCRIPTION

This is a team project of Saida Babu Garlapati and Jaswanth Sai Nathani.


## PROJECT OVERVIEW

* Web Scraping of the Used Cars portal
* Forecasting the price of used cars using regression analysis 
* Predicting the price of the Used Cars. 
* Developing a web design for prediction.


## BACKGROUND

The manufacturer sets the price of new cars in the industry, with the government incurring some additional costs in the form of taxes. Customers who purchase a new car can rest comfortable that the money they spend will be well spent. However, due to rising new car prices and customers' inability to purchase new automobiles due to a lack of cash, used car sales are on the rise worldwide. A used car price prediction system is needed to accurately estimate the car's worthiness based on a range of factors. While there are websites that provide this service, their forecast approach may not be the most accurate. Furthermore, several methods and algorithms may aid in the prediction of a used car's true market worth. When purchasing and selling, it's critical to understand their true market value.

Being able to estimate the market value of used cars can benefit both buyers and sellers. Dealers that sell used cars are one of the most likely groups to be interested in the findings of this study. Used car dealers that have a better understanding of what makes a car desirable and what the most significant qualities are for a used automobile will be able to apply this knowledge and provide better service. As a result, the model established in this study could aid online web services that determine the market worth of a used car. Many people are interested in the used automobile market because they wish to sell their car or buy a used car at some time in their lives. It's a great mistake to pay too much or sell for less than the market worth in this process.


## RESEARCH QUESTIONS:


1.	Our project is based on doing a predictive analysis on the price of used cars and estimating what would be good price to buy or sell a car in open market that would be helpful to buyers and sellers.

2.	Try and estimate what are the most important factors that will best suit in the price determination of a used car.

3.	Understand the current market on which brand has the highest resale market with the historical data under consideration.



## DATASET 

The dataset comprises data extracted from https://www.cars.com/ using Web scraping technique. This information can be utilized for a variety of applications, including price prediction, which demonstrates the application of linear regression in Machine Learning. The following are the columns in our dataset until now which we scraped and would like to add more features

1. Brand
2. Model
3. Trim
4. Manufacture Year
5. Stock Type
6. Mileage
7. Dealer Name
8. Distance
9. Rating
10. Review Count
11. Badge Label
12. Price


## PRIMARY UNIT OF ANALYSIS

This data has numerous observations. For analyzing the trends, we considered the data of 550 pages, resulting in the observations consisting of the details of 10874 cars. Our main target of analysis is based on the ‘Price’ of the car, which involves various other features that are independent and dependent on the price of car like mileage, year, manufacturer etc. Once we scrape more features would also try and base our analysis on transmission, gas etc.


## FEATURE SELECTION:

Checking the correlation of other variables with the price variable and finding the predictor variables with high correlation and also find the independent variables to the price of car.


## METHODOLOGY:

* Firstly, we would like to proceed with data extraction using web scrapping of website with used car data (eg: www.cars.com) and then proceed with data cleaning and feature selection. Also, once data cleaning is done would like to understand how various features are distributed and try normalizing them based on our requirement. 

* Next, we like to develop a regression model to predict the price of used car based on various models like linear regression model, support vector machine and random forest model and understand and base our analysis by comparing the best possible model for our forecasting.

* Next, we would proceed with the development of web design to have a user better understand the price of their car based on our predictions and data we possess.

## MODEL SELECTION: 

* Prediction will be done considering the best performed model.
* Building a web application for the prediction of price of a used car based on the features and specifications of the car.



## OUTCOMES

* Primary goal of the project is to design a predictive model that can be used in real world scenarios to determine the price of used car in market.
* Finding a best fit model for price prediction of used cars.
* Developing a Web application that can suggest the user the price they should be paying or selling their used car.

## Responsibilities

### Saida Babu Garlapati: 
* Web Scraping the cars portal
* Extracting the Dataset
* Data Cleaning
* Exploratory Data Analysis
* Performing Regression analysis

### Jaswanth Sai Nathani
* Performing Data Modeling
* Checking different prediction models
* Model comparision and Cross validating the results
* Finding a best fit model for prediction
* Developing a web design for user friendly prediction

### Along with the individual responsibilities, we will complement each other's work and get the best outcome for the project. We involve in regular discussion to develop the project and to overcome the complications. 
