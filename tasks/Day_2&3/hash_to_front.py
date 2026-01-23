"""
Write a function that accepts a string with some “#” in it. Move all the hashes to the front of the string and return the modified string. (4 methods )

Input: Move#Hash#to#Front

Output: ###MoveHashtoFront
"""

#____________________________________________________________________________________________
#Method_1 using insertion sort
# def move_hash(s):
#     arr = list(s)  
#     n = len(arr)
#     print(n)
#     for i in range(n):
#         j = i
#         while j > 0 and arr[j] == '#':
#             a = arr[j], arr[j - 1] = arr[j - 1], arr[j]
#             # print(a)
#             j -= 1
#         # print(i, j, arr)
#     return ''.join(arr)  

# text = "Move#Hash#to#Front"
# # text = input("Enter a string/Number with hashstags:")

# print("Before:", text)
# print("After: ", move_hash(text))

#____________________________________________________________________________________________
# #Method_2 using new list to store and append that string
# def move_hash(s):
#     result = ""
#     hash_count = 0
    
#     for ch in s:
#         if ch == '#':
#             hash_count += 1   
#     result = '#' *hash_count
    
#     for ch in s:
#         if ch != '#':
#             result += ch
#     # print(result)
#     return result

# text = "Move#Hash#to#Front"
# # text = input("Enter a string/Number with hashstags:")

# print("Before:", text)
# print("After: ", move_hash(text))
#____________________________________________________________________________________________
# #Method_3 using slicing from left to right store them 
# def move_hash(s):
#     n = len(s)
#     result = [""] * n 
#     left = 0          
#     right = n - 1     

#     for ch in s:
#         if ch == '#':
#             result[left] = '#'
#             left += 1
#         else:
#             result[right] = ch
#             right -= 1

#     hash_part = result[:left]
#     non_hash_part = result[left:][::-1]
#     return "".join(hash_part + non_hash_part)

# text = "Move#Hash#to#Front"
# # text = input("Enter a string/Number with hashstags:")

# print("Before:", text)
# print("After: ", move_hash(text))
#________________________________________________________________________________________________________
#Method_4
def move_hash(s):
    n = len(s)
    result = [""] * n
    left = 0           
    right = left + s.count('#')  

    for ch in s:
        if ch == '#':
            result[left] = '#'
            left += 1
        else:
            result[right] = ch
            right += 1

    return "".join(result)

text = "Move#Hash#to#Front"
# text = input("Enter a string/Number with hashstags:")

print("Before:", text)
print("After: ", move_hash(text))
