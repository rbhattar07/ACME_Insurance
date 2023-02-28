import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

sns.set_style('darkgrid')
matplotlib.rcParams['font.size']=14
matplotlib.rcParams['figure.figsize']= (10,6)
matplotlib.rcParams['figure.facecolor']='#00000000'


# Reading & Overview of Data
medical_df = pd.read_csv('medical.csv')
print(medical_df)
print(medical_df.info())
print(medical_df.describe())

# Exploratory Analysis & Visualization
# AGE

px.histogram(
    medical_df,
    x='age',
    marginal='box',
    nbins=47,
    title='Distribution of Age'
    ).update_layout(bargap=0.1).show()

px.histogram(
    medical_df,
    x='bmi',
    marginal='box',
    nbins=47,
    color_discrete_sequence=['red'],
    title='Distribution of BMI (Body Mass Index)'
    ).update_layout(bargap=0.1).show()


