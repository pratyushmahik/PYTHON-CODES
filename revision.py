# QUESTION NUMBER-1
# WRITE A PROGRAM TO SHOW SOME OF THE ARTHEMATIC QUESTIONS BY THE NUMBER GIVEN BY THE USER..

# numb1=int(input("ENTER THE FIRST NUMBER:"))
# numb2=int(input("ENTER THE SECOND NUMBER:"))
# print("THE FIRST NUMBER IS :",numb1)
# print("THE SECOND NUMBER IS :",numb2)
# print("THE SUM OF THE NUMBERS IS :",(numb1+numb2))
# print("THE SUBTRACTION OF THE TWO NUMBERS IS :",(numb1-numb2))
# print("THE MULTIPLICATION OF THE TWO NUMBERS IS :",numb1*numb2)
# print("THE DIVISION OF THE TWO NUMBERS ENTERED IS :",numb1/numb2)
# print("THE FLOOR DIVISION OF THE TWO NUMBERS ENTERED IS :",numb1//numb2)

# QUESTION NUMBER-2
# WRITE A PROGRAM IN PYTHON TO CHECK WHETHER A PERSON IS ELIGIBLE TO APPLY FOR 
# DRIVING LICENSE OR NOT...

# name=input("ENTER THE NAME OF THE APPLICANT :")
# age=int(input("ENTER THE AGE OF THE APPLICANT :"))
# print("NAME OF THE APPLICANT :")
# print("AGE OF THE APPLICANT :")

# if(age>0 and age<18):
#     print("YOU ARE NOT ELIGIBLE TO APPLY FOR DRIVER'S LICENSE ")
# elif(age>=18 and age<=89):
#     print("YOU ARE ELIGIBLE TO APPLY FOR DRIVERS LICENSE")
# elif(age>89):
#     print("SORRY RESPECTED CITIZEN YOU ARE INELIGIBLE TO DRIVE \n  ON INDIAN ROADS!!!!!!") 
# else:
#     print("INVALID INPUT")           

# CONVERSION OF VARIABLE FROM ONE DATA TYPE TO ANOTHER...
# a="90.5"
# print(type(a))
# b=float(a)
# print(type(b))

# FORMAT STRING LITERAL (f-string)
# name=input("ENTER THE NAME :")
# print(f"HEY A WARM AND OVERWHELMING GOODMORNING TO YOU {name} !!!!!!!")

# FIND THE SQUARE AND CUBE OF A NUMBER ENTERED BY A USER 
# n=int(input("ENTER THE NUMBER :"))
# print(f"SO WE HAVE TO FIND THE SQUARE AND CUBE OF {n}")
# print(f"THE SQUARE OF {n} IS :",n**2)
# print(f"THE CUBE OF {n} IS :",n*n*n)
# print(f"THE CUBE OF {n} IS :",n**3)

# name=input("ENTER YOUR NAME :")
# college=input("ENTER THE NAME OF YOUR COLLEGE :")
# course=input("ENTER THE NAME OF YOUR COURSE :")

# print(f"HELLOWWW EVERYONE!!!MY NAME IS {name} AND I STUDY IN {college} \n I HAVE PURSUED {course} HERE")
# hiring_letter='''
#         Dear <Name>,
#         You are selected!!!
#         Our Company Has Hired You as Our 
#         SLD-Engineer 1
#         <Date>'''
# replaced_hiring_letter=hiring_letter.replace("<Name>",f"{name}").replace("<Date>","01/11/2025")
# print(replaced_hiring_letter)

# WRITE A PROGRAM TO CHECK WHETHER A STUDENT HAS PASSED HIS EXAMS OR NOT
# IF HE NEEDS AN OVERALL 40% MARKS AND 33% MARKS IN EACH SUNJECT 

# name=input("ENTER THE NAME OF THE STUDENT:")
# english=float(input("ENTER THE MARKS SCORED IN ENGLISH:"))
# hindi=float(input("ENTER THE MARKS SCORED IN HINDI :"))
# maths=float(input("ENTER THE MARKS SCORED IN MATHS :"))
# # print(f"MARKS SCORED IN ENGLISH BY {name} IS :",english)            
# # print(f"MARKS SCORED IN HINDI BY {name} IS :",hindi)            
# # print(f"MARKS SCORED IN MATHS BY {name} IS :",maths)
# total_percent=((english+hindi+maths)/300)*100

# if(english>=33 and hindi>=33 and maths>=33 and total_percent>=40):
#     print(f"CONGRATULATIONS {name} YOU HAVE PASSED THE EXAM")
#     print(f"YOU HAVE SCORED {total_percent}PERCENTAGE")
# else:
#     print(f"SORRY {name} YOU HAVE FAILED THE EXAM \nBETTER LUCK NEXT TIME \nYOU HAVE TO WORK REALLY HARD")
#     print(f"YOU HAVE SCORED {total_percent} PERCENTAGE")    

# for i in range(1,91):
#     print(i)

# i=1
# while(i<11):
#     print(i)
#     # i+=1
#     i=i+1

# i=1
# while(i<51):
#     print(i)
#     i=i+1

# i=1
# while(i<101):
#     print("I LOVE MY INDIA")
#     i=i+1

# WRITE A PROGRAM TO PRINT THE CONTENTS OF A LIST IN PYTHON 
# USING WHILE LOOP...

# l=[65,23,True,"PRATYUSH MAHIK","LION","TESLA","GUIDO VAN ROSSUM"]
# i=0
# while(i<(len(l))):
#     print(l[i])
#     i+=1


# l1=["TAJ MAHAL",True,"GUIDO VAN ROSSUM ",696969] 
# i=0
# while(i<len(l1)):
#     print(l1[i])
#     i=i+1   

# l2=["PRATYUSH","MAHIK","True","False","GUIDO VAN ROSSUM"]
# i=0
# while(i<len(l2)):
#     print(l2[i])
#     i+=1

# for i in range (15):
#     print("GUIDO VAN ROSSUM")
#     i+=1

  
# USE WHILE LOOP AND FOR LOOP TO PRINT THE CONTENTS OF A LIST

# l=["  ","STRINGRAY","VOLVO","True","RAJPAL YADAV",56,57,58,59,60]
# i=0
# for i in range(len(l)):
#     print(l[i])

# i=0
# while(i<len(l)):
#     print(l[i])
#     i+=1    

# t=(56,25,94,23,"TIZEN")    
# i=0
# for i in t:
#     print(i)

# t=(98,2,23,65,48)    
# i=0 
# while(i<len(t)):
#     print(t[i])
#     i=i+1

# s="PRATYUSH IS A NOOB"
# for i in s:
#     print(i)

# s="PRATYUSH IS A NOOB"
# for i in s:
#     print(i)
# else:
#     print("DONE")

# for i in range(1,15000000):
#     if i>10:
#         break
#     print(i)

# for i in range(100):
#     if i==10:
#         continue
#     print(i)


# for k in range(70):
#     if (k>56 and k<60):
#         continue
#     elif(k==67):
#         break
#     print(k)

# text="FIND THE CARS WHOSE REG.NO ARE 0812 AND 4712"
# import re
# result=re.findall("\dt",text)
# print(result)

# import re

# text = "Hello123"

# # Check if text contains only a-z, A-Z, 0-9
# if re.fullmatch(r'[A-Za-z0-9]+', text):
#     print("Valid: contains only letters and digits")
# else:
#     print("Invalid: contains other characters")

# def avg():
#     a=int(input("ENTER THE FIRST NUMBER :"))
#     b=int(input("ENTER THE SECOND NUMBER :"))
#     c=int(input("ENTER THE THIRD NUMBER :"))
#     avg=(a+b+c)/3
#     print(avg)

# avg()    
# avg()    
# avg()    
# avg()    

# str1="HELLO"
# str2="WORLD!"
# print("str1+str2=",str1+str2)