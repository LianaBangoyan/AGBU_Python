
text = input("Please input some text: ")

if len(text) >= 20:
    print(text[::-1])
else:
    print("Your text is shorter than our expected range")
#
# homework Write a program that get user input and return every third element from inputed string.
#
text = input("Please input some text: ")
print(text[::3])

# 2 Write a program that get user input and return every second element from inputed string from end
#
text = input("Please input some text: ")
print(text[::-2])

#
#

text = input("Please input some text: ")
if len(text) % 2 == 0:
    print(text[::-1])
else:
    print(text[::2])
#
#

myList = ["Doctor", "Teacher", "Manager", "Engineer"]
if len(myList) != 0:
    print(f"Length of myList is: {len(myList)}")
else:
    print(f"Length of myList is: 0")

#
#
mySet = {1, 2, 3, 4}
number = int(input(Please, insert some number: )),
if number in mySet:
    print(f"Number is presented in mySet")
else:
    print(f"Number isn't presented in mySet")


