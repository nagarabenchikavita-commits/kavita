def isevenodd(n):
    if n % 2 == 0:
        return True
    else:
        return False

count = int(input("Enter how many even numbers you want: "))
series = 1

while count > 0:
    flag = isevenodd(series)
    if flag:
        print(series, end=" ")
        count -= 1
    series += 1
