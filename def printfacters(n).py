def printfactors(n):
    countfactors = 0
    countcycles = 0
    for i in range(1, n+1):
        countcycles += 1
        if n % i == 0:
            print(i, end=" ")  # added space for readability
            countfactors += 1
    return countfactors, countcycles

n = int(input("Enter number: "))
resfact, recycles = printfactors(n)

print(f"\nThe count of factors of {n} is: {resfact}")
print(f"The count of cycles of {n} is: {recycles}")
