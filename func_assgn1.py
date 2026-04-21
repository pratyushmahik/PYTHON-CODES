# # WRITE A PROGRAM TO CHECK WHETHER ITS A RIGHT ANGLE TRAINGLE OR NOT

# def check_right_triangle(a, b, c):
#     # Put largest side at c (hypotenuse)
#     sides = sorted([a, b, c])
#     if sides[2]**2 == sides[0]**2 + sides[1]**2:
#         print("It is a right-angled triangle")
#     else:
#         print("It is not a right-angled triangle")


# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# check_right_triangle(a, b, c)




# WRITE A PROGRAM TO DISPLAY ALL THE EVEN NUMBERS IN A RANGE 
# 1 TO 100

def even_numbers():
    for i in range(2, 101, 2):
        print(i, end=" " )
    print()

# Main program
print("Even numbers from 1 to 100 are:")
even_numbers()


# numb=int(input("ENTER A NUMBER :"))
# factors=[]
# i=2
# while i<=numb:
#     factors.append(i)
#     numb=numb//i
# else: 
#     i+=1   
# print("PRIME FACTORS ARE :",factors)    

# factors_conv=set(factors)
# print(factors_conv)


import math

def quadratic_roots(a, b, c):
    d = b**2-4*a*c   # discriminant
    if d < 0:
        print("No real roots")
    elif d == 0:
        root = -b / (2*a)
        print("Roots are real and equal:", root)
    else:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print("Roots are real and different:", root1, "and", root2)

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

quadratic_roots(a, b, c)
