

def sum_digits(num):
    sum = 0
    while(num > 0):
        Reminder = num % 10
        sum = sum + Reminder
        num = num //10
    return sum

def product_digits(num):
    product = 1
    while(num != 0):
        product = product * (num % 10)
        num = num // 10
    return product

for i in range(1):
    print(f"running for the {i + 1}th time")
    n = int(input("Enter any number : "))  
    sum_digits = sum_digits(n)
    print("Sum of digits in a number is", sum_digits)
    product_digits = product_digits(n)
    print("Product of digits in a number is", product_digits)
    print("\n")

