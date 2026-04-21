numb=int(input("ENTER THE NUMBER :"))

if(numb<=1):
    print("ITS NOT A PRIME NUMBER ")
elif(numb==2 or numb==3):
    print("ITS A PRIME NUMBER ")
elif(numb%2==0 or numb%3==0 or numb%4==0 or numb%5==0):
    print("NOT A PRIME NUMBER")    
else:
    print("ITS A PRIME NUMBER")



# LIST OF ALL THE PRIME NUMBERS UPTO 100...

# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
# 31, 37, 41, 43, 47, 53, 59, 61, 67,  
# 71, 73, 79, 83, 89, 97
