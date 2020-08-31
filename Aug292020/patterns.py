def right_angled_triangle(n, pat):
    for i in range(1, n + 1):
        print(pat * i)
    for i in range(n, 0, -1):
        print(pat * i)

right_angled_triangle(5, "*")