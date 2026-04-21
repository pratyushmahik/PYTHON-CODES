# WRITE A PROGRAM TO ACCEPT MARKS IN MATHS AND DISPLAY RESPECTIVE GRADE AS AN OUTPUT
# USING IF-ELIF-ELSE LADDER (MULTIPLE CONDITIONS)

marks=int(input("enter the marks scored in maths :"))

if(marks>=90 and marks<=100):
    print("GRADE : O")
elif(marks>=80 and marks<=89):
    print("GRADE : A+")
elif(marks>=70 and marks<=79):
    print("GRADE : A")
elif(marks>=60 and marks<69):
    print("GRADE : B")
elif(marks>=50 and marks<=59):
    print("GRADE : C")
elif(marks>=40 and marks<=49):
    print("GRADE : p")
elif(marks<40):
    print("GRADE : F")
else:
    print("INVALID MARKS ENTERED BY THE USER") 