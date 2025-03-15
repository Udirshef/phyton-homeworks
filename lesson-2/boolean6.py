def check_number_divisiblity():
    number=int(input('Enter a number: '))
    if number %5==0 and number%3==0:
        print('Number is divisible by both 3 and 5')
    else:
        print('Number is not divisible by both 3 and 5')
check_number_divisiblity()