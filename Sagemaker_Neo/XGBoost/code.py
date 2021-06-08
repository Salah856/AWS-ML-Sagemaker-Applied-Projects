
from pathlib import Path
from sklearn.datasets import load_svmlight_file, dump_svmlight_file

from sklearn.model_selection import train_test_split
import boto3



for p in ['raw_data', 'training_data', 'validation_data']:
    Path(p).mkdir(exist_ok=True)

s3 = boto3.client('s3')
s3.download_file('sagemaker-sample-files', 'datasets/tabular/uci_abalone/abalone.libsvm', 'raw_data/abalone')




X, y = load_svmlight_file('raw_data/abalone')
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1984, shuffle=True)

dump_svmlight_file(x_train, y_train, 'training_data/abalone.train')
dump_svmlight_file(x_test, y_test, 'validation_data/abalone.test')


