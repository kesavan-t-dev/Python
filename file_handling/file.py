import os

# current dir
b = os.getcwd()
print(b)
#change dir
a = os.chdir('D:/Training/Tasks/Python/file_handling')
print(a)
#check current dir changed or not
b = os.getcwd()
print(b)
# make dir
# a = os.makedirs('./tests.txt')
# print(a)

# create a empty text file
# create file using x - execute
# in current directory
# fp = open('sales.txt', 'x')
# fp.close()

# file = open('samples.txt','x')
# file.write("first words")
# file = open('samples.txt','w')
# file.writelines("check this is works or not ")


# #remove the file 
# os.remove('D:/Training/Tasks/Python/file_handling/samples.txt')
