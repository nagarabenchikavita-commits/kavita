def printfactors(n):
    countfactors = 0
    countcycles = 0
    for i in range(1, n+1):
        countcycles += 1
        if n % i == 0:
            print(i, end=" ")
            countfactors += 1
    return countfactors, countcycles

def dispfactors(n):
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i, end=" ")
            if i != n // i:   # avoid duplicate when i*i == n
                print(n // i, end=" ")
        i += 1

# Main Program
n = int(input("Enter num: "))
resfact, recycles = printfactors(n)

print(f"\nThe count of factors of {n} is: {resfact}")
print(f"The count of cycles of {n} is: {recycles}")
print("    ")
res
