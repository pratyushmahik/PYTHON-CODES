age=int(input("ENTER THE AGE OF PERSON :"))
print("AGE OF THE PERSON IS :",age)

if (age < 5):
    print("YOUR TICKET IS FREE")
    
elif (age>=5 and age <=12):
    print("TICKET IS 100 RUPEES")

elif (age >=13 and age<=59):
    print("TICKET IS 3$")

elif (age >=60):
    print("TICKET IS 1$")

else:print("INVALID INPUT")