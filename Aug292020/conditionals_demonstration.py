# input function always accepts string, if we want to convert string to float use float(input())

num = float(input("Enter value : "))
if num < 35.5:
    print(f"{num} less than 35.5")
elif num <= 99.0:
    print(f"{num} is greater than 35.5 and {num} less than 100")
else:
    print(f"{num} greater than or equals to 100")

# unicode is the normal format of strings in python, if you need to convert it in to formatted, you need to add an f before the string.