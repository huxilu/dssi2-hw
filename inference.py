import joblib
import pandas as pd
import numpy as np

def get_prediction(features):
    linear = joblib.load('linear_regression_model.joblib')
    pred = linear.predict(features)
    return pred[0]
