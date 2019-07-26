import pandas as pd


kidneyData = pd.read_csv('~/Documents/bits/Data Mining/Assignment_BLR/kidneyChronic.csv')

print(kidneyData.loc[:,"bp"].median())