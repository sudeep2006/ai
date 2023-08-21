import pandas as pd
import numpy as np

data=pd.read_csv("C:/Users/SPTINT-11/Desktop/sudeep/iris.csv")
print(data)
df=data.head(5)

ser1=pd.Series(data['species'])
print(ser1)
print(ser1.value_counts())

print(df)

d=pd.DataFrame(df['sepal_length'],['petal_length'])
print(d)

