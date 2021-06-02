
from sklearn.externals import joblib  
import boto3  
import json  
import pickle  
	  
s3_client = boto3.client("s3")  
  
def lambda_handler(event, context):  
9.	  
10.	     #Using Pickle + load model from s3  
11.	     filename = "pickled_model.pkl"  
12.	     s3_client.download_file('bucket-withmodels', filename, '/tmp/' + filename)  
13.	       loaded_model = pickle.load(open('/tmp/' + filename, 'rb'))  
14.	       result = loaded_model.predict(X_test)  
15.	  
16.	       # Using Joblib + load the model from local storage  
17.	       loaded_model = joblib.load(“filename.joblib”)  
18.	       result = loaded_model.score(X_test, Y_test)  
19.	       print(result)  
20.	       return {'statusCode': 200, 'body': json.dumps(result)}
