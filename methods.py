


class Student:

  school = 'Grren'

  def __init__(self,m1,m2,m3):
    self.m1 =m1
    self.m2 =m2
    self.m3 =m3

  def avg(self):
    return (self.m1 + self.m2 + self.m3)/3

  @classmethod
  def getSchool(cls):
    return cls.school

  @staticmethod
  def info():
    print(" This is a student class..")

s1 = Student(34,56,67)
s2 = Student(45,67,34)

print(s2.avg())
print(Student.getSchool())
Student.info()