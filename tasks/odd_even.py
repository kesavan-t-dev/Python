#-----ODD & EVEN

#____Method__1

values = int(input("Enter the values :"))

def odd_even(n):
    n = n
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

#____Method__2

def separate_even_odd(nums):
    
    if not nums:
        return [], []
    
    evens, odds = separate_even_odd(nums[1:])
    
    if nums[0] % 2 == 0:
        evens.insert(0, nums[0])
    else:
        odds.insert(0, nums[0])
    
    return evens, odds

numbers = [5, 8, 13, 22, 7]
even_list, odd_list = separate_even_odd(numbers)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)

