"""
Input: [1234, 567, 89, 10]
output: [10, 18, 17, 1] (2 methods) 
"""

#Method_1
def sum_of_digits_while(num):
    num = abs(num)
    total = 0
    while num > 0:
        digit = num % 10  
        total += digit
        num //= 10        
    return total


arr = [1234, 567, 89, 10]
result = []
print("Input",arr)
for n in arr:
    result.append(sum_of_digits_while(n))

print("Output:", result)


# Method 2:
def sum_digits_prealloc(numbers):
    results = [0] * len(numbers)
    for i in range(len(numbers)):
        n = abs(numbers[i])
        while n:
            results[i] += n % 10
            n //= 10
    return results

nums = [1234, 567, 89, 10]
print("Input:", nums)
print("Output:", sum_digits_prealloc(nums)) 