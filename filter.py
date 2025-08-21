def even(num):
    if(num%2==0):
        return True
    else:
        return False
L=[]
i=0
while(i<=4):
    print("enter the value")
    data=int(input())
    L.insert(i,data)
    i=i+1
print(L)
k=list(filter(even,L))
print(k)