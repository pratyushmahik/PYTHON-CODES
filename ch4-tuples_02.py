# Tuples is an immutable datatype in Python 
# (meaning you can’t change, add, or remove elements after creation),


a=(1,90,True,"RAHUL") 
b=(85,65,20,2,189,50025.045)
c=[58,96,59,90]
print(type(a))
print(a.count(90))   #COUNT HOW MANY TIMES(X)APPEARED IN TUPLE
print(a.index(90))   #RETURNS THE INDEX OF FIRST OCCURENCE OF (X)
print(len(a))        #RETURNS THE NUMBER OF ELEMENTS IN TUPLE
print(sum(b))        #RETURNS THE SUM OF ELEMENTS IN TUPLE (NUMBERS ONLY)
print(max(b))        #GIVES US THE MAXIMUM VALUE OF THE TUPLE
print(min(b))        #GIVES US THE MINIMUM VALUE OF THE TUPLE
print(sorted(b))     #IT SORTS THE ELEMENTS OF THE TUPLE IN ASCENDING ORDER
print(max(b))


              # OPERATIONS WITH TUPLES

concatenated_tuple=(a+b) #TWO TUPLES CAN ALSO BE ADDED
print(concatenated_tuple)

repeated=b*5
print(repeated) #TUPLES CAN BE REPEATED USING * U CAN USE ASTERISK * WITH THE TUPLE TO GET 
                # THE TUPLE (X) TIMES
                


 # SO IT IS CALLED MEMBERSHIP YOU CAN USE in KEYWORD TO CHECK WHETHER
 #  THE CHARACTER U ENTERED EXISTS IN THE TUPLE OR NOT
print(98 in c)     
print(64 in c)  
print(96 in c)   
print(90 in c)
print("RAHUL" in a)                
