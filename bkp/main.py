from files.multiply import multiply
from files.add import process_numbers as add
from files.names import names

def main():
    print("Program started this is from main program.")
    
    # #FUNCTION 1 name standard break point: 
    # for name in ["hi", "hellow", "how"]:
    #     print(names(name))

    # Function breakpoint: multiply
    result = multiply(5, 6)
    print("Multiplication result:", result)

    # Cross-file call
    numbers = [1,2,4,5,6,7,8]
    total = add(numbers)
    print("Total sum:", total)

if __name__ == "__main__":
    main()
