# QUICK QUIZ QUESTION-------->
# WRITE A PROGRAM TO GREET THE USER USING FUNCTION

# def greet():
#     name=input("ENTER YOUR NAME:")
#     # text="GOOD MORNING"
#     print(f"A VERY GOODMORNING TO UHHH {name}!!! \n HOPE YOU HAVE A GOOD DAY AHEAD")

# greet()


# WRITE A PROGRAM TO PRINT THE GREATEST OF THREE NUMBERS 
# USING FUNCTIONS IN PYTHON

a=1
b=2
c=6

def greatest():
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
greatest()    

print(greatest(a,b,c))
