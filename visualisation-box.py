#Code for box plots

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv("irisdataset.csv")

# set the backgrounf to a white grid
sns.set(style="whitegrid")
# using seaborn - box plot comparing 3 species sepal length
sns.boxplot(x="species", y="sepal_length", data=df)
plt.show()