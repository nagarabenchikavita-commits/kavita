def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n = 22
print(f"The factorial of {n} is: {factorial(n)}")

