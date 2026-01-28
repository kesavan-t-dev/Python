"""
Given a string with multiple characters that are repeated consecutively, reduce the size of the string using mathematical logic. Replace consecutive repeated characters with the character followed by the count of repetitions.

Input: aabbbbeeeeffggg

Output: a2b4e4f2g3 
(3 methods ) without using inbuilt functions 
"""





# #Method_1 
# def compress_string(s):
#     chars, counts = [], []
#     n = len(chars)
#     for ch in s:
#         idx = -1
#         for i in range(n):
#             if chars[i] == ch: 
#                 idx = i; 
#                 break
#         if idx != -1:
#             counts[idx] += 1
#         else:
#             chars.append(ch)
#             counts.append(1)
#     return "".join(chars[i] + str(counts[i]) for i in range(n))

# n = input("enter a word:") #aabbbbeeeeffaggg
# n = "aabbbbeeeeffaggg"
# print(compress_string(n)) #output : a3b2c1132231

# def compress_string(s):
#     freq = {}
#     order = []

#     for ch in s:
#         if ch not in freq:
#             freq[ch] = 0
#             order.append(ch)
#         freq[ch] += 1

#     result = ""
#     for ch in order:
#         result += ch + str(freq[ch])
#     return result

# n = input("enter a word:") #aabbbbeeeeffaggg
# n = "aabbbbeeeeffaggg"
# print(compress_string(n)) 


#Method_3 ascii
# def compress_string(s):
#     freq = [0] * 256  
#     order = []        

#     for ch in s:
#         ascii_val = ord(ch)
#         if freq[ascii_val] == 0:
#             order.append(ch)
#         freq[ascii_val] += 1

#     result = ""
#     for ch in order:
#         result += ch + str(freq[ord(ch)])
#     return result

# n = input("enter a word:") #aabbbbeeeeffaggg
# n = input("Enter:")  # aabbbbeeeeffaggg
# print(compress_string(n))  # Output: a3b5e4f2g3
