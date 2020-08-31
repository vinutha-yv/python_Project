'''
To find maximum of three numbers
a, b, c are three numbers

'''


def max_num(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        return num1
    elif (num2 > num1) and (num2 > num3):
        return num2
    else:
        return num3

for i in range(1):
    print(f"running for the {i + 1}th time")
    a = float(input("Enter first number : "))
    b = float(input("Enter second number : "))
    c = float(input("Enter third number : "))
    max = max_num(a, b, c)
    print(f"Maximum of three numbers is {max}")
    print("\n")