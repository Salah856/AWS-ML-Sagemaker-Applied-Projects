
# Build reusable, serverless inference functions for your Amazon SageMaker models using AWS Lambda layers and containers

In AWS, you can host a trained model multiple ways, such as via Amazon SageMaker deployment, deploying to an Amazon Elastic Compute Cloud (Amazon EC2) instance (running a Flask + NGINX, for example), AWS Fargate, Amazon Elastic Kubernetes Service (Amazon EKS), or AWS Lambda.

SageMaker provides convenient model hosting services for model deployment, and provides an HTTPS endpoint where your machine learning (ML) model is available to provide inferences. This lets you focus on your deployment options such as instance type, automatic scaling policies, model versions, inference pipelines, and other features that make deployment easy and effective for handling production workloads. The other deployment options we mentioned require additional heavy lifting, such as launching a cluster or an instance, maintaining Docker containers with the inference code, or even creating your own APIs to simplify operations.

This article shows you how to use AWS Lambda to host an ML model for inference and explores several options to build layers and containers, including manually packaging and uploading a layer, and using AWS CloudFormation, AWS Serverless Application Model (AWS SAM), and containers.

Using Lambda for ML inference is an excellent alternative for some use cases for the following reasons:

Lambda lets you run code without provisioning or managing servers.

You pay only for the compute time you consume—there is no charge when you’re not doing inference.

Lambda automatically scales by running code in response to each trigger (or in this case, an inference call from a client application for making a prediction using the trained model). Your code runs in parallel and processes each trigger individually, scaling with the size of the workload.

You can limit the number of concurrent calls to an account-level default of 1,000, or request an appropriate limit increase.
The inference code in this case is just the Lambda code, which you can edit directly on the Lambda console or using AWS Cloud9.

You can store the model in the Lambda package or container, or pulled down from Amazon Simple Storage Service (Amazon S3). The latter method introduces additional latency, but it’s very low for small models.

You can trigger Lambda via various services internally, or via Amazon API Gateway.

One limitation of this approach when using Lambda layers is that only small models can be accommodated (50 MB zipped layer size limit for Lambda), but with SageMaker Neo, you can potentially obtain a 10x reduction in the amount of memory required by the framework to run a model. The model and framework are compiled into a single executable that can be deployed in production to make fast, low-latency predictions. Additionally, the recently launched container image support allows you to use up to a 10 GB size container for Lambda tasks.

