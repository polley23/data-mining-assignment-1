import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

kidneyData = pd.read_csv('~/Documents/bits/Data Mining/Assignment_BLR/project/processed_data.csv')

#feature extraction
array = kidneyData.values
X = array[:,0:24]
Y = array[:,24]
model = LogisticRegression()
rfe = RFE(model, 12)
fit = rfe.fit(X,Y)

c=0;
for e in fit.support_ :
    if(e == False):
        kidneyData=kidneyData.drop(kidneyData.columns[c], axis=1)
    else : 
        c=c+1
kidneyData.to_csv("reduced_data.csv")

    