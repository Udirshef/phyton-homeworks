def invest(amount,rate,years) :
    for year in range(1,years+1):
        amount*=1+rate
        print(f"year{year}: ${amount:.2f}")

amount=float(input("Enter a initial number: "))
rate=float(input("Enter annual rate of return: "))
years=int(input("Enter the number of years: "))
invest(amount,rate,years)

    