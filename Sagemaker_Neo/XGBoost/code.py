
from pathlib import Path
from sklearn.datasets import load_svmlight_file, dump_svmlight_file

from sklearn.model_selection import train_test_split
import boto3

import sagemaker
from sagemaker.xgboost.estimator import XGBoost

from sagemaker.session import Session
from sagemaker.inputs import TrainingInput


for p in ['raw_data', 'training_data', 'validation_data']:
    Path(p).mkdir(exist_ok=True)

s3 = boto3.client('s3')
s3.download_file('sagemaker-sample-files', 'datasets/tabular/uci_abalone/abalone.libsvm', 'raw_data/abalone')




X, y = load_svmlight_file('raw_data/abalone')
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1984, shuffle=True)

dump_svmlight_file(x_train, y_train, 'training_data/abalone.train')
dump_svmlight_file(x_test, y_test, 'validation_data/abalone.test')





bucket = Session().default_bucket()
role = sagemaker.get_execution_role()

# initialize hyperparameters
hyperparameters = {
        "max_depth":"5",
        "eta":"0.2",
        "gamma":"4",
        "min_child_weight":"6",
        "subsample":"0.7",
        "verbosity":"1",
        "objective":"reg:squarederror",
        "num_round":"10000"
}

# construct a SageMaker XGBoost estimator
# specify the entry_point to your xgboost training script
estimator = XGBoost(entry_point = "entrypoint.py", 
                    framework_version='1.2-1', # 1.x MUST be used 
                    hyperparameters=hyperparameters,
                    role=role,
                    instance_count=1,
                    instance_type='local',
                    output_path=f's3://{bucket}/neo-demo') # gets saved in bucket/neo-demo/job_name/model.tar.gz

# define the data type and paths to the training and validation datasets
content_type = "libsvm"
train_input = TrainingInput('file://training_data', content_type=content_type)
validation_input = TrainingInput('file://validation_data', content_type=content_type)

# execute the XGBoost training job
estimator.fit({'train': train_input, 'validation': validation_input}, logs=['Training'])
