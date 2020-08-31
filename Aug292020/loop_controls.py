num = 1
print("""This loop will continue till the time you enter 0 or false or null""")
while num:
    inp = input(">>>")
    if inp == "False":
        break
    elif inp in ["0", "", "None"] or len(inp) > 1:
        print("cannot work for these")
        continue
    else:
        if ord(inp) in range(48, 58):
            print(f"{inp} is a number")
        elif ord(inp) in range(65, 91):
            print(f"{inp} is a capital letter")
        elif ord(inp) in range(97, 123):
            print(f"{inp} is a small letter")
        else:
            print(f"{inp} is a symbol")
    num += 1
    print(num)