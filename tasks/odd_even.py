#-----ODD & EVEN

#____Method__1
"""
values = int(input("Enter the range :"))

def odd_even(n):
    n = abs(n)
    odd = [] 
    even = [] 
    for i in range(1,n+1):
        if(i % 2 ==0):
            odd.append(i)
        else:
            even.append(i)
    return odd, even


odd,even = odd_even(values)
print("Odd numbers are :", odd)
print("Even numbers are :", even)
"""

#____Method__2

def separate_even_odd(n):
    if n < 0:
        print("give positive range")
        exit()

    numbers = list(range(1, n + 1))
    even = [num for num in numbers if num % 2 == 0]
    odd = [num for num in numbers if num % 2 != 0]
    return odd, even

numbers = int(input("Enter the range :"))
even_list, odd_list = separate_even_odd(numbers)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)

