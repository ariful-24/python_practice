from array import *
arr = array('i', [])
n = int(input("Enter the length of array"))

for i in range(n):
    x= int(input("Enter the next value"))
    arr.append(x)

print(arr)

val = int(input("Enter the value of search"))

k = 0
k+=1
for e in arr:
    if e==val:
        print(k)
        break
else:
        print("not in the list")

#print(arr.index(val))
