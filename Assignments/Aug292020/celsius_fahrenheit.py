'''
Convert given temperature from Celsius to Fahreneit
and Fahrenheit to Celsius
a is a given number

'''

def celsiusTofahrenheit(C):
    fahrenheit = (C * 9/5) + 32
    return fahrenheit


def fahrenheitTocelsius(F):
    celsisus = (F - 32) * 5/9
    return celsisus


for i in range(1):
    print(f"running for the {i + 1}th time")
    a = float(input("Enter temperature in celsius : "))  
    b = float(input("Enter temperature in fahrenheit : "))  
    fahrenheit = celsiusTofahrenheit(a)
    print(f"Temperature from celsius to fahrenheit:{fahrenheit}")
    celsisus = fahrenheitTocelsius(b)
    print(f"Temperature from fahrenheit to celsius:{celsisus}")
    print("\n")
