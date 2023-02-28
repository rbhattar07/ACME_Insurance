from urllib.request import urlretrieve

url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'

urlretrieve(url, 'medical.csv')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import plotly.express as px

df = pd.read_csv('medical.csv')

smoker_values = {'no':0, 'yes':1}
df['smoker_numeric'] = df.smoker.map(smoker_values)
gender_values = {'female':0, 'male':1}
df['sex_numeric'] = df.sex.map(gender_values)
region_values = {'southeast':1, 'southwest':2, 'northwest':3, 'northeast':4}
df['region_numeric'] = df.region.map(region_values)

# Creating the basic understanding of our Model in terms of model layout
# Linear Regression Model using scikit learn

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor

inputs = df[['age', 'sex_numeric', 'smoker_numeric', 'bmi', 'children', 'region_numeric']]
targets = df['charges']

lrmodel = LinearRegression()
lrmodel.fit(inputs, targets)
lr_predictions = lrmodel.predict(inputs)
print('LR Precictions',lr_predictions)
print('Linear Regression Model Score:',lrmodel.score(inputs,targets))

sgdmodel = SGDRegressor()
sgdmodel.fit(inputs, targets)
sgd_predictions = sgdmodel.predict(inputs)
print('SGD Predictions:',sgd_predictions)
print('SGD Model Score', sgdmodel.score(inputs,targets))

