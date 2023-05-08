
class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Covention check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
            ide.execute()

#ide = MyEditor()
ide = PyCharm()
lap1 = Laptop()
lap1.code(ide)