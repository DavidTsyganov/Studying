Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def squirrel (N):
    factorial = 1
    for i in range (1, N + 1):
        factorial *= i
    nut = factorial
    c = 0
    while nut > 0:
        c = nut % 10
        nut = nut // 10
    return c
N = int (input ())
Result = squirrel (N)
print (Result)
SyntaxError: invalid syntax
>>> def squirrel (N):
    factorial = 1
    for i in range (1, N + 1):
        factorial *= i
    nut = factorial
    c = 0
    while nut > 0:
        c = nut % 10
        nut = nut // 10
    return c
    N = int (input ())
    Result = squirrel (N)
    print (Result)

    
>>> def squirrel (N):
    factorial = 1
    for i in range (1, N + 1):
        factorial *= i
    nut = factorial
    c = 0
    while nut > 0:
        c = nut % 10
        nut = nut // 10
    return c
