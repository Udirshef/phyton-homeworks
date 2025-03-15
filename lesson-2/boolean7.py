def check_2numbers_sum():
    number1=float(input('Enter first number: '))
    number2=float(input('Enter second number: '))
    if number1+number2>50.8:
        print('Sum of numbers is greater than 50.8')
    else:
        print('Sum of numbers is less than 150.8')
        if 10<number1<20 or 10<number2<20:
            print('One of the numbers is between 10 and 20')
        else:
            print('Neither of the numbers is between 10 and 20')
check_2numbers_sum()