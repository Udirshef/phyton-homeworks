string=input("Enter a string; ")
if string==string[::-1]:
    print("This string is a palindrome.")
else:
    print("This string is not a palindrome.")
    print(string)