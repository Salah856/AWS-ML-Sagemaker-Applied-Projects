
from sklearn.externals import joblib  
import boto3  
import json  
import pickle  
	  
s3_client = boto3.client("s3")  
  
def lambda_handler(event, context):  
	#Using Pickle + load model from s3  
	filename = "pickled_model.pkl"  
	s3_client.download_file('bucket-withmodels', filename, '/tmp/' + filename)  
	loaded_model = pickle.load(open('/tmp/' + filename, 'rb'))  
	result = loaded_model.predict(X_test)  
	       
	 # Using Joblib + load the model from local storage  
	 loaded_model = joblib.load(“filename.joblib”)  
	 result = loaded_model.score(X_test, Y_test)  
	 print(result)  
	 return {'statusCode': 200, 'body': json.dumps(result)}
