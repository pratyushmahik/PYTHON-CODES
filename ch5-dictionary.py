# DICTIONARY IS MUTABLE
# IT IS INDEXED
# IT IS UNORDERED
# CANNOT CONTAIN DUPLICATE KEYS 

marks= {
    "Vedant":98,
    "Chinmayee":99,
    "Prateek":72,
    "Pratyush":88,
    "Rahul":37,
    "Ritesh":59,
    "Saksham":89
}
print(type(marks))  #IT SHOWS class dict INDICATING THAT ITS A DICTIONARY
print(marks)
print(marks["Vedant"])
print(marks["Prateek"])
print(marks["Saksham"])

# SO AS WRITTEN ABOVE THAT IT SHOULD NOT CONTAIN 
# DUPLICATE KEYS LETS TAKE AN EXAMPLE...

my_dict = {
    "name": "Pratyush",  
    "age": 19,
    "name": "Mahik"
}

print(my_dict)

##SO ABOVE YOU CAN SEE THAT ALTHOUGH WE GAVE THE SAME KEY
# i.e. "name" TO OUR VALUES "pratyush" AND "mahik" BUT ONLY 
# THE LAST VALUE GETS PRINTED i.e. "mahik"


d={} #THIS IS AN EMPTY DICTIONARY
print(d)


# WE CAN MERGE A DICTIONARY BY THIS METHOD

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

print(dict1.update(dict2))
print(dict1)