# program to check if number is odd or even


def number(num):
    if (num % 2 ) == 0:
        return "even num"
    else:
        return "odd num"

for i in range(1):
    print(f"running for the {i + 1}th time")
    n = int(input("Enter any number : "))  
    num = number(n)
    print("number is:", num)
    