"""
Write a code to get the count of vowels in given string (2 methods) no inbuilt functions method_1 for loop method_2 switch case 
"""

#Method_1
# def count_vowels(text):
#     vowels = "aeiouAEIOU"  
#     count = 0
#     for ch in text:
#         # try:
#         #     int(ch)
#         #     print(f"Number in string: {ch}")
#         #     continue  
#         # except ValueError:
#             if ch in vowels:
#                 count += 1
#     return count
    
# user_input = input("Enter a string: ")
# print("Vowel count:", count_vowels(user_input))

#Method_2 using case
def count_vowels(text):
    count = 0
    for ch in text:
        # try:
        #     int(ch)
        #     print(f"Number found in string: {ch}")
        #     continue  
        # except ValueError:
            match ch:
                case 'a':
                    count += 1
                case 'A':
                    count += 1
                case 'e':
                    count += 1
                case 'E':
                    count += 1
                case 'i':
                    count += 1
                case 'I':
                    count += 1
                case 'o':
                    count += 1
                case 'O':
                    count += 1
                case 'u':
                    count += 1
                case 'U':
                    count += 1
                case _:
                    pass
    return count

user_input = input("Enter a string: ")
print("Vowel count:", count_vowels(user_input))