# Magic number in python


#for loop version


###Version_1 avoid negative numbers

# n = int(input('Enter a number: '))
# original = n
# n = abs(n)
# while n >= 10:
#   total = 0
#   while n > 0:
#     total += n % 10
#     n //= 10
#   n = total

# if(n == 1):
#   print(f"{original} is a Magic Number")
# else:
#   print(f"{original} is NOT a Magic Number")


##Version_2 is negative numbers are considered as a normal numbers

"""
num_input = input('Enter a number: ')
num = int(num_input)

i = 0
total = 0

if num_input[0] == "-":
    total = -int(num_input[1])  
    i = 2 
else:
    total = int(num_input[0])  
    i = 1

while i < len(num_input):
    total += int(num_input[i])
    i += 1

n = total

temp = 0
while n >= 10:
    temp += n % 10
    n //= 10
n = temp

print(n)
if n == 1:
    print(f"{num_input} is a Magic Number")
else:
    print(f"{num_input} is NOT a Magic Number")

"""


## Armstrong number


num = int(input("Enter a number: "))
if num < 0:
    print("Armstrong numbers are non-negative.")
    exit()

digits = str(num)
power = len(digits)

total = 0
for d in digits:
    total += int(d) ** power

if total == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")
