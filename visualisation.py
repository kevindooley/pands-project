#Keivn Dooley 07 Apr 19 - Graphical Analysis of irish data set

import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv("irisdataset.csv")

#gives an array of axes
df.hist()
#shows histogram
plt.show()