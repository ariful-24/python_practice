

# def add(a,b): #formal Argument
#     c = a+b
#     print(c)
#
# add(6,7)  #Actual Argumnet


# def person(name,age):
#     print(name)
#     print(age)
#
# person("Ariful",22)


# def sum(a,*b):
#     c = a
#
#     for i in b:
#         c =c +i
#
#     print(c)
#
#
# sum(5,6,34,78)



# def person(name, **data):
#
#     print(name)
#     print(data)
#
# person("My name is Ariful",age=28,city="Dhaka",mob=673464593)


def person(name, **data):

    print(name)
    for i,j in data.items():
        print(i,j)

person("My name is Ariful",age=28,city="Dhaka",mobile=673464593)
