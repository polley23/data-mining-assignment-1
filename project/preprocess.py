import pandas as pd
#Reading data set
kidneyData = pd.read_csv('~/Documents/bits/Data Mining/Assignment_BLR/kidneyChronic.csv')

#Dropping data set with missing value
new_data= kidneyData.dropna(how="any")

#Writing the dataset 
new_data.to_csv("processed_data.csv")

print pca.explained_variance_ratio_