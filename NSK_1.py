import numpy as np
import pandas as pd

s1=pd.Series([1,2,3])
s2=pd.Series([4,5,6])
result = s1+s2
print(result)


a=np.arange(10)
s=slice(2,10,2)
print(a[s])

np.nditer(a) #to iterate over an array

a1=np.array([2,3,4,5])
a2=np.array([10,20,30,40])
a3=a1*a2
print(a3)

a1.shape=(2,2)
a1.ndim()

  