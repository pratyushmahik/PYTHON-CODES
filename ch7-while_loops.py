# IN WHILE LOOP,THE CONDITION IS CHECKED FIRST,IF IT EVALUATES TO TRUE,
# THE BODY OF LOOP IS EXECUTED OTHERWISE IS EXITS

# PRINTING 1-10 USING WHILE LOOP
i=1
while(i<11):
    print(i) 
    i+=1
    # i=i+1 #BOTH ARE SAME i+=1 and i=i+1
# THE BLOCK KEEPS EXECUTING UNTIL CONDITION IS TRUE...


# WRITE A PROGRAM TO PRINT ROM 1-50 USING A WHILE LOOP 
# ----->
j=1
while(j<51):
    print(j)
    j=j+1   

a=0
while(a<101):
    print("I LOVE CODING")
    # print(a)
    a=a+1

# WRITE A PROGRAM TO PRINT THE CONTENTS OF A LIST USING 
# WHILE LOOP

l=[23,45,64,"PRATYUSH","MAHIK",63.054]

m=0
while(m<(len(l))):
    print(l[m])
    m=m+1


# PRINTING 1-10 USING FOR LOOP
for i in range(1,11):
    print(i)