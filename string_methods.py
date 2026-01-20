name = input("Enter your name: ")

# it returns how many characters/numbers/signals the string has
result = len(name)
print(result)

# all digits is going to be uppercase
result = name.upper()
print(result)

# all digits is going to be lowercase
result = name.lower()
print(result)

# firts digit is gonna be uppercase
result = name.capitalize()
print(result)

# if it's only characters, it's going to return True, otherwise it returns false (spaces are not included as characters)
result = name.isalpha()
print(result)

# if it is a digit, its going to return true, otherwise it returns false
result = name.isdigit()
print(result)

# first 'character' position, if the method does not find what you want them it returns -1
result = name.find("a")
print(result)
result = name.find("z")
print(result)


# last 'character' position
result = name.rfind("m")
print(result)

# this method counts how many 'characters' it has
result = name.count("a")
print(result)

# this method replace selected 'characters', switching it by the one which you chose
result = name.replace(" ", "")
print(result)
result = len(result)
print(result)


print("------------------")

# exercise 1
username = input("Enter your username: ")

if len(username) > 15:
    print("your username cann't be more than 15 characters")
elif not username.find(" ") == -1:
    print("your usernmae cann't have spaces")
elif not username.isalpha():
    print("your username can only have alphabetic characters")
else:
    print(f"Hello, {username}!")

