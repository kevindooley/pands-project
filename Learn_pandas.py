
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