
# Unlock near 3x performance gains with XGBoost and Amazon SageMaker Neo

When a model gets deployed to a production environment, inference speed matters. Models with fast inference speeds require less resources to run, which translates to cost savings, and applications that consume the models’ predictions benefit from the improved performance.

For example, let’s say your website uses a regression model to predict mortgage rates for aspiring home buyers to see what type of rate they could expect, based on inputs they provide such as the size of the down payment, their loan term, and the county in which they’re looking to buy. A model that can send a prediction back in 10 milliseconds versus 200 milliseconds for every time an input is updated makes a massive difference in terms of the website’s responsiveness and user experience.

Amazon SageMaker Neo allows you to unlock such performance improvements and cost savings in a matter of minutes. It does this by compiling models into optimized executables through various open-source libraries, which can then be hosted on supported devices on the edge or on Amazon SageMaker endpoints. Neo is compatible with eight different machine learning (ML) frameworks, and in the context of gradient boosted tree algorithms such as XGBoost, Neo uses Treelite to optimize model artifacts. Due to the popularity of XGBoost and its unique categorization as a more classical ML framework, we use it as our framework of choice throughout this post. A near 3x speedup will be demonstrated for the optimized XGBoost model compared to the unoptimized one. The Abalone dataset from UCI will be used to train the model. 

![1](https://user-images.githubusercontent.com/23625821/121161445-47f1d480-c84d-11eb-9441-7655290cd843.jpg)

The steps to implement the solution are as follows:

Download and process the popular Abalone dataset with a Jupyter notebook, and then run an XGBoost SageMaker training job on the processed data. We use a local mode SageMaker training job to produce the unoptimized XGBoost model, which can be faster and easier to prototype compared to a remote one.

Deploy the unoptimized XGBoost model artifact to a SageMaker endpoint.

Take the unoptimized artifact and optimize it with a Neo compilation job.

Deploy the Neo-optimized XGBoost artifact to a SageMaker endpoint.

Create an Amazon CloudWatch Dashboard from the SageMaker notebook to monitor inference speed and performance under heavy load of both endpoints.

Deploy Serverless Artillery from the SageMaker notebook, which we use as our load testing tool. We set up Serverless Artillery entirely from the SageMaker notebook, and directly invoke your SageMaker endpoints from the internet through manually signed AWS Signature Version 4 requests—no need for Amazon API Gateway as an intermediary.

Perform load tests against both endpoints.
Analyze the performance of both endpoints under load in the CloudWatch dashboard, and look at how the optimized endpoint outperforms the unoptimized one.
