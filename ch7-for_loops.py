# WHAT IS A FOR LOOP?
# A FOR LOOP IS USED TO ITERATE THROUGH A SEQUENCE LIKE LIST,TUPLE,OR
# STRING (ITERABLES)


# PRINTING 1-10 USING FOR LOOP
for i in range(1,11):
    print(i)

# WHAT IS A RANGE FUNCTION?
# range() function in python is used to generate a sequence of numbers 
#RANGE GIVES US THE VALUE FROM NOTE(0 TO n-1)---->
for i in range(100): #HERE RANGE 100 AUTOMATICALLY MEANS RANGE(0,100) 
    print(i)

# we can also specify the start,stop,step size using range
# range(start,stop,step_size)

for i in range(0,100,4):
    print(i)

# FOR LOOPS WITH TUPLES,LISTS,STRINGS ARE AS FOLLOWS:---

# ITERATE THE ELEMEMTS OF A LIST USING FOR LOOP 
l=[95,1,6,320.5,"PRATYUSH"]
for i in l:
    print(i)

# ITERATE THE ELEMEMTS OF A TUPLE USING FOR LOOP 
t=(65,23,58,98,75,"MAHIK")
for i in t:
    print(i)

# ITERATE THE ELEMEMTS OF A STRING USING FOR LOOP 
s="PRATYUSH MAHIK"
for i in s:
    print(i)


# FOR LOOPS WITH ELSE-----
# EXAMPLE:

l1=[1,7,2,8]
for item in l1:
    print(item)

else:
    print("DONE") #THIS WILL BE PRINTED WHEN THE LOOP EXHAUSTS!!!   





# BREAK STATEMENT IN FOR LOOP-------->
# BREAK IS USED TO COME OUT OF THE LOOP WHEN ENCOUNTERED.
# IT INSTRUCTS THE PROGRAM TO EXIT THE LOOP RIGHT NOW...

for i in range(0,100):
    if(i==50):
        break #EXITS THE LOOP RIGHT NOW
    print(i)

# CONTINUE STATEMENT IN FOR LOOP------->
# CONTINUE IS USED TO STOP THE CURRENT ITERATION OF THE LOOP AND 
# CONTINUE WITH THE NEXT ONE.IT INSTRUCTS THE PROGRAM TO SKIP THE ITERATION 

for j in range(0,100):
    if(j==65):
        continue #SKIPS THE ITERATION
    print(j)


for k in range(0,60):
    if(k==40):
        continue #SKIPS THE ITERATION
    print(k)


# PASS STATEMENT------->
# IT IS A NULL STATEMENT IN PYTHON AND IT INSTRUCTS TO DO NOTHIMG
# EXAMPLE:

for z in range(710):   #WANNA WRITE IT LATER....JUST WRITE PASS STATEMENT AND PYTHON WILL NOT GIVE ANY ERROR!!
    pass

n=0
while(n<100):
    print(n)
    n=n+1