"""
Write a program about remove the mid of element in given array. (2 methods) 

"""
#Method_1 index based shift next value to the mid index 
def remove_middle(arr):
    n = len(arr)
    if n == 0:
        return arr

    mid_index = n // 2  
    new_arr = [0] * (n - 1)  

    j = 0
    for i in range(n):
        if i != mid_index:
            new_arr[j] = arr[i]
            j += 1
    return new_arr



a = []
b = int(input("Enter a range: "))
for i in range(b):
    val = input(f"Enter value: ")
    a.append(val)

result = remove_middle(a)
print(result)

#Method_2
# def remove_middle(arr):
#     n = len(arr)
#     if n == 0:
#         return arr

#     mid_index = n // 2
#     new_arr = [0] * (n - 1)

#     for i in range(mid_index):
#         new_arr[i] = arr[i]  

#     for i in range(mid_index + 1, n):
#         new_arr[i - 1] = arr[i]  
#     return new_arr


# a = []
# b = int(input("Enter a range: "))
# for i in range(b):
#     val = input(f"Enter value: ")
#     a.append(val)

# result = remove_middle(a)
# print(result)