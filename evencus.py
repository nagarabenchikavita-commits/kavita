def isevenodd(n):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input("Enter a number: "))
flag = isevenodd(num)

if flag:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
