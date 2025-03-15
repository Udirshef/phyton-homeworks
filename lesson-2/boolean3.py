def check_number_even_positive():
    number=int(input('Enter a number: '))
    if  number>0 and number%2==0:
        print('Number is even and positive')
    else:
        print('Number is odd and positive')
check_number_even_positive()