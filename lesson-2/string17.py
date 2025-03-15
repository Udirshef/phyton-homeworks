# Program to replace vowels with a symbol
user_string = input("Enter a string: ")
symbol = "*"

vowels = "aeiouAEIOU"
modified_string = ''.join(symbol if char in vowels else char for char in user_string)
print(f"Modified string: {modified_string}")
