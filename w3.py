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
