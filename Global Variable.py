

a = 10

def something():
    a = 15

    print("in fun ", a)

    # globals()['a'] = 16

something()

print("outside",a)