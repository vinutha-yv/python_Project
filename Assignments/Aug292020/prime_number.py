'''
program to check if number is prime or not
prime number is always greater than 1
if (num % ) == 0:
'''


def prime_number(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, ": Number is not a prime")
                break
        else:
            print(num, ": Number is prime")
            print(f": Number is prime: {num}")
  
    else:
        print(num, ": Number is not a prime")

for i in range(1):
    print(f"running for the {i + 1}th time")
    n = int(input("Enter any number : "))  
    prime_number(n)
    