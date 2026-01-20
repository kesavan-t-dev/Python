"""
Write a function that accepts a string with some “#” in it. Move all the hashes to the front of the string and return the modified string.

Input: Move#Hash#to#Front

Output: ###MoveHashtoFront
"""

def move_hash(s):
    arr = list(s)  
    n = len(arr)

    for i in range(n):
        j = i
        while j > 0 and arr[j] == '#':
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    return ''.join(arr)  

text = "he#l#lllo#"
print("Before:", text)
print("After: ", move_hash(text))