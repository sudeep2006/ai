import numpy as np
#crating array from list with type float
a=np.array([[1,2,4],[5,6,7]],dtype='float')
print("array create using passed list:\n",a)

#creating array from tuple 
b=np.array ((1,3,2))
print("/narray crating original,tuple :",b)

# creating a3x4 array with all zeros
c=np.zeros((3,4,))
print ("/n array initialized with all zeros:\n",c)

#creatinfg a contact value array complex type
d=np.full((3,3),6,dtype='complex')
print("/n array initalixzed with all 6s","array types is complex:\n",d)
# crating an array with random values 
e=np.random.random((2,2))
print ("/n random array:/n",e)

# crating a sequence of integer 
# from 0to 30 with step of 5
f=np.arange(0,30,5)
print("\nAsequential array with steps of 5:\n",f)
g=np.linspace(0,30,5)
print("/n a sequence array with 10 values between" " 0 and5:\n",g)

# reshaping 3X4 array to 2X2X3 array
arr=np.array([[1,2,3,4],[5,2,4,2],[1,2,0,1]])
newarr=arr.reshape(2,2,3)
print("/n original array :\n",arr)
print("/n reshape array :\n",newarr)

# flatten array
arr=np.array([[1,2,3],[3,4,6]])
flarr=arr.flatten()
print("/n original array :\n",arr)
print("flattened array :\n",flarr)

