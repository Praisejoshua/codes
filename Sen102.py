#class Myclass:
 #   x = 5
#print(Myclass)
#class Myclass:
 #   x = 5
#p1 = Myclass()
#print(p1.x)
#class Person:
 #   def __init__(self,name,age):
  #      self.name = name
   #     self.age = age
#p1 = Person("john",36)
#print(p1.name)
#print((p1.age))
#class Person:
 #     self.name = name
   #     self.age  = age
#p1 = Person("john", 36)

#print(p1)
#class Person:
 #   def __init__(self,name,age):
  #      self.name = name
   #     self.age = age
    #def myfunc(self):
     #   print("hello my name is " + self.name)
#p1 = Person("john",36)
#p1.myfunc()
class Person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(mysillyobject):
        print("hello my name is "+mysillyobject.name)
p1 = Person("john",36)
p1.myfunc()

#del p1.age===this is to delete a variable name
#class Person:
 #     self.name = name
   #     self.age = age
  #     print("hello my name is " + self.name)
#p1 = Person("john",36)
#del p1.age
#print(p1.age)
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
#use the person class to create an object and then excute the printname method
x = Person("john","Doe")
x.printname()
#child class
class students(Person):
    pass
x = students("mike", "olsen")
x.printname()
