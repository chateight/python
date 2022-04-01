class Test(object):
    c_var = "Hello"

    def __init__(self):
        self.i_var = "World"

    def __str__(self):
        return Test.c_var + " " + self.i_var

    def examine1(self):
        self.c_var = "Hey1"
        return self

    def examine2(self):
        Test.c_var = "Hey2"
        return self

t = Test()
print(t.examine1())
print(Test())
print(t.examine2())

class PersonA:
  def __init__(self, name, age):
    self._name = name
    self._age = age
  
class PersonB(PersonA):
  def __str__(self):
    return ('{}は{}歳です'.format(self._name, self._age))

a = PersonA('太郎', 10)
b = PersonB('花子', 20)
print(a)
print(b)

