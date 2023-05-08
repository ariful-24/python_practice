
# def is_even(n):
#     return n%2==0
#
# nums = [3,2,6,8,4,6,2,9]
#
# evens = list(filter(is_even,nums))
# print(evens)


# nums = [3,2,6,8,4,6,2,9]
#
# evens = list(filter(lambda n: n%2==0,nums))
# odds = list(filter(lambda n: n%2==1,nums))
# print(evens)
# print(odds)


from functools import reduce

# def add_all(a,b):
#     return a+b

nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda n: n%2==0,nums))
doubles = list(map(lambda n: n*2,evens))
print(doubles)

sum = reduce(lambda a,b : a+b,doubles)

print(sum)
