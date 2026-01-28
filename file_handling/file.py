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


#check file is existed or not
#version using exists
if os.path.exists("customers_usa.csv"):
   print("File exists.")
else:
   print("File does not exist.")

#version two using isfile method
file_path = "data/customers_usa.csv"
if os.path.isfile(file_path):
   print(f"{file_path} exists and is a file.")
else:
   print(f"{file_path} does not exist or is not a file.")

## version three using try except using file not found error    
try:
   with open("data/customers_usa.txt", "r") as f:
       print("File opened successfully.")
except FileNotFoundError:
   print("File does not exist.")