from joblib import dump, load
import pandas as pd
import numpy as np

def get_prediction(features):
    linear = load('models/mdl.joblib')
    pred = linear.predict(features)
    return pred[0]
