# input variables
name = input("enter your name: ")
age = input("how old are you? ")

print("-------------")

# the input cames as a string
print(type(name))
print(type(age))

print("-------------")

# if you want to change something in the age, you gotta cast it like this
age = int(age)
age = age + 3
print(f"hello, {name}!")
print(f"you are {age} years old.")

print("-------------")

# exercise 1
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")

print("-------------")

print(f"Today i went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun}")
print(f"{noun} was {adjective2} and {verb}ing")
print(f"I was {adjective3}")

print("-------------")

# exercise 2
height = float(input("Enter the height of a rectangle: "))
width = float(input("Enter the width: "))
length = float(input("Enter the length: "))

volume = height * width * length
print(type(volume))
print(f"Your rectangle area is: {volume}cm^3")

print("-------------")

# exercise 3
item = input("What item would you like to buy? ")
price = float(input("What's the price ? "))
quantity = int(input("How many would you like? "))

total = price * quantity

print(f"you bought {quantity} {item}s, each one of them costs {price}. \n So your total is: ${total}. ")