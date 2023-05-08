
# pos = -1
#
# def search(list,n):
#     i = 0
#
#     while i<len(list):
#         if list[i]==n:
#             globals()['pos']= i
#             return True
#         i=i+1
#     return False
#
#
#
# list = [5,8,4,6,9,2]
#
# n = int(input("Enter number to find "))
#
# if search (list,n):
#     print("found at",pos ,"position")
#
# else:
#     print("Not found")



pos = -1

def search(list,n):
    i = 0

    for i in range(len(list)):
        if list[i]==n:
            globals()['pos']= i
            return True

    return False



list = [5,8,4,6,9,2]

n = int(input("Enter number to find "))

if search (list,n):
    print("found at",pos ,"position")

else:
    print("Not found")