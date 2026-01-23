"""
Given a string with multiple characters that are repeated consecutively, reduce the size of the string using mathematical logic. Replace consecutive repeated characters with the character followed by the count of repetitions.

Input: aabbbbeeeeffggg

Output: a2b4e4f2g3 
(3 methods ) without using inbuilt functions 
"""

#Method_1 count and reset count 
# def compress_string(s):
#     if not s:
#         return ""

#     chars, counts = [], []
#     count = 1

#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             if s[i - 1] in chars:
#                 counts[chars.index(s[i - 1])] += count
#             else:
#                 chars.append(s[i - 1])
#                 counts.append(count)
#             count = 1

#     if s[-1] in chars:
#         counts[chars.index(s[-1])] += count
#     else:
#         chars.append(s[-1])
#         counts.append(count)

#     return "".join(chars[i] + str(counts[i]) for i in range(len(chars)))

# input = input("Enter:")
# print(compress_string(input)) #output : a3b2c1132231


#Method_2 
def compress_string(s):
    if not s: return ""
    chars, counts = [], []
    n = len(chars)
    for ch in s:
        idx = -1
        for i in range(n):
            if chars[i] == ch: idx = i; break
        if idx != -1:
            counts[idx] += 1
        else:
            chars.append(ch)
            counts.append(1)
    return "".join(chars[i] + str(counts[i]) for i in range(n))

n = input("enter a word:")
print(compress_string(n)) #output : a3b2c1132231

#Method_3
# def compress_stack(s):
#     stack = [] 
#     for ch in s:
#         found = False
#         for item in stack:
#             if item[0] == ch:
#                 item[1] += 1
#                 found = True
#                 break
#         if not found:
#             stack.append([ch, 1])  

#     result = "".join(ch + str(cnt) for ch, cnt in stack)
#     return result
# n = input("enter a word:")
# print(compress_stack(n))  
