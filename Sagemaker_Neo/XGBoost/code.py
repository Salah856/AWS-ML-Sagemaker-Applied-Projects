
from pathlib import Path
import boto3

for p in ['raw_data', 'training_data', 'validation_data']:
    Path(p).mkdir(exist_ok=True)

s3 = boto3.client('s3')
s3.download_file('sagemaker-sample-files', 'datasets/tabular/uci_abalone/abalone.libsvm', 'raw_data/abalone')

