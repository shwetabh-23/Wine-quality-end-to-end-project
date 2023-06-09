import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import  read_params

def spilt_and_saved_data(config_path):
    config = read_params(config_path)
    train_data_path = config['split_data']['train_path']
    test_data_path = config['split_data']['test_path']
    split_ratio = config['split_data']['test_size']
    random_state = config['base']['random_state']

    raw_data_path = config['load_data']['raw_dataset_csv']

    df = pd.read_csv(raw_data_path, sep= ',', encoding= 'utf-8')
    train, test = train_test_split(df, random_state=random_state)

    train.to_csv(train_data_path, sep = ',', index = False, encoding = 'utf-8')
    test.to_csv(test_data_path, sep = ',', index = False, encoding = 'utf-8')

if __name__=='__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    spilt_and_saved_data(parsed_args.config)
