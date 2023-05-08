

class A:

    def __init__(self):
        print("In a Init")

    def feature1(self):
        print("Feature 1-a working")

    def feature2(self):
        print("Feature 2 working")


class B():
    def __init__(self):
        print("In b Init")

    def feature3(self):
        print("Feature 1-b working")

    def feature4(self):
        print("Feature 4 working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in c init")

    def feat(self):
        self.feature2()


a1 = C()
a1.feat()
