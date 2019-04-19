#Kevin Dooley 19 Apr 19
#Overview of all the functions used to give a top level overview of the dataset
#not all of these functions will be presented in the Readme but these are all 
#examples of ones I learned how to use

import numpy as np
import pandas as pd

# imported iris dataset csv file
# prints out the data set
df = pd.read_csv("irisdataset.csv")
print(df)


# prints out first out first 5 rows of dataset (default)
# input any number to get that many rows displayed
print(df.head())

#default displays last 3 rows of data set
print(df.tail())

#tells me what data type (i.e. floating no./integer/ string etc) stored in each column
print(df.dtypes)

#top level info of the index column (most left column)
print(df.index)

#gives a list of the column headings
print(df.columns)

#outputs top level statistical analysis of the dataset ie mean, min, max etc
print(df.describe())

#sort a column descending highest to lowest
print(df.sort_values("sepal_length", ascending=False))

#how many rows and columns (in that order)
print(df.shape)

#species distribution
print(df.groupby('species').size())

#min, max, mean, median, standard deviation
print(df.min())
print(df.max())
print(df.std())
print(df.median())
print(df.mean())

#Output 5 random rows from the set
print(df.sample(5))

