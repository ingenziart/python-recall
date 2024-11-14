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
