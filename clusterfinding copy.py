"""
Docstring for clusterfinding
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from itertools import cycle
from matplotlib import cm as cm
from sklearn.cluster import KMeans
#requirements needed when using the program: Installing pip, installing the modules, etc. #
#Any .csv added to the project folder will be read #
df = pd.read_csv('thesis_poverty_dataset.csv') #read_csv()
df = df.replace('nan', np.nan)
df = df.dropna()
print(df)

# 2 Features to be utilized
col1 = "Households Population with No Access to Clean Water"
col2 = "Proportion of households with no access to clean water"
# Values with 0 on respective data will be excluded from the clusters and scatter plot

new_df = df[[col1, col2]]
print(new_df)


# Elbow method of finding the clusters #
# Set the number of clusters (num), to the selected cluster where the points create an elbow angle #
inertias = []
# What we can put here is perhaps an input to identify the cluster to input num
num = 4
k_range = range(2, 15)

for k in k_range:
    km_model = KMeans(n_clusters=k, n_init="auto")
    km_model.fit(new_df)
    inertias.append([k, km_model.inertia_])

print(inertias)

inertias = np.array(inertias)
plt.plot(inertias[:,0], inertias[:,1], 'x-')
plt.show()
print('Pick the number that you would like to pick as the elbow for this set of data.')
num = int(input())
plt.plot(inertias[:,0], inertias[:,1], 'x-')
plt.axvline(x=num, color = 'y', linestyle='--')
plt.show()



if num > 0:
    km_model = KMeans(n_clusters=num, n_init="auto")
    km_model.fit(new_df)
    predict = km_model.predict(new_df)
    centers = km_model.cluster_centers_

    # labels = {0: "Cluster 1", 1: "Cluster 2", 2: "Cluster 3", 3: "Cluster 4"}

    new_df.plot.scatter(col1, col2, c = km_model.labels_,
                         cmap="viridis",
                         colorbar=False)
    plt.show()
    