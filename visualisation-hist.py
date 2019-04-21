#Kevin Dooley 07 Apr 19 - Graphical Analysis of iris data set

import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv("irisdataset.csv")

#Histogram of all 4 columns in one image

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

# colour of the histogram, range, layout 
plt.hist(x, color = "blue", bins=20, rwidth=0.8) 
#title of histogram
plt.title("Histogram showing Sepal Length(cm) of all iris species")
#x axis label 
plt.xlabel("Sepal Length (cm)") 
#y axis label
plt.ylabel("Number of iris species")

plt.show()

#Sepal Width
plt.figure(figsize = (10, 5)) 
x = df["sepal_width"] 
  
plt.hist(x, color = "blue", bins=20, rwidth=0.8) 
plt.title("Histogram showing Sepal Width(cm) of all iris species") 
plt.xlabel("Sepal Width (cm)") 
plt.ylabel("Number of iris species")

plt.show()

#Petal Length
plt.figure(figsize = (10, 5)) 
x = df["petal_length"] 
  
plt.hist(x, color = "blue", bins=20, rwidth=0.8) 
plt.title("Histogram showing Petal Length(cm) of all iris species") 
plt.xlabel("Petal Length (cm)") 
plt.ylabel("Number of iris species")

plt.show()

#Petal Width
plt.figure(figsize = (10, 5)) 
x = df["petal_width"] 
  
plt.hist(x, color = "blue", bins=20, rwidth=0.8) 
plt.title("Histogram showing Petal Width(cm) of all iris species") 
plt.xlabel("Petal Width (cm)") 
plt.ylabel("Number of iris species")

plt.show()