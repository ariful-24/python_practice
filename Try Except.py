


""" The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks."""



# try:
#   print(x)
# except:
#   print("An exception occurred")

""" You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:"""

# try:
#   print(x)
# except NameError:
#   print("Variable is not defined")
# except:
#   print("Something else went wrong")

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

"""The finally block, if specified, will be executed regardless if the try block raises an error or not."""
# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("the 'try except' is finished")



try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")