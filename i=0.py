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
i=0
while(i<=4):
    ext=L[i]
    status=even(ext)
    if(status==True):
        print(L[i])
    i=i+1