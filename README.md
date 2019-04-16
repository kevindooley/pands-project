# Programming and Scripting Project 2019
### Summary of Fisher's Iris Dataset by Kevin Dooley
# Background & Objectives

The aim of this project is to give an overview of the well-known Fisher's Iris data set.
The objectives of the project are as follows:

1. Research background information about the data set and write a summary about
it.
2. Keep a list of references you used in completing the project.
3. Download the data set and write some Python code to investigate it.
4. Summarise the data set by, for example, calculating the maximum, minimum and
mean of each column of the data set. A Python script will quickly do this for you.
5. Write a summary of your investigations.
6. Include supporting tables and graphics as you deem necessary.

# Dataset Background

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper "The use of multiple measurements in taxonomic problems as an example of linear 
discriminant analysis.". The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. The data set contains 150 observations of iris flowers. 
![](iris.png)

# Getting Started

1.  If not already installed, download and install Python 3.
2.  Recommend downloading python via Anaconda to get useful additional software including Visual Studio Code and Ipython.
3.  Download and install a command prompt - recommend Cmder (Windows) or Terminal (Mac).
4.  Download the files from this repository to your desktop.

# Python Libraries Used in Project

![](libraries.png "Image showing libraries")

I originally found information on the different libraries to use for this project from the lecture videos. Matplotlib and pandas were suggested to use to assist in this project. After further research I found the seaborn was also a useful library to use to graphically visualise data. Scikit-learn is a further tool available that would be perfect for this project but after research I felt this library was slightly too advanced for me at the moment and so just used the tools as mentioned above.

# Starting the dataset
To be able to give an overview of Fisher's Iris dataset, I had to first obtain it. I found the dataset online and copied and saved it as a CSV file in my repository. This was saved as irisdataset.csv and was the basis of the project.

## Reading from irisdataset.csv
I refered back to the lecture in week 7 "opening files for reading and writing" which provided the foundation to develop some code to read the data in irisdataset.csv.
By importing pandas as pd, I created pd.read_csv("irisdataset.csv") which imported the dataset.

'''
# imported iris dataset csv file
# prints out the data set
df = pd.read_csv("irisdataset.csv")
print(df)
'''

