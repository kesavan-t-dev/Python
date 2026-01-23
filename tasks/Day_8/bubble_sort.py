"""
Bubble sort (ascending order) ( 2 methods )
"""

#Method_1 
# def bubble_sort(lst):
#   size = len(lst)
#   for i in range(size):
#     for j in range(size - 1):
#       if lst[j] > lst[j + 1]:
#         lst[j], lst[j + 1] = lst[j + 1], lst[j]

#   return lst


# data = [-2, 45, 0, 11, -9]
# print("Unsorted Array:",data)
# bubble_sort(data)

# print('Sorted Array in Ascending Order:')
# print(data)



#Method_2 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  

arr = [64, 14, 25, 12, 22, 11, 90]
print("Unsorted array",arr)
bubble_sort(arr)
print('Sorted Array in Ascending Order:')
print(arr)