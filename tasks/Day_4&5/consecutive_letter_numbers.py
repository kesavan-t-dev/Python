"""
Given a string with multiple characters that are repeated consecutively, reduce the size of the string using mathematical logic. Replace consecutive repeated characters with the character followed by the count of repetitions.

Input: aabbbbeeeeffggg

Output: a2b4e4f2g3 
(3 methods ) without using inbuilt functions 
"""

#Method_1 count and reset count 
# def compress_string(s):
#     # print(s)
#     result = ""
#     count = 1

#     for i in range(1, len(s)):
#         # print(i)    
#         if s[i] == s[i - 1]:
#             count += 1
#             # a = s[i]
#             # b = s[i-1]
#             # print(a , "s[i]")
#             # print(count, "count")
#             # print(b , "s[i-1]")
#         else:
#             result += s[i - 1] + str(count)
#             # print("result :",result)
#             count = 1
#     result += s[-1] + str(count)
#     # print("result :",result)
#     return result

# # input = "aabbca1123123" #it will not show correct output change the logic for this sligh correct but keep the structurelike check the i -1 u can use annother for loop give with correct changes
# print(compress_string(input)) #output : a3b2c1132231


#Method_2 
# def compress_two(s):
#     start = 0
#     result = ""
#     while start < len(s):
#         end = start
#         while end < len(s) and s[end] == s[start]:
#             end += 1
#         result += s[start] + str(end - start)
#         start = end
#     return result
# n = input("enter a word:")
# print(compress_two(n))  


#Method_3
# def compress_stack(s):
#     stack = []
#     for ch in s:
#         if stack and stack[-1][0] == ch:
#             stack[-1][1] += 1
#             # print( stack[-1][1])
#         else:
#             stack.append([ch, 1])
#             # print(stack)
#     result = ""
#     for ch, cnt in stack:
#         result += ch + str(cnt)
#         # print(result)      

#     # print(result)    
#     return result

# n = input("enter a word:")
# print(compress_stack(n))  # a2b4e4f2g3
