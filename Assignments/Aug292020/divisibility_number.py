'''
Checking the divisibility of a number from andother number
a is dividend
b is divisor
'''

def div_num(d1, d2):
    if d1 == d2:
        if d2 == 0:
            return "0/0 not possible"
        else:
            return True
    elif d1 > d2:
        if d2 == 0:
            return "division by 0 not possible, d2 is 0"
        elif (d1 % d2) == 0:
            return True     
        else:
            return False               
    elif d1 == 0:
        return "division by 0 not possible, d1 is 0"

for i in range(5):
    print(f"running for the {i + 1}th time")
    a = int(input("Enter dividend number  : "))  
    b = int(input("Enter divisor : "))  
    num = div_num(a, b)
    print("number is divisible:", num)