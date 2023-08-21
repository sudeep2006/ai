import pandas as pd
import numpy as np

info=pd.array([1,2,3,4,5])
p=pd.Series(info)
q=pd.Series([1,2,3,4])
print(q)
print(p)

arr=pd.Series(4,[0,1,2,3,4,5])
print(arr)

p=pd.Index([1,2,3,np.nan,5])
print(p.value_counts())

