"""
Write a function that accepts a string with some “#” in it. Move all the hashes to the front of the string and return the modified string.

Input: Move#Hash#to#Front

Output: ###MoveHashtoFront
"""

#Method_1 using bubble sort little bit slow based on the input it takes more time TC - O(N^2)&SC - O(N) 
class BubbleSort:
    def move_hashes_to_front(self, s):
        chars = list(s)
        n = len(chars)

        for i in range(n):
            for j in range(n - 1, i, -1):
                if chars[j] == '#' and chars[j - 1] != '#':
                    chars[j], chars[j - 1] = chars[j - 1], chars[j]
        return "".join(chars)


sorter = BubbleSort()

input_str = "Move#Hash#to#Front"
# input_str = input("enter a string with hashstags")
print("\nBefore : ",input_str)
result = sorter.move_hashes_to_front(input_str)
print("After : ",result)


