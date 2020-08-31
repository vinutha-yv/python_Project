'''
print all prime numbers in a given range
'''

def all_prime_numbers(l, u):
    for num in range(l, u + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break

            else:
                return num


for i in range(4):
    print(f"running for the {i + 1}th time")
    lower = int(input("Enter lower range : "))
    upper = int(input("Enter upper range : "))
    num = all_prime_numbers(lower, upper)
    print("List of prime numbers", num)
    print("\n")