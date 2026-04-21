# SO WE HAVE CREATED A TUPLE NAMED CITIES
cities=("DELHI","MUMBAI","CHENNAI","DELHI","KOLKATA")

# NOW WE ARE USING THE INDEX NUMBER OF THE FIRST CITY
# TO PRINT IT
print(cities[0])

# HERE WE PRINTED LAST TWO CITIES USING SLICING OF TUPLE
sliced_cities=cities[3:5]
print(sliced_cities)

# SO HERE WE ARE USING A NEW VARIABLE NAMED
# UPDATED TUPLE AND UPDATE CHENNAI TO BANGLORE
updated_tuple=("DELHI","MUMBAI","BANGLORE","DELHI","KOLKATA")
print(updated_tuple)

# SO NOW WE ARE UNPACKING THE TUPLES
(city1,city2,city3,city4,city5)=updated_tuple
print(city1)
print(city2)
print(city3)
print(city4)
print(city5)

