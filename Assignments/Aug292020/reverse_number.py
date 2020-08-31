'''
program to reverse given number 


'''


def reverse_number(num):
    reverse = 0
    while(num > 0):
        remainder = num % 10
        reverse = (reverse * 10) + remainder
        num = num // 10
    return reverse

for i in range(1):
    print(f"running for the {i + 1}th time")
    n = int(input("Enter any number : "))  
    reverse = reverse_number(n)
    print(f"Reversed number is:{reverse}")
    