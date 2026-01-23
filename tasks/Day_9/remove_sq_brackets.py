"""
Input: [2,4,[3,5,[1,[9]]],0]

Output: [2,4,3,5,1,9,0] 
"""
#Method_1
def lists_remove(nested):
      stack = nested[::-1] 
      result = []

      while stack:
        item = stack.pop()  
        if type(item) is list:  
            stack.extend(item[::-1])  
        else:
            result.append(item)
      return result

data = [2, 4, [3, 5, [1, [9]]], 0]
print(lists_remove(data))  # Output: [2, 4, 3, 5, 1, 9, 0]
