## __ Write a function to print a list of prime numbers for a given input range (2 methods)
#method_1
# def prime_num(number):
#     # assert number > 1 , "value must be greater than 1 "
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

# prime_num(number)


##Method_2
def primes_up_to_n(n, current=2, primes=0):
    if primes == 0:
        primes = []

    if current > n:
        return primes

    def is_prime(num, divisor=2):
        if num < 2:
            return False
        if divisor * divisor > num:
            return True
        if num % divisor == 0:
            return False
        return is_prime(num, divisor + 1)

    if is_prime(current):
        primes.append(current)

    return primes_up_to_n(n, current + 1, primes)

limit = int(input("Enter a positive integer (n): "))
if limit < 2:
    print("No prime numbers exist below 2.")
else:
    print(f"Prime numbers: {primes_up_to_n(limit)}")
