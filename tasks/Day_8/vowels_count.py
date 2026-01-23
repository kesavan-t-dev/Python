"""
Write a code to get the count of vowels in given string (2 methods) no inbuilt functions method_1 for loop method_2 switch case 
"""

#Method_1
def count_vowels_for_loop(text):
    vowels = "aeiouAEIOU"  
    count = 0
    for ch in text:
        # try:
        #     int(ch)
        #     print(f"Number in string: {ch}")
        #     continue  
        # except ValueError:
            if ch in vowels:
                count += 1
    return count
    

user_input = input("Enter a string: ")
print("Vowel count:", count_vowels_for_loop(user_input))