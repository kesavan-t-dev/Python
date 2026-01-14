#__________PALINDROME - Write a code for the given str is print palindrome or not
#---Method_1 

# def check_palind(word):
#     if len(word) <= 1:
#         print("Enter more than one letter")
#         exit()
#     original = word 
#     rev = word[::-1] 
#     return original == rev

# if check_palind(input("Enter a word: ")):
#     print(f"{word} is a Palindrome")
# else:
#     print(f"{word} Not Palindrome")

#----Method_2
def checks_palind(word):
    word = word.lower()  
    length = len(word)
    
    for i in range(length // 2):  
        if word[i] != word[length - i - 1]:
            print(f"{word} is not a palindrome.")
            return  
   
    print(f"{word} is a palindrome.")


word = input("Enter a word: ")
checks_palind(word)

    