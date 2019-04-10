
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
df = pd.read_csv("irisdataset.csv")

sns.pairplot(df,hue="species", palette="GnBu_d")

