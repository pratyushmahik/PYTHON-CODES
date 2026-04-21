marks= {
    "AMIT":85,
    "NEHA":92,
    "RAHUL":78,
    "SNEHA":90,
    100:"PRABJOT"
}
print(marks)
print(marks[100])

print(marks.items())  #SO BASICALLY IT PRINTS THE KEY-VALUE PAIRS IN FORM OF TUPLE
print(marks.keys())   #PRINT ALL THE KEYS OF THE DICTIONARY 
print(marks.values()) #PRINT ALL THE VALUES OF THE DICTIONARY

(marks.update({"SNEHA":88})) #SO UPDATE FUNCTION IS USED TO UPDATE THE
                                  #KEYS OR VALUES OF THE DICTIONARY ALSO WE
                                  # CAN ADD NEW ENTRIES USING THIS FUNCTION 
print(marks)

print(marks.get("RAHUL")) #SO IT GIVES THE VALUE OF THE KEY AND IF THAT KEY 
                          #DOESN'T EXISTS THEN IT SIMPLY GIVES AN OUTPUT NONE  

print(marks["RAHUL"])  #WHEREAS IF U THINK THIS METHOD TO PRINT THE VALUES 
                       #IS SAME AS USING .get function THEN U R WRONG

# THE DIFFERENCE IS THAT IF WE USE .get FUNCTION AND THE KEY IS NOT THERE
# THEN IT RETURNS NONE 
# WHEREAS 
# IF WE USE print DIRECTLY TO PRINT THE VALUE AND IF THE KEY DOESN'T 
# EXISTS IT GIVES US AN ERROR WHICH IS PROBLEMATIC

print(marks.pop(100))  #dict.pop(key) IS USED TO REMOVE A KEY AND RETURNS ITS VALUE
print(marks)

print(marks.popitem()) #SO IT POPS THE LAST INSERTED KEY*VALUE PAIR
print(marks)

print(len(marks)) #IT PRINTS THE LENGTH OF THE DICTIONARY 

marks.clear()  #IT CLEARS OUT THE WHOLE DICTIONARY AND MAKES IT EMPTY     
print(marks)


marks={
    "AMIT":89,
    "FORD MUSTANG":"FORD",
    "PRATYUSH":"MAHIK"
}
print(marks)
print(marks.get("PRATYUSH"))
print(marks.items())
print(marks.keys())
print(marks.values())
# print(marks.update({"PRATYUSH":89}))
