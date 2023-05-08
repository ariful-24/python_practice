from numpy import *

# arr = array([1,2,3,4,5,6])
# arr = arr + 5
# print(arr)

# arr1 = array([1,2,3,4,5,])
# arr2 = array([6,1,9,3,2])
#
# arr3 = arr1 + arr2
# print(arr3)

#
# arr1 = array([1,2,3,4,5,])
# print(sum(arr1))
# print(min(arr1))
# print(max(arr1))


# arr1 = array([1,2,3,4,5,])
# arr2 = array([6,1,9,3,2])
# print(concatenate([arr1,arr2]))


# arr1 = array([2,6,8,1,3])
# arr2 = arr1
#
# print(arr1)
# print(arr2)
#
# print(id(arr1))
# print(id(arr2))



arr1 = array([2,6,8,1,3])

#arr2 = arr1.view() # Shallow copy
arr2 = arr1.copy() #deep copy

arr1[1] = 7

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))
