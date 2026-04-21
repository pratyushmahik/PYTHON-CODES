# WRITE A PROGRAM TO PRINT MULTIPLICATION TABLE OF A GIVEN NUMBER 
# USING FOR LOOP AND WHILE LOOP 

# FOR LOOP----->
# a=int(input("WHICH MULTIPLICATION TABLE DO YOU WANT:"))

# for i in range(1,11):
#     print(f"{a} X {i} = {a*i}")

# WHILE LOOP----->
t=int(input(" WHICH MULTIPLICATION TABLE DO YOU WANT:"))

i=1
while(i<11):
    print(f"{t}*{i}={t*i}")
    i+=1