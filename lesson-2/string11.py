string=input('Enter a string: ' )
digits=1234567890
if any(char.isdigit() for char in string):
    print('This string contains digits.')   
else:
    print('This string does not contain digits.')
    