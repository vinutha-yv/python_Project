# program to check if number is positive or negative


def number(num):
    if num > 0:
        return "positive num"
    elif num == 0:
        return 0
    else:
        return "negative num"

for i in range(1):
    print(f"running for the {i + 1}th time")
    n = float(input("Enter any number : "))  
    num = number(n)
    print("number is:", num)
    