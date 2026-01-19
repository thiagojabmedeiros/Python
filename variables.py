# strings
first_name = "Thiago"
food = "pizza"
email = "thi123@fake.com"

print(first_name)
print(f"hello, {first_name}!")
print(f"you like {food}!")
print(f"your new e-mail is gonna be '{email}'.")

print("--------------------")

# integers
age = 22
quantity = 3
number_of_students = 1280

print(f"you are {age} years old.")
print(f"i bought {quantity} bananas today!")
print(f"in that school {number_of_students} were approved on the CS exam.")


print("--------------------")

# float
price = 89.90
gpa = 3.2
distance = 5.5

print(f"the price is ${price}.")
print(f"your gpa is: '{gpa}'.")
print(f"you ran {distance}km.")

print("--------------------")

# boolean

is_student = True
is_female = False
is_online = True

if is_student:
    print("you are a student")
else:
    print("you are not a student")

if is_female:
    print("you are a woman")
else:
    print("you are not a woman")

if is_online:
    print("im online")
else: 
    print("im offline")