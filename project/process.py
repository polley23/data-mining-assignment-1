import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

kidneyData = pd.read_csv('~/Documents/bits/Data Mining/Assignment_BLR/project/reduced_data.csv')


# kmeansoutput=kmeans.fit(td)
array = kidneyData.values
X = array[:,0:12]
Y = array[:,12]
model = GaussianNB()
# Train the model using the training sets
model.fit(X,Y)

testData = pd.read_csv('~/Documents/bits/Data Mining/Assignment_BLR/project/test_data.csv')
t_array=testData.values[:,0:12]
actual = array[:,12]
c=0
m=0
#Predict Output
for t in t_array.tolist():
    print(t)
    predicted = model.predict([t])
    print("Test case : "+str(c+1)+" actual : "+str(actual[c])+ " predicted : " + str(predicted))
    if actual[c] != predicted[0]:
        m=m+1
    c=c+1
print("miss ratio : ",m/(c+1)*100)