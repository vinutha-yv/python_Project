'''
Multiplication table using for loop


'''
def multi_table(num):
    print("Multiplication table of: ", num)
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)


for i in range(5):
    print(f"running for the {i + 1}th time")
    a = int(input("Enter number : "))
    multi_table(a)
