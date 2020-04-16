def squirrel (N):
    factorial = 1
    for i in range (1, N + 1):
        factorial *= i
    nut = factorial
    c = 0
    while nut > 0:
        c = nut % 10
        nut = nut // 10
    return c
