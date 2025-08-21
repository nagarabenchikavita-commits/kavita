def findgcd(n1, n2):
    lower = n2

    gcd = 1
    for i in range(2, lower + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd

def arecoprime(n1, n2):
    if findgcd(n1, n2) == 1:
        return True
    else:
        return False

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if arecoprime(num1, num2):
    print(f"{num1} and {num2} are coprime.")
else:
    print(f"{num1} and {num2} are not coprime.")
