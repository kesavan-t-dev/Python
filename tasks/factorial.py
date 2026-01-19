##_____Write a function to print a factorial numbers for a given input range (2 methods )
#Method_1
# def factorial(n):
#     i = n - 1
#     org = n
#     while i > 0:
#         n = n * i
#         i -=  1
#     print(f"{n} is a factorial of {org}")
    

# n = int(input("Enter a number: "))
# factorial(n)

# #Method_2
def fact(n):
    org = n
    i = n - 1
    for i in range(n,0,-1):
        i -= 1
        if(i == 0):
            break
        else:
            n *= i
           
    print(f"{n} is a factorial of {org}")
    

n = int(input("Enter a number: "))
fact(n)

