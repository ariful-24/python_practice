

# a = 5
# b = 0
# try:
#     print(a/b)
# except Exception as e:
#     print("Hey, you can not divided a number by zero ", e)
#
# print("Bey")



# a = 5
# b = 0
# try:
#     print("resource open")
#     print(a/b)
#     #print("resource closed ")
# except Exception as e:
#     print("Hey, you can not divided a number by zero ", e)
#     #print("resource closed ")
#
# finally:
#     print("resource closed ")




a = 5
b = 2


try:

    print("resource open")
    print(a/b)
    k = int(input("Enter a number "))
    print(k)


except ZeroDivisionError as e:
    print("Hey, you can not divided a number by zero ", e)

except ValueError as e:
    print("Invalid error")
except Exception as e:
    print("something error")


finally:
    print("resource closed ")