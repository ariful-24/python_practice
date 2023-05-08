names = ("Arif","Owasib","Shawn")
comps = ("Dell","Apple","MS")

# zipped = list(zip(names,comps))
# zipped = set(zip(names,comps))
# zipped = dict(zip(names,comps))
# print(zipped)


zipped = zip(names,comps)

for (a,b) in zipped:
    print(a,b)