# a = 4
# b = 3
# print(a+b)


# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# print(a + b)

def add_num(num1, num2):
    print("running add_num machine")
    return num1 + num2

# return only 0 or positive numbers -> num1 > num2, num2 > num1, num1 == num2 -> elif
def sub_num(num1, num2):
    print("running sub_num machine")
    if num1 > num2:
        print("num1 > num2")
        return num1 - num2
    elif num2 > num1:
        print("num2 > num1")
        return num2 - num1
    else:
        print("num1 == num2")
        return 0

def mul_num(num1, num2):
    print("running mul_num machine")
    return num1 * num2

# return 1 or > 1
def div_num(num1, num2):
    print("running div_num machine")
    # if num2 == 0:
    #     print(f"Division by zero is not supported, {num2} is 0")
    #     return 0
    # return num1/num2
    if num1 == num2: # 0 0 
        print(f"{num1} == {num2}")
        if num1 == 0:
            print("Both the numbers are 0 and division by zero is not supported")
            return 0
        else:
            return 1
    elif num1 > num2:
        print(f"{num1} > {num2}")
        if num2 == 0:
            print("num2 is 0 and division by zero is not supported")
            return 0
        else:
            return num1/num2
    else: # num2 > num1
        print(f"{num2} > {num1}")
        if num1 == 0:
            print("num1 is 0 and division by zero is not supported")
            return 0
        else:
            return num2/num1

number_of_operations = int(input("Enter the number of operations: "))

for operation in range(number_of_operations):
    print(f"operating for the {operation + 1} time")
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    print("\n") # new line
    print(f"sum of {a} and {b} is {add_num(a, b)}")
    print("\n") # new line
    print(f"subtraction from {a} to {b} is {sub_num(a, b)}")
    print("\n") # new line
    print(f"multiplication of {a} and {b} is {mul_num(a, b)}")
    print("\n") # new line
    print(f"division of {a} and {b} is {div_num(a, b)}")
    print("\n") # new line

# Prasant - 8217050278
