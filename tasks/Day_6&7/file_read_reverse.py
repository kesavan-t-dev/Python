"""
File read operations (Read one file - print the file content in reverse order) (2 methods)

(in file)
Input:- Hi file handling in reverse 

Output: iH elif gnildnah ni esrever
"""
#get current directory 

"""
import os

a = os.getcwd()
print(a)
"""

# create multiple directory in single cmd using 
# """
# import os
# root_dir = 'D:\Training\Tasks\Python\tasks'
# list_ = ['Folder_1', 'Folder_x', 'Folder_y']
# for folder in list_:
#     os.makedirs(root_dir + folder)
# """

# Method 1: Using Stack
# def reverse_words_stack(content):
#     result = ""
#     stack = []

#     for ch in content:
#         if ch != " " and ch != "\n":
#             stack.append(ch)  
#         else:
#             while stack:  
#                 result += stack.pop()
#             result += ch  

#     while stack:
#         result += stack.pop()

#     print(result)    
    


# try:
#     filename = "D:/Training/Tasks/Python/tasks/Day_6&7/input.txt"
#     content = open(filename, "r")
#     context = content.read()
#     reverse_words_stack(context)

# except Exception as e :
#     print("Error :", e)
# else:
#     content.close()

# # Method 2: Manual reverse without stack
def reverse_words(content):
        result = ""
        word = ""

        for ch in content:
            if ch != " " and ch != "\n":
                word += ch
            else:
                
                for i in range(len(word) - 1, -1, -1):
                    result += word[i]
                result += ch
                word = ""

        for i in range(len(word) - 1, -1, -1):
            result += word[i]

        print(result)

try:
    filename = "D:/Training/Tasks/Python/tasks/Day_6&7/input.txtx"
    content = open(filename, "r")
    context = content.read()
    reverse_words(context)

except Exception as e :
    print(e)
else:
    content.close()
