## __ Write a function to print a list of prime numbers for a given input range (2 methods)
#method_1
# def p_num(number):
#     assert number > 1 , "value must be greater than 1 "
#     primes = []
#     num = 2  
#     while num <= number:
#         i = 2

#         is_prime = True
#         while i * i <= num:
#             if num % i == 0:
#                 is_prime = False
#                 break
#             i += 1
#         if is_prime:
#             primes.append(num)
#         num += 1
#     print(primes)
  
# number = int(input("Enter a number :"))

# p_num(number)


##Method_2
def primes_up_to_n(n, current=2, primes=0, divisor=2):

    if primes == 0:
        primes = []

    if current > n:
        return primes

    
    if divisor * divisor > current:  
        primes.append(current)
        return primes_up_to_n(n, current + 1, primes, 2)

    if current % divisor == 0:  
        return primes_up_to_n(n, current + 1, primes, 2)

    return primes_up_to_n(n, current, primes, divisor + 1)

try:
    limit = int(input("Enter a positive integer (n): "))
    if limit < 2:
        print("No prime numbers exist below 2.")
    else:
        print(f"Prime numbers: {primes_up_to_n(limit)}")
except ValueError:
    print("Invalid input. Please enter an integer.")
