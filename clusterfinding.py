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


# Elbow method of finding the clusters #
# Set the number of clusters (num), to the selected cluster where the points create an elbow angle #
inertias = []
num = 0
k_range = range(2, 15)

for k in k_range:
    km_model = KMeans(n_clusters=k, n_init="auto")
    km_model.fit(new_df)
    intertias.append([k, km_model.inertia_])

inertias = np.array(inertias)
plt.plot(inertias[:,0], inertias[:,1], 'x-')
plt.axvline(x=num, color = 'y', linestyle='---')
plt.show()


if num > 0:
    km_model = KMeans(n_clusters=num, n_init="auto")
    km_model.fit(new_df)

    new_df.plot.scatter(col1, col2, c = km_model.labels_, 
                        cmap="rainbow", 
                        colorbar=False)