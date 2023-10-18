# 1.Write a Python program to get the largest number from a list.
#
myList = [52, 147, 3, 148, 3000, 2520]
myList.sort()
print(f"Result after sorted is: {myList}")
print(5, myList)

# 2. Write a Python program to check a list is empty or not.
#
myList = ["Doctor", "Teacher", "Manager", "Engineer"]
if len(myList) != 0:
    print(f"Length of myList is: {len(myList)}")
else:
    print(f"Length of myList is: 0")

# 3. Write a Python program to remove all elements from a given set.

mySet = {"Fruits", "Berries", "Vegetables", "Flowers"}
print(mySet)
print(type(mySet))
mySet.remove("Fruits")
print(f"Result after removing is {mySet}")


# 4. Write a Python program to check if a given value is present in a set or not.
#
mySet = {1, 2, 3, 4}
myNumber = int(input(f"Please, insert some number: "))
if myNumber in mySet:
    print(f"Number is presented in mySet")
else:
    print(f"Number isn't presented in mySet")

# 5. Write a Python program to convert a list to a tuple.

myList = (11, 22, 33, 44, 55)
print(type(myList))
print(tuple(myList))
# 6. Write a Python program to remove an item from a tuple.
myTuple = [9, 8, 7, 6, 5]
x = list(myTuple)
x.remove(6)
myTuple = tuple(x)

#
# 7. Write a Python script to check whether a given key already exists in a dictionary or not.

myDict = {"Flowers": ["rose", "orchid", "lily"],
        "Fruits": ['Peach', 'Banana', 'Pineapple'],
        "Metals": ['Gold','Aluminium', 'Ferrum']}
if "Fruits" in myDict:
    print(f"Mentioned key exists in the myDict dictionary"),

# 8. Write a Python script to merge two Python dictionaries.
myDict1 = {"Flowers": ["rose", "orchid", "lily"],
        "Fruits": ['Peach', 'Banana', 'Pineapple'],
        "Metals": ['Gold','Aluminium', 'Ferrum']}
myDict2 = {"Cars": ["Audi", "Lexus", "BMV"],
          "Vegetables": ['Tomato', 'Cucumber', 'Potato'],
          "Berries": ['Strawberry', 'Watermelon', 'Blackberry']}
myDict = {
    "myDict1": myDict1,
    "myDict2": myDict2}

print(myDict)

