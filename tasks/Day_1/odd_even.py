#-----ODD & EVEN

#____Method__1

values = int(input("Enter the range :"))

def odd_even(n):
    odd = [] 
    even = [] 
    a = 0
    b = 0
    if n < 0:
        a = n
        b = 0
    else:
        a = 0
        b = n
    for i in range(a,b):
        if(i % 2 ==0):
            odd.append(i)
        else:
            even.append(i)
    return odd, even


odd,even = odd_even(values)
print("Odd numbers are :", odd)
print("Even numbers are :", even)


#____Method__2

def separate_even_odd(n):
    a = 0
    b = 0
    if n < 0:
        a = n
        b = 0
    else:
        a = 0
        b = n
    
    numbers = list(range(a, b))
    even = [num for num in numbers if num % 2 == 0]
    odd = [num for num in numbers if num % 2 != 0]
    return odd, even

numbers = int(input("Enter the range :"))
even_list, odd_list = separate_even_odd(numbers)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)

