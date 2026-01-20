##_____Write a function to print a factorial numbers for a given input range (2 methods )
#Method_1
# def fact(n):
#     assert n >= 0 , "Enter a positive numbers"
#     org = n
#     i = n - 1
#     for i in range(n,1,-1):
#         i -= 1
#         if(i == 0):
#             break
#         else:
#             n *= i
           
#     print(f"{n} is a factorial of {org}")
    

# n = int(input("Enter a number: "))

# fact(n)

#Method_2

def factorial(X):
    ans = 1

    for i in range(1, X + 1):
        ans *= i

    return ans

X =  int(input("Enter a number: "))
assert X >= 0 , "Enter a positive numbers"
result =  factorial(X)

print("{}is a factorial of {} ".format(result, X))