from numpy import *

# arr1 = array([
#                 [1,2,3],
#                 [4,5,6]
#              ])
#
#
# arr2 = arr1.flatten()
# print(arr1.ndim)
# print(arr2)



# arr1 = array([
#                 [1,2,3,6,2,9],
#                 [4,5,6,7,5,3]
#              ])
#
#
# arr2 = arr1.flatten()
# #arr3 = arr2.reshape(3,4)
# arr3 = arr2.reshape(2,2,3)
#
# print(arr3)





# arr1 = array([
#                 [1,2,3],
#                 [4,5,6]
#              ])
#
#
# m = matrix('1 2 3; 6 4 5; 2 6 7')
# print(diagonal(m))
# print(m.max())



m1 = matrix('1 2 3; 6 4 5; 1 6 7')
m2 = matrix('1 2 3; 6 8 5; 2 6 7')

m3 = m1*m2

print(m3)