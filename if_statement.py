# exercise 1
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up.")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't born yet.")
else:
    print("You must be 18+ to sign up.")

print("---------------")

# exercise 2 
response = input("Would you like some food? (Y/N) ")

if response == "Y":
    print("Have some food!")
elif response == "N":
    print("Shut up and get away.")
else:
    print("I didn't understand.")

print("---------------")

# exercise 3
name = input("Enter your name: ")

if name == "":
    print("You didn't type your name.")
else:
    print(f"Hello, {name}!")

print("---------------")

# exercise 4
is_sale = True

if is_sale:
    print("The item is for sale")
else:
    print("The item is not for sale")
