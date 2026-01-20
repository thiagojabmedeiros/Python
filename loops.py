username = input("Enter your username: ")

while not username.isalpha():
    print(f"{username} is not valid, it can not have digits")
    username = input("Enter another username: ")

print(f"hello, {username}")
    

