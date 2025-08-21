n1 = int(input("enter the first num:"))
n2 = int(input("enter the second num:"))
lower = n1
if n2<n1:
    lower = n2
gcd = 1
for i in range(2,lower+1):
    if n1% i == 0 and n2%i == 0:
        gcd = i
print(f"the GCD of {n1} and {n2} is:{gcd}")