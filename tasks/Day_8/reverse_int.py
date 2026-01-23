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
