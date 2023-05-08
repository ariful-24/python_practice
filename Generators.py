
#
# def topten():
#
#     #return 5
#     yield 5
#     yield 6
#     yield 7
#     yield 8
#     yield 9
#
# values = topten()
# print(values.__next__())
# print(values.__next__())
#
# for i in values:
#     print(i)


def topten():

    n=1

    while n<= 10:
        sq = n*n
        yield sq
        n+=1

values = topten()

for i in values:
    print(i)