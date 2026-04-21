# WRITE A PROGRAM TO CHECK THAT A STRING CONTAINS ONLY A CERTAIN SET OF CHARACTERS 
# (IN THIS CASE a-z,A-Z and 0-9) USING PYTHON PROGRAMMING...... 

import re
text = input("HEY USER ENTER ANYTHING YOU WANT:")

if re.fullmatch(r'[A-Za-z0-9]+', text):
    print("It contains only letters and digits")
else:
    print("Invalid Input")