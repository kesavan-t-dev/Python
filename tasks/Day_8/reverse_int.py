"""
Reverse integer value (3 methods)
"""
#Method_1 swap value to first and next value swap and current untill 0 
def reverse_integer(n):
    lists = list(str(n))
    length = len(lists)


    for i in range(length):
        j = i
        while j > 0:  
            lists[j],lists[j-1] = lists[j-1],lists[j]
            j-=1

    reversed_number = int("".join(lists)) 
    return reversed_number

n = int(input("Enter a Digit:"))
print("Before reverse :",n,"\n After Reverse: ",reverse_integer(n))

#Method_2 use two pointer to swap last and first 
def reverse_integer(n):
    lists = list(str(n))
    left, right = 0, len(lists) - 1

    while left < right:
        lists[left], lists[right] = lists[right], lists[left]
        left += 1
        right -= 1

    reversed_number = int("".join(lists))
    return reversed_number


n = int(input("Enter a Digit:"))
print("Before reverse:", n, "\nAfter Reverse:", reverse_integer(n))

#Method_3 use slice
def reverse_integer_recursive(n, left=None, right=None):
    if left is None and right is None:
        n = list(str(n))
        return int("".join(reverse_integer_recursive(n, 0, len(n) - 1)))

    if left >= right:
        return n

    n[left], n[right] = n[right], n[left]

    return reverse_integer_recursive(n, left + 1, right - 1)



num = int(input("Enter a Digit: "))
print("Before reverse:", num, "\nAfter Reverse:", reverse_integer_recursive(num))