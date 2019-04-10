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