

"""A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern."""

import re

txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
#
# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")


"""The findall() function returns a list containing all matches."""

# x = re.findall("ai",txt)
# print(x)


"""The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned:"""

# x = re.search("\s", txt)
# print("The first white-space character is located in position:", x.start())


# x = re.split("\s", txt)
# x = re.split("\s", txt, 1)
# print(x)

"""The sub() function replaces the matches with the text of your choice:"""
# x = re.sub("\s", "9", txt)
# print(x)
"""Replace the first 2 occurrences"""
# x = re.sub("\s", "9", txt, 2)
# print(x)

""" The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match """

x = re.search(r"\bS\w+", txt)
print(x.span())
#print(x.string)
#print(x.group())



