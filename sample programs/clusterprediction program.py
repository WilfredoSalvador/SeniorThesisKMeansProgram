"""
Docstring for Cluster Prediction
https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
https://www.youtube.com/watch?v=_-zUnQVk8XY&feature=youtu.be
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.scatter.html
https://www.w3schools.com/python/numpy/numpy_intro.asp
"""
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
#requirements needed when using the program: Installing pip, installing the modules, etc. #
#Any .csv added to the project folder will be read #
df = pd.read_csv('any_dataset.csv') #read_csv()
df = df.replace('nan', np.nan)
df = df.dropna()
print(df)

# 2 Features to be utilized
col1 = "XValue"
col2 = "YValue"

# Tell them that the recovery likelihood, has an emphasis on this type of data set, that focuses on length and width, in this case, population and proportion
# Values with 0 on respective data will be excluded from the clusters and scatter plot

new_df = df[[col1, col2]]
print(new_df)

# K should be selected after doing cluster finding.
km_model = KMeans(n_clusters=4, n_init="auto")
km_model.fit(new_df)

# change to the real names of the columns in the database


x = df[col1]
y = df[col2]

samples = new_df

km_prediction = km_model.predict(samples)

# labels = {0: "Cluster 1", 1: "Cluster 2", 2: "Cluster 3", 3: "Cluster 4"}

df_test_result = new_df.copy()
df_test_result["KPredict"] = km_prediction


print(df_test_result)

df_test_result.to_csv("cluster_predict.csv", index=False)
