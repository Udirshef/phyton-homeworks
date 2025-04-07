password=input('Enter a password:' )

if len(password)<8:
    print('Pease, enter 8 character at least')
elif not any(char.isupper() for char in password):
    print('password should contain one uppercase letter')
else :
    print('pasword is strong')