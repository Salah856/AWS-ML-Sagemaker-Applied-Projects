

# Build regression models with Amazon Redshift ML 

With the rapid growth of data, many organizations are finding it difficult to analyze their large datasets to gain insights. As businesses rely more and more on automation algorithms, machine learning (ML) has become a necessity to stay ahead of the competition.

Amazon Redshift, a fast, fully managed, widely used cloud data warehouse, natively integrates with Amazon SageMaker for ML. With Amazon Redshift ML, you can use simple SQL statements to create and train ML models from your data in Amazon Redshift and then use these models for a variety of use cases, such as classification of a binary or multiclass outcome or predicting a numeric value through regression. Amazon SageMaker Autopilot provides all the benefits of automatic model creation, but as an advanced user, you can also influence the model training by providing different parameters such as model type, objective, and so on.

Amazon Redshift ML allows you to address several ML challenges, such as the following:

Binary classification – Predict a true/false outcome, such as whether a customer will churn. 

Multiclass classification – Identify the class of an input value within a discrete number of classes.
For example, you can identify which will be the best-selling product.

Regression – Predict a numerical outcome, like the price of a house or how many people will use a city’s bike rental service.


In this post, we use Amazon Redshift ML to build a regression model that predicts the number of people that may use the city of Toronto’s bike sharing service at any given hour of a day. The model accounts for various aspects, including holidays and weather conditions. Because we need to predict a numerical outcome, we create a regression model.

We walk you through the following high-level steps:

1. Input the raw data.

2. Prepare the input data.

3. Create the model.

4. Validate the predictions.


## Input the raw data: 

refer to : https://github.com/Salah856/AWS-ML-Sagemaker-Applied-Projects/blob/main/Redshift_ML/Regression_Model/data.sql 



