# typecasting

name = "Thiago"
last_name = ""
age = 30
gpa = 8.999999
student = True 
online = False

# types
print(type(gpa))
print(type(name))
print(type(age))
print(type(student))
print(type(online))

print("-----------")

# explicit casting
age = float(age)
print(age)

gpa = int(gpa)
print(gpa)

#if the boolean is True, it values 1, else it values 0 
student = int(student)
print(student)

online = float(online)
print(online)

#if the str space is empty, it values False, else it values True
name = bool(name)
print(name)
last_name = bool(last_name)
print(last_name)


#implict casting
x = 2
y = 3.0

x = x / y

print(x)