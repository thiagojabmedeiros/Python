username = input("Enter your username: ")

# infinte loop conditional
while not username.isalpha():
    print(f"{username} is not valid, it can not have digits")
    username = input("Enter another username: ")

print(f"hello, {username}")
    
print("-----------")

# finite loop determinated
for x in range(1, 11):
    print(x)

print("-----------")

credit_number = "1234-5678-9012-3456"
for x in credit_number:
    if x == "-":
        continue
    else:
        print(x)

print("-----------")

num2 = "123.456.787654.32343546.543"
for x in num2:
    if x == "7":
        break
    else: 
        print(x)

print("-----------")

# nested loop
for z in range(3):
    for y in range(1 ,10):
        print(y, end="")
    print()

# exercise nested loop to create a block with user's chose size
height = int(input("Enther the height of your rectangle: "))
width = int(input("Enter the width of your rectangle: "))
symbol = input("Wich symbol do you want to fill your rectangle? ($, %, *, #, @)\n")

for x in range(height):
    for y in range(width):
        print(symbol, end=" ")
    print()