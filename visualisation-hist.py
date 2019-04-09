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

#Separate histograms for each column
# Sepal Length
plt.figure(figsize = (10, 5)) 
x = df["sepal_length"] 
  
plt.hist(x, color = "red", bins=20, rwidth=0.8) 
plt.title("Sepal Length in cm") 
plt.xlabel("Sepal Length cm") 
plt.ylabel("Number of iris")

plt.show()

#Sepal Width
plt.figure(figsize = (10, 5)) 
x = df["sepal_width"] 
  
plt.hist(x, color = "red", bins=20, rwidth=0.8) 
plt.title("Sepal Width in cm") 
plt.xlabel("Sepal Width cm") 
plt.ylabel("Number of iris")

plt.show()

#Petal Length
plt.figure(figsize = (10, 5)) 
x = df["petal_length"] 
  
plt.hist(x, color = "red", bins=20, rwidth=0.8) 
plt.title("Petal Length in cm") 
plt.xlabel("Petal Length cm") 
plt.ylabel("Number of iris")

plt.show()

#Petal Width
plt.figure(figsize = (10, 5)) 
x = df["petal_width"] 
  
plt.hist(x, color = "red", bins=20, rwidth=0.8) 
plt.title("Petal Width in cm") 
plt.xlabel("Petal Width cm") 
plt.ylabel("Number of iris")

plt.show()