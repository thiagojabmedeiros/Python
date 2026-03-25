import math

print(math.pi)
print(math.e)
n = 9
result = math.sqrt(n)
print(result)
m = 9.5
result = math.ceil(m)
print(result)
j = 8.5
result = math.floor(j)
print(result)

print("-------------")

# longest version to operate
friends = 0
print(f"friends: {friends}")
friends = friends + 1
print(f"friends plus one: {friends}")
friends = friends * 6
print(f"friends times six: {friends}")
friends = friends / 2
print(f"friends divided by 2: {friends}")
friends = friends ** 3
print(f"friends power 3: {friends}")

remainder = friends % 5
print(f"the remainder if we divide {friends} by 5 is: {remainder}.")

print("-------------")

# shortest version to operate
hamburguers = 1 
print(f"hamburguers: {hamburguers}")
hamburguers += 3
print(f"hamburguers plus two: {hamburguers}")
hamburguers -= 1
print(f"hamburguers minus one: {hamburguers}")
hamburguers *= 10
print(f"hamburguers times ten: {hamburguers}")
hamburguers /= 2
print(f"hamburguers dived : {hamburguers}")

remainder = hamburguers % 4
print(f"the remainder if we divide {hamburguers} by 4 is: {remainder}.")

print("-------------")

# math functions
w = 8
x = 3.14
y = -4
z = 5

resultx = round(x)
print(resultx)

resulty = abs(y)
print(resulty)

resultz = pow(z, 2)
print(resultz)

resultmin = min(w, x, z)
resultmax = max(x, y, z)
print(resultmin)
print(resultmax)

print("-------------")

# exercise circle 
radius = int(input("Enter a radius for the circle (cm): "))
size = 2 * (math.pi) * radius
area = math.pi * pow(radius, 2)
print(f"your cicunference size is: {round(size, 2)}cm")
print(f"your circle area is: {round(area, 2)}cm^2")

print("-------------")

# exercise hypotenuse
a = int(input("Enter the side 'a' of your triangle (cm): "))
b = int(input("Enter the side 'b' of your triangle (cm): "))
c = math.sqrt((pow(a, 2) + pow(b, 2)))

print(f"This triangle hypotenuse values: {round(c, 2)}cm")


