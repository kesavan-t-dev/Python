"""
Construct a one user defined function similar to inbuild range function (2 methods)
"""

#Method_1
# def my_range(start, stop=None, step=1):

#     if stop is None:  
#         stop = start
#         start = 0
#     result = []
#     current = start

#     if step > 0:
#         while current < stop:
#             result.append(current)
#             current += step

#     else:
#         while current > stop:
#             result.append(current)
#             current += step

#     if result == []:
#           raise ValueError("Error Executing code") 
#     return result
# try:
#     print(my_range(12,1,-1))

# except Exception as e:
#     print(e)

#Method_2 use recursion 
def my_range(start, stop=None, step=1):

    if stop is None:
        stop = start
        start = 0
    
    if (step > 0 and start >= stop) or (step < 0 and start <= stop):
        return []

    return [start] + my_range(start + step, stop, step)

try:
    print(my_range(12,1,-1))

except Exception as e:
    print(e)