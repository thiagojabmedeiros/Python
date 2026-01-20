# index operator [] - [start : end : step]
# start includes the index's value
# end excludes the index's value
# the step is just the 'step' c:

credit_number = "1234-5678-9012-3456"
print(credit_number)

# the bucket counting starts on 0
print(credit_number[0])
print(credit_number[1])
print(credit_number[2])

# lets combine start and end
# the 6th bucket's value is not appearing because the end exclude the index's value
print(credit_number[0:6])
# you can represent it just putting a colon
print(credit_number[:6]) 

# to finish this tool idea we have the step as the last index inside the operator
print(credit_number[0:18:2])
# the same we can do here, but it does not exclude the last index
print(credit_number[::2])
# this step reverse all the string items
print(credit_number[::-1])
# here you can select the last digits by using a minus signal before the position
# you get the string values reversed
print(credit_number[-1])
print(credit_number[-10:])


print("----------------")

# exercise 
email = input("Enter your e-mail: ")

index = email.index("@")
indexdot = email.index(".com")
print(indexdot)

username = email[:index]
domain = email[index + 1: indexdot]

print(f"Your username is {username} and your domain is '{domain}'.")