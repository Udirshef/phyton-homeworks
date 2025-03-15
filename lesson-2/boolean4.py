def check_numbers_different():
    number1=int(input('Enter first number: '))
    number2=int(input('Enter second number: '))
    number3=int(input('Enter third number'))
    if number1!=number2 and number2!=number3 and number1!=number3:
        print('All numbers are different')
    else:
        print('Numbers are not different')
check_numbers_different()