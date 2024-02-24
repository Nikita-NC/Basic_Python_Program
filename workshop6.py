def factorial(n):
    if n == 0:
        return 1

    else:
        return n * factorial(n-1) 

factorial_7 = factorial(7)
factorial_5 = factorial(5)

result = factorial_7 - factorial_5
print("7 factoial minus 5 factorial is:",result)