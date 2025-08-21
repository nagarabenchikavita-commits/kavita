def printfactors(n):
    """Naive method: check all numbers from 1 to n"""
    countfactors = 0
    countcycles = 0
    for i in range(1, n + 1):
        countcycles += 1
        if n % i == 0:
            print(i, end=" ")
            countfactors += 1
    return countfactors, countcycles

def dispfactors(n):
    """Optimized method: check numbers only up to sqrt(n)"""
    i = 1
    small = []
    large = []
    while i * i <= n:
        if n % i == 0:
            small.append(i)
            if i != n // i:   # avoid duplicate when i*i == n
                large.append(n // i)
        i += 1
    # print all factors in ascending order
    factors = small + large[::-1]
    print(" ".join(map(str, factors)))

# Main Program
n = int(input("Enter num: "))
resfact, recycles = printfactors(n)

print(f"\nThe count of factors of {n} is: {resfact}")
print(f"The count of cycles of {n} is: {recycles}")

print("Factors using sqrt method:", end=" ")
dispfactors(n)
