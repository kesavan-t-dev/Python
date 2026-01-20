## __ Write a function to print a list of prime numbers for a given input range (2 methods)
#method_1
def p_num(number):
    assert number > 1 , "value must be greater than 1 "
    primes = []
    num = 2  
    while num <= number:
        i = 2

        is_prime = True
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            primes.append(num)
        num += 1
    print(primes)
  
number = int(input("Enter a number :"))

p_num(number)
