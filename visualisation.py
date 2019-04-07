#Keivn Dooley 07 Apr 19 - Graphical Analysis of irish data set

import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv("irisdataset.csv")

#Histogram of all 4 columns

#gives an array of axes
#figsize - defines the size of the histogram
#bins - range
#rwidth - space between 
df.hist(figsize=(10,5), bins=10, rwidth=0.8)


#shows histogram
plt.show()

#Separate histograms