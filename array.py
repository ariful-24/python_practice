from array import *

#vals = array('i',[4,6,9,1])
#vals.reverse()

# for i in range(5):
#     print(vals[i])


# for e in vals:
#     print(e)



# vals = array('u',['a','e','i','o'])
#
# for i in range(4):
#     print(vals[i])


vals = array('i',[5,6,7,2,9])
newArr = array(vals.typecode,(a for a in vals))
for e in newArr:
    print(e)


newArr = array(vals.typecode,(a*a for a in vals))
for e in newArr:
    print(e)
