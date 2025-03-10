import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


df= pd.read_csv('titanic.csv')
print(df.head())
print(df.info())
print(df.describe())

#This part will be Histograms

#columns we want
Using_col= df.select_dtypes(include=['int64','float64']).columns
print(Using_col)
for n in range(len(Using_col)):
    plt.figure()
    plt.hist(df[Using_col[n]].dropna(),bins=20, edgecolor='black')
    plt.xlabel("columns")
    plt.ylabel("# of observations")
    plt.title(Using_col[n])
plt.tight_layout()   
plt.show()
#Histogram Part Finished

#Max, min, mean, median, and Outliers Boxplot
plt.figure()
df[Using_col].boxplot()
plt.title("All Variable Boxplot")
plt.ylabel("# of Observation")
plt.show()


#Pair-wise relationship scatterplot
sns.pairplot(df[Using_col], height=3) 
plt.show()
