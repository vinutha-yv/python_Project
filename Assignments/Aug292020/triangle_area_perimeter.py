'''
a, b, c are three sides of triangle
s is the semi perimeter of the triangle

'''

def area_triangle(s1, s2, s3): 
    # calculate the semi-perimeter  
    s = (s1 + s2 + s3) / 2  
    # calculate the area  
    area = (s*(s-s1)*(s-s2)*(s-s3)) ** 0.5 
    return area

def perimeter_triangle(s1, s2, s3):
    perimeter = s1 + s2 + s3
    return  perimeter

for i in range(1):
    print(f"running for the {i + 1}th time")
    a = float(input("Enter first side : "))
    b = float(input("Enter second side : "))
    c = float(input("Enter third side : "))
    area = area_triangle(a, b, c)
    print(f"Area of triangle is: {area}")
    perimeter = perimeter_triangle(a, b, c)
    print(f"Perimeter of triangle is:{perimeter}")
    print("\n")
