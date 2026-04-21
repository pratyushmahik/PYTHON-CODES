# NOW AFTER LEARNING THE BASICS OF NUMERICAL PYTHON (NUMPY)
# LETS PERFORM SOME BASIC CALCULATIONS IN PYTHON USING THE
# NUMPY LIBRARY.....

# import numpy as np 
# a=np.array([1,2,3,4])
# b=np.array([4,3,2,1])

# print("THE SUM OF BOTH THE ARRAY IS :",a+b)
# print("THE DIFFERENCE B/W BOTH THE ARRAY IS :",a-b)
# print("THE MULTIPLICATION B/W BOTH THE ARRAY IS :",a*b)
# print("THE DIVISION B/W BOTH THE ARRAY IS :",a/b)


# PERFORM 3D MATRIX OPERATIONS USING NUMPY.... 

import numpy as np 
A=np.array([[1,2,3],
            [4,5,6],
            [1,2,3]])

B=np.array([[7,8,9],
            [10,11,12],
            [13,14,15]])

print(A.shape)
print(B.shape)
print(A.dtype)
print(B.dtype)

print("THE SUM OF THE TWO MATRICES IS :\n",A+B)
print("THE DIFFERENCE OF THE TWO MATRICES IS :\n",A-B)
print("THE MULTIPLICATION OF THE TWO MATRICES IS :\n",A*B)
print("THE DIVISION  OF THE TWO MATRICES IS :\n",A/B)


# PERFORM 2D MATRIX OPERATION USING NUMPY......

import numpy as np
C=np.array([[45,21,6],
           [21,6,5]])

D=np.array([[6,1,2],
            [5,21,31]])

print("THE SUM OF THE ARRAYS IS \n",C+D)
print("THE SUBTRACTION OF THE ARRAYS IS \n",C-D)
print("THE MULTIPLICATION OF THE ARRAYS IS \n",C*D)
print("THE DIVSION OF THE ARRAYS IS \n",C/D)