arr = [3,4,9,6]
arr2 = [23,45,90,61]
for i in arr:
    print(i)
for i, n in enumerate(arr):
    print(i, n)
for i in range(len(arr)):
    print(arr[i])
for n1, n2 in zip(arr, arr2):
    print(n1,n2)