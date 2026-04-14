# SeniorThesisKMeansProgram
Senior Thesis K Means Algorithm process

List of instructions to use the programs:
This is a program that processes exactly 1 value for X and 1 value for Y while using it in creating the scatter plot maps for every data point that gets clustered by the K-Means algorithm.

1. Prepare your spreadsheet files into a .csv file
2. Add the file to the directory of your python file, and label it to the filename from the directory.
2. Write down in the value set for col 1 = (column name in spreadsheet you'd like to set to X)
3. Write down in the value set for col 2 = (column name in spreadsheet you'd like to set to Y)
4. Run the program in terminal
5. when the line graph appears, take note of which number of clusters shows the last point it goes from a sharp down decline, to an angle flattening out for the succeeding numbers, this will be set and known as the "elbow" which determines the number of optimal clusters for your set of data.
6. This will then create a graph with a yellow x over the number you set it to, you may also save this image for your personal data.
7. After you close the graph, it will create your scatter plot data with each of the clusters already colored based on their distance on centroids, you may also save this for reference later to identify which clusters pertain to a level of intensity, depending on which part of the color map set, was equivalent to the cluster set.

Colormap guide: If you set your color map to "viridis" for example, viridis starts clustering sequentially from dark green to yellow, making it clear which data got clustered in what order when the data starts counting its clusters from 0 to 1 to 2 to 3, etc.

Note: Taking note of your choice of color map is important since when the program clusters, it does not adjust by itself in organizing which cluster pertains to what, it is still your job to find out which data points belongs to which cluster, to layout a proper interpretation of the data, which was a need, given the maps I had to make for my set of data.

Cluster Prediction program guide:
Now that you have the number of clusters available, this other program follows relatively the same steps as the former program, with the main exception being that the file will generate a readable CSV files of the 2 columns you have set, by adding a third column labelled as "KCluster" to place the data value set by the predict function done for every point of data in the rows of data.

1. Prepare your spreadsheet files into a .csv file
2. Add the file to the directory of your python file, and label it to the filename from the directory.
2. Write down in the value set for col 1 = (column name in spreadsheet you'd like to set to X)
3. Write down in the value set for col 2 = (column name in spreadsheet you'd like to set to Y)
4. Write down the optimal number of clusters you had set from the cluster prediction program into the value of "clusters"
5. Run the program in terminal.


    