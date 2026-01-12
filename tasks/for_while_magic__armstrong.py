# Magic number in python


#for loop version


###Version_1 avoid negative numbers

# n = int(input('Enter a number: '))
# n = abs(n)
# while n >= 10:
#   total = 0
#   while n > 0:
#     total += n % 10
#     n //= 10
#   n = total

# if(n == 1):
#   print(f"{n} is a Magic Number")
# else:
#   print(f"{n} is NOT a Magic Number")


##Version_2 is negative numbers are considered as a normal numbers


n = int(input("Enter a number: "))
n = abs(n)
original = n  
while n > 9:
    n = n // 10 
    n = n % 10  

if n == 1:
    print(f"{original} is a Magic Number")
else:
    print(f"{original} is NOT a Magic Number")


## Armstrong number

