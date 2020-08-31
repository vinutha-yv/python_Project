'''
addition
substraction
multiplication
division

conditions - substraction function should only return values >= 0
condition - division must return values >= 1, where only one of the numbers is negative.
'''

def add_num(num1, num2): # num1 , num2 = a , b -> num1 = a, num2 = b
    return num1 + num2

# thisfunction should only return 0 or positive values
def sub_num(num1, num2):
    # return num1 - num2
    if num1 == num2:
        return 0
    elif num1 > num2:
        return num1 - num2
    else:
        return num2 - num1

def mul_num(num1, num2):
    return num1 * num2

def div_num(num1, num2):
    if num1 == num2:
        if num2 == 0:
            return "0/0 not possible"
        else:
            return 1.0
    elif num1 > num2:
        if num2 == 0:
            return "division by 0 not possible, num2 is 0"
        else:
            return num1 / num2
    else:
        if num1 == 0:
            return "division by 0 not possible, num1 is 0"
        else:
            return num2 / num1
    # return num1 / num2

for i in range(5):
    print(f"running for the {i + 1}th time")
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    print(add_num(a, b))
    print(sub_num(a, b))
    print(mul_num(a, b))
    print(div_num(a, b))
    print("\n")

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

