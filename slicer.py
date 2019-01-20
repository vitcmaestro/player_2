n,k = map(int,input().split())
mem = list(map(int,input().split()))
c= 0
for i in range(0,n-k):
    if(c ==0):
        print(mem[i],end= "")
        c+=1
    else:
        print("",mem[i],end ="")
