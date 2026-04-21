# a=(1,90,True,"RAHUL",5,5,5,5,5) 
# print(a.count(True))
# print(a.index(90))

# students={
#     "PRATYUSH":"100",
#     "PRANAV":"52",
#     "RACHIT":"85",
#     "SANCHIT":"90",
#     "list":"778899,25625"
# }
# print(students)
# print(students["PRATYUSH"])
# print(students["RACHIT"])
# print(students["list"])

# cars={
#     "PRATYUSH":"BMW M5",
#     "RAHUL":"GWAGON R",
#     "MANSI":"PINK BWM",
#     "list":[56,23,1]
# }
# print(cars)
# print(type(cars))
# print(cars["MANSI"])
# print(cars["RAHUL"])
# print(cars.items())
# print(cars.keys())
# cars.update({"RAHUL": "TESLA"})
# print(cars)
# cars.update({"PRATYUSH":"BMW M5 COMPETITION","ASTHA":"FORTUNER"})
# print(cars)
# cars.update({"PAPA":"DEFENDER 130"})
# print(cars)
# print(cars["list"])
# print(cars.get("PRATYUSH"))
# print(cars["PRATYUSH"])
# print(cars.pop("MANSI"))
# print(cars)
# print(cars.popitem())
# print(cars)
# print(cars.items())

# age=int(input("ENTER YOUR AGE :"))

# if(age>=18):
#     print("YES")
# elif(age<=0):
#     print("HAHAH")
# else:
#     print("NO")

# WRITE A PROGRAM TO CALCULATE THE GRADE OF A STUDENT 
# FROM HIS MARKS 

# name=input("ENTER THE NAME OF THE STUDENT :")
# marks=int(input("ENTER THE MARKS : "))

# if(marks>90 and marks<100):
#     print("EXCELLENT SCORE")
# elif(marks>80 and marks<90):
#     print("YOU SCORED GRADE A \n KEEP IT UP") 
# elif(marks>70 and marks<80):
#     print("YOU SCORED GRADE B \n PLZ IMPROVE YOURSELF")
# elif(marks>60 and marks<70):
#     print("YOU SCORED GRADE C \n MEET ME IN THE OFFICE") 
# elif(marks>50 and marks<60):
#     print("YOU SCORED GRADE D \n MEET ME IN THE OFFICE") 
# elif(marks<50):
#     print("YOU SCORED GRADE F AND FAILED THE TEST")
# else:
#     print("INVALID INPUT") 


# post=(input("THE COMMENT IS :"))

# if ("subscribe me".lower() in post.lower()):
#     print("SPAM COMMENT")
# else:
#     print("NOT A SPAM COMMENT")

# a=[5,4,3,2,1]
# a.reverse()
# print(a)

# a=(1,2,"PRATYUSH",True)
# print(a,type(a))
# print(a.count(2))
# print(a)

# Program to demonstrate List, Tuple and Dictionary operations

# # ----- List Operations -----
# print("---- List Operations ----")
# my_list = [1, 2, 3]
# print("Original List:", my_list)

# my_list.append(4)
# print("After append:", my_list)

# my_list.insert(1, 10)
# print("After insert :", my_list)

# my_list.remove(2)
# print("After remove :", my_list)

# my_list.sort()
# print("After sort:", my_list)

# my_list.reverse()
# print("After Reverse:", my_list)


# # ----- Tuple Operations -----
# print("\n---- Tuple Operations ----")
# my_tuple = (10, 20, 30, 40, 20)
# print("Tuple:", my_tuple)

# print("Count of 20:", my_tuple.count(20))
# print("Index of 30:", my_tuple.index(30))
# print("Length of tuple:",len(my_tuple))
# print("Sliced tuple:", my_tuple[1:4])
# print("Sum of tuple:", sum(my_tuple))
# print("Nested tuple example:", (1, 2, (3, 4)))
# print("Immutability: Tuples cannot be modified")


# ----- Dictionary Operations -----
# print("\n---- Dictionary Operations ----")
# my_dict = {
#             "name": "Pratyush",
#             "college": "MIT-WPU"
#           }
# print("Original Dictionary:", my_dict)

# print("Keys:", my_dict.keys())
# print("Values:", my_dict.values())
# print("Items:", my_dict.items())

# print("Get name:", my_dict.get("name"))
# my_dict["branch"] = "CSE"
# print("After adding branch:", my_dict)

# my_dict.clear()
# print(my_dict)

# removed = my_dict.pop("name")
# print("After popping 'age':", my_dict, "| Removed:", removed)

# WRITE A PROGRAM TO FIND THE GREATEST NUMBER OUT OF THREE NUMBERS 
# ENTERED BY THE USER...

# a=int(input("ENTER NUMB 1:"))
# b=int(input("ENTER NUMB 2:"))
# c=int(input("ENTER NUMB 3:"))

# if(a>b and a>c):
#     print("THE GREATEST NUMBER IS a :",a )
# elif(b>a and b>c):
#     print("THE GREATEST NUMBER IS b:",b) 
# elif(c>a and c>b):
#     print("THE GREATEST NUMBER IS c:",c)
# else:
#     print("INVALID INPUT BY THE USER")           

# marks=int(input("enter the marks scored in maths :"))

# if(marks>=90 and marks<=100):
#     print("GRADE : O")
# elif(marks>=80 and marks<=89):
#     print("GRADE : A+")
# elif(marks>=70 and marks<=79):
#     print("GRADE : A")
# elif(marks>=60 and marks<69):
#     print("GRADE : B")
# elif(marks>=50 and marks<=59):
#     print("GRADE : C")
# elif(marks>=40 and marks<=49):
#     print("GRADE : p")
# elif(marks<40):
#     print("GRADE : F")
# else:
#     print("INVALID MARKS ENTERED BY THE USER")    


# a=[1,2,3,4,5,6,7,8,9]
# print(a[::2])

# l=[1,2,3]
# init_tuple=('Python',)*(l.__len__()-l[::-1][0])
# print(init_tuple)

# marks=int(input("ENTER THE MARKS:"))

# if (marks>=90 and marks<=100):
#     print("you scored a")
# elif(marks>=80 and marks<=89):
#     print("you scored a+")    
# elif(marks>=70 and marks<=79):
#     print("you scored a")    
# elif marks>=60 and marks<=69:
#     print("YOU SCORED B")
# elif (marks>50 and marks<=59):
#     print("you scored c")        
# elif (marks>40 and marks<49):
#     print("you scored p")
# elif(marks<39):
#     print("failed")  
# else:
#     print("INVALID INPUT BY THE USER")




# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
#
# print(dict1.update(dict2))
# print(dict1)


# a=[1,32,6,"pratyush"]
# b=a.index("pratyush")
# print(b)


# names=["AMIT","NEHA","RAHUL","SNEHA","RAHUL"]
# names.append("VIKASH")
# names.insert(2,"PRIYA")
# print(names.count("RAHUL"))
# print(names.index("NEHA"))
# names.remove("RAHUL") 
#   #REMOVES THE FRST OCCURENCE OF (X) FROM THE LIST
# names.pop(4)
# backup=names.copy()

# backup.extend(["KARAN","MEENA"])
# print(backup)

# names.clear()
# print(names)

# numb=int(input("enter a number:"))

# if(numb>0):
#     print("postive")
# elif(numb<0):
#     print("negative")
# elif(numb==0):
#     print("THE NUMBER IS ZERO")

# marks= {
#     "AMIT":85,
#     "NEHA":92,
#     "RAHUL":78,
#     "SNEHA":90,
#     100:"PRABJOT"
# }

# print(marks["NEHA"])
# print(marks.items())
# print(marks.keys())
# print(marks.values())

# print()
# # -7 -6 -5 -4 -3 -2 -1 
# a=[1,2,3,4,5,6,7]
# #  0 1 2 3 4 5 6
# print(a[3:6]) 
# print(a[-1:-4]) #SO WE CANNOT WRITE NEGATIVE SLICING LIKE THIS BECAUSE IT WILL RETURN AN EMPTY LIST

# print(a[-4:-1])

# dict_1={
#     "PRATYUSH":56,
#     "RESHMA":65
# }

# dict_2={
#     "MANSI":60,
#     "RAHUL":8

# }
# print(dict_1.update(dict_2))
# print(dict_1)

# cities=["SIKKIM","JAMMU","KASHMIR"]
# print(cities)
# cities.append("PATNA")
# cities.append("LEH")
# print(cities)

# cities.remove("LEH")
# print(cities)

# cities_tuple=tuple(cities)
# print(cities_tuple)

# print(cities_tuple[0:1])
# print(cities_tuple[-1:])
# print(cities_tuple[1:3])

# scores=[50,200,110,2,65]
# scores.sort()
# scores.reverse()
# print(scores)

# scores_tuple=tuple(scores)
# print(scores_tuple)

# p1,p2,p3,p4,p5=scores_tuple

# print("THE HIGHEST SCORE IS ",p1)
# print("THE LOWEST SCORE IS ",p5)
# print("THE AVERAGE SCORE IS :",round(sum(scores_tuple)/len(scores_tuple)))

# WRITE A PROGRAM TO FIND THE BODY MASS INDEX 

# weight=float(input("ENTER THE WEIGHT (in kgs) :"))
# height=float(input("ENTER THE HEIGHT (in metre^2)"))

# body_mass_index=(weight/height)

# if(body_mass_index<18.5):
#     print("UNDERWEIGHT")
# elif(body_mass_index>=18.5 and body_mass_index<=24.9):
#     print("NORMAL WEIGHT") 
# elif(body_mass_index>=25.0 and body_mass_index<29.9):
#     print("OVERWEIGHT")
# elif(body_mass_index>30.0):
#     print("OBESE")
# else:
#     print("INVALID INPUT")   

# numb=(input("ENTER THE NUMBER :"))

# if numb==numb[::-1]:
#     print("ITS A PALINDROME NUMBER",numb)
# else:
#     print("ITS NOT A PALINDROME NUMBER",numb)    


# Take input from user
# num = input("Enter a number: ")

# # Check if the number is the same when reversed
# if num == num[::-1]:
#     print(num, "is a palindrome number.")
# else:
#     print(num, "is not a palindrome number.")

# a=(56,23,True,False,"PRATYUSH")
# print("THE INDEX NUMBER IS ",a.index(56))
# print("THE INDEX NUMBER IS ",a.index("PRATYUSH"))

# print(a[0:5])
# print(a[0:])
# print(a[:5])
# print("THE NEGATIVE SLICING IS:",(a[-5:]))

# WRITE A PROGRAM TO PRINT THE CONTENTS OF LIST USING WHILE LOOP

# l=["MANGO","PINEAPPLE","56",63.2,556,69]

# i=0
# while(i<len(l)):
#     print(l[i])
#     i=i+1

# a=(56,23,91.05,"PRATYUSH",True,56,91,56)
# print("THE NUMBER OF TIMES 56 APPEARED IS :",(a.count(56)))

# print(a.index(True))

# comment=input("TYPE UR COMMENT HERE :")

# if("pratyush".lower() in comment.lower()):
#     print("THIS COMMENT IS TALKING ABOUT PRATYUSH ")

# WAP TO FIND THE GREATEST OF FOUR NUMBERS 
# numb1=int(input("ENTER THE FIRST NUMBER :"))
# numb2=int(input("ENTER THE SECOND NUMBER :"))
# numb3=int(input("ENTER THE THIRD NUMBER :"))
# numb4=int(input("ENTER THE FORTH NUMBER :"))

# print("THE FIRST NUMBER IS :",numb1)
# print("THE SECOND  NUMBER IS :",numb2)
# print("THE THIRD NUMBER IS :",numb3)
# print("THE FORTH NUMBER IS :",numb4)

# if(numb1==numb2 or numb1==numb3 or numb1==numb4):
#     print("ALL THE NUMBERS ARE EQUAL")
# elif(numb1==numb2):
#     print("FIRST NUMBER AND SECOND NUMBER IS EQUAL")    

# if(numb1>numb2 and numb1>numb3 and numb1>numb4):
#     print("THE GREATEST NUMBER IS NUMB 1:",numb1)

# elif(numb2>numb1 and numb2>numb3 and numb2>numb4):
#     print("THE GREATEST NUMBER IS NUMB 2:",numb2) 

# elif(numb3>numb1 and numb3>numb2 and numb3>numb4):
#     print("THE GREATEST NUMBER IS NUMB 3:",numb3)

# elif(numb4>numb1 and numb4>numb2 and numb4>numb3):
#     print("THE GREATEST NUMBER IS NUMB 4:",numb4)

# else:
#     print("INVALID INPUT BROTHER")    


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


# import pandas as pd
# data = {'Name': ['Amit', 'Priya', 'Ravi'], 'Age': [20, 21, 19]}
# df = pd.DataFrame(data)
# print(df)


# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3], [10, 20, 30])
# plt.title("Simple Graph")
# plt.show()

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# print("NumPy, Pandas, and Matplotlib imported successfully!")

# # Quick test
# data = {'Name': ['Amit', 'Priya', 'Ravi'], 'Age': [20, 21, 19]}
# df = pd.DataFrame(data)
# print(df)

# plt.plot([1, 2, 3], [10, 20, 30])
# plt.title("Test Graph")
# plt.show()

# Program to demonstrate List, Tuple and Dictionary operations

# List Operations
print("---LIST OPERATIONS---")
my_list = [1, 2, 3]
print("Original List:", my_list)

my_list.append(4)
print("After append:", my_list)

my_list.insert(1, 10)
print("After insert:", my_list)

my_list.remove(2)
print("After remove:", my_list)

my_list.reverse()
print("After reverse:", my_list)

# Tuple Operations
print("\n---TUPLE OPERATIONS---")
my_tuple = (10, 20, 30, 40, 20)
print("Tuple:", my_tuple)

print("Count of 20:", my_tuple.count(20))
print("Index of 30:", my_tuple.index(30))

print("Length of tuple:", len(my_tuple))
print("Sliced tuple:", my_tuple[1:4])
print("Sum of tuple:", sum(my_tuple))

# Dictionary Operations
print("\n---DICTIONARY OPERATIONS---")
my_dict = {
    "name": "Pratyush",
    "college": "NIT-AP"
}

print("Original Dictionary:", my_dict)

print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

print("Get 'name':", my_dict.get('name'))

my_dict["branch"] = "CSE"
print("After adding branch:", my_dict)

my_dict.clear()
print("After clear:", my_dict)