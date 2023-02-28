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
print(df)

# Creating the basic understanding of our Model in terms of model layout
# Charges = w * age * b

