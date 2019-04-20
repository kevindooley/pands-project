# violin plot to represent the data
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("irisdataset.csv")

#Comparision of species sepal length
# set the background to a white grid
sns.set(style="whitegrid", palette="Set2")
# using seaborn - violin plot comparing 3 species sepal length
sns.violinplot(x="species", y="sepal_length", data=df)
plt.title("Comparision of different Iris species sepal length", fontsize=14, fontweight='bold')
plt.show()

#Comparision of species sepal width
# set the background to a white grid
sns.set(style="whitegrid", palette="Set2")
# using seaborn - violin plot comparing 3 species sepal width
sns.violinplot(x="species", y="sepal_width", data=df)
plt.title("Comparision of different Iris species sepal width", fontsize=14, fontweight='bold')
plt.show()

#Comparision of species petal length
# set the background to a white grid
sns.set(style="whitegrid", palette="Set2")
# using seaborn - violin plot comparing 3 species petal length
sns.violinplot(x="species", y="petal_length", data=df)
plt.title("Comparision of different Iris species petal length", fontsize=14, fontweight='bold')
plt.show()

#Comparision of species petal width
# set the background to a white grid
sns.set(style="whitegrid", palette="Set2")
# using seaborn - violin plot comparing 3 species petal width
sns.violinplot(x="species", y="petal_width", data=df)
plt.title("Comparision of different Iris species petal width", fontsize=14, fontweight='bold')
plt.show()