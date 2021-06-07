

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


To load the data, use the following COPY commands. Replace the AWS Identity and Access Management (IAM) role with the IAM role that you created as part of the prerequisite steps earlier.

refer to : https://github.com/Salah856/AWS-ML-Sagemaker-Applied-Projects/blob/main/Redshift_ML/Regression_Model/commands.sh 

## Data preparation

Let’s discuss about how the data can be biased and how selecting the right distribution of data impacts accuracy. For most ML problems, data preparation is the most time-consuming process; it involves preparing the data, finding relevant attributes, and cleaning and curating it to be used as input to the ML model. Bias or anomalies in the input data distribution also play a key role in model accuracy, therefore it’s very important to curate that as much as possible. Let’s explore and prepare our input dataset.


### Ridership
The ridership table contains Bike Share Toronto’s ridership information for 2017 and 2018. We performed the following data preparation steps to make it more meaningful for our ML model:

