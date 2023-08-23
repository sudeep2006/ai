import pandas as pd
import numpy as np

dict={'first score':[10,20,np.nan,30],
      'second score':[20,30,np.nan,40],
      'third score':[30,np.nan,40,50]}

data=pd.DataFrame(dict)
print(data)
print(data.isnull())
print(data.notnull())
print(data.fillna(0))
print(data.fillna(method='pad'))
print(data.fillna(method='bfill'))
print(data.replace(to_replace=np.nan,value=-50))
print(data.dropna())
print(data.dropna(how='all'))
