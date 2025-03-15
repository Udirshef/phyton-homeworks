def check_same_length():
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")
    
    if len(string1) == len(string2):
        print("The strings have the same length.")
    else:
        print("The strings have different lengths.")
        
check_same_length()
