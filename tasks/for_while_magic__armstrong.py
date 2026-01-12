# Magic number in python

###Version_1 avoid negative numbers

n = input('Enter a number: ')
num = str(abs(int(n)))
# Convert to absolute integer to handle negatives
n = int(num)

while n >= 10:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    n = total

if n == 1:
    print(f"{n} is a Magic Number")
else:
    print(f"{n} is NOT a Magic Number")

##Version_2 is negative numbers are considered as a normal numbers





