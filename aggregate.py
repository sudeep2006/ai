import numpy as np

arr=np.array([[1,2,3],[3,4,5]])
arr1=np.array([[6,7,8],[9,4,5]])
print(arr.ndim)
print(arr.sum())
print(arr.sum(axis=1))
print(arr.max())
print(arr.min())
print(arr.max(axis=1))
print(arr.min(axis=1))
print(arr.transpose())
print(arr.cumsum())
print(arr.cumsum(axis=1))
print(arr+arr1)

