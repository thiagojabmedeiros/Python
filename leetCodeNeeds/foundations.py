# this file is gonna help us to remeber what is important to know before leetcoding

# variables are really flexible, you dont need to cast it to change its type
number = 12
print(number)
print(type(number))
number = "12"
print(number)
print(type(number))
print("1#######")


# multiple assignments 
n, m = 0, "abc"

# incrementing
n = n + 1
n += 1
print(n)
print("2#######")

# None is null = no value
x = 3
x = None
print("x =", x)
print("3#######")

# if statements dont need parentheses or curly braces
n = 4
if n > 2:
    print("n is greater than 2")
elif n == 2:
    print("n is equal to 2")
else:
    print("n is less than 2")
print("4#######")

# or == ||
# and == &&
# not = !
if n < 2 or n == 2:
    print(n)
elif n > 2 and not n == 3:
    print(n)
print("5#######")

# loops
n = 0
while n < 5:
    print(n)
    n += 1
print("6#######")

# i starts from 0 and goes until n - 1: range(n) 
for i in range(5):
    print(i)
print("7#######")
# range(start, end, step)
for i in range(2, 5):
    print(i)
print("8#######")
for i in range(5, 1, -1):
    print(i)
print("9#######")

# math in python:
import math
# integer division
print(3 / 2)
print(3 // 2)
print(-3 / 2)
print(-3 // 2)
print(int(-3 / 2))
# Math functions
print(math.floor(3/2))
print(math.ceil(3/2))
print(math.sqrt(4))
print(math.pow(2, 3))

# infinite numbers
print(float("inf"))
print(float("-inf"))
if math.pow(100, 100) > float("inf"):
    print(True)
else:
    print(False)
print("10#######")

# arrays
arr = [1,2,3]
print(arr)
# the append function in arrays only add elements in the end
arr.append(4)
arr.append(5)
# pop function if not used with parameters removes the last element in the array, otherwise it removes the element where the index is equal to the parameter
arr.pop()
arr.pop(0)
print(arr)
# we can also use insertions to add the eleemnt in any position inside the array, insert(index, value)
arr.insert(2,5)
print(arr)
# dinamically changing the size of the array
arr = [1] * 5
print(arr)
# slicing eleemnts
arr = [1,2,3,4,5,6,7,8,9,10]
print(arr[1:])
print(arr[1:9])
print(arr[-1])
print(arr[:-1])
# unpacking
a, b, c = [1,2,3]
print(a,b,c)

print("11#######")
nums = [312,22,435,1000]
for i in range(len(nums)):
    print(nums[i], i)
for n in nums:
    print(n)
for i, n in enumerate(nums):
    print(i, n)
numx = [32, 435, 3215, 12343]
for n1, n2 in zip(nums, numx):
    print(n1, n2)
print("12#######")

nums = [6,4,1,2,9,5,7,3,8]
print(nums)
nums.sort()
print(nums)
nums.reverse()
print(nums)

# some short hand
arr = [[0] * 4 for i in range(5)]
print(arr)