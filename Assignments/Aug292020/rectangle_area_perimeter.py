'''
l is length and b is breadth of rectangle


'''

def area_rectangle(l1, b1): 
    return (l1 * b1)

def perimeter_rectangle(l1, b1):
    return  (2 * (l1 + b1)) 

for i in range(1):
    print(f"running for the {i + 1}th time")
    l = float(input("Enter length : "))
    b = float(input("Enter breadth : "))
    area = area_rectangle(l, b)
    print("Area of rectangle is", area)
    perimeter = perimeter_rectangle(l, b)
    print("Perimeter of rectangle is", perimeter)
    print("\n")