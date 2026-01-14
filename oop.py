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