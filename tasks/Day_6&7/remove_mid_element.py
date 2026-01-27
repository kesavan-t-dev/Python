"""
Write a program about remove the mid of element in given array. (2 methods) 

"""
#Method_1 
# def remove_middle(arr):
#     n = len(arr)
#     if n == 0:
#         return arr  

#     if n % 2 == 0:
#         mid1 = n // 2 - 1
#         mid2 = n // 2
#         new_arr = [arr[i] for i in range(n) if i != mid1 and i != mid2]
#     else:
#         mid = n // 2
#         new_arr = [arr[i] for i in range(n) if i != mid]

#     return new_arr

# a = []
# b = int(input("Enter a range: "))
# for i in range(b):
#     val = input(f"Enter value: ")
#     a.append(val)

# result = remove_middle(a)
# print(result)

#Method_2 index based 
def remove_middle(arr):
    if not arr:
        return []
    
    length = 0

    for _ in arr:
        length += 1


    if length % 2 == 1:
        mid1 = length // 2
        mid2 = mid1
    else:
        mid1 = length // 2 - 1
        mid2 = length // 2

    new_arr = []
    index = 0
    for item in arr:
        if not (mid1 <= index <= mid2):
            new_arr.append(item)
        index += 1

    return new_arr

a = []
b = int(input("Enter a range: "))
for i in range(b):
    val = input(f"Enter value: ")
    a.append(val)

result = remove_middle(a)
print(result)