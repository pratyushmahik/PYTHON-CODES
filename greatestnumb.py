# WRITE A PROGRAM TO FIND THE GREATEST OF FOUR NUMBERS
# ENTERED BY THE USER.......

numb1=int(input("ENTER THE FIRST NUMBER :"))
numb2=int(input("ENTER THE SECOND NUMBER :"))
numb3=int(input("ENTER THE THIRD NUMBER :"))
numb4=int(input("ENTER THE FOURTH NUMBER :"))
print("THE FIRST NUMBER IS :",numb1)
print("THE SECOND NUMBER IS :",numb2)
print("THE THIRD NUMBER IS :",numb3)
print("THE FOURTH NUMBER IS :",numb4)

if(numb1>numb2 and numb1>numb3 and numb1>numb4):
    print("THE GREATEST NUMBER IS NUMB1:",numb1)

elif(numb2>numb1 and numb2>numb3 and numb2>numb4):
     print("THE GREATEST NUMBER IS NUMB2:",numb2)

elif(numb3>numb1 and numb3>numb2 and numb3>numb4):
    print("THE GREATEST NUMBER IS NUMB3:",numb3) 

elif(numb4>numb1 and numb4>numb2 and numb4>numb3):
    print("THE GREATEST NUMBER IS NUMB4:",numb4) 

else:
    print("INVALID INPUT")               