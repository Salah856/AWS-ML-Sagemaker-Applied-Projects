# Perform inference using the SDK 

import boto3

def show_custom_labels(model, bucket, image, min_confidence):
    client=boto3.client('rekognition')

    #Call DetectCustomLabels
    response = client.detect_custom_labels(Image={'S3Object': {'Bucket': bucket, 'Name': image}},
        MinConfidence=min_confidence,
        ProjectVersionArn=model)

    # Print results
    for customLabel in response['CustomLabels']:
        print('Label ' + str(customLabel['Name']))
        print('Confidence ' + str(customLabel['Confidence']) + "\n")

    return len(response['CustomLabels'])

def main():
    bucket = 'crop-weed-bucket'
    image = "Weed-1.jpg"
    model = 'arn:aws:rekognition:us-east-2:xxxxxxxxxxxx:project/Weed-detection-in-crops/version/Weed-detection-in-crops.2021-03-30T10.02.49/yyyyyyyyyy'
    min_confidence=1

    label_count=show_custom_labels(model, bucket, image, min_confidence)
    print("Custom labels detected: " + str(label_count))

if __name__ == "__main__":
    main()
    
    

    
# The results from using the SDK are the same as earlier from the browser:

# Label weed
# Confidence 92.1469955444336

# Label good-crop
# Confidence 7.852999687194824

# Custom labels detected: 2

