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