# Automate weed detection in farm crops using Amazon Rekognition Custom Labels 

Amazon Rekognition Custom Labels makes automated weed detection in crops easier. Instead of manually locating weeds, you can automate the process with Amazon Rekognition Custom Labels, which allows you to build machine learning (ML) models that can be trained with only a handful of images and yet are capable of accurately predicting which areas of a crop have weeds and need treatment. This saves farmers time, effort, and weed treatment costs.

Every farm has weeds. Weeds compete with crops and if not controlled can take up precious space, sunlight, water, and nutrients from crops and reduce their yield. Weeds grow much faster than crops and need immediate and effective control. Detecting weeds in crops is a lengthy and time-consuming process and is currently done manually. Although weed spray machines exist that can be coded to go to an exact location in a field and spray weed treatment in just those spots, the process of locating where those weeds exist is not yet automated.

Weed location automation isn’t an easy process. This is where computer vision and AI come in. Amazon Rekognition is a fully managed computer vision service that allows developers to analyze images and videos for a variety of use cases, including face identification and verification, media intelligence, custom industrial automation, and workplace safety. Detecting custom objects and scenes can be hard. Training and improving the accuracy of a computer vision model requires a large amount of data and is a complex problem. Amazon Rekognition Custom Labels allows you to detect custom labeled objects and scenes with just a handful of training images.

In this post, we use Amazon Rekognition Custom Labels to build an ML model that detects weeds in crops. We’re presently helping researchers at a US university automate this process for local farmers.


## Create and train a weed detection model

We solve this problem by feeding images of crops with and without weeds to Amazon Rekognition Custom Labels and building an ML model. After the model is built and deployed, we can perform inference by feeding the model images from field cameras. This way farmers can automate weed detection in their fields. Our experiments showed that highly accurate models can be built with as few as 32 images.

1 .On the Amazon Rekognition console, choose Use Custom Labels.

![1-3259-Graphic](https://user-images.githubusercontent.com/23625821/120065517-f2aa0c00-c071-11eb-8d1f-b615f9c844f4.jpg)

2. Choose Projects.
3. Choose Create project.
4. For Project name, enter a name (for example, Weed-detection-in-crops).
5. Choose Create project.

