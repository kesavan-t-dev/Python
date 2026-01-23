"""
Bubble sort (ascending order) ( 2 methods )
"""

#Method_1 
def bubble_sort(array):
  for i in range(len(array)):
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = [-2, 45, 0, 11, -9]

bubble_sort(data)

print('Sorted Array in Ascending Order:')
print(data)



#Method_2 
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if not swapped:
#             break  

# arr = [64, 14, 25, 12, 22, 11, 90]
# bubble_Sort(arr)
#print('Sorted Array in Ascending Order:')
# print(arr)