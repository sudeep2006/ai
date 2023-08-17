import pandas as pd

data=pd.read_csv("C:/Users/SPTINT-28/Desktop/dataset/pubg.csv")
print(data)
print(data.head(5))
print(data.tail(5))
print(data.info())
print(data.dtypes)
print(data.count())
