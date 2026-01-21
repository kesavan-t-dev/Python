"""
Write a function that accepts a string with some “#” in it. Move all the hashes to the front of the string and return the modified string. (4 methods )

Input: Move#Hash#to#Front

Output: ###MoveHashtoFront
"""

#Method_1 using bubble sort little bit slow based on the input it takes more time TC - O(N^2)&SC - O(N) 
# class BubbleSort:
#     def move_hashes_to_front(self, s):
#         chars = list(s)
#         n = len(chars)

#         for i in range(n):
#             # print(i) 
#             for j in range(n - 1, i, -1):
#                 # print(j)
#                 if chars[j] == '#' and chars[j - 1] != '#':
#                     a = chars[j], chars[j - 1] = chars[j - 1], chars[j]
#                     # print(chars[j],chars[j - 1])
#                     # print(a)
#             # print(i,j,chars)                
#         return "".join(chars)


# sorter = BubbleSort()

# input_str = "Move#Hash#to#Front"
# # input_str = input("Enter a string/Number with hashstags:")
# print("\nBefore : ",input_str)
# result = sorter.move_hashes_to_front(input_str)
# print("After : ",result)

#____________________________________________________________________________________________
# #Method_2 using insertion sort
def move_hash(s):
    arr = list(s)  
    n = len(arr)

    for i in range(n):
        j = i
        while j > 0 and arr[j] == '#':
            a = arr[j], arr[j - 1] = arr[j - 1], arr[j]
            print(a)
            j -= 1
        print(i, j, arr)
    return ''.join(arr)  

text = "Move#Hash#to#Front"
# text = input("Enter a string/Number with hashstags:")

print("Before:", text)
print("After: ", move_hash(text))

# #Method_3 using new list to store and append that string
# def move_hash_append(s):
#     result = []
#     hash_count = 0
    
#     for ch in s:
#         if ch == '#':
#             hash_count += 1
    
#     for _ in range(hash_count):
#         result.append('#')
    
#     for ch in s:
#         if ch != '#':
#             result.append(ch)
    
#     return "".join(result)

# print("\nBefore: Move#Hash#to#Front ", "\nafter:",move_hash_append("Move#Hash#to#Front"))

# #Method_4 using slicing from left to right store them 
# def move_hash_reverse_fill(s):
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

# print("\nBefore: Move#Hash#to#Front ", "\nafter:",move_hash_reverse_fill("Move#Hash#to#Front"))