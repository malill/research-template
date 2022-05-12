import pandas as pd
import os
import joblib


def load_data(level, name):
    # DATA_DIR = os.path.dirname(__file__)
    DATA_DIR = os.path.abspath('')
    FILENAME = os.path.join(DATA_DIR, '../../data/{}/{}.csv'.format(level, name))
    print('Loading dataset {}.csv from {}'.format(name, level))
    df = pd.read_csv(FILENAME, index_col=0, low_memory=False)
    return df


def write_data(df, level, name):
    df.to_csv('../../data/{}/{}.csv'.format(level, name))


def load_model(name):
    return joblib.load('../../data/04_models/{}.pkl'.format(name))


def write_model(model, name):
    joblib.dump(model, '../../data/04_models/{}.pkl'.format(name))
