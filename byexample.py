text = input("inter text vslue: ")

num1 = int(input("enter the number: "))
num2 = int(input("enter the second value:"))
answer = num1 + num2
print(answer)

num1 = 12
if num1 > 10:
    print("its over")
elif num1 == 10:
    print("this is equal")
else:
    print("none of them")

santense = "januzaj aime mbabazi"
print(len(santense))
print(santense.upper())
print(santense.capitalize())
print(santense.title())

# math
import math

num = round(6466, 2)
print(math.sqrt(num))

# for loop

for i in range(1, 10):
    print(i)

word = "januzaj"
for i in word:
    print(i)

fruit_tuple = ("banana", "mango", "passion")
print(fruit_tuple.index("strawbery"))

list1 = ["janu", "aime", "mbabazi"]
del list1[0]

print(list1)

# in python list is array and dictionary is object in javascripts
