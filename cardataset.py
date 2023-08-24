import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/SPTINT-11/Desktop/sudeep/auto-mpg.csv")

a=pd.DataFrame(data)
print(a)

stats=data.describe()
print(stats)

print(data[data['cylinders']==8]['car name'])


