def birthday(name, age):
    print(f"happy birthday to {name}!")
    print(f"you are {age} years old!")
    print("happy birthday to you!")
    print()

birthday("thiago", 22)

print("---------------------------")
def add(x, y):
    z = x + y
    return z
def subtraction(x, y):
    z = x - y
    return z
def multiple(x, y):
    z = x * y
    return z
def divide(x, y):
    z = x // y
    return z

n = add(1,6)
print(n)
n = subtraction(n, 5)
print(n)
n = multiple(n, 5)
print(n)
n = divide(n, 2)
print(n)

print("---------------------------")
def create_name(first_name, last_name):
    first = first_name.capitalize()
    last = last_name.capitalize()
    full_name = first + " " + last
    return full_name

full_name = create_name("thiago", "medeiros")
print(full_name)
