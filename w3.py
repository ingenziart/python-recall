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
