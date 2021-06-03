import boto3
import argparse
import logging
import os
import numpy as np
import pandas as pd
from catboost import CatBoostClassifier
from sklearn.metrics import balanced_accuracy_score, recall_score, precision_score, f1_score

if __name__ =='__main__':

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    print('Extracting arguments')
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--train_file', type=str)
    parser.add_argument('--test_file', type=str)
    parser.add_argument('--model_file', type=str)
    parser.add_argument('--target', type=str) 
    parser.add_argument('--categorical_fields', type=str)
    parser.add_argument('--learning_rate', type=str)
    parser.add_argument('--depth', type=str)
    parser.add_argument('--imbalance_penalty', type=str, default='3')

    args, _ = parser.parse_known_args()
    
    logging.info('Reading data . . .')
    train_df = pd.read_csv(args.train_file)
    test_df = pd.read_csv(args.test_file)

    logging.info('Building training and testing datasets . . .')
    categorical_fields = args.categorical_fields.split()
    X_train = train_df[[col for col in train_df.columns if col != args.target]]
    X_val = test_df[[col for col in train_df.columns if col != args.target]]
    y_train = train_df[args.target]
    y_val = test_df[args.target]
        
    # Sample fixed hyper-parameters
    model_params = dict()
    model_params['iterations'] = 1000
    model_params['loss_function'] = 'Logloss'
    model_params['eval_metric'] = 'F1'
    model_params['random_seed'] = 21
    
    # Read hyperparameters as arguments (to tune in future using SageMaker)
    model_params['depth'] = int(args.depth)
    model_params['learning_rate'] = float(args.learning_rate)
    imbalance_penalty_factor = int(args.imbalance_penalty)
    
    # minority_weight assignment for binary classes: 0 and 1
    minority_class_weight = imbalance_penalty_factor * (len(y_train) - sum(y_train)) / sum(y_train)
    model_params['class_weights'] = [1, minority_class_weight]

    model = CatBoostClassifier(**model_params)
    
    model.fit(X_train, y_train, 
        cat_features=categorical_fields, eval_set=(X_val, y_val), verbose=False)
    
    y_val_pred = model.predict(data=X_val)
    
    precision = precision_score(y_val, y_val_pred)
    recall = recall_score(y_val, y_val_pred)
    f1 = f1_score(y_val, y_val_pred)
    # Increase the influence of recall in the model evaluation metric
    model_score = f1 * recall
    
    logging.info ('Precision: {:.3f}'.format(precision))
    logging.info ('Recall: {:.3f}'.format(recall))
    logging.info ('F1: {:.3f}'.format(f1))
    logging.info ('ModelScore: {:.3f}'.format(model_score))
    
    # persist model
    model.save_model(args.model_file
