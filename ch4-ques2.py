# WRITE A PROGRAM TO ACCEPT MARKS OF 
# 6 STUDENTS AMD DISPLAY THEM 
# IN A SORTED MANNER

marks=[]
m1=int(input("ENTER THE MARKS OF FIRST STUDENT :"))
marks.append(m1)
m2=int(input("ENTER THE MARKS OF SECOND STUDENT :"))
marks.append(m2)
m3=int(input("ENTER THE MARKS OF THIRD STUDENT :"))
marks.append(m3)
m4=int(input("ENTER THE MARKS OF FORTH STUDENT :"))
marks.append(m4)
m5=int(input("ENTER THE MARKS OF FIFTH STUDENT :"))
marks.append(m5)
m6=int(input("ENTER THE MARKS OF SIXTH STUDENT :"))
marks.append(m6)

marks.sort()
print(marks)
