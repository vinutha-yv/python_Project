'''
Program to check if triangle is valid or not
a, b, c are three sides of triangle
1.a + b > c 
2.a + c > b 
3.b + c > a  

if triangel(a, b, c):
    print("Triangle is possible)
else:
    print("Triangle is not possible)

    Use above condition when you return true or False

'''

def triangle(s1, s2, s3):
    if ((a + b > c) and (a + c > b) and (b + c > a)):
        return True
    else:
        return False

for i in range(1):
    print(f"running for the {i + 1}th time")
    a = float(input("Enter first side : "))
    b = float(input("Enter second side : "))
    c = float(input("Enter third side : "))
    triangle = triangle(a, b, c)
    print("Triangle is valid: ", triangle)
    print("\n")