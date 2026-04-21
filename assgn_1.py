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
    "college": "MIT-WPU"
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