def factorial(n):
    if n == 1:
        return 1
    print(n)
    return n * factorial(n - 1)
   
    return n

n = int(input("Escribe numero: "))
print(factorial(n))

