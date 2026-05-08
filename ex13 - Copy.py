n1, n2 = map(int, input("Enter two numbers: ").split())
while n2 >= n1:
    row = range(n1, n2 + 1)
    print(*row)
    n2 -= 1
