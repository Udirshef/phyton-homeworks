def check_username_password():
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    if username and password:
        print('Both are not empty')
    else:
        print('Either username or password is empty')
check_username_password()

        