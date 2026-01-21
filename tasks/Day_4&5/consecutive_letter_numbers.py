"""
Given a string with multiple characters that are repeated consecutively, reduce the size of the string using mathematical logic. Replace consecutive repeated characters with the character followed by the count of repetitions.

Input: aabbbbeeeeffggg

Output: a2b4e4f2g3 
(3 methods ) 
"""

#Method_1 
def compress_string_basic(s):
    print(s)
    result = ""
    count = 1

    for i in range(1, len(s)):
        print(i)    
        if s[i] == s[i - 1]:
            count += 1
            # a = s[i]
            # b = s[i-1]
            # print(a , "s[i]")
            # print(count, "count")
            # print(b , "s[i-1]")
        else:
            result += s[i - 1] + str(count)
            # print("result :",result)
            count = 1
    result += s[-1] + str(count)
    # print("result :",result)
    return result

# input = "aabbbbeeeeffggg"
input = "aabb"
print(compress_string_basic(input))
