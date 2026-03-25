# 'and' if all items in the statement are true, the entire statement is true. else if only one is false the entire statement is false

number = 30

if number >= 10 and number <= 35:
    print("That number fits in our notes.")
else:
    print("That number doesn't make sense for us.")

# 'or' if only one statement is true, the entire statement is tru. else it is not
a = 35
if a <= 30 or a >= 50:
    print("True")
else:
    print("False")

# 'not' represents the opposite of the idea
boolean = False
if not boolean:
    print("false")
else:
    print("true")