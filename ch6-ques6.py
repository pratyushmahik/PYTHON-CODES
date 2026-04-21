#WRITE A PROGRAM TO CALCULATE THE GRADE OF A STUDENT FROM HIS MARKS
# FROM THE FOLLOWING SCHEME:
# 90-100=>EXCELLENT
# 80-90=> A
# 70-80=> B
# 60-70=> C
# 50-60=> D
#  50=>   F

marks=float(input("ENTER YOUR MARKS :"))

if(marks>90 and marks<100):
    print("excellent!!!")
elif(marks>80 and marks<90):
    print("GRADE A")
elif(marks>70 and marks<80):
    print("GRADE B")        
elif(marks>60 and marks<70):
    print("GRADE C")
elif(marks>50 and marks<60):
    print("GRADE D")
elif(marks<50):
    print("GRADE F")
    print("YOU ARE FAILED -RETEST")            