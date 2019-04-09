#Code for box plots

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv("irisdataset.csv")

#Comparision of species sepal length
# set the background to a white grid
sns.set(style="whitegrid", palette="Set2")
# using seaborn - box plot comparing 3 species sepal length
sns.boxplot(x="species", y="sepal_length", data=df)
plt.title("Comparision of different Iris species sepal length", fontsize=14, fontweight='bold')
plt.show()

#Comparision of species sepal width
sns.set(style="whitegrid", palette="Set2")

sns.boxplot(x="species", y="sepal_width", data=df)
plt.title("Comparision of different Iris species sepal width", fontsize=14, fontweight='bold')
plt.show()

#Comparision of species petal width
sns.set(style="whitegrid", palette="Set2")

sns.boxplot(x="species", y="petal_width", data=df)
plt.title("Comparision of different Iris species petal width", fontsize=14, fontweight='bold')
plt.show()

#Comparision of species petal length
sns.set(style="whitegrid", palette="Set2")

sns.boxplot(x="species", y="petal_length", data=df)
plt.title("Comparision of different Iris species petal length", fontsize=14, fontweight='bold')
plt.show()