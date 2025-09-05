import numpy as np

ar1=np.array([1,2,3,4,5])
ar2=np.array([4,5,6,7,8])

print ('Addition of each positional element of the array',ar1+ar2)

#Using a single dimensional array and changing its shape to 2D array
ar3=np.array([1,2,3,4,5,6])
print('Original array',ar3.shape)
ar3=ar3.reshape(2,3)
print('Reshaped array',ar3.shape)
print(ar3)

#Creating a 3D array
ar4=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print('3D array',ar4)
print('Dimension of 3D array',ar4.ndim)
print('Shape of 3D array',ar4.shape)
print('Size of 3D array',ar4.size)

#Add 1 to each element of the array
ar5=np.array([1,2,3,4,5])
print('Original array',ar5)
ar5=ar5+1 #This is called broadcasting. Used in matrix operations.
print('Array after adding 1 to each element',ar5)

#Dot product of two arrays
ar6=np.array([[1,2],[3,4]])
ar7=np.array([[5,6],[7,8]])
print('Dot product of two arrays')
print(np.dot(ar6,ar7))

#Array contains nan
ar8=np.array([1,2,np.nan,4,5])
print('Array with nan',ar8)
print('Check if array contains nan',np.isnan(ar8))

#Interesting bits of numpy.
print ('Interesting bits of numpy.')
import time
ls=list(range(100000000))
npArray=np.array(ls)
start=time.time()
np.sum(npArray)
print('Time taken by numpy',time.time()-start)

start=time.time()
sum(ls)
print('Time taken by python',time.time()-start)
