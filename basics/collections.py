# list = [] - ordered and changeable. duplicates OK
# tuple = ()

fruits = ["banana", "apple", "orange", "coconut"]

for fruit in fruits:
    print(fruit, end=" ")

print()
print(len(fruits))
print("chocolate" in fruits)
print("apple" in fruits)

# to add in the end of the list
fruits.append("pineapple")
print(fruits)

# replace in any position, you just gotta change the index 
fruits[0] = "lemon"
print(fruits)

# or you can do something different  by the function
fruits.insert(2, "strawberry")
print(fruits)

# and if you want to remove out of the list any item 
fruits.remove("coconut")
for fruit in fruits:
    print(fruit, end=" ")
print()

# sort list
fruits.append("banana")
fruits.sort()
print(fruits)

# reverse list
fruits.reverse()
print(fruits)

# find the index of some item
print(fruits.index("banana"))

# how many items this list has?
print(len(fruits))



# set = {} - unordered and imutable, but add/remove ok. duplicates are not allowed
cars = {"civic", "crv", "corola", "sw4", "sentra", "kicks"}

print(cars)
print(len(cars))

cars.add("peugeot passion")
print(cars)
print(len(cars))

cars.remove("kicks")
print(cars)

cars.pop()
print(cars)