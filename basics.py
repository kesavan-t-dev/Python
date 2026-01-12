print("hellow")

name = "my name"
print(name)
# it will update the below name initialise
name = 12
print(name)
# it is a dynamic language we change the datatype for their variable names 

#'''This is for indentation for selection statements'''

if 9 > 5:  
  print("9 is greater than 5")      # proper indentation  
  print("This is part of the if block")  
print("This is outside the if block")  
print('\n')
print('\n')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Operators 
# Arithmetic operator
# example
a = 46    # Initializing the value of a      
b = 4     # Initializing the value of b      
    
print("For a =", a, "and b =", b,"\nCalculate the following:")    
    
# printing different results    
print('1. Addition of two numbers: a + b =', a + b)      
print('2. Subtraction of two numbers: a - b =', a - b)      
print('3. Multiplication of two numbers: a * b =', a * b)      
print('4. Division of two numbers: a / b =', a / b)      
print('5. Floor division of two numbers: a // b =',a // b)      
print("""6. Reminder of two numbers: a '%' b =""", a % b)     # '%' for it takes the values for the operator in the single string and triple string so i use the single '  
print("""7. Exponent of two numbers: a ^/'**' b =""",a ** b)    # '**' it will multiply the two string from before and after 
print('\n')
print('\n')

################################################################################################################################################

## Comparison Operator
# example
a = 46    # Initializing the value of a      
b = 4     # Initializing the value of b      
    
print("For a =", a, "and b =", b,"\nCheck the following:")    
    
# printing different results    
print('1. Two numbers are equal or not:', a == b)      
print('2. Two numbers are not equal or not:', a != b)      
print('3. a is less than or equal to b:', a <= b)      
print('4. a is greater than or equal to b:', a >= b)      
print('5. a is greater than b:', a > b)      
print('6. a is less than b:', a < b) 
print('7. a is not equal b:', a != b) 
print('\n')
####################################################################################################################################

# assignment operator
a = 34         # Initialize the value of a      
b = 6          # Initialize the value of b      
    
# printing the different results    
print('a += b:', a + b)      
print('a -= b:', a - b)      
print('a *= b:', a * b)      
print('a /= b:', a / b)      
print('a %= b:', a % b)    
print('a **= b:', a ** b)      
print('a //= b:', a // b)   


#########################################################################################################################################
'''
1   Numeric Types
int, float, complex

2   Sequence Types
str, list, tuple, range

3   Set Types
set, frozenset

4   Mapping Type
dict

5   Boolean Type
bool

6   Binary Types
bytes, bytearray, memoryview
7  None Type
NoneType

'''
# python program to show how to declare integers in Python  
  
# initializing some variables with integers  
var_1 = 16  # positive integer  
var_2 = -21 # negative integer  
var_3 = 0   # zero  
  
# printing the types of initialized variables  
print("Data Type of", var_1, "=", type(var_1))  
print("Data Type of", var_2, "=", type(var_2))  
print("Data Type of", var_3, "=", type(var_3))  
print()

# python program to show how to declare floating-point numbers in Python  
  
# initializing some variables with floating-point numbers  
var_1 = 1.72  # positive float  
var_2 = -0.05 # negative float  
var_3 = 0.0   # zero as a float  
var_4 = 1.6e4 # scientific notation  
  
# printing the types of initialized variables  
print("Data Type of", var_1, "=", type(var_1))  
print("Data Type of", var_2, "=", type(var_2))  
print("Data Type of", var_3, "=", type(var_3))  
print("Data Type of", var_4, "=", type(var_4)) 

print()

# python program to show how to declare complex numbers in Python  
  
# initializing some variables with complex numbers  
var_1 = 3 + 5j  # where 2 is the real part and 5 is the imaginary part  
var_2 = -3.4 + 2.8j  
var_3 = -5 - 1.9j  
var_4 = -6 + 0j  
  
# printing the types of initialized variables  
print("Data Type of", var_1, "=", type(var_1))  
print("Data Type of", var_2, "=", type(var_2))  
print("Data Type of", var_3, "=", type(var_3))  
print("Data Type of", var_4, "=", type(var_4))  
print()

# simple python program to show how to initialize a list  
  
# creating a list  
list_1 = [1, 0.5, 'hello', 1+5j, 1.7e2, -12, 'welcome'] # different types of elements  
  
# printing details  
print("Initialized List:", list_1) # printing elements of the list  
print("Data Type:", type(list_1)) # printing data type  

print()

# simple python program to show how to initialize a tuple  
  
# creating a tuple  
tuple_1 = (1, 0.5, 'hello', 1+5j, 1.7e2, -12, 'welcome') # different types of elements  
  
# printing details  
print("Initialized tuple:", tuple_1) # printing elements of the tuple  
print("Data Type:", type(tuple_1)) # printing data type  
print()

# simple python program to show how to initialize string  
  
# initializing variables with some string  
str_1 = 'TpointTech'  
str_2 = 'I love learning Python from TpointTech'  
  
# printing details  
print("String 1 :", str_1) # printing string  
print("Data Type of String 1:", type(str_1)) # printing data type  
  
print("String 2 :", str_2) # printing string  
print("Data Type of String 2:", type(str_2)) # printing data type  
print()

# simple python program to show how to initialize a range  
  
# creating a range  
r = range(3, 26, 2)  
  
# printing the results  
print("Range:", r) # printing range  
print("Range as List:", list(r)) # printing range as a list  
print("Data Type:", type(r)) # printing data type 
print()

# simple python program to show how to initialize a set  
  
# creating sets  
set_1 = {"mango", "apple", "orange", "banana"} # using {}  
set_2 = set(["ginger", "lemon", "potato", "tomato"])  
  
# printing the results  
print("Set 1:", set_1) # set 1  
print("Data type of Set 1:", type(set_1)) # data type of set 1  
  
print("Set 2:", set_2) # set 2  
print("Data type of Set 2:", type(set_2)) # data type of set 2  
print()

# simple python program to show how to create a frozeset  
  
# creating an iterable  
list_1 = ["berries", "orange", "mango", "apple"]      # a list  
  
# using the frozenset() function to create a frozenset object  
f_1 = frozenset(list_1)  
  
# printing results  
print("Frozenset:", f_1) # frozenset  
print("Data Type:", type(f_1)) # data type  
print()

  
# creating a dictionary  
person_1 = {  
    'name' : 'Mark',  
    'age': '25',  
    'gender' : 'Male',  
}  
  
# printing results  
print("Person Details:\n", person_1)  # dictionary  
print("Data Type:", type(person_1))   # its data type  
print()


# read about 
# Numbers
# Type casting
# string
# string Methods
# boolean
# small check but as per we thought if we use input it has the data type string only it not change if i give number
#val = input("Enter letter or number")
#print(type(val))
#val = input("Enter letter or number")
#print(type(val))
# # # # # # # # # ### # # # # # # # # # # # # # # # # # # # ### # # # # # # # # # ## # # # # # # # # ### # # # # # # # # # #
# now we move to the selection statements 
# first is if else 
# val = input("Enter a password :")
#if len(val) >= 8:  # checking the length of the password
#  # outer if block
#  if any(char.isdigit() for char in val): # checking if the password consists of any numeral value
#    # inner if block
#    print("Password is Strong")
#  else:
#    print("password is contain one number")
#else:
#  print("Password is must in above 8 character(s)")


##for loop
#a = range(1,10,2)
#print(list(a))

##for loop
# we can iterate them
#for i in range(1,10,2):
#  print(i)
#for j in range(1,10,2):
#  print(j)

#list - mutable, and it changes the values for the object
lists = [2,3,46,87,89]
print(lists[3])

#set -  immutable, and it doesn't change the value for the object it creates a new object for every variable assign or reassign show error or add can't be done.
example_set = {"object","values","object","new word","another object"}
print(example_set)

#tuple - immutable, and it can't change values once initialized or declared it can't change like immutable list with parenthesis
example_tuple = (23,) # if we give a single value as a tuple we can give the trailing comma's to know the memory it is an tuple without comma's it is a int data type
print(example_tuple)
print(type(example_tuple))

example_tuple = (23,12,45,654.65,87)
print(example_tuple)
print(type(example_tuple))


#dictionary - it is a collection of key-value pair , each key is associated with value and it has the number, string, list, tuple or another dictionary
#dict[key] - syntax
person = {
  'name' : 'Mark',
  'age': '25',
  'gender' : 'Male',
  'favourite_color': ['blue','white'],
  'status':'active'
}
print(person)
print(type(person))
print(person['name'])
print(person['age'])
print(person['favourite_color'])
person['gender'] = 'Female'
print(person['gender'])
persons_list = person.items()
print(persons_list)

for key,values in persons_list:
  print('My {} is {}'.format(key,values))

