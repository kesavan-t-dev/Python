'''
Docstring for oop
in python we now know about 
            - class, 
            - object, 
            - inheritance, 
            - abstraction, 
            - polymorphism, 
            - encapsulation
'''
'''
#________Class
#___example
class specimen:

    def __init__(self, name , age):
        self.name = name ## attributes
        self.age = age

a = specimen("hi", 12)
# print(a)
print(a.name)

#_class with methods
class specimen:

    def __init__(self, name , age):
        self.name = name ## attributes
        self.age = age

    def sample(self,n):
        roll_no = "name is {} roll no is {}".format(self.name,n)
        return roll_no

b = specimen("user1",65) # we can acess the method not this
n = b.sample("41") # we can acess the method via this
print(b.sample(12))

#exercise
#__create a car class

class Car:
    def __init__(self, color, mileage):
        self.__private_balance = 50
        self.color = color
        self.mileage = mileage
    def __str__(self):
        return f"The {self.color} car has {self.mileage:,} miles"
    
c = Car("red",24000)
print(c)

print(c._Car__private_balance)
'''
# __now we learn about constructors
'''
in python have only one constructor (__init__)
it helps to create an object or instantiate them when a class is called 
it has two types
        - default constructor => self only
        - parameterized constructor self + paramters 
'''

## Here is the example of the default constructor 
# class Employee:
#    def __init__(self, name="Bhavana", age=24): #<-- it is a default values + parameterized constructor
#       self.name = name
#       self.age = age
#    def displayEmployee(self):
#       print ("Name : ", self.name, ", age: ", self.age)

# e1 = Employee()
# e2 = Employee("Bharat", 25)

# e1.displayEmployee()
# e2.displayEmployee()

                ## default constructor we have that 

# class Employee:
#    'Common base class for all employees'
#    def __init__(self):
#       self.name = "Bhavana"
#       self.age = 24

# e1 = Employee()
# print ("Name: {}".format(e1.name))
# print ("age: {}".format(e1.age))

# In python we don't support multiple constructor we can achieve that via *args + scenario based like if - elif - else 
class Student:
   def __init__(self, *args):
      if len(args) == 1:
         self.name = args[0]
        
      elif len(args) == 2:
         self.name = args[0]
         self.age = args[1]
        
      elif len(args) == 3:
         self.name = args[0]
         self.age = args[1]
         self.gender = args[2]
            
st1 = Student("Santhiya")
print("Name:", st1.name)
st2 = Student("Ram", 25)
print(f"Name: {st2.name} and Age: {st2.age}")
st3 = Student("Shyam", 26, "M")
print(f"Name: {st3.name}, Age: {st3.age} and Gender: {st3.gender}")

'''
# access modifiers 
in this access modifiers is used to restrict the class member
    it has three types 
        - public 
        - private 
        - protected

public 
    - access anywhere
private 
    - it with double underscore (such as "__age").
    - it can't be accessible from outside.
    - it can accessible from within the class only.
protected
    - it can be access from the base or derieved class only or same class only.
    - it with single underscore (such as "_age").
'''

#example 
class Employee:
   def __init__(self, name, age, salary):
      self.name = name # public variable
      self.__age = age # private variable
      self._salary = salary # protected variable
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)

e1=Employee("Bhavana", 24, 10000)

print (e1.name)
print (e1._salary)
print (e1.__age)

#output be like
'''
Bhavana
10000
Traceback (most recent call last):
 File "C:\Users\user\example.py", line 14, in <module>
  print (e1.__age)
        ^^^^^^^^
AttributeError: 'Employee' object has no attribute '__age'

because __age is private, and not available for use outside the class.
'''
# we can access that via mangling techique - not recommended
#  the private instance variable "__name" is mangled by changing it to the format −
     #_______ ` obj._class__privatevar `

