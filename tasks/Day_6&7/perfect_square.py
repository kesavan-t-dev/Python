"""
Given a positive integer num, write a function that returns True if num is a perfect square else False. (2 methods)
"""

#Method_1
# def perfect_square(num):

#     if num < 1:
#         return False

#     left, right = 1, num
#     while left <= right:
#         mid = (left + right) // 2
#         square = mid * mid

#         if square == num:
#             return True
#         elif square < num:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return False

# n = int(input("Enter a number:"))
# print(perfect_square(n))

#Method_2
# def perfect_square(num):

#     if num < 1:
#         return False

#     odd = 1
#     while num > 0:
#         num -= odd
#         odd += 2

#     return num == 0

# n = int(input("Enter a number:"))
# print(perfect_square(n))