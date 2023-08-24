import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/SPTINT-11/Desktop/sudeep/deptment.csv")

a=pd.DataFrame(data)
print(a)

print(data[data['gender']=='female']['salary'].sum())

print((data[(data['gender']=='female')&(data['salary']>200000)].value_counts()))

