"""
Docstring for clusterfinding
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
#requirements needed when using the program: Installing pip, installing the modules, etc. #
#Any .csv added to the project folder will be read #
df = pd.read_csv('thesis_poverty_dataset.csv') #read_csv()
print(df)

# 2 Features to be utilized
col1 = "Number of households"
col2 = "Proportion of households"
# Values with 0 on respective data will be excluded from the clusters and scatter plot

new_df = df[[col1, col2]]
new_df

km_model = KMeans(n_clusters=5, n_init="auto")
km_model.fit(new_df)

pov = ['population', 'proportion']

df[pov] = df

x = df['population']
y = df['proportion']
df

samples = df[['population', 'proportion']]

km_prediction = km_model.fit_predict(samples)

df_test_result = new_df.copy()
df_test_result["KPredict"] = km_prediction
print(df_test_result)