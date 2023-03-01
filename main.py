from urllib.request import urlretrieve

url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'

urlretrieve(url, 'medical.csv')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import plotly.express as px

medical_df = pd.read_csv('medical.csv')

#Creating the basic understanding of our Model in terms of model layout
# Linear Regression Model using scikit learn

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing

# Categorical columns to numeric cols
sex_codes = {
    'female':0,
    'male':1
}
sex_val = medical_df.sex.map(sex_codes)
medical_df['sex_code'] = sex_val

smoker_codes = {
    'yes': 1,
    'no':0
}
smoker_val = medical_df.smoker.map(smoker_codes)
medical_df['smoker_code']=smoker_val

enc = preprocessing.OneHotEncoder()
enc.fit(medical_df[['region']])
enc.categories_
one_hot = enc.transform(medical_df[['region']]).toarray()
medical_df[['northeast', 'northwest', 'southeast', 'southwest']] = one_hot

# Feature Scaling
numeric_cols = ['age', 'bmi', 'children']
scaler = StandardScaler()
scaler.fit(medical_df[numeric_cols])
scaled_inputs = scaler.transform(medical_df[numeric_cols])
cat_cols = ['smoker_code', 'sex_code', 'northeast', 'northwest', 'southeast', 'southwest']
categorical_data = medical_df[cat_cols].values

inputs = np.concatenate((scaled_inputs, categorical_data), axis=1)
targets = medical_df.charges

# Create and train the model
model = LinearRegression().fit(inputs, targets)

# Generate predictions
predictions = model.predict(inputs)

# Compute loss to evalute the model
def rmse(targets, predictions):
    return np.sqrt(np.mean(np.square(targets - predictions)))
loss = rmse(targets, predictions)
print('Loss:', loss)