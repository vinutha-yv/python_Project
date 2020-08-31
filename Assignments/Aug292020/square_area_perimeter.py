'''
l is the side of square

'''

def area_square(s):  
    area = s*s
    return area

def perimeter_square(s):
    perimeter = 4 * s
    return  perimeter

for i in range(1):
    print(f"running for the {i + 1}th time")
    l = float(input("Enter first side : "))
    area = area_square(l)
    print("Area of rectangle is", area)
    perimeter = perimeter_square(l)
    print("Perimeter of rectangle is", perimeter)
    print("\n")