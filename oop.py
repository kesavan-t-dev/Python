# '''
# Docstring for oop
# in python we now know about 
#             - class, 
#             - object, 
#             - inheritance, 
#             - abstraction, 
#             - polymorphism, 
#             - encapsulation
# '''
# '''
# #________Class
# #___example
# class specimen:

#     def __init__(self, name , age):
#         self.name = name ## attributes
#         self.age = age

# a = specimen("hi", 12)
# # print(a)
# print(a.name)

# #_class with methods
# class specimen:

#     def __init__(self, name , age):
#         self.name = name ## attributes
#         self.age = age

#     def sample(self,n):
#         roll_no = "name is {} roll no is {}".format(self.name,n)
#         return roll_no

# b = specimen("user1",65) # we can acess the method not this
# n = b.sample("41") # we can acess the method via this
# print(b.sample(12))

# #exercise
# #__create a car class

# class Car:
#     def __init__(self, color, mileage):
#         self.__private_balance = 50
#         self.color = color
#         self.mileage = mileage
#     def __str__(self):
#         return f"The {self.color} car has {self.mileage:,} miles"
    
# c = Car("red",24000)
# print(c)

# print(c._Car__private_balance)
# '''
# # __now we learn about constructors
# '''
# in python have only one constructor (__init__)
# it helps to create an object or instantiate them when a class is called 
# it has two types
#         - default constructor => self only
#         - parameterized constructor self + paramters 
# '''

# ## Here is the example of the default constructor 
# # class Employee:
# #    def __init__(self, name="Bhavana", age=24): #<-- it is a default values + parameterized constructor
# #       self.name = name
# #       self.age = age
# #    def displayEmployee(self):
# #       print ("Name : ", self.name, ", age: ", self.age)

# # e1 = Employee()
# # e2 = Employee("Bharat", 25)

# # e1.displayEmployee()
# # e2.displayEmployee()

#                 ## default constructor we have that 

# # class Employee:
# #    'Common base class for all employees'
# #    def __init__(self):
# #       self.name = "Bhavana"
# #       self.age = 24

# # e1 = Employee()
# # print ("Name: {}".format(e1.name))
# # print ("age: {}".format(e1.age))

# # # In python we don't support multiple constructor we can achieve that via *args + scenario based like if - elif - else 
# # class Student:
# #    def __init__(self, *args):
# #       if len(args) == 1:
# #          self.name = args[0]
        
# #       elif len(args) == 2:
# #          self.name = args[0]
# #          self.age = args[1]
        
# #       elif len(args) == 3:
# #          self.name = args[0]
# #          self.age = args[1]
# #          self.gender = args[2]
            
# # st1 = Student("Santhiya")
# # print("Name:", st1.name)
# # st2 = Student("Ram", 25)
# # print(f"Name: {st2.name} and Age: {st2.age}")
# # st3 = Student("Shyam", 26, "M")
# # print(f"Name: {st3.name}, Age: {st3.age} and Gender: {st3.gender}")

# '''
# # access modifiers 
# in this access modifiers is used to restrict the class member
#     it has three types 
#         - public 
#         - private 
#         - protected

# public 
#     - access anywhere
# private 
#     - it with double underscore (such as "__age").
#     - it can't be accessible from outside.
#     - it can accessible from within the class only.
# protected
#     - it can be access from the base or derieved class only or same class only.
#     - it with single underscore (such as "_age").
# '''

# #example 
# # class Employee:
# #    def __init__(self, name, age, salary):
# #       self.name = name # public variable
# #       self.__age = age # private variable
# #       self._salary = salary # protected variable
# #    def displayEmployee(self):
# #       print ("Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)

# # e1=Employee("Bhavana", 24, 10000)

# # print (e1.name)
# # print (e1._salary)
# # print (e1.__age)

# #output be like

# '''
# Bhavana
# 10000
# Traceback (most recent call last):
#  File "C:\Users\user\example.py", line 14, in <module>
#   print (e1.__age)
#         ^^^^^^^^
# AttributeError: 'Employee' object has no attribute '__age'

# because __age is private, and not available for use outside the class.
# '''
# # we can access that via mangling techique - not recommended
# #  the private instance variable "__name" is mangled by changing it to the format −
#      #_______ ` obj._class__privatevar `

# #_______Inheritance 
# '''
#  It is used to inherit the properties and behaviours of one class to another. 
#  The class that inherits another class is called a child class and the class that 
#  gets inherited is called a base class or parent class.

#  types of inheritance 
#     - Single Inheritance
#     - Multiple Inheritance
#     - Multilevel Inheritance
#     - Hierarchical Inheritance
#     - Hybrid Inheritance
# '''
# # #sample example for SINGLE inheritance
# # # parent class
# class Parent: 
#    def parentMethod(self):
#       print ("Calling parent method")

# # child class
# class Child(Parent): 
#    def childMethod(self):
#       print ("Calling child method")

# # instance of child
# c = Child()  
# # calling method of child class
# c.childMethod() 
# # calling method of parent class
# c.parentMethod() 


#__Multiple inheritance
# its can be used when you want to get the functionality of multiple classes into a single class
# class Father:
#     def skill1(self):
#         print("Father's skill: Gardening")

# class Mother:
#     def skill2(self):
#         print("Mother's skill: Cooking")

# class Child(Father, Mother):
#     pass
# c = Child()
# c.skill1()
# c.skill2()
# print(Child.mro())

#output
# Father's skill: Gardening
# Mother's skill: Cooking

#'''
# if we multiple inheritance it create a diamond problem python will handle this mature like it has a mro method resolution order it is a c3 linearization algorithm and its is a depth first search algorithm
# it helps to pick which class method call and override it and which one is first and with super we can use that and without super function we can also use that 
#'''
 
# without super or same functions in child how its works in the above u see the father and mother first we have a child class and then father and then mother it the correct order 

#with super and its order 
# class A:
#     def show(self):
#         print("Class A")

# class B(A):
#     def show(self):
#         print("Class B")
#         super().show()

# class C(A):
#     def show(self):
#         print("Class C")
#         super().show()

# class D(B, C):
#     def show(self):
#         print("Class D")
#         super().show()

# d = D()
# d.show()

#output 
#Class D
#Class B
#Class C
#Class A

#_______ Class method 
# in this we use the instance method and class method
class Cloth:
    price = 4000

    def __init__(self, price):
        self.price = price
    ##normal instance  method 
    def show_price(self):
        print("the price is ",self.price)

    @classmethod
    def show_price(self): 
        n = "name"
        print("the price is ",self.price)

    @classmethod 
    def showPrice(cls):
        return cls.price
    @classmethod 
    def showPrice(k7):
        return k7.price

# print(Cloth.showPrice(), "")  
print(Cloth.show_price())
# a = Cloth(10000)
# print(a.show_price())
