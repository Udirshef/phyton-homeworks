def convert_cel_to_far(C) :
    return  C * 9/5 + 32
def convert_far_to_cel(F) :
    return (F - 32) * 5/9
c=float(input("Enter a temperature in celcius: "))
f=convert_cel_to_far(c)
print(f"{c} C={round(f,2)} F ")

f=float(input("Enter a temperature in F: "))
c=convert_far_to_cel(f)
print(f"{f} F={round(c,2)} C")