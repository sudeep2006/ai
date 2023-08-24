import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/SPTINT-11/Desktop/sudeep/branch.csv")

a=pd.DataFrame(data)
print(a)

print(data[data['gender']=='male']['dept']=='cs')

print(data[data['gender']=='female']['dept']=='cs')

salary=data.groupby('dept')['salary'].sum()
print(salary)
