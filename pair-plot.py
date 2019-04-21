#Kevin Dooley 21 Apr 19 - Graphical Analysis of iris data set


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
df = pd.read_csv("irisdataset.csv")


#create a pair plot/scatterplot
#markers - gives legend 
#hue - determines which column in the data frame should be used for colour encoding
sns.pairplot(df, hue="species", palette="husl", markers=["o", "s", "D"])

#show plot
plt.show()

