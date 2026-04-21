# WHY TO USE NUMPY (NUMERICAL PYHTON) ????
#-------> NUMPY REPLACES NORMAL LISTS WITH POWERFUL OBJECTS CALLED "ARRAYS" WHICH IS FASTER,MORE EFFICIENT AND
#         ALLOWS US TO MATHEMATICAL OPERATIONS ON ENTIRE DATASETS AT ONCE... 

# IT PROVIDES EFFICIENT STORAGE 
# IT ALSO PROVIDES BETTER WAYS OF HANDLING DATA FOR PRPCESSING 
# IT IS FAST
# IT IS EASY TO LEARN
# IT USED RELATIVELY LESS MEMORY TO STORE DATA

import numpy as np
print("NumPy Imported Successfully...!!!")

import numpy as np
myarr=np.array([3,6,37,7],np.int64)
myarr1=np.array([2,1,3,6,65.2],np.int16)
print(myarr)
print(myarr1)
print(myarr[0])
print(myarr[1])
print(myarr[2])
print(myarr[3])

print(myarr.shape) #TELLS US HOW MANY ROWS AND COLUMNS ARE THERE 
print(myarr.dtype) #TELLS US THE TYPE IT IS MADE OF (int8,int16,int32,int64,float16,.....)

print(myarr1)
myarr1[4]=81
print(myarr1) #AS YOU CAN SEE THAT ITS MUTABLE TOO....

# myarr2=np.array([[2,5,15,32,64,8.6]])
myarr2=np.array([[2,5,15,32,64,8]])
print(myarr2)
print(myarr2.dtype)
print(myarr2.shape)
squared=myarr2**2
cubed=myarr2**3
print(squared)
print(cubed)