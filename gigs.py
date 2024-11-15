def addition(x, y):
    return x + y


newNumber = addition(2, 5)
print(newNumber)


def myfunction():
    print("hello python programming")


myfunction()


class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def __str__(self):
        return self.firstname


print(person("aime", "januzaj"))


class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def myfunction(self):
        return f"{self.firstname}, {self.lastname}"


p = person("aime", "januzaj")
print(p.myfunction())


class person:
    def __init__(self, fname, lastname):
        self.firstname = fname
        self.lastname = lastname

    def allname(self):
        print(self.firstname, self.firstname)


p = person("aime", "januzaj")
print(p.allname())

my_array = [7, 12, 9, 4, 11]
minval = my_array[0]
for i in my_array:
    if i < minval:
        minVal = i


print("the Lowest", minval)

my_array = [7, 12, 9, 4, 11]
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i

print("Lowest value:", minVal)

# inhrertance


class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = person("John", "Doe")
x.printname()
