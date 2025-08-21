def fiboseriesincre(pos):
    n1,n2=0,1
    i=1
    while i<=pos:
        print(n1, end="")
        temp=n1+n2
        n1=n2
        n2=temp
        i+=1
pos=int(input("enter the pos:"))
fiboseriesincre(pos)
