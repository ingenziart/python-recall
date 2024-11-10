x = "hello word "
print(x.replace("h", "j"))

# concatenate

a = "hello"
b = "januzaj"
c = a + " " + b
print(c)
# concatenate str with int ypu add f in the beginning and {}.
age = 36
tx = f"mynamje is aime and i am {age}"
print(tx)

num = 34
str1 = f"my rate{num}"
print(str1)

# escaping character \"\"
text3 = 'halland is from "viking" clan '
print(text3)

# accs the list

thislist = ["mango", "banana", "passion", "blueberry", "stwaberry"]
print(thislist[-4:-1])

# change the list


thislist = ["mango", "banana", "passion", "blueberry", "stwaberry"]
thislist[1:3] = ["januzaj", "aime"]
print(thislist)

# insert method
thislist = ["mango", "banana", "passion", "blueberry", "stwaberry"]
thislist.insert(2, "watermellon")
print(thislist)

# extend()


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# remove method in the list

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# delete method (will couse the error but its actually its deleted completery )
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)

# clear method
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# loop list

thislist = ["apple", "banana", "cherry"]
for i in thislist:
    print(i)

# list complession

thislist = ["apple", "banana", "cherry"]

newlist = []

for i in thislist:
    if "a" in i:
        newlist.append(i)

print(newlist)

# sort list

thislist = ["apple", "banana", "cherry"]
thislist.sort()
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.sort(reverse=True)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.sort(reverse=True)
for i in thislist:
    print(i)

# copy the list

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
print(list1)


# turple

thisturple = ("apple", "banana", "mango", "strawbelly")
print(thisturple)

thistuple = ("apple",)
print(type(thistuple))

# turple can store different data type

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

# convert turple to list

thisturple = ("apple", "banana", "mango", "strawbelly")
x = list(thisturple)
x[1] = "kiwi"
print(x)

# the secret is to change turple into list coz turple can not be changeble.

thisturple = ("apple", "banana", "mango", "strawbelly")
x = list(thisturple)
x.append("orange")
print(x)

# to add turple (concatenate turple)


thisturple = ("apple", "banana", "mango", "strawbelly")
athor = ("orange",)
thisturple += athor
print(thisturple)

# Note: When creating a tuple with only one item, remember to include a comma after
# the item, otherwise it will not be identified as a tuple.

# remove items
# you can not rwmove something on turple coz is unchangable you just tun into list

thisturple = ("apple", "banana", "mango", "strawbelly")
x = list(thisturple)
x.remove("banana")
print(x)

# set

thisset = {"banana", "orange", "brueberry", "strawbelly"}
print(thisset)

# set can not repeat items
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


thisset = {"apple", "banana", "cherry", "apple"}

for x in thisset:
    print(x)
# dictionary is like object in javascripts

mydictional = {"name": "aime", "surname": "januzaj", "dob": 2000}
print(mydictional)

# print out one property

mydictional = {"name": "aime", "surname": "januzaj", "dob": 2000}
print(mydictional["name"])

mydictional = {"name": "aime", "surname": "januzaj", "dob": 2000}
x = mydictional.keys()
print(x)

mydictional = {"name": "aime", "surname": "januzaj", "dob": 2000}
x = mydictional.values()
print(x)

mydictional = {"name": "aime", "surname": "januzaj", "dob": 2000}
x = mydictional.values()
print(x)
mydictional["dob"] = 2024
print(x)

# change dictional using update()

mydictional = {"name": "aime", "surname": "januzaj", "dob": 2000}

mydictional.update({"dob": 2024})

print(mydictional)

# remove item on dictional is pop
mydictional = {"name": "aime", "surname": "januzaj", "dob": 2000}
mydictional.pop("dob")
print(mydictional)

# loop
mydictional = {"name": "aime", "surname": "januzaj", "dob": 2000}

for x in mydictional:
    print(mydictional[x])

# if

a = 30
b = 20
if a < b:
    print("yes")
else:
    print("noo")

# while loop note you have to increment the loop
i = 1

while i < 6:
    i += 1
    print(i)

# break method

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# for loop and break


fruit = ["apple", "banana", "mango"]
for i in fruit:
    if i == "banana":
        break
    print(i)


# function


def my_function():
    print("hello")


my_function()


def my_function(fname):
    print(fname + " mbabazi")


my_function("ingenzi")

# function with passing arguments and parameters


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("mbbabazi", "aime")


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


def my_function(**kids):
    print("lastborn is" + kids["lname"])


my_function(fname="janu", lname="januzaj")


def my_country(country="norway"):
    print("my country is " + country)


my_country()
my_country("rwanda")

# passing a list as argument


def my_function(food):
    for i in food:
        print(i)


fruit = ["banana", "mango", "berry"]
my_function(fruit)
